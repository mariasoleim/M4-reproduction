from precision import *
from variance import *

# How equal are the reruns to the test set?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecasts.csv", "../../data/test/all.csv",
                    "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv")
    get_average("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                      "../results/118/comparison-to-test-set/rerun-" + rerun + "/sMAPE-average.txt")
    get_value_for_each_timestep("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                                "../results/118/comparison-to-test-set/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/118/comparison-to-test-set/rerun-" + rerun +
                              "/precision-resolution-timestep.csv",
                              "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.png",
                              "Average sAPE")

paths = ["../results/118/comparison-to-test-set/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_values_for_all_reruns("../results/118/comparison-to-test-set/precision.csv", *paths)
get_average("../results/118/comparison-to-test-set/precision.csv",
                  "../results/118/comparison-to-test-set/sMAPE-average.txt")
get_value_for_each_timestep("../results/118/comparison-to-test-set/precision.csv",
                            "../results/118/comparison-to-test-set/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/118/comparison-to-test-set/precision-resolution-timestep.csv",
                                "../results/118/comparison-to-test-set/precision.png", "Average sAPE")


# How equal are the reruns to the original submission?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecasts.csv",
                    "../../forecasts/118/original/submission-118.csv",
                    "../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv")
    get_average("../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                      "../results/118/comparison-to-original-submission/rerun-" + rerun + "/sMAPE-average.txt")
    get_value_for_each_timestep("../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                                "../results/118/comparison-to-original-submission/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/118/comparison-to-original-submission/rerun-" + rerun +
                                    "/precision-resolution-timestep.csv",
                                    "../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.png"
                              , "Average sAPE"
                              )

paths = ["../results/118/comparison-to-original-submission/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_values_for_all_reruns("../results/118/comparison-to-original-submission/precision.csv", *paths)
get_average("../results/118/comparison-to-original-submission/precision.csv",
                  "../results/118/comparison-to-original-submission/sMAPE-average.txt")
get_value_for_each_timestep("../results/118/comparison-to-original-submission/precision.csv",
                            "../results/118/comparison-to-original-submission/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/118/comparison-to-original-submission/precision-resolution-timestep.csv",
                          "../results/118/comparison-to-original-submission/precision.png",
                          "Average sAPE")

# How equal are the reruns to each others?
reruns = ["../../forecasts/118/rerun-" + str(rerun) + "/forecasts.csv" for rerun in range(1, 6)]
get_coefficient_of_variation("../results/118/variation/coefficient-of-variation.csv", *reruns)
get_average("../results/118/variation/coefficient-of-variation.csv",
            "../results/118/variation/coefficient-of-variation-average.txt")
get_value_for_each_timestep("../results/118/variation/coefficient-of-variation.csv",
                            "../results/118/variation/coefficient-of-variation-resolution-timestep.csv")
resolution_timestep_graph("../results/118/variation/coefficient-of-variation-resolution-timestep.csv",
                          "../results/118/variation/coefficient-of-variation.png", "Average coefficient of variation")

# How equal are the reruns to the test set?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/069/rerun-" + rerun + "/forecasts.csv", "../../data/test/all.csv",
                    "../results/069/comparison-to-test-set/rerun-" + rerun + "/precision.csv")
    get_average("../results/069/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                      "../results/069/comparison-to-test-set/rerun-" + rerun + "/sAPE-average.txt")
    get_value_for_each_timestep("../results/069/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                                "../results/069/comparison-to-test-set/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/069/comparison-to-test-set/rerun-" + rerun +
                              "/precision-resolution-timestep.csv",
                              "../results/069/comparison-to-test-set/rerun-" + rerun + "/precision.png",
                              "Average sAPE")

paths = ["../results/069/comparison-to-test-set/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_values_for_all_reruns("../results/069/comparison-to-test-set/precision.csv", *paths)
get_average("../results/069/comparison-to-test-set/precision.csv",
                  "../results/069/comparison-to-test-set/sMAPE-average.txt")
get_value_for_each_timestep("../results/069/comparison-to-test-set/precision.csv",
                            "../results/069/comparison-to-test-set/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/069/comparison-to-test-set/precision-resolution-timestep.csv",
                                "../results/069/comparison-to-test-set/precision.png", "Average sAPE")


# How equal are the reruns to the original submission?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/069/rerun-" + rerun + "/forecasts.csv",
                    "../../forecasts/069/original/submission-069.csv",
                    "../results/069/comparison-to-original-submission/rerun-" + rerun + "/precision.csv")
    get_average("../results/069/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                      "../results/069/comparison-to-original-submission/rerun-" + rerun + "/sMAPE-average.txt")
    get_value_for_each_timestep("../results/069/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
                                "../results/069/comparison-to-original-submission/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/069/comparison-to-original-submission/rerun-" + rerun +
                                    "/precision-resolution-timestep.csv",
                                    "../results/069/comparison-to-original-submission/rerun-" + rerun + "/precision.png"
                              , "Average sAPE"
                              )

paths = ["../results/069/comparison-to-original-submission/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_values_for_all_reruns("../results/069/comparison-to-original-submission/precision.csv", *paths)
get_average("../results/069/comparison-to-original-submission/precision.csv",
                  "../results/069/comparison-to-original-submission/sMAPE-average.txt")
get_value_for_each_timestep("../results/069/comparison-to-original-submission/precision.csv",
                            "../results/069/comparison-to-original-submission/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/069/comparison-to-original-submission/precision-resolution-timestep.csv",
                          "../results/069/comparison-to-original-submission/precision.png",
                          "Average sAPE")

# How equal are the reruns to each others?
reruns = ["../../forecasts/069/rerun-" + str(rerun) + "/forecasts.csv" for rerun in range(1, 6)]
get_coefficient_of_variation("../results/069/variation/coefficient-of-variation.csv", *reruns)
get_average("../results/069/variation/coefficient-of-variation.csv",
            "../results/069/variation/coefficient-of-variation-average.txt")
get_value_for_each_timestep("../results/069/variation/coefficient-of-variation.csv",
                            "../results/069/variation/coefficient-of-variation-resolution-timestep.csv")
resolution_timestep_graph("../results/069/variation/coefficient-of-variation-resolution-timestep.csv",
                          "../results/069/variation/coefficient-of-variation.png", "Average coefficient of variation")
