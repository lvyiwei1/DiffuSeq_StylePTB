# DiffuSeq_StylePTB

This repository is contains code for reproducing the results in [Fine-grained Text Style Transfer with Diffusion-Based Language Models](https://arxiv.org/abs/2305.19512).

The majority of code from this repository is taken or adapted from [DiffuSeq repository](https://github.com/Shark-NLP/DiffuSeq). Please see their repository for environment configuration and package installation instructions.

We included the processed data of [StylePTB](https://github.com/lvyiwei1/StylePTB) under the dataset folder. Each subfolder is either a single style transfer (such as "VEM" for verb emphasis), the combined dataset for multitask training ("multitask"), or compositional style transfers (such as "Tense + PP Removal").

To train a model on a particular dataset, first go into the `scripts` directory with `cd scripts`. Then, in `train.sh`, edit the field "data_dir" to your desired dataset (for example, to train on the transfer "verb emphiasis", set data_dir to ".../datasets/VEM"). Also edit "dataset" and "notes" to the desired dataset name. Then you can start training by `bash train.sh`.

When training is done, trained model checkpoints will show up under `diffusiom_models/`. To run inference, edit `run_decode.sh` to include your desired dataset as well as the checkpoint you want to use. Then, run `bash run_decode.sh`. The result will be under `generation_outputs/` folder.

To evaluate the results, use `tohypref.py` to convert an output json under `generation_outputs/` into hypothesis+reference. Then use [nlgeval](https://github.com/Maluuba/nlg-eval) to evaluate metrics between `../hyp.txt` and `../ref.txt` using 
```
nlg-eval --hypothesis ../hyp.txt --references ../ref.txt
```

