import math

admitted_percentage = 0.3
sync_tolerance      = 3

def glucose_values(list_of_readings):
    try:
        reading_out_of_sync(list_of_readings)
        reading_stuck_at(list_of_readings)
        reading_random(list_of_readings)
        reading_out_of_range(list_of_readings)

        parsed_list = parse_reading(list_of_readings)

        for index, reading in enumerate(parsed_list):
            if(reading != 'FAIL'):
                #CHECK: memory check for the glucose function
                if(blood_glucose(1) == 0.36019):
                    parsed_list[index] = blood_glucose(reading)
                else:
                    raise ValueError('Memory corrupted')

        return parsed_list
    except ValueError, e:
        raise e

def blood_glucose(entry_value):
    glucose_function = -3.4+1.354*entry_value+1.545*math.tan(entry_value**(0.25))
    return round(glucose_function, 5)

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

def out_of_range(entry_value):
    #CHECK: range for entry_value

    if (entry_value < 1 or entry_value > 5):
        return '--'
    return entry_value

def reading_out_of_range(list_of_readings):
    for entry in list_of_readings:
        entry[0] = out_of_range(entry[0])
        entry[1] = out_of_range(entry[1])
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

def reading_out_of_sync(list_of_readings):
    #CHECK: if the values from the sensor are too different from each other raise an exception

    tolerance = 0

    for reading in list_of_readings:
        entry_difference = round(math.fabs(reading[0] - reading[1]), 5)
        admitted_difference1 = round(reading[0]*admitted_percentage, 5)
        admitted_difference2 = round(reading[1]*admitted_percentage, 5)
        if(entry_difference > admitted_difference1 or entry_difference > admitted_difference2):
            tolerance += 1
        else:
            tolerance -= 1

    if(tolerance >= sync_tolerance):
        raise ValueError('Sensors malfunctioning')

    return list_of_readings
