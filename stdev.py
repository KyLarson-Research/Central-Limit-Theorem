# File Name: stdev.py
# Author: Kyle Carlton Larson
# Purpose: To calculate standard deviation for AP_Stats practice test
import math
work_schedule_data = [[45, 0.3], [40, 0.2], [25, 0.4], [12, 0.1]]

def mean(data_list):
	mew = 0
	for xy in data_list:
		mew += xy[0]*xy[1]
	return mew
	
print(mean(work_schedule_data))

def stdev(_mew, _data_list):
	sigma = 0
	for _xy in _data_list:
		sigma += ((_xy[0] - _mew)**2) * _xy[1]
	return sigma

print(stdev(mean(work_schedule_data), work_schedule_data))	