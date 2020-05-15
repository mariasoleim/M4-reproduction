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
WORKDIR ..

# Copy over files
COPY install_packages.R .
COPY final_M4.R .
COPY README.md .

# Install necessary packages
RUN Rscript install_packages.R

# Remove files that were just needed for setup
RUN rm R-3.4.3.tar.gz
RUN rm install_packages.R

