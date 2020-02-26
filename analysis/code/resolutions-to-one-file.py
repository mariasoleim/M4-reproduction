from helper import *
import pandas as pd


def combine(submission_id):
    """
    Some of the methods submitted to the M4 challenge writes the result to six different files, one for each resolution.
    This method combines those files to one file.
    :param submission_id: string or int. Id of the method to combine the results
    :return: nothing. Writes five new files with all the results
    """
    if isinstance(submission_id, int):
        submission_id = str(submission_id)

    path_to_forecasts = "../../forecasts/" + submission_id
    for rerun_number in range(1, 6):
        path_to_forecasts_rerun = path_to_forecasts + "/rerun-" + str(rerun_number)

        frames = []

        for resolution in resolutions:
            path_to_forecasts_rerun_resolution = path_to_forecasts_rerun + "/" + resolution + "Forec.csv"
            try:
                data = pd.read_csv(path_to_forecasts_rerun_resolution, index_col="id")
                frames.append(data)
            except FileNotFoundError:
                raise Exception("There was no file at the destination: " + path_to_forecasts_rerun_resolution)

        result = pd.concat(frames)
        result.columns = ["F" + str(i) for i in range(1, 49)]
        result.to_csv(path_to_forecasts_rerun + "/forecast.csv")


combine(118)
