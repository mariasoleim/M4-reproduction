from helper import *
from statistics import mean
import csv
import matplotlib.pyplot as plt
import pandas as pd


def sMAPE(value_1, value_2):
    """
    Calculate the sMAPE between two single values.
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return 200.0 * abs((value_2 - value_1)) / (abs(value_2) + abs(value_1))


def compare_results(file_1, file_2, output_path):
    """
    Takes in two files. Each file has a forecast for all the time series in the M4 competition. Writes a new file that
    contains the sMAPES between all the forecasted values. The files are expected to have a header line.
    :param file_1: path to file 1
    :param file_2: path to file 2
    :return: nothing. Writes a new file with sMAPES
    """

    file_1 = open(file_1).read().split("\n")
    file_2 = open(file_2).read().split("\n")
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["id"] + ["F" + str(i) for i in range(1, 49)])

    for series_number in range(1, len(file_1) - 1):
        series_1 = file_1[series_number].split(",")
        series_2 = file_2[series_number].split(",")
        id_1 = series_1[0]
        id_2 = series_2[0]
        if id_1 != id_2:
            raise Exception("Series ids not matching")
        series_forecast_1 = series_1[1:]
        series_forecast_2 = series_2[1:]

        # Store sMAPEs between the two forecasts for this series
        sMAPEs = [id_1]

        for j in range(len(series_forecast_1)):
            if series_forecast_1[j] == "NA" or series_forecast_1[j] == "":
                break
            value_1 = float(series_forecast_1[j])
            value_2 = float(series_forecast_2[j])
            smape = sMAPE(value_1, value_2)
            sMAPEs.append(smape)

        writer.writerow(sMAPEs)


compare_results("../../forecasts/118/rerun-1/forecast.csv", "../../forecasts/118/rerun-2/forecast.csv",
                "../../forecasts/118/comparison-delete.csv")


"""

def get_sMAPE_for_timesteps(submission_id, resolution):
    
    #Calculate the sMAPE between reruns and the original results in the competition.
    #:param submission_id: id of the method to compare original result with reruns
    #:param resolution:
    #:return:

    if isinstance(submission_id, int):
        submission_id = str(submission_id)
    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")
    average_sMAPEs_for_timesteps = []
    for timestep_in_horizon in range(1, horizon[resolution] + 1):
        print(str(timestep_in_horizon) + " / " + str(horizon[resolution])
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

    path_to_folder = "../results/" + submission_id + "/" + resolution
    create_path_if_not_exists(path_to_folder)
    with open(path_to_folder + "/average_sMAPE.csv", "w") \
            as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(average_sMAPEs_for_timesteps)

    plt.plot(range(1, horizon[resolution] + 1), average_sMAPEs_for_timesteps, label=resolution)
    plt.xlabel("Timestep after last observed value")
    plt.ylabel("Average sMAPE")
    plt.legend(loc='best')
    plt.savefig("../results/" + submission_id + "/" + resolution + "/sMAPE")
    plt.show()


#get_sMAPE_for_timesteps(237, "Yearly")
"""