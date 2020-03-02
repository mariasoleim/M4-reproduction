from precision import *
from variance import *

# # How equal are the reruns to the test set?
# for rerun in range(1, 6):
#     rerun = str(rerun)
#     compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv", "../../data/test/all.csv",
#                     "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv")
#     get_average_sMAPE("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
#                       "../results/118/comparison-to-test-set/rerun-" + rerun + "/average-sMAPE.txt")
#     get_sMAPE_for_each_timestep("../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.csv",
#                                 "../results/118/comparison-to-test-set/rerun-" +
#                                 rerun + "/precision-resolution-timestep.csv")
#     resolution_timestep_sMAPE_graph("../results/118/comparison-to-test-set/rerun-" + rerun +
#                                     "/precision-resolution-timestep.csv",
#                                     "../results/118/comparison-to-test-set/rerun-" + rerun + "/precision.png")
#
# rerun_sMAPEs = ["../results/118/comparison-to-test-set/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
# get_average_sMAPEs_for_all_reruns("../results/118/comparison-to-test-set/precision.csv", *rerun_sMAPEs)
# get_average_sMAPE("../results/118/comparison-to-test-set/precision.csv",
#                   "../results/118/comparison-to-test-set/average-sMAPE.txt")
# get_sMAPE_for_each_timestep("../results/118/comparison-to-test-set/precision.csv",
#                             "../results/118/comparison-to-test-set/precision-resolution-timestep.csv")
# resolution_timestep_sMAPE_graph("../results/118/comparison-to-test-set/precision-resolution-timestep.csv",
#                                 "../results/118/comparison-to-test-set/precision.png")
#
#
# # How equal are the reruns to the original submission?
# for rerun in range(1, 6):
#     rerun = str(rerun)
#     compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv",
#                     "../../forecasts/118/original/submission-118.csv",
#                     "../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv")
#     get_average_sMAPE("../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
#                       "../results/118/comparison-to-original-submission/rerun-" + rerun + "/average-sMAPE.txt")
#     get_sMAPE_for_each_timestep("../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.csv",
#                                 "../results/118/comparison-to-original-submission/rerun-" +
#                                 rerun + "/precision-resolution-timestep.csv")
#     resolution_timestep_sMAPE_graph("../results/118/comparison-to-original-submission/rerun-" + rerun +
#                                     "/precision-resolution-timestep.csv",
#                                     "../results/118/comparison-to-original-submission/rerun-" + rerun + "/precision.png"
#                                     )
#
# rerun_sMAPEs = ["../results/118/comparison-to-original-submission/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
# get_average_sMAPEs_for_all_reruns("../results/118/comparison-to-original-submission/precision.csv", *rerun_sMAPEs)
# get_average_sMAPE("../results/118/comparison-to-original-submission/precision.csv",
#                   "../results/118/comparison-to-original-submission/average-sMAPE.txt")
# get_sMAPE_for_each_timestep("../results/118/comparison-to-original-submission/precision.csv",
#                             "../results/118/comparison-to-original-submission/precision-resolution-timestep.csv")
# resolution_timestep_sMAPE_graph("../results/118/comparison-to-original-submission/precision-resolution-timestep.csv",
#                                 "../results/118/comparison-to-original-submission/precision.png")


# Calculate sMAPE between the original forecasts and the test set
# The results should be:
# 118: 11.374
# 245: 11.270
# 237: 11.845
# 072: 11.695
# 069: 11.836
# compare_results("../../forecasts/118/original/submission-118.csv", "../../data/test/all.csv",
# "../../forecasts/118/delete_this.csv")
# get_average_sMAPE("../../forecasts/118/delete_this.csv", "../../forecasts/118/delete_this_as_well.txt")
# Have tested 118. Worked.

reruns = ["../../forecasts/118/rerun-" + str(rerun) + "/forecast.csv" for rerun in range(1, 6)]
get_coefficient_of_variation("../results/118/coefficient_of_variation.csv", *reruns)
