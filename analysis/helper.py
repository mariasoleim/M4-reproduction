import pandas as pd

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


def get_real_value(resolution, time_series_id, number_in_horizon):
    test = pd.read_csv("../data/test/" + resolution + "-test.csv", index_col=0)
    series = test.loc[time_series_id].tolist()
    target = series[number_in_horizon - 1]
    return target


