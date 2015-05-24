package utils;

import java.util.ArrayList;

import logic.Sensor;

public abstract class Utils {
	
	public static float measuredValueToGlucose(float measuredValue) {
		return (float) (-3.4 + 1.354 * measuredValue + 1.545 * Math.tan(nthSqrt(4, measuredValue)));
	}
	
	public static float nthSqrt(float degree, float value) {
		return (float) Math.pow(value, (1/degree) ); 
	}
	
	public static boolean isSubstanciallyDifferentFromMedium(float v1, float v2) {
		float signigicantDifference = (float) 0.4; //percentage
		float higherValue = v1 + signigicantDifference * v1;
		float lowerValue = v1 - signigicantDifference * v1;
		if(v2 < lowerValue || v2 > higherValue)
			return true;
		return false;
	}
	
	public static boolean substanciallyDifferentValues(float v1, float v2) {
		float signigicantDifference = (float) 0.4; //percentage
		float higherValue = v1 + signigicantDifference * v1;
		float lowerValue = v1 - signigicantDifference * v1;
		if(v2 < lowerValue || v2 > higherValue)
			return true;
		return false;
	}
	
	public static boolean isSensorGettingRandomValues(Sensor s, int measure) {
		float signigicantDifference = (float) 1; //percentage
		
		if(measure == 0)
			return false;
		
		int lastMeasure = measure - 1; 
		float measureValue = s.getGlucoseMeasures().get(measure);
		float lastmeasureValue = s.getGlucoseMeasures().get(lastMeasure);
		
		if(lastmeasureValue == -1)
			return false;
		
		float higherValue = lastmeasureValue + lastmeasureValue * signigicantDifference; 
		float lowerValue = lastmeasureValue - lastmeasureValue * signigicantDifference;
		if(measureValue < lowerValue || measureValue > higherValue)
			return true;
		return false;
	}
	
	public static boolean checkIfGettingSameValues(Sensor s, int measure) {
		if(measure == 0)
			return false;
		
		int lastMeasure = measure -1;
		if(s.getGlucoseMeasures().get(measure).equals(s.getGlucoseMeasures().get(lastMeasure)))
			return true;
		return false;
	}
	
	public static float computeDGvalue(float glucose) {
		return (float) ((0.38625 * Math.pow((1/Math.cos(Math.pow(glucose, 0.25))), 2) / Math.pow(glucose, 0.75)) + 1.354);
	}
	
	public static float computeDDGvalue(float glucose) {
		return (float) ((0.193125 * Math.tan(Math.pow(glucose, 0.25)) * Math.pow((1 / Math.cos(Math.pow(glucose, 0.25))), 2)) / (Math.pow(glucose, 1.5)) - ((0.289688 * Math.pow((1 / Math.cos(Math.pow(glucose, 0.25))), 2)) / Math.pow(glucose, 1.75)));
	}
	
	public static boolean checkIfUpwardTrend(int index, ArrayList<Float> glucoseMeasures) {
		int firstIndex = -1;
		int trend_measures = 3;
		
		if(index >= trend_measures)
			firstIndex = index - (trend_measures - 1);
		else
			firstIndex = 0;

		if((glucoseMeasures.get(index) - glucoseMeasures.get(firstIndex)) / 2.0 >= 0.4)
			return true;
		else 
			return false;
	}
	
	public static boolean checkIfDownwardTrend(int index, ArrayList<Float> glucoseMeasures) {
		int firstIndex = -1;
		int trend_measures = 3;

		if(index >= trend_measures)
			firstIndex = index - (trend_measures - 1);
		else
			firstIndex = 0;
		
		if((glucoseMeasures.get(firstIndex) - glucoseMeasures.get(index)) / 2.0 >= 0.4)
			return true;
		else 
			return false;
	}
}