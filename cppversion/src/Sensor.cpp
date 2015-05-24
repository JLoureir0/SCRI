/*
 * ManageFile.cpp
 *
 *  Created on: Apr 13, 2015
 *      Author: ricardo
 */
#include "Sensor.h"

Sensor::Sensor(string src_dir, int id) {
	this->src_dir = src_dir;
	this->id = id;
}

void Sensor::read() {
	ifstream file(this->src_dir.c_str());
	string line;
	if(file.is_open()) {
		while(getline(file, line)) {
				string splited = split(line);
				if(splited == "--") {
					reading.push_back(-1.0);
				} else {
					float val = atof(splited.c_str());
					reading.push_back(val);
				}

		}
		file.close();
	} else cerr << "Something went wrong reading file!" << endl;
}

string Sensor::split(string line) {
	string delimenter = " ";
	if(this->id == 1)
		return line.substr(0, line.find(delimenter));
	return line.substr(line.find(delimenter)+1, line.find("\n"));
}

vector<float> Sensor::getResults() {
	return this->reading;
}



