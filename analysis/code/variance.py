import csv
from statistics import mean, pstdev
import matplotlib.pyplot as plt
from helper import *


def average_and_standard_deviation(submission_id, resolution):
    if isinstance(submission_id, int):
        submission_id = str(submission_id)
    averages = []
    standard_deviations = []
    coefficients_of_variation = []
    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")
    for series_count in range(1, resolution_count[resolution] + 1):
        print(str(series_count) + " / " + str(resolution_count[resolution] + 1))
        series_id = resolution[0] + str(series_count)
        averages_for_series = [series_id]
        standard_deviations_for_series = [series_id]
        coefficients_of_variation_for_series = [series_id]
        for number_in_horizon in range(1, horizon[resolution] + 1):
            predicted_values = get_predicted_values(submission_id, resolution, series_id, number_in_horizon)
            average = mean(predicted_values)
            averages_for_series.append(average)
            standard_deviation = pstdev(predicted_values)
            standard_deviations_for_series.append(standard_deviation)
            try:
                coefficient_of_variation = standard_deviation / average
            except ZeroDivisionError:
                # The average of the predicted values for this series at this timestep is zero
                # The coefficient of variation is not defined
                # If the standard deviation also is zero, then we define the coefficient of variation to be zero (this
                # differs from the original definition)
                if standard_deviation == 0:
                    coefficient_of_variation = 0
                else:
                    raise ValueError(
                        "The coefficient of variation is not defined for a standard deviation of %f and an average of "
                        "%f" % (standard_deviation, average))
            coefficients_of_variation_for_series.append(coefficient_of_variation)
        averages.append(averages_for_series)
        standard_deviations.append(standard_deviations_for_series)
        coefficients_of_variation.append(coefficients_of_variation_for_series)

    with open("../results/" + submission_id + "/" + resolution + "/averages.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in averages:
            writer.writerow(row)

    with open("../results/" + submission_id + "/" + resolution + "/standard-deviations.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in standard_deviations:
            writer.writerow(row)

    with open("../results/" + submission_id + "/" + resolution + "/coefficients_of_variation.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for row in coefficients_of_variation:
            writer.writerow(row)


def coefficient_of_variation_each_timestep(submission_id, resolution):
    if isinstance(submission_id, int):
        submission_id = str(submission_id)
    coefficients = pd.read_csv("../results/" + submission_id + "/" + resolution +
                               "/coefficients_of_variation.csv", header=None, index_col=0)
    averages = []
    for i in range(1, horizon[resolution] + 1):
        coefficients_at_step = coefficients[i].tolist()
        average = mean(coefficients_at_step)
        averages.append(average)

    with open("../results/" + submission_id + "/" + resolution + "/average_coefficient_of_variation.csv", "w") \
            as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(averages)

    plt.plot(range(1, horizon[resolution] + 1), averages, label=resolution)
    plt.xlabel("Timestep after last observed value")
    plt.ylabel("Average coefficient of variation")
    plt.legend(loc='best')
    plt.savefig("../results/" + submission_id + "/" + resolution + "/coefficient_of_variation.png")
    plt.show()

average_and_standard_deviation(237, "Yearly")
coefficient_of_variation_each_timestep(237, "Yearly")
