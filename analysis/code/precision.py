from helper import *
from statistics import mean
import csv
import matplotlib.pyplot as plt


def sMAPE(predicted, actual):
    """
    :param predicted: float
    :param actual: float
    :return: float
    """
    return 200.0 * abs((actual - predicted)) / (abs(actual) + abs(predicted))


def get_sMAPE_for_timesteps(submission_id, resolution):
    if isinstance(submission_id, int):
        submission_id = str(submission_id)
    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")
    average_sMAPEs_for_timesteps = []
    for timestep_in_horizon in range(1, horizon[resolution] + 1):
        print(str(timestep_in_horizon) + " / " + str(horizon[resolution] + 1))
        sMAPEs_for_timestep = []
        for series_count in range(1, resolution_count[resolution] + 1):
            series_id = resolution[0] + str(series_count)
            predicted_values = get_predicted_values(submission_id, resolution, series_id, timestep_in_horizon)
            real_value = get_real_value(resolution, series_id, timestep_in_horizon)
            for prediction in predicted_values:
                sMAPE_value = sMAPE(prediction, real_value)
                sMAPEs_for_timestep.append(sMAPE_value)
        average_sMAPE_this_timestep = mean(sMAPEs_for_timestep)
        average_sMAPEs_for_timesteps.append(average_sMAPE_this_timestep)

    with open("../results/" + submission_id + "/" + resolution + "/average_sMAPE.csv", "w") \
            as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(average_sMAPEs_for_timesteps)

    plt.plot(range(1, horizon[resolution] + 1), average_sMAPEs_for_timesteps, label=resolution)
    plt.xlabel("Timestep after last observed value")
    plt.ylabel("Average sMAPE")
    plt.legend(loc='best')
    plt.savefig("../results/" + submission_id + "/" + resolution + "/sMAPE")
    plt.show()


get_sMAPE_for_timesteps(237, "Weekly")
