#!/bin/bash

#SBATCH --job-name=diffuseq
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem-per-cpu=5g
#SBATCH --gres=gpu:1
#SBATCH --time=3:00:00
#SBATCH --account=eecs598s007f22_class
#SBATCH --partition=spgpu
#SBATCH --mail-user=yiweilyu@umich.edu
#SBATCH --export=ALL



python -u run_decode.py \
--model_dir /home/yiweilyu/DiffuSeq/diffusion_models/diffuseq_TPA_h128_lr1e-05_t1000_sqrt_lossaware_seed103_TPA20230111-17:39:51 \
--seed 132 \
--split test \
--pattern ema_0.9999_1


