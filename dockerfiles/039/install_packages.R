# Set CRAN repository
r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

install.packages("devtools")
require(devtools)

# Install package forecast (Version 8.3 was the last version that were available at the date of the deadline of the M4 competition.)
install_version("forecast", version="8.3")

sessionInfo()

