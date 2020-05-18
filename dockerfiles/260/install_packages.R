install.packages("https://github.com/carlanetto/M4comp2018/releases/download/0.2.0/M4comp2018_0.2.0.tar.gz", repos=NULL)

# Set CRAN repository
r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

install.packages("devtools")
require(devtools)

install_version("forecast", version="8.3")

