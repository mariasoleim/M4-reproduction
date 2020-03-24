import csv
import numpy as np
import matplotlib.pyplot as plt
import os

resolutions = ["Yearly", "Quarterly", "Monthly", "Weekly", "Daily", "Hourly"]

resolution_count = {
    "Yearly": 23000,
    "Quarterly": 24000,
    "Monthly": 48000,
    "Weekly": 359,
    "Daily": 4227,
    "Hourly": 414,
    "Total": 100000
}

horizon = {
    "Yearly": 6,
    "Quarterly": 8,
    "Monthly": 18,
    "Weekly": 13,
    "Daily": 14,
    "Hourly": 48
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


def remove_file_from_path(path):
    """
    Takes in a path of folders that ends with a file name. Removed the file name so that only the path of folders are left.
    E.g. "forecasts/118/rerun-1/forecsts.csv" -> "forecasts/118/rerun-1"
    :param path:
    :return:
    """
    # Remove possible slash after filename
    if path.endswith("/"):
        path = path[:-1]

    # Remove the file from path
    folders = "/".join(path.split("/")[:-1])
    return folders


def create_path_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def get_resolution(id):
    id = remove_quotes_if_any(id)
    for resolution in resolutions:
        if resolution[0] == id[0]:
            return resolution


def get_average(path, output_path):
    """
    Given the path to a file with one value for each forecasted value for each time series, like the one
    generated in compare_results. Gives the average of all those values.
    :param path: String. Path to file
    :param output_path: String. Path to file in which to write the result.
    :return: Nothing
    """
    reader = csv.reader(open(path))

    # Skip header line
    next(reader)

    # Create variable to keep track of the sum
    sum = 0

    # Create variable to keep track of number of values
    number_of_values = 0

    for series_forecast in reader:
        sMAPEs = [float(i) for i in series_forecast[1:] if i != "NA" and i != ""]
        for sMAPE in sMAPEs:
            sum += sMAPE
            number_of_values += 1

    average = sum / number_of_values

    output_file = open(output_path, "w")
    output_file.write("Average: ")
    output_file.write(str(average))


def get_value_for_each_timestep(path, output_path):
    """
    For each timestep ahead in time, calculate the average value for this timestep.
    Since time series with different resolutions have different length of the forecasting horizon we will sort on
    resolution.
    :param path: String. Path to a file with resolution for each timestep on each series
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
        # Sometimes theres a newline in the end of the file
        if len(series_forecast) == 1:
            break
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


def resolution_timestep_graph(path, output_path, y_label):
    """
    Given a path to a file with average sMAPE for each resolution and each timestep (like the one made by
    get_sMAPE_for_each_timestep), creates a graph for this.
    :param path: String. Path to a file with average sMAPE for each resolution and each timestep (like the one made by
    get_sMAPE_for_each_timestep)
    :return: Nothing. Writes a file to output_path.
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
    plt.ylabel(y_label)
    plt.legend(loc='best')
    plt.savefig(output_path)
    plt.clf()