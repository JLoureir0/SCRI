/*
 * ReadFile.h
 *
 *  Created on: Apr 13, 2015
 *      Author: ricardo
 */

#ifndef SRC_SENSOR_H_
#define SRC_SENSOR_H_

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdlib.h>

using namespace std;

class Sensor {
	private:
		string src_dir;
		int id;
		vector<float> reading;
		string split(string line);

	public:
		Sensor(string src_dir, int id);
		void read();
		void WriteResults();
		vector<float> getResults();


};


#endif
