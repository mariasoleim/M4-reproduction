from precision import *
from variance import *

test_set_path = "../../data/test/all.csv"

# Calculate sAPE and ASE for the naive2 method compared to the test set
naive2_sAPE = "../results/naive2/comparison-to-test-set/sAPE.csv"
naive2_ASE = "../results/naive2/comparison-to-test-set/ASE.csv"
compare_results_sAPE("../../forecasts/naive2/submission-Naive2.csv", test_set_path, naive2_sAPE)
compare_results_ASE("../../forecasts/naive2/submission-Naive2.csv", test_set_path, naive2_ASE)
get_average_each_series("../results/naive2/comparison-to-test-set/sAPE.csv", "../results/naive2/comparison-to-test-set/sMAPE.csv")
get_average_each_series("../results/naive2/comparison-to-test-set/ASE.csv", "../results/naive2/comparison-to-test-set/MASE.csv")
get_average_resolution_origin("../results/naive2/comparison-to-test-set/sMAPE.csv", "../results/naive2/comparison-to-test-set/sMAPE-resolution-origin.csv")
get_average_resolution_origin("../results/naive2/comparison-to-test-set/MASE.csv", "../results/naive2/comparison-to-test-set/MASE-resolution-origin.csv")

forecasts = ["036/computer-a", "036/computer-b", "039/computer-a", "039/computer-b", "069/computer-a", "078/computer-a", "118/computer-a", "118/computer-b", "237/computer-a", "245/computer-a", "260/computer-a", "260/computer-b"]

# Calculate OWA for the original submissions
ids = list(dict.fromkeys([i.split("/")[0] for i in forecasts]))
for method_id in ids:
    original_submission_path = "../../forecasts/" + method_id + "/original/submission-" + method_id + ".csv"
    result_path = "../results/" + method_id + "/original/"
    result_folder = result_path + "comparison-to-test-set/"
    compare_results_sAPE(original_submission_path, test_set_path, result_folder + "sAPE.csv")
    compare_results_ASE(original_submission_path, test_set_path, result_folder + "ASE.csv")
    get_average_each_series(result_folder + "sAPE.csv", result_folder + "sMAPE.csv")
    get_average_each_series(result_folder + "ASE.csv", result_folder + "MASE.csv")
    get_average_resolution_origin(result_folder + "sMAPE.csv", result_folder + "sMAPE-resolution-origin.csv")
    get_average_resolution_origin(result_folder + "MASE.csv", result_folder + "MASE-resolution-origin.csv")
    calculate_OWA(result_folder + "sMAPE-resolution-origin.csv", result_folder + "MASE-resolution-origin.csv",
                  "../results/naive2/comparison-to-test-set/sMAPE-resolution-origin.csv",
                  "../results/naive2/comparison-to-test-set/MASE-resolution-origin.csv",
                  result_folder + "OWA.csv")


for forecast in forecasts:
    print(forecast)
    method_id = forecast.split("/")[0]
    result_path = "../results/" + forecast
    comparison_to_test_set_path = result_path + "/comparison-to-test-set/"
    comparison_to_original_submission_path = result_path + "/comparison-to-original-submission"
    variation_path = result_path + "/variation"
    original_submission_path = "../../forecasts/" + method_id + "/original/submission-" + method_id + ".csv"

    # How equal are the reruns to the test set?
    for rerun in range(1, 6):
        rerun = str(rerun)
        forecast_path = "../../forecasts/" + forecast + "/rerun-" + rerun + "/forecasts.csv"
        result_folder = comparison_to_test_set_path + "rerun-" + rerun + "/"
        compare_results_sAPE(forecast_path, test_set_path, result_folder + "/sAPE.csv")
        compare_results_ASE(forecast_path, test_set_path, result_folder + "/ASE.csv")

        get_value_for_each_timestep(result_folder + "sAPE.csv", result_folder + "sAPE-resolution-timestep.csv")
        get_value_for_each_timestep(result_folder + "ASE.csv", result_folder + "ASE-resolution-timestep.csv")

        get_average_each_series(result_folder + "sAPE.csv", result_folder + "sMAPE.csv")
        get_average_each_series(result_folder + "ASE.csv", result_folder + "MASE.csv")

        get_average_resolution_origin(result_folder + "sMAPE.csv", result_folder + "sMAPE-resolution-origin.csv")
        get_average_resolution_origin(result_folder + "MASE.csv", result_folder + "MASE-resolution-origin.csv")

        calculate_OWA(result_folder + "sMAPE-resolution-origin.csv", result_folder + "MASE-resolution-origin.csv", "../results/naive2/comparison-to-test-set/sMAPE-resolution-origin.csv",
                      "../results/naive2/comparison-to-test-set/MASE-resolution-origin.csv", result_folder + "OWA.csv")

    sAPE_paths = [comparison_to_test_set_path + "rerun-" + str(rerun) + "/sAPE-resolution-timestep.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "sAPE.csv", sAPE_paths)
    resolution_timestep_graph(comparison_to_test_set_path + "sAPE.csv", comparison_to_test_set_path + "sAPE.png", "Average sAPE")

    ASE_paths = [comparison_to_test_set_path + "rerun-" + str(rerun) + "/ASE-resolution-timestep.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "ASE.csv", ASE_paths)
    resolution_timestep_graph(comparison_to_test_set_path + "ASE.csv", comparison_to_test_set_path + "ASE.png", "Average ASE")

    OWA_paths = [comparison_to_test_set_path + "rerun-" + str(rerun) + "/OWA.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "OWA.csv", OWA_paths)

    compare_files("../results/" + method_id + "/original/comparison-to-test-set/OWA.csv", comparison_to_test_set_path + "OWA.csv", comparison_to_test_set_path + "OWA-difference.csv")


    # How equal are the reruns to the original submission?
    for rerun in range(1, 6):
        rerun = str(rerun)
        forecast_path = "../../forecasts/" + forecast + "/rerun-" + rerun + "/forecasts.csv"
        result_folder = comparison_to_original_submission_path + "/rerun-" + rerun
        # Calculate the sAPE between a rerun and the original submission
        compare_results_sAPE(forecast_path, original_submission_path, result_folder + "/sAPE.csv")
        # Finds the average of all sAPEs and writes the average to a text file
        get_average(result_folder + "/sAPE.csv", result_folder + "/sAPE-average.txt")
        # Sorts on resolution and calculate average sAPE for each time step
        get_value_for_each_timestep(result_folder + "/sAPE.csv", result_folder + "/sAPE-resolution-timestep.csv")
        # Creates a graph of the result
        resolution_timestep_graph(result_folder + "/sAPE-resolution-timestep.csv", result_folder + "/sAPE.png", "Average sAPE")
        # Calculates the sMAPE for each series
        get_average_each_series(result_folder + "/sAPE.csv", result_folder + "/sMAPE.csv")
        # Finds the average of all sMAPEs and writes the average to a text file
        get_average(result_folder + "/sMAPE.csv", result_folder + "/sMAPE-average.txt")
        # Calculates the share of the time series that has an sMAPE less than some number
        get_share_less_than(result_folder + "/sMAPE.csv", 0, result_folder + "/sMAPE-less-than-")
        get_share_less_than(result_folder + "/sMAPE.csv", 0.00001, result_folder + "/sMAPE-less-than-")

    sAPE_paths = [comparison_to_original_submission_path + "/rerun-" + str(rerun) + "/sAPE.csv" for rerun in range(1, 6)]
    # Calculate the average sAPE of the five reruns for every entry
    get_average_values_for_all_reruns(comparison_to_original_submission_path + "/sAPE.csv", sAPE_paths)
    # Calculate the average of the preceding result
    get_average(comparison_to_original_submission_path + "/sAPE.csv", comparison_to_original_submission_path + "/sAPE-average.txt")
    # # Sorts on resolution and calculate average sAPE for each time step
    get_value_for_each_timestep(comparison_to_original_submission_path + "/sAPE.csv", comparison_to_original_submission_path + "/sAPE-resolution-timestep.csv")
    # Creates a graph of the preceding result
    resolution_timestep_graph(comparison_to_original_submission_path + "/sAPE-resolution-timestep.csv", comparison_to_original_submission_path + "/sAPE.png", "Average sAPE")
    # Calculates the share of the time series that has an sMAPE less than some number
    share_less_than_0_paths = [comparison_to_original_submission_path + "/rerun-" + str(rerun) + "/sMAPE-less-than-0.txt" for rerun in range(1, 6)]
    share_less_than_almost_zero_paths = [comparison_to_original_submission_path + "/rerun-" + str(rerun) + "/sMAPE-less-than-1e-05.txt" for rerun in range(1, 6)]
    get_average_of_text_files(share_less_than_0_paths, comparison_to_original_submission_path + "/share-less-than-0.txt")
    get_average_of_text_files(share_less_than_almost_zero_paths, comparison_to_original_submission_path + "/share-less-than-1e-05.txt")
    sMAPE_paths = [comparison_to_original_submission_path + "/rerun-" + str(rerun) + "/sMAPE-average.txt" for rerun in range(1, 6)]
    get_average_of_text_files(sMAPE_paths, comparison_to_original_submission_path + "/sMAPE-average.txt")


    # How equal are the reruns to each others?
    reruns = ["../../forecasts/" + forecast + "/rerun-" + str(rerun) + "/forecasts.csv" for rerun in range(1, 6)]
    get_coefficient_of_variation(variation_path + "/coefficient-of-variation.csv", *reruns)
    get_average(variation_path + "/coefficient-of-variation.csv", variation_path + "/coefficient-of-variation-average.txt")
    get_value_for_each_timestep(variation_path + "/coefficient-of-variation.csv", variation_path + "/coefficient-of-variation-resolution-timestep.csv")
    resolution_timestep_graph(variation_path + "/coefficient-of-variation-resolution-timestep.csv", variation_path + "/coefficient-of-variation.png", "Average coefficient of variation")


# Compare original OWA to reruns' OWAs
output_path = "../results/OWA-comparisons/OWA"
cut_axis = [True, False]
for ca in cut_axis:
    for resolution in resolutions:
        compare_original_and_rerun_OWA(forecasts, resolution, ca, output_path)
    for origin in origins:
        compare_original_and_rerun_OWA(forecasts, origin, ca, output_path)
    compare_original_and_rerun_OWA(forecasts, "All", ca, output_path)

# Find all the methods that are run on both computers
ids = [forecast.split("/")[0] for forecast in forecasts]
ids = set(i for i in ids if ids.count(i) == 2)

# Calculate DRMSD and PD for methods that are run on both computers
for id in ids:
    print(id)

    paths_a = ["../../forecasts/" + id + "/computer-a/rerun-" + str(i) + "/forecasts.csv" for i in range(1, 6)]
    paths_b = ["../../forecasts/" + id + "/computer-b/rerun-" + str(i) + "/forecasts.csv" for i in range(1, 6)]
    result_path = "../results/" + id + "/computer-comparison/"

    compare_computers(paths_a, paths_b, result_path + "DRMSD.csv", DRMSD)
    average_path = result_path + "DRMSD-average.txt"
    get_average(result_path + "DRMSD.csv", average_path)

    if open(average_path, "r").read() != "NA":
        get_value_for_each_timestep(result_path + "DRMSD.csv", result_path + "DRMSD-rt.csv")
        resolution_timestep_graph(result_path + "DRMSD-rt.csv", result_path + "DRMSD-rt.png", "Average DRMSD")
        get_average_each_series(result_path + "DRMSD.csv", result_path + "DRMSD-each-series.csv")
        get_average_resolution_origin(result_path + "DRMSD-each-series.csv", result_path + "DRMSD-resolution-origin.csv")
        scatterplot(result_path + "DRMSD-resolution-origin.csv", result_path + "DRMSD-scatter.png", "DRMSD")

    compare_computers(paths_a, paths_b, result_path + "PD.csv", percentage_difference)
    average_path = result_path + "PD-average.txt"
    get_average(result_path + "PD.csv", average_path)

    if open(average_path, "r").read() != "NA":
        get_value_for_each_timestep(result_path + "PD.csv", result_path + "PD-rt.csv")
        resolution_timestep_graph(result_path + "PD-rt.csv", result_path + "PD-rt.png", "Average PD")
        get_average_each_series(result_path + "PD.csv", result_path + "PD-each-series.csv")
        get_average_resolution_origin(result_path + "PD-each-series.csv",
                                      result_path + "PD-resolution-origin.csv")
        scatterplot(result_path + "PD-resolution-origin.csv", result_path + "PD-scatter.png", "PD")


# Scatter plot of the average sMAPE for reruns of the same method on the same computer
scatterplot_from_paths("../results/", forecasts, "/comparison-to-original-submission/sMAPE-average.txt", "../results/sMAPE-between-original.png", "sMAPE")
