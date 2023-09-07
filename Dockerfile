FROM ubuntu:22.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get install git -y
RUN apt install python3-pip -y
RUN apt install locales
RUN locale-gen en_US.UTF-8
RUN apt-get install doxygen -y
RUN apt-get install graphviz -y
RUN apt install npm -y
RUN pip3 install sphinx
RUN pip3 install sphinx-js
RUN pip3 install sphinx_rtd_theme
RUN pip3 install breathe
RUN pip3 install linuxdoc
RUN npm install -g jsdoc
