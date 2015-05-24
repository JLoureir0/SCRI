/*
 * Calc.cpp
 *
 *  Created on: Apr 13, 2015
 *      Author: ricardo
 */
#include "Calc.h"

Calc::Calc(){
	// The initial value for ic is 0
	icHistory.push_back(0.0);
}

void Calc::calc_glucose(double val) {

	if(val >= 0) {
		float glucose = -3.4 + 1.354 * val + 1.545 * tan(pow(val, 1.0/4));
		if(this->glucoseHistory.size() < 100)
			this->glucoseHistory.push_back(glucose);
		else {
				this->glucoseHistory.pop_front();
				this->glucoseHistory.push_back(glucose);
			}
	} else { // the value received from voting process between the 2 sensors is -1, so no sensor could be considered correct
		this->glucoseHistory.push_back(-1.0);
	}
}

void Calc::calc_dg(double val) {
	if(val >= 0) {
			float dg = (0.38625 * pow((1/cos(pow(val, 0.25))), 2) / pow(val, 0.75)) + 1.354;
			this->dgHistory.push_back(dg);
		} else { // the value received from voting process between the 2 sensors is -1, so no sensor could be considered correct
			this->dgHistory.push_back(-1.0);
		}

}

void Calc::calc_ddg(double val) {
	if(val >= 0) {
			float ddg = (0.193125 * tan(pow(val, 0.25)) * pow((1 / cos(pow(val, 0.25))), 2)) / (pow(val, 1.5)) - ((0.289688 * pow((1 / cos(pow(val, 0.25))), 2)) / pow(val, 1.75));
			this->ddgHistory.push_back(ddg);
		} else { // the value received from voting process between the 2 sensors is -1, so no sensor could be considered correct
			this->ddgHistory.push_back(-1.0);
		}

}

void Calc::calc_dosage(vector<float> glucose) {

	float dosage = 0.0;
	float dg = this->dgHistory[this->dgHistory.size() - 1];
	float ddg = this->ddgHistory[this->ddgHistory.size() - 1];
	float trend = calc_trend();

	if(glucose[0] == -1) {
		// Fail case when the last 2 glucose values have -1 value
		if(glucose[1] == -1 && glucose[2] != -1) {
			dosage = glucose[2];
			if(round(dosage) < 0)
				dosageHistory.push_back(round(0.0));
			else dosageHistory.push_back(round(dosage));
			return;
		} else if(glucose[1] != -1 && glucose[2] == -1) {
			dosage = glucose[1];
			if(round(dosage) < 0)
				dosageHistory.push_back(round(0.0));
			else dosageHistory.push_back(round(dosage));
			return;
		} else if(glucose[1] == -1 && glucose[2] == -1){
			if(round(dosage) < 0)
				dosageHistory.push_back(round(0.0));
			else dosageHistory.push_back(-1.0);
			return;
		}
		// do the mean value between the two last values
		glucose[0] = (glucose[1] + glucose[2]) / 2;

	}
	if(glucose[0] < MAX_GLUCOSE) {
		if(round(dosage) < 0)
			dosageHistory.push_back(round(0.0));
		else this->dosageHistory.push_back(round(dosage));
	}
	else {
		if(trend > -0.4) {
			dosage = 0.8 * glucose[0] + 0.2 * dg + 0.5 * ddg - icHistory[this->icHistory.size() - 1];
			if(round(dosage) < 0)
				dosageHistory.push_back(round(0.0));
			else dosageHistory.push_back(round(dosage));
		} else {
			dosage = 0.0;
			dosageHistory.push_back(round(dosage));
		}
	}

	calc_estimate_body_insulin();

}

void Calc::calc_estimate_body_insulin() {
	if(this->dosageHistory[this->dosageHistory.size()-1] != -1)
		this->icHistory.push_back(this->dosageHistory[this->dosageHistory.size()-1] + 0.9 * this->icHistory[this->icHistory.size() - 1]);
}

vector<float> Calc::get3MostRecentGlucose() {
	vector<float> last3;
	if(this->glucoseHistory.size() >= 3) {
		for(unsigned int i = 1; i < 4; i++)
				last3.push_back(this->glucoseHistory[glucoseHistory.size()-i]);
	} else {
		last3.push_back(this->glucoseHistory[glucoseHistory.size()-1]);
		return last3;
	}

	return last3;
}

float Calc::calc_trend() {
	float result = 0.0;
	if(glucoseHistory.size() >= 2) {

		if(glucoseHistory.size() <= 5) {
			result = (glucoseHistory[glucoseHistory.size() - 1] - glucoseHistory[0]) / glucoseHistory.size();
		} else {
			int final = glucoseHistory.size() - 1;
			int initial = final - 4;
			result = (glucoseHistory[final] - glucoseHistory[initial]) / 5;
		}

		return result;
	} else return 0.0; // consider a constant glucose level
}

int Calc::calc_Glucose_valid_values() {
	int counter = 0;
	for(unsigned int i = 0; i < this->glucoseHistory.size(); i++)
		if(this->glucoseHistory[i] != -1)
			counter++;
	return counter;
}
deque<float> Calc::getGlucoseHistory() {return this->glucoseHistory;}

vector<float> Calc::getDosageHistory() {return this->dosageHistory;}





