package logic;

import java.util.ArrayList;

public class Sensor {
	
	private int id;
	private String filename;
	private ArrayList<Float> glucoseMeasures;
	
	public Sensor(int id, String fileName, ArrayList<Float> measures) {
		this.id = -1;
		this.filename = fileName;
		this.glucoseMeasures = new ArrayList<Float>();
		convertToGlucose(measures);
	}
	
	public void printMeasuresForDebug() {
		for(int i = 0; i < glucoseMeasures.size(); i++) {
			System.out.println(i + ") " + glucoseMeasures.get(i));
		}
	}
	
	private void convertToGlucose(ArrayList<Float> measures) {
		for(int i = 0; i < measures.size(); i++) {
			if(measures.get(i).equals( (float) -1))
				glucoseMeasures.add( (float) -1);
			else 
				glucoseMeasures.add(measures.get(i));
		}
	}
	
	public ArrayList<Float> getGlucoseMeasures() {
		return glucoseMeasures;
	}
	
	public void setGlucoseMeasures(ArrayList<Float> glucoseMeasures) {
		this.glucoseMeasures = glucoseMeasures;
	}
	
	public int getSensorId() {
		return id;
	}
	
	public void setSensorId(int id) {
		this.id = id;
	}
	
	public String getFileName() {
		return filename;
	}
	
	public void setFileName(String fileName) {
		this.filename = fileName;
	}
}