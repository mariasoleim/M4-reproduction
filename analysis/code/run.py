from precision import *

for rerun in range(1, 6):
    rerun = str(rerun)
    compare_results("../../forecasts/118/rerun-" + rerun + "/forecast.csv", "../../data/test/all.csv",
                    "../results/118/rerun-" + rerun + "/precision.csv")
    print(get_average_sMAPE("../results/118/rerun-" + rerun + "/precision.csv"))
    get_sMAPE_for_each_timestep("../results/118/rerun-" + rerun + "/precision.csv", "../results/118/rerun-" +
                                rerun + "/precision-resolution-timestep.csv")
    resolution_timestep_sMAPE_graph("../results/118/rerun-" + rerun + "/precision-resolution-timestep.csv",
                                    "../results/118/rerun-" + rerun + "/precision.png")
