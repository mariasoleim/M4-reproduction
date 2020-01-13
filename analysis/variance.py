import pandas as pd
import csv
from statistics import mean, pstdev
import matplotlib.pyplot as plt

resolutions = ["Yearly", "Quarterly", "Monthly", "Weekly", "Daily", "Hourly"]

resolution_count = {
    "Yearly": 23000,
    "Quarterly": 24000,
    "Monthly": 48000,
    "Weekly": 359,
    "Daily": 4227,
    "Hourly:": 414,
    "Total": 100000
}

horizon = {
    "Yearly": 6,
    "Quarterly": 8,
    "Monthly": 18,
    "Weekly": 13,
    "Daily": 14,
    "Hourly:": 48
}

def remove_quotes_if_any(word):
    """
    Removes all quotes from a string
    """
    out_word = ""
    for char in word:
        if char != "\"":
            out_word += char
    return out_word


def get_predicted_values(resolution, time_series_id, number_in_horizon):
    """
    Get all the predicted values with a specific resolution, time series id a certain number,
    number_in_horizon, after the last observed value
    :param resolution: A string, either "Yearly", "Quarterly", "Monthly", "Weekly", "Daily" or "Hourly"
    :param time_series_id: A string with the id of the series in which the average should be calculated
    :param number_in_horizon: An integer, the specific timestep succeeding the last observed value. E.g. a number in the
    range 1-13 for weekly series.
    :return:
    """
    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")

    values = []
    for rerun_id in range(1, 6):
        path_to_results = "../reproduced-results/rerun-" + str(rerun_id) + "/" + resolution + "Forec.csv"
        with open(path_to_results) as results:
            for line in results:
                line = line.split(",")
                if remove_quotes_if_any(line[0]) == time_series_id:
                    value = line[number_in_horizon]
                    values.append(float(value))
    return values


def average_and_standard_deviation(resolution):
    averages = []
    standard_deviations = []
    coefficients_of_variation = []
    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")
    for series_count in range(1, resolution_count[resolution] + 1):
        series_id = resolution[0] + str(series_count)
        averages_for_series = [series_id]
        standard_deviations_for_series = [series_id]
        coefficients_of_variation_for_series = [series_id]
        for number_in_horizon in range(1, horizon[resolution] + 1):
            predicted_values = get_predicted_values(resolution, series_id, number_in_horizon)
            average = mean(predicted_values)
            averages_for_series.append(average)
            standard_deviation = pstdev(predicted_values)
            standard_deviations_for_series.append(standard_deviation)
            coefficient_of_variation = standard_deviation / average
            coefficients_of_variation_for_series.append(coefficient_of_variation)
        averages.append(averages_for_series)
        standard_deviations.append(standard_deviations_for_series)
        coefficients_of_variation.append(coefficients_of_variation_for_series)

    with open("../reproduced-results/analysis-results/" + resolution + "/averages.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in averages:
            writer.writerow(row)

    with open("../reproduced-results/analysis-results/" + resolution + "/standard-deviations.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in standard_deviations:
            writer.writerow(row)

    with open("../reproduced-results/analysis-results/" + resolution + "/coefficients_of_variation.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in coefficients_of_variation:
            writer.writerow(row)


def coefficient_of_variation_each_timestep(resolution):
    coefficients = pd.read_csv("../reproduced-results/analysis-results/" + resolution +
                               "/coefficients_of_variation.csv", header=None, index_col=0)
    averages = []
    for i in range(1, horizon[resolution] + 1):
        coefficients_at_step = coefficients[i].tolist()
        average = mean(coefficients_at_step)
        averages.append(average)

    with open("../reproduced-results/analysis-results/" + resolution + "/average_coefficient_of_variation.csv", "w") \
            as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(averages)

    plt.plot(range(1, horizon[resolution] + 1), averages)
    plt.xlabel("Timestep after last observed value")
    plt.ylabel("Average coefficient of variation")
    plt.savefig("../reproduced-results/analysis-results/" + resolution + "/coefficient_of_variation.png")
    plt.show()


coefficient_of_variation_each_timestep("Weekly")
