package cli;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Cli {
	
	private String filename;
	private ArrayList<Float> sensor1;
	private ArrayList<Float> sensor2;
		
	public Cli() {
		this.filename = null;
		this.sensor1 = new ArrayList<Float>();
		this.sensor2 = new ArrayList<Float>();
		receiveFilePath();
	}
	
	public Cli(String filePath) {
		this.filename = filePath;
		this.sensor1 = new ArrayList<Float>();
		this.sensor2 = new ArrayList<Float>();
		readEntryFile();
	}
	
	private void receiveFilePath() {
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Enter the path of the entry file: ");
		filename = keyboard.nextLine();
		keyboard.close();
		System.out.print("Reading File .... ");
		readEntryFile();
	}
	
	private void readEntryFile() {
		try {
			String line = null;
		    FileReader fileReader = new FileReader(filename);
		    BufferedReader bufferedReader = new BufferedReader(fileReader);
		    while((line = bufferedReader.readLine()) != null) {
		    	String[] lineSplitted = line.split(" ");
		    	
		    	if(lineSplitted[0].equals("--"))
		    		sensor1.add((float) -1.0);
		    	else
		    		sensor1.add(Float.valueOf(lineSplitted[0]));
		    	
		    	if(lineSplitted[1].equals("--"))
		    		sensor2.add((float) -1.0);
		    	else
		    		sensor2.add(Float.valueOf(lineSplitted[1]));
		    }    

		    bufferedReader.close(); 
		}
		catch(FileNotFoundException ex) {
			System.out.println("Fail");
			System.out.println("Unable to open file '" + filename + "'");                
		}
		catch(IOException ex) {
			System.out.println("Fail");
		    System.out.println("Error reading file '" + filename + "'");  
		    ex.printStackTrace();
		}
	}
	
	public String getFilename() {
		return filename;
	}
	
	public ArrayList<Float> getSensorAplhaMeasures() {
		return sensor1;
	}
	
	public ArrayList<Float> getSensorBetaMeasures() {
		return sensor2;
	}
}