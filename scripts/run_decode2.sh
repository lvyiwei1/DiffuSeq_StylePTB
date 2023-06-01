#!/bin/bash

#SBATCH --job-name=diffuseq
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=10g
#SBATCH --gres=gpu:1
#SBATCH --time=03:00:00
#SBATCH --account=eecs598s007f22_class
#SBATCH --partition=spgpu
#SBATCH --mail-user=yiweilyu@umich.edu
#SBATCH --export=ALL



python -u run_decode.py \
--model_dir /scratch/tocho_root/tocho1/yiweilyu/diffuseq_single_fusion_h128_lr0.0001_t1000_sqrt_lossaware_seed102_single_fusion20221206-21:31:40 \
--seed 123 \
--split test \
--pattern ema_0.9999_052
