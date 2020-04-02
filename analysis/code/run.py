from precision import *
from variance import *

method_ids = ["118", "069"]
for method_id in method_ids:
    
    # How equal are the reruns to the test set?
    for rerun in range(1, 6):
        rerun = str(rerun)
        compare_results_sAPE("../../forecasts/" + method_id + "/rerun-" + rerun + "/forecasts.csv", "../../data/test/all.csv",
                        "../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun + "/precision.csv")
        get_average("../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                          "../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun + "/sMAPE-average.txt")
        get_value_for_each_timestep("../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                                    "../results/" + method_id + "/comparison-to-test-set/rerun-" +
                                    rerun + "/precision-resolution-timestep.csv")
        resolution_timestep_graph("../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun +
                                  "/precision-resolution-timestep.csv",
                                  "../results/" + method_id + "/comparison-to-test-set/rerun-" + rerun + "/precision.png",
                                  "Average sAPE")

    paths = ["../results/" + method_id + "/comparison-to-test-set/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
    get_average_values_for_all_reruns("../results/" + method_id + "/comparison-to-test-set/precision.csv", *paths)
    get_average("../results/" + method_id + "/comparison-to-test-set/precision.csv",
                      "../results/" + method_id + "/comparison-to-test-set/sMAPE-average.txt")
    get_value_for_each_timestep("../results/" + method_id + "/comparison-to-test-set/precision.csv",
                                "../results/" + method_id + "/comparison-to-test-set/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/" + method_id + "/comparison-to-test-set/precision-resolution-timestep.csv",
                                    "../results/" + method_id + "/comparison-to-test-set/precision.png", "Average sAPE")

    # How equal are the reruns to the original submission?
    for rerun in range(1, 6):
        rerun = str(rerun)
        # Calculate the sAPE between a rerun and the original submission
        compare_results_sAPE("../../forecasts/" + method_id + "/rerun-" + rerun + "/forecasts.csv",
                        "../../forecasts/" + method_id + "/original/submission-" + method_id + ".csv",
                        "../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun + "/precision.csv")
        # Finds the average of all sAPEs and writes the average to a text file
        get_average("../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                          "../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun + "/sMAPE-average.txt")
        # Sorts on resolution and calculate average sAPE for each time step
        get_value_for_each_timestep("../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                                    "../results/" + method_id + "/comparison-to-original-submission/rerun-" +
                                    rerun + "/precision-resolution-timestep.csv")
        # Creates a graph of the result
        resolution_timestep_graph("../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun +
                                        "/precision-resolution-timestep.csv",
                                        "../results/" + method_id + "/comparison-to-original-submission/rerun-" + rerun + "/precision.png"
                                  , "Average sAPE"
                                  )

    paths = ["../results/" + method_id + "/comparison-to-original-submission/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
    # Calculate the average sAPE of the five reruns for every entry
    get_average_values_for_all_reruns("../results/" + method_id + "/comparison-to-original-submission/precision.csv", *paths)
    # Calculate the average of the preceding result
    get_average("../results/" + method_id + "/comparison-to-original-submission/precision.csv",
                      "../results/" + method_id + "/comparison-to-original-submission/sMAPE-average.txt")
    # # Sorts on resolution and calculate average sAPE for each time step
    get_value_for_each_timestep("../results/" + method_id + "/comparison-to-original-submission/precision.csv",
                                "../results/" + method_id + "/comparison-to-original-submission/precision-resolution-timestep.csv")
    # Creates a graph of the preceding result
    resolution_timestep_graph("../results/" + method_id + "/comparison-to-original-submission/precision-resolution-timestep.csv",
                              "../results/" + method_id + "/comparison-to-original-submission/precision.png",
                              "Average sAPE")

    # How equal are the reruns to each others?
    reruns = ["../../forecasts/" + method_id + "/rerun-" + str(rerun) + "/forecasts.csv" for rerun in range(1, 6)]
    get_coefficient_of_variation("../results/" + method_id + "/variation/coefficient-of-variation.csv", *reruns)
    get_average("../results/" + method_id + "/variation/coefficient-of-variation.csv",
                "../results/" + method_id + "/variation/coefficient-of-variation-average.txt")
    get_value_for_each_timestep("../results/" + method_id + "/variation/coefficient-of-variation.csv",
                                "../results/" + method_id + "/variation/coefficient-of-variation-resolution-timestep.csv")
    resolution_timestep_graph("../results/" + method_id + "/variation/coefficient-of-variation-resolution-timestep.csv",
                              "../results/" + method_id + "/variation/coefficient-of-variation.png", "Average coefficient of variation")
