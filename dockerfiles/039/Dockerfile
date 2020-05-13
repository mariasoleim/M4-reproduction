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

# Install R-3.5.0
COPY R-3.5.0.tar.gz .
RUN tar -xzvf R-3.5.0.tar.gz
WORKDIR R-3.5.0
RUN ./configure --with-readline=no
RUN make
RUN make install
RUN R --version 

# Install necessary packages
WORKDIR ..
COPY install_packages.R .
RUN Rscript install_packages.R

# Copy over the last files and change working directory
COPY ./data .
COPY auxiliar.R .
COPY forecast.R .
COPY README.md .

# Remove files that were just needed for setup
RUN rm R-3.5.0.tar.gz
RUN rm install_packages.R

