#!/bin/bash

#SBATCH --job-name=diffuseq
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --mem-per-cpu=10g
#SBATCH --gres=gpu:2
#SBATCH --time=240:00:00
#SBATCH --account=tocho1
#SBATCH --partition=spgpu
#SBATCH --mail-user=yiweilyu@umich.edu
#SBATCH --export=ALL


python -m torch.distributed.launch --nproc_per_node=2 --master_port=12258 --use_env run_train.py \
--diff_steps 1000 \
--lr 0.00001 \
--learning_steps 100000 \
--save_interval 1000 \
--seed 103 \
--noise_schedule sqrt \
--hidden_dim 128 \
--bsz 1024 \
--microbatch 256 \
--dataset TPA \
--data_dir ~/DiffuSeq/datasets/TPA \
--vocab bert \
--seq_len 64 \
--schedule_sampler lossaware \
--notes TPA
#--model_path diffusion_models/diffuseq_TFU_h768_lr0.0001_t1000_sqrt_lossaware_seed102_TFU20221130-16:15:47/ema_0.9999_029000.pt

