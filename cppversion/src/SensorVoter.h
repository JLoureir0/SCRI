/*
 * SensorVoter.h
 *
 *  Created on: 07/05/2015
 *      Author: ricardo
 */

#ifndef SENSORVOTER_H_
#define SENSORVOTER_H_


#include <vector>

using namespace std;

class SensorVoter {

	private:
		vector<float> sensor1;
		vector<float> sensor2;
		vector<float> voted;
		bool isSensorStuck(vector<float>, int pos);
		bool isSensorDeviated(vector<float>, int pos);
		bool isSensorNotWorking(vector<float>, int pos);
		bool isSensorOutOfRange(vector<float>, int pos);
	public:
		SensorVoter(vector<float> sensor1, vector<float> sensor2);
		void doVoting();
		vector<float> getVoted();
};

#endif
