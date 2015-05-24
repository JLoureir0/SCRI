/*
 * SensorVoter.cpp
 *
 *  Created on: 07/05/2015
 *      Author: ricardo
 */
#include "SensorVoter.h"
#include <iostream>
#include <stdlib.h>
#include <cmath>

using namespace std;

SensorVoter::SensorVoter(vector<float> sensor1, vector<float> sensor2) {
	this->sensor1 = sensor1;
	this->sensor2 = sensor2;
}

void SensorVoter::doVoting() {
	if(this->sensor1.size() == this->sensor2.size()) {
		for(unsigned int i = 0; i < this->sensor1.size(); i++) {
			bool sensor1Stuck = this->isSensorStuck(this->sensor1, i);
			bool sensor1Deviated = this->isSensorDeviated(this->sensor1, i);
			bool sensor1NotWorking = this->isSensorNotWorking(this->sensor1, i);
			bool sensor1OutRange = this->isSensorOutOfRange(this->sensor1, i);
			bool sensor2Stuck = this->isSensorStuck(this->sensor2, i);
			bool sensor2Deviated = this->isSensorDeviated(this->sensor2, i);
			bool sensor2NotWorking = this->isSensorNotWorking(this->sensor2, i);
			bool sensor2OutRange = this->isSensorOutOfRange(this->sensor2, i);

			bool sensor1Operational = !sensor1Stuck && !sensor1Deviated && !sensor1NotWorking && !sensor1OutRange;
			bool sensor2Operational = !sensor2Stuck && !sensor2Deviated && !sensor2NotWorking && !sensor2OutRange;

			// If the 2 sensors are in good conditions lets compute the arithmetic mean between the two readings
			if(sensor1Operational && sensor2Operational)
				this->voted.push_back((float)(this->sensor1[i] + this->sensor2[i]) / 2.0);
			else if(sensor1Operational)
				this->voted.push_back(this->sensor1[i]);
			else if(sensor2Operational)
				this->voted.push_back(this->sensor2[i]);
			else if(!sensor1Operational && !sensor2Operational)
				this->voted.push_back(-1.0);
		}
	} else cerr << "Sensor1's and Sensor2's don't have the same cardinality" << endl;
}

/*
 * If the last 3 readings have an absolute difference of less than 0.01 than we consider that the sensor is stuck
 */
bool SensorVoter::isSensorStuck(vector<float> readings, int pos) {
	if(pos == 0)
		return false;

	if(pos >= 2)
		if(abs((readings[pos] - readings[pos-1])) < 0.01 && abs(readings[pos-1] - readings[pos-2]) < 0.01)
			return true;
	return false;
}

/*
	After first read, if a sensor has a variation bigger than 10, we consider
	that is impossible to happen, so sensor must be damaged, and it's info thrown away
*/
bool SensorVoter::isSensorDeviated(vector<float> readings, int pos) {
	if(pos == 0)
		return false;

	if(abs(readings[pos] - readings[pos-1]) > 2 && readings[pos] != -1 && readings[pos-1] != -1)
		return true;
	return false;
}

/*
 * When the readings on text file are -- the sensor readings inside the readings vector becomes -1, so i there's a -1 value the sensor is not working
 */
bool SensorVoter::isSensorNotWorking(vector<float> readings, int pos) {
	if(readings[pos] == -1.0)
		return true;
	return false;
}

/*
 * If the entry values are out of the range they are not considered and the sensor's output is considered wrong
 */
bool SensorVoter::isSensorOutOfRange(vector<float> readings, int pos) {
	if(readings[pos] <= 1 || readings[pos] > 5)
		return true;
	return false;
}

vector<float> SensorVoter::getVoted() {
	return this->voted;
}

