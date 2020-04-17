from precision import *
from variance import *

test_set_path = "../../data/test/all.csv"

# Calculate sAPE and ASE for the naive2 method compared to the test set
naive2_sAPE = "../results/naive2/sAPE.csv"
naive2_ASE = "../results/naive2/ASE.csv"
compare_results_sAPE("../../forecasts/naive2/submission-Naive2.csv", test_set_path, naive2_sAPE)
compare_results_ASE("../../forecasts/naive2/submission-Naive2.csv", test_set_path, naive2_ASE)

method_ids = ["069/malvik", "118/malvik", "245/malvik"]

for method_id in method_ids:

    forecast_path = "../../forecasts/" + method_id + "/rerun-" + rerun + "/forecasts.csv"
    original_submission_path = "../../forecasts/" + method_id + "/original/submission-" + method_id + ".csv"
    result_path = "../results/" + method_id
    comparison_to_test_set_path = result_path + "/comparison-to-test-set"
    comparison_to_original_submission_path = result_path + "/comparison-to-original-submission"
    variation_path = result_path + "/variation"

    # How equal are the reruns to the test set?
    for rerun in range(1, 6):
        rerun = str(rerun)
        result_folder = comparison_to_test_set_path + "/rerun-" + rerun
        compare_results_sAPE(forecast_path, test_set_path, result_folder + "/sAPE.csv")
        # compare_results_ASE(forecast_path, test_set_path, result_folder + "/ASE.csv")
        calculate_OWA(result_folder + "/sAPE.csv", result_folder + "/ASE.csv", naive2_sAPE, naive2_ASE, result_folder + "/OWA.csv")

        get_average(result_folder + "/sAPE.csv", result_folder + "/sAPE-average.txt")
        get_average(result_folder + "/ASE.csv", result_folder + "/ASE-average.txt")
        get_average(result_folder + "/OWA.csv", result_folder + "/OWA-average.txt")

        get_value_for_each_timestep(result_folder + "/sAPE.csv", result_folder + "/sAPE-resolution-timestep.csv")
        get_value_for_each_timestep(result_folder + "/ASE.csv", result_folder + "/ASE-resolution-timestep.csv")
        get_value_for_each_timestep(result_folder + "/OWA.csv", result_folder + "/OWA-resolution-timestep.csv")

        resolution_timestep_graph(result_folder + "/sAPE-resolution-timestep.csv", result_folder + "/sAPE.png", "Average sAPE")
        resolution_timestep_graph(result_folder + "/ASE-resolution-timestep.csv", result_folder + "/ASE.png", "Average ASE")
        resolution_timestep_graph(result_folder + "/OWA-resolution-timestep.csv", result_folder + "/OWA.png", "Average OWA")

    sAPE_paths = [comparison_to_test_set_path + "/rerun-" + str(rerun) + "/sAPE.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "/sAPE.csv", *sAPE_paths)
    get_average(comparison_to_test_set_path + "/sAPE.csv", comparison_to_test_set_path + "/sAPE-average.txt")
    get_value_for_each_timestep(comparison_to_test_set_path + "/sAPE.csv", comparison_to_test_set_path + "/sAPE-resolution-timestep.csv")
    resolution_timestep_graph(comparison_to_test_set_path + "/sAPE-resolution-timestep.csv", comparison_to_test_set_path + "/sAPE.png", "Average sAPE")

    ASE_paths = [comparison_to_test_set_path + "/rerun-" + str(rerun) + "/ASE.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "/ASE.csv", *ASE_paths)
    get_average(comparison_to_test_set_path + "/ASE.csv", comparison_to_test_set_path + "/ASE-average.txt")
    get_value_for_each_timestep(comparison_to_test_set_path + "/ASE.csv", comparison_to_test_set_path + "/ASE-resolution-timestep.csv")
    resolution_timestep_graph(comparison_to_test_set_path + "/ASE-resolution-timestep.csv", comparison_to_test_set_path + "/ASE.png", "Average ASE")

    OWA_paths = [comparison_to_test_set_path + "/rerun-" + str(rerun) + "/OWA.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns(comparison_to_test_set_path + "/OWA.csv", *OWA_paths)
    get_average(comparison_to_test_set_path + "/OWA.csv", comparison_to_test_set_path + "/OWA-average.txt")
    get_value_for_each_timestep(comparison_to_test_set_path + "/OWA.csv", comparison_to_test_set_path + "/OWA-resolution-timestep.csv")
    resolution_timestep_graph(comparison_to_test_set_path + "/OWA-resolution-timestep.csv", comparison_to_test_set_path + "/OWA.png", "Average OWA")

    # How equal are the reruns to the original submission?
    for rerun in range(1, 6):
        rerun = str(rerun)
        result_folder = comparison_to_original_submission_path + "/rerun-" + rerun
        # Calculate the sAPE between a rerun and the original submission
        compare_results_sAPE(forecast_path, original_submission_path, result_folder + "/sAPE.csv")
        # Finds the average of all sAPEs and writes the average to a text file
        get_average(result_folder + "/sAPE.csv", result_folder + "/sAPE-average.txt")
        # Sorts on resolution and calculate average sAPE for each time step
        get_value_for_each_timestep(result_folder + "/sAPE.csv", result_folder + "/sAPE-resolution-timestep.csv")
        # Creates a graph of the result
        resolution_timestep_graph(result_folder + "/sAPE-resolution-timestep.csv", result_folder + "/sAPE.png", "Average sAPE")

    sAPE_paths = [comparison_to_original_submission_path + "/rerun-" + str(rerun) + "/sAPE.csv" for rerun in range(1, 6)]
    # Calculate the average sAPE of the five reruns for every entry
    get_average_values_for_all_reruns(comparison_to_original_submission_path + "/sAPE.csv", *sAPE_paths)
    # Calculate the average of the preceding result
    get_average(comparison_to_original_submission_path + "/sAPE.csv", comparison_to_original_submission_path + "/sAPE-average.txt")
    # # Sorts on resolution and calculate average sAPE for each time step
    get_value_for_each_timestep(comparison_to_original_submission_path + "/sAPE.csv", comparison_to_original_submission_path + "/sAPE-resolution-timestep.csv")
    # Creates a graph of the preceding result
    resolution_timestep_graph(comparison_to_original_submission_path + "/sAPE-resolution-timestep.csv", comparison_to_original_submission_path + "/sAPE.png", "Average sAPE")

    # How equal are the reruns to each others?
    reruns = ["../../forecasts/" + method_id + "/rerun-" + str(rerun) + "/forecasts.csv" for rerun in range(1, 6)]
    get_coefficient_of_variation(variation_path + "/coefficient-of-variation.csv", *reruns)
    get_average(variation_path + "/coefficient-of-variation.csv", variation_path + "/coefficient-of-variation-average.txt")
    get_value_for_each_timestep(variation_path + "/coefficient-of-variation.csv", variation_path + "/coefficient-of-variation-resolution-timestep.csv")
    resolution_timestep_graph(variation_path + "/coefficient-of-variation-resolution-timestep.csv", variation_path + "/coefficient-of-variation.png", "Average coefficient of variation")
