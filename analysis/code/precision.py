from helper import *
import csv
import matplotlib.pyplot as plt
import numpy as np


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


def get_average_sMAPE(path):
    """
    Given the path to a file with one sMAPE value for each forecasted value for each time series, like the one
    generated in compare_results. Gives the average of all those values.
    :param path: string, path to file
    :return:
    """
    reader = csv.reader(open(path))

    # Skip header line
    next(reader)

    # Create variable to keep track of the sum
    sum = 0

    # Create variable to keep track of number of values
    number_of_values = 0

    for series_forecast in reader:
        sMAPEs = [float(i) for i in series_forecast[1:] if i != "NA" or i != ""]
        for sMAPE in sMAPEs:
            sum += sMAPE
            number_of_values += 1

    average_sMAPE = sum / number_of_values
    return average_sMAPE


def get_sMAPE_for_each_timestep(path, output_path):
    """
    For each timestep ahead in time, calculate the average sMAPE for this timestep.
    Since time series with different resolutions have different length of the forecasting horizon we will sort on
    resolution.
    :param path: string. Path to a file with resolution for each timestep on each series
    :return: Writes a new file with average sMAPE for each series on each timestep
    """
    reader = csv.reader(open(path))

    # Skip header line
    next(reader)

    sums = {
        "Yearly": [0] * 6,
        "Quarterly": [0] * 8,
        "Monthly": [0] * 18,
        "Weekly": [0] * 13,
        "Daily": [0] * 14,
        "Hourly": [0] * 48
    }

    resolution_count = {
        "Yearly": 0,
        "Quarterly": 0,
        "Monthly": 0,
        "Weekly": 0,
        "Daily": 0,
        "Hourly": 0
    }

    # Sum up the sMAPEs for each timestep on each resolution
    for series_forecast in reader:
        id = series_forecast[0]
        resolution = get_resolution(id)
        sMAPEs = [float(i) for i in series_forecast[1:] if i != "NA" or i != ""]
        sums[resolution] = np.add(sums[resolution], sMAPEs)
        resolution_count[resolution] += 1

    # Write to file
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["resolution"] + ["F" + str(i) for i in range(1, 49)])

    for resolution in resolutions:
        number_of_this_resolution = resolution_count[resolution]
        sum_sMAPEs = sums[resolution]
        averages = [i / number_of_this_resolution for i in sum_sMAPEs]
        writer.writerow([resolution] + averages)


def resolution_timestep_sMAPE_graph(path, output_path):
    """
    Given a path to a file with average sMAPE for each resolution and each timestep (like the one made by
    get_sMAPE_for_each_timestep), creates a graph for this.
    :param path:
    :return:
    """
    reader = csv.reader(open(path))

    # Skip header line
    next(reader)


    # For each resolution
    for resolution_sMAPEs in reader:
        resolution = resolution_sMAPEs[0]
        sMAPEs = [float(i) for i in resolution_sMAPEs[1:]]

        # Plot the graph for this resolution
        plt.plot(range(1, len(sMAPEs) + 1), sMAPEs, label=resolution)

    plt.xlabel("Timestep after last observed value")
    plt.ylabel("Average sMAPE")
    plt.legend(loc='best')
    plt.savefig(output_path)
    plt.clf()
