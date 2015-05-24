package logic;

import java.util.ArrayList;

import utils.Utils;

public abstract class FaultTolerance {
	
	protected static float FAIL = Float.NEGATIVE_INFINITY;
	
	protected static Sensor sensorAlpha;
	protected static Sensor sensorBeta;
	protected static int numberOfMeasures;
	protected static ArrayList<Float> measuredValues;
	protected static float medium = Float.NEGATIVE_INFINITY;
	
	public static void initFaultToleranceMechanisms(int nMeasures, Sensor sa, Sensor sb) {
		sensorAlpha = sa;
		sensorBeta = sb;
		numberOfMeasures = nMeasures;
		manageSensorsFaults();
	}
	
	public static ArrayList<Float> getMeasuredValues() {
		return measuredValues;
	}
	
	private static void updateMedium(float newValue) {
		if(medium == Float.NEGATIVE_INFINITY) {
			medium = newValue;
		} else {
			medium = (medium + newValue) / 2;
		}
	}
	
	private static float restrictMeasuredValuesAsymptote(float measuredValue) {
		float upperBound = (float) 5.0;
		float lowerBound = (float) 1.0;
		if(measuredValue > upperBound || measuredValue < lowerBound) {
			return Float.NEGATIVE_INFINITY;
		}
		else
			return measuredValue;
	}
	
	private static void manageSensorsFaults() {
		measuredValues = new ArrayList<Float>();
		
		for(int i = 0; i < numberOfMeasures; i++) {
			float valueSensorAlpha = sensorAlpha.getGlucoseMeasures().get(i);
			float valueSensorBeta = sensorBeta.getGlucoseMeasures().get(i);
			
			if(valueSensorAlpha == -1 && valueSensorBeta == -1) { //nenhum sensor obteve uma leitura -> fail
				if(medium == Float.NEGATIVE_INFINITY) {
					measuredValues.add(FAIL);
				}
				else {
					measuredValues.add(medium);
					updateMedium(medium);
				}
			} else if(valueSensorAlpha == -1 || valueSensorBeta == -1) { //apenas um sensor obtem leitura
		
				boolean nullSensorAlpha = false;
				if(valueSensorAlpha == -1) {
					nullSensorAlpha = true;
				}
				else {
					nullSensorAlpha = false;
				}
				
				if(nullSensorAlpha) {
					if(medium == Float.NEGATIVE_INFINITY) {
						float chosenValue = sensorBeta.getGlucoseMeasures().get(i);
						chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
						measuredValues.add(chosenValue);
						updateMedium(chosenValue);
					} else {
						if(Utils.isSubstanciallyDifferentFromMedium(medium, sensorBeta.getGlucoseMeasures().get(i))) {
							float chosenValue = (float) ((medium + sensorBeta.getGlucoseMeasures().get(i)) / 2.0);
							chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
							measuredValues.add(chosenValue);
							updateMedium(chosenValue);
						}
						else {
							float chosenValue = sensorBeta.getGlucoseMeasures().get(i); 
							chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
							measuredValues.add(chosenValue);
							updateMedium(chosenValue);
						}
					}
				} else { //nullSensorBeta = true
					if(medium == Float.NEGATIVE_INFINITY) {
						float chosenValue = sensorAlpha.getGlucoseMeasures().get(i);
						chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
						measuredValues.add(chosenValue);
						updateMedium(chosenValue);
					} else {
						if(Utils.isSubstanciallyDifferentFromMedium(medium, sensorAlpha.getGlucoseMeasures().get(i))) {
							float chosenValue = (float) ((medium + sensorAlpha.getGlucoseMeasures().get(i)) / 2.0);
							chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
							measuredValues.add(chosenValue);
							updateMedium(chosenValue);
						}
						else {
							float chosenValue = sensorAlpha.getGlucoseMeasures().get(i);
							chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
							measuredValues.add(chosenValue);
							updateMedium(chosenValue);
						}						
					}					
				}		
			} else { 
				if(Utils.checkIfGettingSameValues(sensorAlpha, i) || Utils.isSensorGettingRandomValues(sensorAlpha, i)) { //sensorAplha stuck in the same values
					if(Utils.checkIfGettingSameValues(sensorBeta, i) || Utils.isSensorGettingRandomValues(sensorBeta, i)) { //sensorBeta stuck in the same values or getting random values
						measuredValues.add(FAIL);
					} else {
						float chosenValue = sensorBeta.getGlucoseMeasures().get(i);
						chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
						measuredValues.add(chosenValue);
						updateMedium(chosenValue);
					}
				} else if(Utils.checkIfGettingSameValues(sensorBeta, i) || Utils.isSensorGettingRandomValues(sensorBeta, i)) { //sensorBeta stuck in the same values
					if(Utils.checkIfGettingSameValues(sensorAlpha, i) || Utils.isSensorGettingRandomValues(sensorAlpha, i)) { //sensorAlpha stuck in the same values
						measuredValues.add(FAIL);
					} else {
						float chosenValue = sensorAlpha.getGlucoseMeasures().get(i);
						chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
						measuredValues.add(chosenValue);
						updateMedium(chosenValue);
					}
				} else {
					float sensorAlphaValue = sensorAlpha.getGlucoseMeasures().get(i);
					float sensorBetaValue = sensorBeta.getGlucoseMeasures().get(i);
					if(Utils.substanciallyDifferentValues(sensorAlphaValue, sensorBetaValue)) { //Sensors getting significantly different values
						if(medium == Float.NEGATIVE_INFINITY) {
							float chosenValue = (float) ((sensorAlphaValue + sensorBetaValue) / 2.0);
							chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
							measuredValues.add(chosenValue);
							updateMedium(chosenValue);
						} else {
							float diffSensorAlpha = Math.abs(medium - sensorAlphaValue);
							float diffSensorBeta = Math.abs(medium - sensorBetaValue);
							if(diffSensorAlpha < diffSensorBeta) { //Sensor Alpha mais perto da media
								sensorAlphaValue = restrictMeasuredValuesAsymptote(sensorAlphaValue);
								measuredValues.add(sensorAlphaValue);
								updateMedium(sensorAlphaValue);
							} else {
								sensorBetaValue = restrictMeasuredValuesAsymptote(sensorBetaValue);
								measuredValues.add(sensorBetaValue);
								updateMedium(sensorBetaValue);
							}
						}
					} else {
						float chosenValue = (float) ((sensorAlphaValue + sensorBetaValue) / 2.0);
						chosenValue = restrictMeasuredValuesAsymptote(chosenValue);
						measuredValues.add(chosenValue);
						updateMedium(chosenValue);
					}
				}
			}
		}
	}
	
}
