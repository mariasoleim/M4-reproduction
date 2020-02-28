import pandas as pd
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


def get_predicted_values(submission_id, resolution, time_series_id, number_in_horizon):
    """
    Get all the predicted values with a specific resolution, time series id a certain number,
    number_in_horizon, after the last observed value
    :param submission_id: A string or an integer giving the id of the submission in the M4 competition
    :param resolution: A string, either "Yearly", "Quarterly", "Monthly", "Weekly", "Daily" or "Hourly"
    :param time_series_id: A string with the id of the series in which the average should be calculated
    :param number_in_horizon: An integer, the specific timestep succeeding the last observed value. E.g. a number in the
    range 1-13 for weekly series.
    :return:
    """
    if isinstance(submission_id, int):
        submission_id = str(submission_id)

    if resolution not in resolutions:
        raise Exception("This is not a valid resolution")

    values = []
    for rerun_id in range(1, 6):
        path_to_results = "../../forecasts/" + submission_id + "/rerun-" + str(rerun_id) + "/" + resolution + "Forec.csv"
        with open(path_to_results) as results:
            for line in results:
                line = line.split(",")
                if remove_quotes_if_any(line[0]) == time_series_id:
                    value = line[number_in_horizon]
                    values.append(float(value))
    return values


def get_resolution(id):
    id = remove_quotes_if_any(id)
    for resolution in resolutions:
        if resolution[0] == id[0]:
            return resolution
