import csv
from statistics import mean, stdev


def get_coefficient_of_variation(output_path, *files):
    """
    Given a set of forecasts for a number of time series several steps ahead in time, calculate the coefficient of variation between all the predicted values for each step in the forecasting horizon for each time series.
    :param output_path: String. The path to the destination where a new file will be created with all the coefficients of variation.
    :param files: A number of strings. The strings are paths to different forecasts.
    :return: Nothing. A new file is created in output_path with the result.
    """

    # Creates an output file for the final result
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["id"] + ["F" + str(i) for i in range(1, 49)])

    reruns = []
    for file in files:
        reruns.append(open(file).read().split("\n"))

    # For each time series
    for series in range(1, len(reruns[0])):

        # Get the id of this series for the first rerun to later check that the id is equal for all reruns
        series_id = reruns[0][series].split(",")[0]

        horizon = [i for i in reruns[0][series].split(",")[1:] if i != "" and i != "NA"]

        # Creating a list for saving the coefficients of variation for this series
        coefficients_of_variation = []

        # For each step in the forecasting horizon
        for step in range(1, len(horizon) + 1):

            # Save the different forecasts in a list to later find the coefficient of variation between them
            predicted_values = []

            # For each rerun
            for rerun in reruns:
                series_id_this_rerun = rerun[series].split(",")[0]

                # Check that all the ids are equal
                if series_id_this_rerun != series_id:
                    raise Exception("Series ids are not equal.")

                # Add the forecast
                predicted_value = float(rerun[series].split(",")[step])
                predicted_values.append(predicted_value)

            coefficient_of_variation = stdev(predicted_values) / mean(predicted_values)
            coefficients_of_variation.append(coefficient_of_variation)

        # Write the coefficients of variation for the given series to file
        writer.writerow([series_id] + coefficients_of_variation)

