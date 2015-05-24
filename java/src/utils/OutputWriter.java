package utils;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;

public class OutputWriter {
	
	private String filePath = null;
	private ArrayList<Float> results;
	
	public OutputWriter(String filePath, ArrayList<Float> dosage) {
		this.filePath = filePath;
		this.results = new ArrayList<Float>();
		this.results = dosage;
		writeFileResults();
	}
	
	private void writeFileResults() {
		try {
			BufferedWriter writer = null;
			File resultFile = new File(filePath);
			
			if(resultFile.exists()) {
				resultFile.delete();
			}
			
			 writer = new BufferedWriter(new FileWriter(resultFile, true));
			 for(int i = 0; i < results.size(); i++) {
				
				 if(results.get(i).equals(Float.NaN)) {
					 writer.write("FAIL");
					 System.out.println("FAIL");
				 }
				 else {
					 writer.write("" + Math.round(results.get(i)));
					 System.out.println(Math.round(results.get(i)));
				 }
				 
				 if((i + 1) < results.size())
					 writer.write("\n");
			 }
			 writer.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
