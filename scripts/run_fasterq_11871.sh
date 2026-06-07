#!/bin/bash

fasterq-dump data/SRR19077323/SRR19077323.sra \
    --split-files \
    -e 16 \
    -O fastq/11871T

pigz -p 16 fastq/11871T/*.fastq

fasterq-dump data/SRR19077324/SRR19077324.sra \
    --split-files \
    -e 16 \
    -O fastq/11871N

pigz -p 16 fastq/11871N/*.fastq
