package logic;

import java.util.ArrayList;

import utils.OutputWriter;
import utils.Utils;
import cli.Cli;

public class Main {
		
	protected static Sensor sensorAlpha;
	protected static Sensor sensorBeta;
	protected static ArrayList<Float> measuredValues;
	protected static ArrayList<Float> glucoseValues;
	protected static ArrayList<Float> dosageToInfuse;
	protected static float INSULINE_MAX_VALUE = (float) 6.0;
	
	public static void main(String [] args) {
		String filePath = args[0];
		Cli cli = new Cli(filePath);
		
		sensorAlpha = new Sensor(0, cli.getFilename(), cli.getSensorAplhaMeasures());
		sensorBeta = new Sensor(1, cli.getFilename(), cli.getSensorBetaMeasures());
		int numberOfMeasures =  sensorAlpha.getGlucoseMeasures().size();
				
		FaultTolerance.initFaultToleranceMechanisms(numberOfMeasures, sensorAlpha, sensorBeta);
		
		measuredValues = FaultTolerance.getMeasuredValues();
		computeGlucoseValues(measuredValues);
		
		computeDosagesToInfuse();
		checkIfAnyNegativeDosage();
		printDosageToInfuse();
		
		new OutputWriter(dosageToInfuse);
	}

	private static void printDosageToInfuse() {
		System.out.println("Dosage to infuse");
		for(int i = 0; i < dosageToInfuse.size(); i++) {
			System.out.println(i + ") " + Math.round(dosageToInfuse.get(i)));
		}
	}
	
	private static void computeGlucoseValues(ArrayList<Float> measuredValues) {
		glucoseValues = new ArrayList<Float>();
		for(int i = 0; i < measuredValues.size(); i++) {
			glucoseValues.add(Utils.measuredValueToGlucose(measuredValues.get(i)));
		}
	}
	
	private static float computeInsulineDosageToGive(float glucose, float dg, float ddg, float ic) {
		return (float) (0.8 * glucose + 0.2 * dg + 0.5 * ddg - ic);
	}
	
	private static float computeInsulineInBlood(float dosage, float icAnt) {
		return (float) (dosage + 0.9 * icAnt);
	}
	
	private static void checkIfAnyNegativeDosage() {
		for(int i = 0; i < dosageToInfuse.size(); i++) {
			if(dosageToInfuse.get(i) < 0) {
				dosageToInfuse.set(i, (float) 0);
			}
		}
	}
	
	private static void computeDosagesToInfuse() {
		int counter = 1;
		dosageToInfuse = new ArrayList<Float>();
		ArrayList<Float> insulineInBlood = new ArrayList<Float>();
		insulineInBlood.add((float) 0.0);
		for(int i = 0; i < glucoseValues.size(); i++) {
			if(counter == 3) {
				float glucoseValue = (float) -1.0;
				float measuredValue = (float) -1.0;
				if(glucoseValues.get(i).equals(Float.NaN)) {
					if(!glucoseValues.get(i - 1).equals(Float.NaN) && !glucoseValues.get(i - 2).equals(Float.NaN)) {
						glucoseValue = (float) (glucoseValues.get(i - 1) + glucoseValues.get(i - 2) / 2.0);
						System.out.println("1: " + measuredValues.get(i-2) + " 2: " + measuredValues.get(i-1));
						measuredValue = (float) ((measuredValues.get(i - 1) + measuredValues.get(i - 2)) / 2.0);
					} else if(!glucoseValues.get(i - 1).equals(Float.NaN)) {
						glucoseValue = glucoseValues.get(i - 1);
						measuredValue = measuredValues.get(i - 1);
					} else if(!glucoseValues.get(i - 2).equals(Float.NaN)) {
						glucoseValue = glucoseValues.get(i - 2);
						measuredValue = measuredValues.get(i - 2); 
					} else {
						glucoseValue = -1;
					}
				} else {
					glucoseValue = glucoseValues.get(i);
					measuredValue = measuredValues.get(i);
				}
				
				if(glucoseValue == -1) {
					dosageToInfuse.add(Float.NaN);
				} else {
					if(glucoseValue >= INSULINE_MAX_VALUE) {
						if(Utils.checkIfDownwardTrend(i, glucoseValues)) {
							dosageToInfuse.add((float)0.0);
							int icIndex = insulineInBlood.size() - 1;
							float icAnt = insulineInBlood.get(icIndex);
							insulineInBlood.add(computeInsulineInBlood((float) 0.0, icAnt));
						} else if(Utils.checkIfUpwardTrend(i, glucoseValues)) {
							float dg = Utils.computeDGvalue(measuredValue);
							float ddg = Utils.computeDDGvalue(measuredValue);
							int icIndex = insulineInBlood.size() - 1;
							float icAnt = insulineInBlood.get(icIndex);
							float dosage = computeInsulineDosageToGive(glucoseValue, dg, ddg, icAnt);
							dosageToInfuse.add(dosage);
							insulineInBlood.add(computeInsulineInBlood(dosage, icAnt));
						} else {
							float dg = Utils.computeDGvalue(measuredValue);
							float ddg = Utils.computeDDGvalue(measuredValue);
							int icIndex = insulineInBlood.size() - 1;
							float icAnt = insulineInBlood.get(icIndex);
							float dosage = computeInsulineDosageToGive(glucoseValue, dg, ddg, icAnt);
							dosageToInfuse.add(dosage);
							insulineInBlood.add(computeInsulineInBlood(dosage, icAnt));
						}
					} else {
						dosageToInfuse.add((float) 0.0);
						int icIndex = insulineInBlood.size() - 1;
						float icAnt = insulineInBlood.get(icIndex);
						insulineInBlood.add(computeInsulineInBlood((float) 0.0, icAnt));
					}
				}
				counter = 1;
			} else {
				counter++;
			}
		}
	}
}