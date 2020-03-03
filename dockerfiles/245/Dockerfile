FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	gnupg \
	libcurl4-openssl-dev \
	libssl-dev \
	libxml2-dev \
	nano \
	software-properties-common

# Adding public key
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'

RUN apt-get update && apt-get install -y r-base && rm -rf /var/lib/apt/lists/*

# Install necessary R packages
COPY install_packages.R .
RUN Rscript install_packages.R
RUN rm install_packages.R

# Copy over the main script for running the project and a readme file
COPY run.R .
COPY README.md .

