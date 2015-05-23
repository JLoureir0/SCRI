import math
from copy import deepcopy

admitted_percentage = 0.3
sync_tolerance      = 3

def glucose_values(list_of_readings, variation):
    readings = deepcopy(list_of_readings)

    reading_out_of_range(readings)
    reading_out_of_sync(readings)
    reading_stuck_at(readings)
    reading_random(readings)

    parsed_list = parse_reading(readings)

    for index, reading in enumerate(parsed_list):
        if(reading != 'FAIL'):
            #CHECK: memory check for the glucose functions
            if(variation == 0):
                if(blood_glucose(1) == 0.36019):
                    parsed_list[index] = blood_glucose(reading)
                else:
                    parsed_list[index] = 'FAIL'
            elif(variation == 1):
                if(glucose_variation(1.12345) == 2.68741):
                    parsed_list[index] = glucose_variation(reading)
                else:
                    parsed_list[index] = 'FAIL'
            elif(variation == 2):
                if(glucose_variation_variation(1.12345) == 0.12616):
                    parsed_list[index] = glucose_variation_variation(reading)
                else:
                    parsed_list[index] = 'FAIL'

    return glucose_for_dosage(parsed_list)

def reading_out_of_range(list_of_readings):
    for entry in list_of_readings:
        entry[0] = out_of_range(entry[0])
        entry[1] = out_of_range(entry[1])
    return list_of_readings

def out_of_range(entry_value):
    #CHECK: range for entry_value

    if (entry_value < 1 or entry_value > 5):
        return '--'
    return entry_value

def reading_out_of_sync(list_of_readings):
    #CHECK: if the values from the sensor are too different from each other raise an exception

    tolerance = 0

    for index, reading in enumerate(list_of_readings):
        if(reading[0] != '--' and reading[1] != '--'):
            entry_difference = round(math.fabs(reading[0] - reading[1]), 5)
            admitted_difference1 = round(reading[0]*admitted_percentage, 5)
            admitted_difference2 = round(reading[1]*admitted_percentage, 5)

            if(entry_difference > admitted_difference1 or entry_difference > admitted_difference2):
                tolerance += 1
            else:
                tolerance -= 1

            if(tolerance >= sync_tolerance):
                list_of_readings[index][0] = '--'
                list_of_readings[index][1] = '--'



    return list_of_readings

def reading_stuck_at(list_of_readings):
    #CHECK: if the two previous valid values are equal to the current value sensor is stuck at that value

    for i in range(len(list_of_readings)-1, -1, -1):
        if(i > 1):
            j = i
            repeated = 0

            while(j != 0 and repeated < 2):
                if(list_of_readings[j-1][0] != '--'):
                    if(list_of_readings[i][0] == list_of_readings[j-1][0]):
                        repeated += 1
                    else:
                        break
                j-=1

            if(repeated == 2):
                list_of_readings[i][0] = '--'

            j = i
            repeated = 0

            while(j != 0 and repeated < 2):
                if(list_of_readings[j-1][1] != '--'):
                    if(list_of_readings[i][1] == list_of_readings[j-1][1]):
                        repeated += 1
                    else:
                        break
                j-=1

            if(repeated == 2):
                list_of_readings[i][1] = '--'

    return list_of_readings

def reading_random(list_of_readings):
    #CHECK: if the values are too diferent from the previous valid value discard it

    for i in range(len(list_of_readings)-1, -1, -1):
        if(i > 0):
            if(list_of_readings[i][0] != '--' and list_of_readings[i][1] != '--'):
                j = i
                while(j != 0):
                    if(list_of_readings[j-1][0] != '--'):
                        previous_difference = round(math.fabs(list_of_readings[i][0] - list_of_readings[j-1][0]), 5)
                        admitted_difference = round(list_of_readings[j-1][0]*admitted_percentage, 5)
                        if(previous_difference > admitted_difference):
                            list_of_readings[i][0] = '--'
                        break
                    j-=1

                j = i
                while(j != 0):
                    if(list_of_readings[j-1][1] != '--'):
                        previous_difference = round(math.fabs(list_of_readings[i][1] - list_of_readings[j-1][1]), 5)
                        admitted_difference = round(list_of_readings[j-1][1]*admitted_percentage, 5)
                        if(previous_difference > admitted_difference):
                            list_of_readings[i][1] = '--'
                        break
                    j-=1

            elif(list_of_readings[i][0] != '--'):
                j = i
                while(j != 0):
                    if(list_of_readings[j-1][0] != '--'):
                        previous_difference = round(math.fabs(list_of_readings[i][0] - list_of_readings[j-1][0]), 5)
                        admitted_difference = round(list_of_readings[j-1][0]*admitted_percentage, 5)
                        if(previous_difference > admitted_difference):
                            list_of_readings[i][0] = '--'
                        break
                    j-=1
            elif(list_of_readings[i][1] != '--'):
                j = i
                while(j != 0):
                    if(list_of_readings[j-1][1] != '--'):
                        previous_difference = round(math.fabs(list_of_readings[i][1] - list_of_readings[j-1][1]), 5)
                        admitted_difference = round(list_of_readings[j-1][1]*admitted_percentage, 5)
                        if(previous_difference > admitted_difference):
                            list_of_readings[i][1] = '--'
                        break
                    j-=1

    return list_of_readings

def parse_reading(list_of_readings):
    parsed_list = []
    for entry in list_of_readings:
        if (entry[0] == '--' and entry[1] == '--'):
            parsed_list.append('FAIL')
        elif entry[0] == '--':
            parsed_list.append(entry[1])
        elif entry[1] == '--':
            parsed_list.append(entry[0])
        else:
            parsed_list.append((entry[0] + entry[1])/2)
    return parsed_list

def blood_glucose(entry_value):
    glucose_function = -3.4+1.354*entry_value+1.545*math.tan(entry_value**(0.25))
    return round(glucose_function, 5)

def glucose_for_dosage(glucose_list):
    list_for_dosage = []

    i = 2

    while i < len(glucose_list):
        if(glucose_list[i] != 'FAIL'):
            list_for_dosage.append(glucose_list[i])
        elif(glucose_list[i-1] != 'FAIL'):
            list_for_dosage.append(glucose_list[i-1])
        elif(glucose_list[i-2] != 'FAIL'):
            list_for_dosage.append(glucose_list[i-2])
        else:
            list_for_dosage.append('FAIL')

        i+=3

    return list_for_dosage

def glucose_variation(entry_value):
    glucose_variation_function = ((0.38625*(1/math.cos(entry_value**0.25)**2))/entry_value**0.75)+1.354
    return round(glucose_variation_function, 5)

def glucose_variation_variation(entry_value):
    glucose_variation_variation_function = -(0.289688*((1/math.cos(entry_value**0.25))**2))/entry_value**1.75+(0.193125*((1/math.cos(entry_value**0.25))**2)*math.tan(entry_value**0.25))/entry_value**1.5
    return round(glucose_variation_variation_function, 5)
