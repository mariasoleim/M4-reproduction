FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

# software-properties-common contains add-apt-repository
RUN apt-get update && apt-get install -y \
	software-properties-common \
	gnupg \
	libcurl4-openssl-dev

# Adding public key
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
RUN apt update
RUN apt-get install -y r-base

COPY jafiorucci.R .
COPY install_packages.R .
RUN Rscript install_packages.R
COPY README.md .

