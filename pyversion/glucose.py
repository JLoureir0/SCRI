import math

def blood_glucose(entry_value):
    glucose_function = -3.4+1.354*entry_value+1.545*math.tan(entry_value**(0.25))
    return round(glucose_function, 5)
