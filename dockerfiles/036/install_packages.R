# Set CRAN repository
r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

install.packages("devtools")
require(devtools)

install_version("doSNOW", version="1.0.16")
install_version("foreach", version="1.4.4")
install_version("forecast", version="8.2")
install_version("forecTheta", version="2.2")
install_version("iterators", version="1.0.9")
install_version("smooth", version="2.3.1")
install_version("snow", version="0.4-2")

sessionInfo()

