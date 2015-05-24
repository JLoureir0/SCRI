/*
 * Calc.h
 *
 *  Created on: Apr 13, 2015
 *      Author: ricardo
 */

#ifndef SRC_CALC_H_
#define SRC_CALC_H_

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <cmath>

using namespace std;

class Calc {
	private:
		// Will store the information about last 30 minutes readings (10 readings)
		deque<float> glucoseHistory;
		vector<float> dosageHistory;
		vector<float> dgHistory;
		vector<float> ddgHistory;
		static const float MAX_GLUCOSE = 6.0;
	public:
		Calc();
		vector<float> icHistory;
		// Computes glucose values and stores the last 10 values in one queue
		void calc_glucose(double val);
		void calc_dg(double val);
		void calc_ddg(double val);
		void calc_dosage(vector<float> glucose);
		void calc_estimate_body_insulin();
		int calc_Glucose_valid_values();
		float calc_trend();
		deque<float> getGlucoseHistory();
		vector<float> get3MostRecentGlucose();
		vector<float> getDosageHistory();
};


#endif /* SRC_CALC_H_ */
