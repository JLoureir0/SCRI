import sys
import itertools
import math

admitted_deviation = 2

def main():
    try:
        dosage_v1 = [line.strip() for line in open(sys.argv[1])]
        dosage_v2 = [line.strip() for line in open(sys.argv[2])]
        dosage_v3 = [line.strip() for line in open(sys.argv[3])]

        dosage_list = vote_dosage(dosage_v1, dosage_v2, dosage_v3)

        output = open(sys.argv[4],'w')

        for dosage in dosage_list:
            output.write("%s\n" % dosage)

        output.close()
    except Exception, e:
        print 'usage: python voter.py v1_file v2_file v3_file output_file'

def vote_dosage(dosage_v1, dosage_v2, dosage_v3):
    dosage_list = []

    for v1, v2, v3 in itertools.izip(dosage_v1, dosage_v2, dosage_v3):

        if v1 == 'FAIL' and v2 == 'FAIL' and v3 == 'FAIL':
            dosage = 'FAIL'
        elif v2 == 'FAIL' and v3 == 'FAIL':
            dosage = int(v1)
        elif v1 == 'FAIL' and v3 == 'FAIL':
            dosage = int(v2)
        elif v1 == 'FAIL' and v2 == 'FAIL':
            dosage = int(v3)
        elif v3 == 'FAIL':
            difference = math.fabs(int(v1)-int(v2))

            if difference <= admitted_deviation:
                dosage = int(round((int(v1) + int(v2))/2.0))
            else:
                dosage = 'FAIL'
        elif v2 == 'FAIL':
            difference = math.fabs(int(v1)-int(v3))

            if difference <= admitted_deviation:
                dosage = int(round((int(v1) + int(v3))/2.0))
            else:
                dosage = 'FAIL'
        elif v1 == 'FAIL':
            difference = math.fabs(int(v2)-int(v3))

            if difference <= admitted_deviation:
                dosage = int(round((int(v2) + int(v3))/2.0))
            else:
                dosage = 'FAIL'
        else:
            difference1 = math.fabs(int(v1)-int(v2))
            difference2 = math.fabs(int(v1)-int(v3))
            difference3 = math.fabs(int(v2)-int(v3))

            condition1 = difference1 <= admitted_deviation
            condition2 = difference2 <= admitted_deviation
            condition3 = difference3 <= admitted_deviation

            if condition1 and condition2 and condition3:
                dosage = int(round((int(v1) + int(v2) + int(v3))/3.0))
            elif condition1 and condition2:
                dosage = int(round((int(v1) + int(v2))/2.0))
            elif condition1 and condition3:
                dosage = int(round((int(v1) + int(v3))/2.0))
            elif condition2 and condition3:
                dosage = int(round((int(v2) + int(v3))/2.0))
            else:
                dosage = 'FAIL'

        dosage_list.append(dosage)

    return dosage_list

if __name__ == '__main__':
    main()
