import math

def blood_glucose(entry_value):
    #CHECK: range for entry_value
    if (entry_value < 1 or  entry_value > 5):
        raise ValueError('entry value must be a number between 1 and 5')

    glucose_function = -3.4+1.354*entry_value+1.545*math.tan(entry_value**(0.25))
    return round(glucose_function, 5)
