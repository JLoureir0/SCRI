/*
 * Output.cpp
 *
 *  Created on: 21/05/2015
 *      Author: ricardo
 */

#include "Output.h"

Output::Output(string fileName, vector<float> dosages) {
	this->fileName = fileName;
	this->dosages = dosages;

}

void Output::writeResults() {
	ofstream file;
	file.open(fileName.c_str());
	cout << "Dosages:" << endl;
	for(unsigned int i = 0; i < dosages.size(); i++) {
		if(dosages[i] == -1) {
			file << "FAIL" << endl;
			cout << "FAIL" << endl;
		} else {
			file << dosages[i] << endl;
			cout << dosages[i] << endl;
		}

	}
}

