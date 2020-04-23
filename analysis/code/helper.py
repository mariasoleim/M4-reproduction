import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

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
    output_file.write("Average: ")
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
        except ValueError:
            # Sum is not available
            average = "NA"
        writer.writerow([series_id, average])


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
        list.append(float(value))

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
        values = [float(i) for i in resolution_values[1:]]

        # Plot the graph for this resolution
        plt.plot(range(1, len(values) + 1), values, label=resolution)

    plt.xlabel("Timestep after last observed value")
    plt.ylabel(y_label)
    plt.legend(loc='best')
    plt.savefig(output_path)
    plt.clf()
