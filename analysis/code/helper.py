import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from matplotlib import collections as matcoll

resolutions = ["Yearly", "Quarterly", "Monthly", "Weekly", "Daily", "Hourly"]
origins = ["Demographic", "Finance", "Industry", "Macro", "Micro", "Other"]

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

frequency = {
    "Yearly": 1,
    "Quarterly": 4,
    "Monthly": 12,
    "Weekly": 1,
    "Daily": 1,
    "Hourly": 24
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


def get_origin(id):
    id = remove_quotes_if_any(id)
    resolution_letter = id[0]
    number = int(id[1:])
    if resolution_letter == "Y":
        if 1 <= number <= 3903:
            return "Macro"
        elif 3904 <= number <= 10441:
            return "Micro"
        elif 10442 <= number <= 11529:
            return "Demographic"
        elif 11530 <= number <= 15245:
            return "Industry"
        elif 15246 <= number <= 21764:
            return "Finance"
        elif 21765 <= number <= 23000:
            return "Other"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    elif resolution_letter == "Q":
        if 1 <= number <= 5315:
            return "Macro"
        elif 5216 <= number <= 11335:
            return "Micro"
        elif 11336 <= number <= 13193:
            return "Demographic"
        elif 13194 <= number <= 17830:
            return "Industry"
        elif 17831 <= number <= 23135:
            return "Finance"
        elif 21136 <= number <= 24000:
            return "Other"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    elif resolution_letter == "M":
        if 1 <= number <= 10016:
            return "Macro"
        elif 10017 <= number <= 20991:
            return "Micro"
        elif 20992 <= number <= 26719:
            return "Demographic"
        elif 26720 <= number <= 36736:
            return "Industry"
        elif 36737 <= number <= 47723:
            return "Finance"
        elif 47724 <= number <= 48000:
            return "Other"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    elif resolution_letter == "W":
        if 1 <= number <= 12:
            return "Other"
        elif 13 <= number <= 53:
            return "Macro"
        elif 54 <= number <= 59:
            return "Industry"
        elif 60 <= number <= 223:
            return "Finance"
        elif 224 <= number <= 247:
            return "Demographic"
        elif 248 <= number <= 359:
            return "Micro"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    elif resolution_letter == "D":
        if 1 <= number <= 127:
            return "Macro"
        elif 128 <= number <= 1603:
            return "Micro"
        elif 1604 <= number <= 1613:
            return "Demographic"
        elif 1614 <= number <= 2035:
            return "Industry"
        elif 2036 <= number <= 3594:
            return "Finance"
        elif 3595 <= number <= 4227:
            return "Other"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    elif resolution_letter == "H":
        if 1 <= number <= 414:
            return "Other"
        else:
            raise Exception("This id does not exist: " + resolution_letter + str(number))
    else:
        raise Exception("This id does not exist: " + resolution_letter + str(number))


def get_frequency(id):
    resolution = get_resolution(id)
    return frequency[resolution]


def get_horizon(id):
    resolution = get_resolution(id)
    return horizon[resolution]


def get_training_values(id):
    """
    Given a series id, e.g. "Y12333", gives all training values for that series.
    :param id: String. E.g. "Y12333"
    :return: A list of floats.
    """
    id = remove_quotes_if_any(id)
    training_set = open("../../data/training/all.csv")
    current_id = ""
    while current_id != id:
        current_line = training_set.readline()
        current_id = remove_quotes_if_any(current_line.split(",")[0])
    training_values = [float(remove_quotes_if_any(i)) for i in current_line.split(",")[1:] if i.strip() != ""]
    return training_values


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
        values = [float(i) for i in series_forecast[1:] if i != "NA" and i != ""]
        for value in values:
            sum += value
            number_of_values += 1

    average = sum / number_of_values

    output_file = open(output_path, "w")
    output_file.write(str(average))


def get_average_each_series(path, output_path):
    """
    Given the path to a file with one value for each forecasted value for each time series, like the one
    generated in compare_results. Calculates the average of all the values for each series.
    :param path: String. Path to file
    :param output_path: String. Path to file in which to write the result.
    :return: Nothing
    """
    # Makes file ready to be written to
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["id", "value"])

    reader = csv.reader(open(path))

    # Skip header line
    next(reader)

    for series_forecast in reader:
        series_id = series_forecast[0]
        horizon = get_horizon(series_id)
        values = series_forecast[1:horizon+1]
        sum = 0
        for value in values:
            if value == "NA":
                sum = "NA"
                break
            else:
                sum += float(value)
        try:
            average = sum / horizon
        except TypeError:
            # Sum is not available
            average = "NA"
        writer.writerow([series_id, average])


def get_share_less_than(path, threshold, output_path):
    """
    Takes in a path to a file with one value for each series, such as the one created in get_average_each_series().
    Calculated the share of the values that are below or equal to a given threshold
    :param path:
    :param threshold:
    :param output_path: String of the form "path/to/save/share-less-than-". The threshold will be appended to the filename in addition to a .txt suffix.
    :return:
    """
    total = 0
    less_than_threshold = 0

    reader = csv.reader(open(path))
    next(reader)  # Skip the header line
    for series in reader:
        total += 1
        value = series[1]
        try:
            value = float(value)
        except ValueError:
            if value == "NA":
                continue
            raise Exception("The value %s could not be converted to float" % value)
        if value <= threshold:
            less_than_threshold += 1

    share = float(less_than_threshold) / total

    output_file = open(output_path + str(threshold) + ".txt", "w")
    output_file.write(str(share))


def get_average_of_text_files(paths, output_path):
    """
    Given a list of paths to text files containing only one single number, such as the file produced by get_share_less_than(), calculates the average of those values.
    :param paths: List of paths
    :param output_path: Writes the result to this path
    :return:
    """
    values_to_average = []

    for path in paths:
        values_to_average.append(float(open(path, "r").read()))

    average = float(sum(values_to_average)) / len(values_to_average)
    rounded = round(average, 2)

    open(output_path, "w").write(str(rounded))


def get_average_resolution_origin(path, output_path):
    """
    Takes in a path to a file with one value for each series such as the one created in get_average_each_series().
    For each combination of resolution and origin, calculates the average value for all the series in that category.
    :param path: String. Path to file with one value for each series.
    :param output_path: String. Where to write the result.
    :return: Nothing.
    """
    # A dataframe is created to keep track of the values for the different resolutions and origins
    all_values = pd.DataFrame(index=resolutions, columns=origins)

    # The data frame is filled with empty lists
    for resolution in resolutions:
        for origin in origins:
            all_values.at[resolution, origin] = []

    # Each series' value is put in the correct field in the dataframe
    reader = csv.reader(open(path))
    next(reader)  # Skip the header line
    for series in reader:
        series_id = series[0]
        resolution = get_resolution(series_id)
        origin = get_origin(series_id)
        value = series[1]
        list = all_values.loc[resolution, origin]
        try:
            list.append(float(value))
        except ValueError:
            # Value may not be available
            pass

    # A dataframe for the final result is created
    # For all combinations of resolutions and origins, the average is calculated and written to the result
    result = pd.DataFrame(index=resolutions + ["Total"], columns=origins + ["Total"])
    for resolution in resolutions:
        for origin in origins:
            values = all_values.loc[resolution, origin]
            try:
                average = sum(values) / len(values)
            except ZeroDivisionError:
                # There are no time series with this resolution and origin
                average = "NA"
            result.at[resolution, origin] = average

    # For all resolutions, the average value for that resolution is calculated and written to the result
    for resolution in resolutions:
        values = []
        for origin in origins:
            values = values + all_values.loc[resolution, origin]
        average = sum(values) / len(values)
        result.at[resolution, "Total"] = average

    # For all origins, the average value for that resolution is calculated and written to the result
    for origin in origins:
        values = []
        for resolution in resolutions:
            values = values + all_values.loc[resolution, origin]
        average = sum(values) / len(values)
        result.at["Total", origin] = average

    # The average of all values is calculated and written to the result
    values = []
    for resolution in resolutions:
        for origin in origins:
            values = values + all_values.loc[resolution, origin]
    average = sum(values) / len(values)
    result.at["Total", "Total"] = average

    # Write the final result to file
    result.to_csv(output_path)


def get_value_for_each_timestep(path, output_path):
    """
    For each timestep ahead in time, calculate the average value for this timestep. Could for instance be the average of
    sAPE values, ASE values or OWA values.
    Since time series with different resolutions have different length of the forecasting horizon we will sort on
    resolution.
    :param path: String. Path to a file with resolution for each timestep on each series
    :return: Writes a new file with average values for each series on each timestep
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
        "Yearly": [0] * 6,
        "Quarterly": [0] * 8,
        "Monthly": [0] * 18,
        "Weekly": [0] * 13,
        "Daily": [0] * 14,
        "Hourly": [0] * 48
    }

    # Sum up the values for each timestep on each resolution
    for series_forecast in reader:
        # Sometimes there's a newline in the end of the file
        if len(series_forecast) == 1:
            break
        id = series_forecast[0]
        resolution = get_resolution(id)
        horizon = get_horizon(id)
        values = []
        resolution_count_incrementer = []
        for i in series_forecast[1:horizon + 1]:
            if remove_quotes_if_any(i) == "NA":
                values.append(0)
                resolution_count_incrementer.append(0)
            else:
                values.append(float(i))
                resolution_count_incrementer.append(1)

        sums[resolution] = np.add(sums[resolution], values)
        resolution_count[resolution] = np.add(resolution_count[resolution], resolution_count_incrementer)

    # Write to file
    output_file = open(output_path, "w")
    writer = csv.writer(output_file)
    writer.writerow(["resolution"] + ["F" + str(i) for i in range(1, 49)])

    for resolution in resolutions:
        resolution_average = []
        for h in range(len(resolution_count[resolution])):
            sum_values = sums[resolution][h]
            number_of_this_resolution_horizon = resolution_count[resolution][h]
            average = sum_values / number_of_this_resolution_horizon
            resolution_average.append(average)
        writer.writerow([resolution] + resolution_average)


def resolution_timestep_graph(path, output_path, y_label):
    """
    Given a path to a file with a value (for instance average sMAPE) for each resolution and each timestep (like the one
    made by get_value_for_each_timestep), creates a graph for this.
    :param path: String. Path to a file with value for each resolution and each timestep (like the one made by
    get_value_for_each_timestep)
    :return: Nothing. Writes a file to output_path.
    """
    reader = csv.reader(open(path))

    # Skip header line
    next(reader)

    # For each resolution
    for resolution_values in reader:
        resolution = resolution_values[0]
        values = []
        for i in resolution_values[1:]:
            try:
                value = float(i)
            except ValueError:
                value = math.nan
            values.append(value)

        # Plot the graph for this resolution
        plt.plot(range(1, len(values) + 1), values, label=resolution)

    # plt.xlabel("Timestep after last observed value")
    # plt.ylabel(y_label)
    plt.legend()
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()


def get_average_values_for_all_reruns(output_path, input_files):
    """
    Given a set of files containing values (for instance sMAPE values), creates a new file giving the average values of
    every entry in those files.
    :param output_path: String. Path to write the output file.
    :param input_files: List of strings. Each element in the list is a string with a path to a csv file containing values (for instance sAPE values) for all timesteps and all series between two
    forecasts (or a forecast and a test set). This kind of file can be generated by get_average_resolution_origin()
    :return: Writes a file to output_path of the same format like the input_files. In every field in the new file is
    the average of the corresponding fields in the input_files.
    """
    # Write the different files to dataframes
    reruns = []
    for file in input_files:
        reruns.append(pd.read_csv(file, index_col=0))

    index = reruns[0].index.values
    columns = reruns[0].columns.values

    # Creates an output file for the final result
    result_df = pd.DataFrame(index=index, columns=columns)

    # Calculate the average of the reruns for each entry
    for i in index:
        for c in columns:
            values = []
            for rerun in reruns:
                values.append(rerun.loc[i, c])
            average = sum(values) / len(values)
            if math.isnan(average):
                average = "NA"
            result_df.at[i, c] = average

    # Write to csv
    result_df.to_csv(output_path)


def scatterplot(path, output_path):
    """
    Creates a scatter plot from a csv file such as the one produced by get_average_resolution_origin().
    Scatter each resoliution, origin and the total.
    :param path:
    :param output_path:
    :return:
    """
    df = pd.read_csv(path, index_col=0)

    resolutions = df.index.values.tolist()
    origins = df.columns.values.tolist()
    resolutions.remove("Total")
    origins.remove("Total")

    x = []
    y = []

    for resolution in resolutions:
        x.append(resolution)
        y.append(df.loc[resolution, "Total"])
    for origin in origins:
        x.append(origin)
        y.append(df.loc["Total", origin])
    x.append("Total")
    y.append(df.loc["Total", "Total"])

    lines = []
    for i in range(len(x)):
        pair = [(i, 0), (i, y[i])]
        lines.append(pair)

    linecoll = matcoll.LineCollection(lines)
    fig, ax = plt.subplots()
    ax.add_collection(linecoll)

    plt.scatter(x, y)
    plt.xticks(rotation=70)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.01)
    plt.close()


def scatterplot_from_paths(prefix, list_of_ids, suffix, output_path):
    """
    Creates a scatter plt from the values found in different paths
    :param prefix: String. E.g. "../results/"
    :param list_of_ids: List of strings with methods. E.g. ["036/computer-a", "039/computer-b"]
    :param suffix: String. E.g. "/comparison-to-original-submission/sMAPE-average.txt"
    :param output_path: String. Where to save the plot.
    :return:
    """
    x = []
    y = []

    for method in list_of_ids:
        path = prefix + method + suffix
        value = float(open(path, "r").read())
        method_name = method.split("/")[0] + "-" + method.split("/")[1][-1].upper()
        x.append(method_name)
        y.append(value)

    lines = []
    for i in range(len(x)):
        pair = [(i, 0), (i, y[i])]
        lines.append(pair)

    linecoll = matcoll.LineCollection(lines)
    fig, ax = plt.subplots()
    ax.add_collection(linecoll)

    plt.scatter(x, y)
    plt.xticks(rotation=70)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.03)
    plt.close()
