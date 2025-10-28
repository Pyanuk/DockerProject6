FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    x11-apps \
    xauth \
    python3 \
    python3-tk \
    && rm -rf /var/lib/apt/lists/* 
    
ENV DISPLAY=host.docker.internal:0

COPY calc.py .

CMD [ "python3", "calc.py" ]