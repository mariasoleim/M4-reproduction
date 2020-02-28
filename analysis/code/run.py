from precision import *

for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv", "../../data/test/all.csv",
                    "../results/118/rerun-" + rerun + "/precision.csv")
    get_average_sMAPE("../results/118/rerun-" + rerun + "/precision.csv",
                      "../results/118/rerun-" + rerun + "/average-sMAPE.txt")
    get_sMAPE_for_each_timestep("../results/118/rerun-" + rerun + "/precision.csv", "../results/118/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_sMAPE_graph("../results/118/rerun-" + rerun + "/precision-resolution-timestep.csv",
                                    "../results/118/rerun-" + rerun + "/precision.png")

rerun_sMAPEs = ["../results/118/rerun-" + str(rerun) + "/precision.csv" for rerun in range(1, 6)]
get_average_sMAPEs_for_all_reruns("../results/118/precision.csv", *rerun_sMAPEs)
get_average_sMAPE("../results/118/precision.csv", "../results/118/average-sMAPE.txt")


# Calculate sMAPE between the original forecasts and the test set
# The results should be:
# 118: 11.374
# 245: 11.270
# 237: 11.845
# 072: 11.695
# 069: 11.836
#compare_results("../../forecasts/118/original/submission-118.csv", "../../data/test/all.csv", "../../forecasts/118/delete_this.csv")
#get_average_sMAPE("../../forecasts/118/delete_this.csv", "../../forecasts/118/delete_this_as_well.txt")
# Have tested 118. Worked.
