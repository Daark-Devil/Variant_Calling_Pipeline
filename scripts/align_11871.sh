#!/bin/bash

REF=reference/fasta/Homo_sapiens_assembly38.fasta

# Tumor
bwa mem -t 16 \
$REF \
fastq/11871T/SRR19077323_1.fastq.gz \
fastq/11871T/SRR19077323_2.fastq.gz \
> alignment/11871T.sam

# Normal
bwa mem -t 16 \
$REF \
fastq/11871N/SRR19077324_1.fastq.gz \
fastq/11871N/SRR19077324_2.fastq.gz \
> alignment/11871N.sam

