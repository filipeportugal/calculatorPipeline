RUN apk update
RUN apk add git
RUN apk add openssh
RUN apk update

RUN git clone https://github.com/filipeportugal/calculatorPipeline.git
WORKDIR calculatorPipeline/dockerfile

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /calculatorPipeline
ENV PYTHONPATH /calculatorPipeline
