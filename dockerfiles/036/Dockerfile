FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	gfortran \ 
	libbz2-dev \ 
	libcurl4-openssl-dev \ 
	liblzma-dev \ 
	libpcre3-dev \ 
	libssl-dev \ 
	libxml2-dev \ 
	xorg-dev

# Install R-3.4.3
COPY R-3.4.3.tar.gz .
RUN tar -xzvf R-3.4.3.tar.gz
WORKDIR R-3.4.3
RUN ./configure --with-readline=no
RUN make
RUN make install
RUN R --version 

# Install necessary packages
WORKDIR ..
COPY install_packages.R .
RUN Rscript install_packages.R

# Copy over the last files and change working directory
COPY ./data ./data
COPY M4-FPIS-create-datasets-20180523.R .
COPY M4-FPIS-submission-code-20180525.R .
COPY README.md .

# Translate the dataset given by the M4 competitions organizers to a new format
RUN Rscript M4-FPIS-create-datasets-20180523.R .

# Remove files that were just needed for setup
RUN rm R-3.4.3.tar.gz
RUN rm install_packages.R
RUN rm M4-FPIS-create-datasets-20180523.R
RUN rm -r data/train

