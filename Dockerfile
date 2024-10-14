# Use NVIDIA CUDA base image
FROM pytorch/pytorch:2.4.1-cuda11.8-cudnn9-runtime

WORKDIR /app

RUN apt-get update
RUN apt-get install gcc g++ libsm6 libxext6 wget -y
RUN apt-get update && apt-get install -y git ffmpeg

# SET BASH AS CURRENT SHELL
RUN chsh -s /bin/bash
SHELL ["/bin/bash", "-c"]

# ADD CONDA PATH TO PATH
ENV PATH /opt/conda/bin:$PATH

# Creating conda environment
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

# ADD ENV PATH TO PATH
ENV PATH /opt/conda/envs/computer_vision/bin:$PATH
ENV CONDA_DEFAULT_ENV computer_vision

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "computer_vision", "/bin/bash", "-c"]

RUN rm /tmp/environment.yml

COPY . /app

ENTRYPOINT [ "python", "-u", "main.py" ]