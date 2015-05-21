import sys
import glucose

def main():
    list_of_readings = [line.strip().split() for line in open(sys.argv[1])]

    parse_list_from_file(list_of_readings)

    print glucose.glucose_values(list_of_readings)

def parse_list_from_file(list_of_readings):
    for index, reading in enumerate(list_of_readings):
        if(reading[0] != '--' and reading[1] != '--'):
            list_of_readings[index] = [float(reading[0]), float(reading[1])]
        elif(reading[0] != '--'):
            list_of_readings[index] = [float(reading[0]), reading[1]]
        elif(reading[1] != '--'):
            list_of_readings[index] = [reading[0], float(reading[1])]

    return list_of_readings

if __name__ == '__main__':
    main()
