# Set CRAN repository
r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

install.packages("devtools")
require(devtools)

install.packages("https://github.com/carlanetto/M4comp2018/releases/download/0.2.0/M4comp2018_0.2.0.tar.gz", repos=NULL)

#install_version("M4comp2018", version="0.1.0")
install_version("trend", version="1.1.0")
install_version("pracma", version="2.1.4")
install_version("forecast", version="8.2")
install_version("sets", version="1.0-18")
install_version("dplyr", version="0.8.0")
install_version("pbapply", version="1.3-4")
install_version("robustbase", version="0.93-0")
install_version("abind", version="1.4-5")
#devtools::install_version("parallel", version="3.5.0")
#devtools::install_version("stats", version="3.5.0")

require(trend)
require(pracma)
require(forecast)
require(sets)
require(dplyr)
require(pbapply)
require(robustbase)
require(abind)
require(parallel)
require(stats)

sessionInfo()

