FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	xorg-dev \ 
	libcurl4-openssl-dev \ 
	gfortran \ 
	libbz2-dev \ 
	liblzma-dev \ 
	libpcre3-dev \
	libcurl4-openssl-dev \
	libxml2-dev \
	libssl-dev \
	libssh2-1-dev \
	nano

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

# Remove files that were just needed for setup
RUN rm R-3.5.0.tar.gz
RUN rm install_packages.R

# Copy over the last files and change working directory
COPY tester /tester/
COPY M4 /M4/
COPY README.md .


