#!/bin/bash

#SBATCH --partition=pool3-bigmem

# set the number of nodes
#SBATCH --nodes=1

# set max wallclock time
#SBATCH --time=4:00:00

# set name of job
#SBATCH --job-name=smith

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=haohanw@andrew.cmu.edu

# run the application
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/clustering/clustering.py > logs.txt