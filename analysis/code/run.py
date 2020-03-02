from precision import *
from variance import *

# How equal are the reruns to the test set?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv", "../../data/test/all.csv",
                    "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv")
    get_average("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                      "../results/118/comparison-to-test-set/rerun-" + rerun + "/sMAPE-average.txt")
    get_value_for_each_timestep("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
                                "../results/118/comparison-to-test-set/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_graph("../results/118/comparison-to-test-set/rerun-" + rerun +
                              "/precision-resolution-timestep.csv",
                              "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.png",
                              "Average sMAPE")

rerun_sMAPEs = ["../results/118/comparison-to-test-set/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_sMAPEs_for_all_reruns("../results/118/comparison-to-test-set/precision.csv", *rerun_sMAPEs)
get_average("../results/118/comparison-to-test-set/precision.csv",
                  "../results/118/comparison-to-test-set/sMAPE-average.txt")
get_value_for_each_timestep("../results/118/comparison-to-test-set/precision.csv",
                            "../results/118/comparison-to-test-set/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/118/comparison-to-test-set/precision-resolution-timestep.csv",
                                "../results/118/comparison-to-test-set/precision.png", "Average sMAPE")


# How equal are the reruns to the original submission?
for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv",
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
                              , "Average sMAPE"
                              )

rerun_sMAPEs = ["../results/118/comparison-to-original-submission/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_sMAPEs_for_all_reruns("../results/118/comparison-to-original-submission/precision.csv", *rerun_sMAPEs)
get_average("../results/118/comparison-to-original-submission/precision.csv",
                  "../results/118/comparison-to-original-submission/sMAPE-average.txt")
get_value_for_each_timestep("../results/118/comparison-to-original-submission/precision.csv",
                            "../results/118/comparison-to-original-submission/precision-resolution-timestep.csv")
resolution_timestep_graph("../results/118/comparison-to-original-submission/precision-resolution-timestep.csv",
                          "../results/118/comparison-to-original-submission/precision.png",
                          "Average sMAPE")


# Calculate sMAPE between the original forecasts and the test set
# The results should be:
# 118: 11.374
# 245: 11.270
# 237: 11.845
# 072: 11.695
# 069: 11.836
# compare_results("../../forecasts/118/original/submission-118.csv", "../../data/test/all.csv",
# "../../forecasts/118/delete_this.csv")
# get_average("../../forecasts/118/delete_this.csv", "../../forecasts/118/delete_this_as_well.txt")
# Have tested 118. Worked.

reruns = ["../../forecasts/118/rerun-" + str(rerun) + "/forecast.csv" for rerun in range(1, 6)]
get_coefficient_of_variation("../results/118/variation/coefficient-of-variation.csv", *reruns)
get_average("../results/118/variation/coefficient-of-variation.csv", "../results/118/variation/coefficient-of-variation-average.txt")
get_value_for_each_timestep("../results/118/variation/coefficient-of-variation.csv", "../results/118/variation/coefficient-of-variation-resolution-timestep.csv")
resolution_timestep_graph("../results/118/variation/coefficient-of-variation-resolution-timestep.csv", "../results/118/variation/coefficient-of-variation.png", "Average coefficient of variation")