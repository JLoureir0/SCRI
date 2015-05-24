/*
 * main.cpp
 *
 *  Created on: Apr 13, 2015
 *      Author: ricardo
 */
#include <iostream>
#include "Sensor.h"
#include "SensorVoter.h"
#include "Calc.h"
#include "Output.h"
#include <sstream>
using namespace std;

int main(int argc, char** argv) {

	if(argc == 3) {

		// Instantiate sensors
		Sensor sensor1(argv[1], 1);
		Sensor sensor2(argv[1], 2);

		string destFile = argv[2];


		// Reads sensor values
		sensor1.read();
		sensor2.read();


		vector<float> finalValues;

		SensorVoter voter = SensorVoter(sensor1.getResults(), sensor2.getResults());
		voter.doVoting();

		Calc calc = Calc();
		vector<float> voted = voter.getVoted();

		int calcDosage = 0;
		for(unsigned int i = 0; i < voted.size(); i++) {
			calc.calc_glucose(voted[i]);
			calc.calc_dg(voted[i]);
			calc.calc_ddg(voted[i]);
			calcDosage++;
			if(calcDosage == 3) {
				calc.calc_dosage(calc.get3MostRecentGlucose());
				calcDosage = 0;
			}


		}


		Output out = Output(destFile, calc.getDosageHistory());
		out.writeResults();


	} else cerr << "Usage: executable input_file output_file" << endl;

}


