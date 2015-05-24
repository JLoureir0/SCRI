/*
 * Output.h
 *
 *  Created on: 21/05/2015
 *      Author: ricardo
 */

#ifndef SRC_OUTPUT_H_
#define SRC_OUTPUT_H_

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

class Output {
private:
	string fileName;
	vector<float> dosages;
public:
	Output(string fileName, vector<float> dosages);
	void writeResults();
};

#endif /* SRC_OUTPUT_H_ */
