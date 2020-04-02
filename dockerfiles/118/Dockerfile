FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	curl \
	git \
	locales \
	wget \
	littler \
	nano && \
    	rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -f UTF-8 en_US.UTF-8

RUN useradd -m -s /bin/bash linuxbrew && \
    echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers

USER linuxbrew
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

USER root
ENV PATH="/home/linuxbrew/.linuxbrew/bin:${PATH}"

# Install Cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.15.2/cmake-3.15.2.tar.gz && \
	tar -zxvf cmake-3.15.2.tar.gz && \
	cd cmake-3.15.2 && \
	./bootstrap && \
	make && \
	make install

RUN brew install --HEAD eigen

# Install DyNet
WORKDIR opt
ENV DYNET_VERSION 72211da
RUN git clone https://github.com/clab/dynet.git && \
        cd dynet && \
        git checkout ${DYNET_VERSION} && \
        mkdir build && \
        cd build && \
        cmake .. -DEIGEN3_INCLUDE_DIR=/home/linuxbrew/.linuxbrew/Cellar/eigen/HEAD-94875feeeeb9/include/eigen3 && \
        make -j8

WORKDIR ../home/es-rnn

# Copy over the necessary files
COPY ./c++/linux_example_scripts ./c++/linux_example_scripts
COPY ./c++ ./c++
COPY ./R ./R
COPY ./data/M4-info.csv ./data/M4-info.csv
COPY ./data/train ./data/train
RUN mkdir output


# Compile the code by running the build_mkl file
WORKDIR c++
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Yearly"]
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Quarterly"]
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Monthly"]
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Weekly"]
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Daily"]
RUN ["/bin/bash", "-c", "source linux_example_scripts/build_mkl ES_RNN_Hourly"]

# Delete files that are not needed any more
RUN rm ES_RNN_Yearly.cc
RUN rm ES_RNN_Quarterly.cc
RUN rm ES_RNN_Monthly.cc
RUN rm ES_RNN_Weekly.cc
RUN rm ES_RNN_Daily.cc
RUN rm ES_RNN_Hourly.cc
RUN rm linux_example_scripts/build_mkl

