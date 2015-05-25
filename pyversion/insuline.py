import glucose as glu

glucose_limit       = 6
glucose_trend_limit = -0.4
glucose_history_len = 5

def calculate_dosages(list_of_readings):
    list_for_dosage                     = glu.glucose_values(list_of_readings, 0)
    list_for_dosage_variation           = glu.glucose_values(list_of_readings, 1)
    list_for_dosage_variation_variation = glu.glucose_values(list_of_readings, 2)

    list_of_dosages = []
    list_of_trends  = calculate_trends(list_for_dosage)

    ic = 0

    for index, glucose in enumerate(list_for_dosage):
        if glucose == 'FAIL':
            list_of_dosages.append('FAIL')
        elif glucose < glucose_limit:
            list_of_dosages.append(0)
            ic = 0.9*ic
        elif list_of_trends[index] < glucose_trend_limit:
            list_of_dosages.append(0)
            ic = 0.9*ic
        else:
            dosage = int(round(0.8*glucose+0.2*list_for_dosage_variation[index]+0.5*list_for_dosage_variation_variation[index]-ic))
            if dosage < 0:
                list_of_dosages.append(0)
            else:
                list_of_dosages.append(dosage)

            ic = dosage+0.9*ic

    return list_of_dosages

def calculate_trends(list_for_dosage):
    list_of_trends = []
    glucose_history = []

    for glucose in list_for_dosage:
        if not list_of_trends:
            list_of_trends.append(0)
            glucose_history.append(glucose)
        elif glucose == 'FAIL':
            list_of_trends.append('FAIL')
        else:
            trend = round((glucose-glucose_history[0])/float(len(glucose_history)), 5)

            list_of_trends.append(trend)

            if len(glucose_history) < glucose_history_len:
                glucose_history.append(glucose)
            else:
                glucose_history.pop(0)
                glucose_history.append(glucose)

    return list_of_trends
