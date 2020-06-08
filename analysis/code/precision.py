from helper import *
import csv
import math
import matplotlib.pyplot as plt


def sAPE(value_1, value_2):
    """
    Calculate the sAPE between two single values.
    :param value_1: Float
    :param value_2: Float
    :return: Float
    """
    try:
        result = 200.0 * abs((value_2 - value_1)) / (abs(value_2) + abs(value_1))
    except ZeroDivisionError:
        # The values are both zero and the sAPE is not defined
        result = "NA"
    return result


def get_mean_absolute_scaled_error(training_values, m):
    """
    Gives the mean absolute scaled error of a time series as needed when calculating ASE.
    :param training_values: List of floats.
    :param m: Integer. Gives the frequency of the series.
    :return: Float.
    """
    n = len(training_values)
    total_seasonal_naive_error = 0
    for t in range(m, n):
        seasonal_error = abs(training_values[t] - training_values[t - m])
        total_seasonal_naive_error += seasonal_error
    mean_seasonal_naive_error = total_seasonal_naive_error / (n - m)
    return mean_seasonal_naive_error


def ASE(value_1, value_2, mean_absolute_scaled_error):
    """
    Calculate ASE where the denominator (mean_absolute_scaled_error) is already given.
    :param value_1: Float
    :param value_2: Float
    :param mean_absolute_scaled_error: Float
    :return:
    """
    absolute_error = abs(value_1 - value_2)
    try:
        result = absolute_error / mean_absolute_scaled_error
    except ZeroDivisionError:
        # ASE is not defined is this case
        result = "NA"
    return result


def compare_results_sAPE(file_1, file_2, output_path):
    """
    Takes in two files. Each file has a forecast for all the time series in the M4 competition. Writes a new file that
    contains the error between all the forecasted values. The files are expected to have a header line.
    :param file_1: String. Path to file 1
    :param file_2: String. Path to file 2
    :return: Nothing. Writes a new file with errors
    """

    file_1 = open(file_1).read().split("\n")
    file_2 = open(file_2).read().split("\n")

    # Create folders if they don't already exists and create an output file
    folders_path = remove_file_from_path(output_path)
    create_path_if_not_exists(folders_path)
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["id"] + ["F" + str(i) for i in range(1, 49)])

    for series_number in range(1, len(file_1) - 1):
        series_1 = file_1[series_number].split(",")
        series_2 = file_2[series_number].split(",")
        id_1 = remove_quotes_if_any(series_1[0])
        id_2 = remove_quotes_if_any(series_2[0])
        if id_1 != id_2:
            raise Exception("Series ids not matching")
        series_forecast_1 = series_1[1:]
        series_forecast_2 = series_2[1:]

        # Store error between the two forecasts for this series
        errors = [id_1]

        horizon = get_horizon(id_1)
        for j in range(horizon):
            # A model might not have been able to predict a value
            if series_forecast_1[j] == "NA" or series_forecast_2[j] == "NA":
                error = "NA"
            else:
                value_1 = float(series_forecast_1[j])
                value_2 = float(series_forecast_2[j])
                error = sAPE(value_1, value_2)
            errors.append(error)

        writer.writerow(errors)


def compare_results_ASE(file_1, file_2, output_path):
    """
    Takes in two files. Each file has a forecast for all the time series in the M4 competition. Writes a new file that
    contains the error between all the forecasted values. The files are expected to have a header line.
    :param file_1: String. Path to file 1
    :param file_2: String. Path to file 2
    :return: Nothing. Writes a new file with errors
    """

    file_1 = open(file_1).read().split("\n")
    file_2 = open(file_2).read().split("\n")

    # Create folders if they don't already exists and create an output file
    folders_path = remove_file_from_path(output_path)
    create_path_if_not_exists(folders_path)
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["id"] + ["F" + str(i) for i in range(1, 49)])

    for series_number in range(1, len(file_1) - 1):
        series_1 = file_1[series_number].split(",")
        series_2 = file_2[series_number].split(",")
        id_1 = remove_quotes_if_any(series_1[0])
        id_2 = remove_quotes_if_any(series_2[0])
        if id_1 != id_2:
            raise Exception("Series ids not matching")
        series_forecast_1 = series_1[1:]
        series_forecast_2 = series_2[1:]

        # Calculate the denominator in the formula. This is the mean absolute error the seasonal naive method would
        # have made on the training data.
        training_values = get_training_values(id_1)
        m = get_frequency(id_1)
        mean_seasonal_naive_error = get_mean_absolute_scaled_error(training_values, m)

        # Store error between the two forecasts for this series
        errors = [id_1]

        horizon = get_horizon(id_1)
        for j in range(horizon):
            # A model might not have been able to predict a value
            if series_forecast_1[j] == "NA" or series_forecast_2[j] == "NA":
                error = "NA"
            else:
                value_1 = float(series_forecast_1[j])
                value_2 = float(series_forecast_2[j])
                error = ASE(value_1, value_2, mean_seasonal_naive_error)
            errors.append(error)

        writer.writerow(errors)


def calculate_OWA(sMAPE_df, MASE_df, naive2_sMAPE_df, naive2_MASE_df, output_path):
    """
    Calculate OWA between two files with sMAPE and MASE values.
    :return: Nothing. Writes a file to output_path.
    """
    sMAPE_df = pd.read_csv(sMAPE_df, index_col=0)
    MASE_df = pd.read_csv(MASE_df, index_col=0)
    naive2_sMAPE_df = pd.read_csv(naive2_sMAPE_df, index_col=0)
    naive2_MASE_df = pd.read_csv(naive2_MASE_df, index_col=0)

    result = pd.DataFrame(index=resolutions + ["Total"], columns=origins + ["Total"])

    for row in result.index.values:
        for col in result.columns.values:
            sMAPE = sMAPE_df.loc[row, col]
            MASE = MASE_df.loc[row, col]
            naive2_sMAPE = naive2_sMAPE_df.loc[row, col]
            naive2_MASE = naive2_MASE_df.loc[row, col]

            relative_sMAPE = sMAPE / naive2_sMAPE
            relative_MASE = MASE / naive2_MASE

            OWA = 0.5 * (relative_sMAPE + relative_MASE)

            result.at[row, col] = OWA

    # Create folders if they don't already exists and create an output file
    folders_path = remove_file_from_path(output_path)
    create_path_if_not_exists(folders_path)
    result.to_csv(output_path, na_rep="NA")


def compare_files(file_1, file_2, output_path):
    """
    Takes in two files. For each entry, calculate the difference between the files: file_1[entry] - file_2[entry]
    """
    df_1 = pd.read_csv(file_1, index_col=0)
    df_2 = pd.read_csv(file_2, index_col=0)

    result = pd.DataFrame(index=resolutions + ["Total"], columns=origins + ["Total"])

    for row in result.index.values:
        for col in result.columns.values:
            value_1 = df_1.loc[row, col]
            value_2 = df_2.loc[row, col]
            diff = value_1 - value_2
            if not math.isnan(diff):
                diff = "%.5f" % diff
            result.at[row, col] = diff

    # Create folders if they don't already exists and create an output file
    folders_path = remove_file_from_path(output_path)
    create_path_if_not_exists(folders_path)
    result.to_csv(output_path, na_rep="NA")


def compare_original_and_rerun_OWA(methods, data, cut_axis, output_path):
    """
    Calculates the difference in OWA between a list of original submissions and reruns of the same methods. Display the results with a graph.
    :param reruns: List of strings.. e.g. ["036/computer-a", "069/computer-a", "118/computer-a"]
    :param data: String. A resolution, origin or "All". E.g. "Yearly", "Finance" or "All"
    :return:
    """

    original_OWAs = []
    rerun_OWAs = []
    method_ids = []

    for reruns in methods:
        method_id = reruns.split("/")[0]
        computer_letter = reruns.split("/")[1][-1].upper()
        method_ids.append(method_id + "-" + computer_letter)
        path_to_original = "../results/" + method_id + "/original/comparison-to-test-set/OWA.csv"
        path_to_reruns = "../results/" + reruns + "/comparison-to-test-set/OWA.csv"

        original_df = pd.read_csv(path_to_original, index_col=0)
        reruns_df = pd.read_csv(path_to_reruns, index_col=0)

        if data in resolutions:
            resolution = data
            origin = "Total"
        elif data in origins:
            resolution = "Total"
            origin = data
        elif data == "All":
            resolution = "Total"
            origin = "Total"
        else:
            raise Exception("Data should be a resolution, origin or 'All', but was " + data)

        OWA_original = original_df.loc[resolution, origin]
        OWA_reruns = reruns_df.loc[resolution, origin]

        original_OWAs.append(OWA_original)
        rerun_OWAs.append(OWA_reruns)

    # Sort from lowest to highest original OWA
    sorted_OWAs = [[x, y, z] for x, y, z in sorted(zip(original_OWAs, rerun_OWAs, method_ids))]
    original_OWAs = [values[0] for values in sorted_OWAs]
    rerun_OWAs = [values[1] for values in sorted_OWAs]
    method_ids = [values[2] for values in sorted_OWAs]

    plt.scatter(method_ids, original_OWAs, label="Original submission")
    plt.scatter(method_ids, rerun_OWAs, label="Average of reruns", marker="x")
    plt.xticks(rotation=70)
    if not cut_axis:
        plt.ylim(0, max([max(original_OWAs), max(rerun_OWAs)]) * 1.2)
        suffix = ""
    else:
        suffix = "-truncated"
    plt.ylabel("OWA")
    plt.legend()

    # Create folders if they don't already exists and create an output file
    folders_path = remove_file_from_path(output_path)
    create_path_if_not_exists(folders_path)

    plt.savefig(output_path + "-" + data + suffix, bbox_inches='tight', pad_inches=0.03)
    plt.close()
