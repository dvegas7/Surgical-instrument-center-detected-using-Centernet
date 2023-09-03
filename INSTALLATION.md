# Installation

Everything was carried out on Ubuntu 18.04, with Anconda (or Miniconda). You'll need a Nvidia GPU with CUDA 10.0 or 11.0 (tested on 10.0). The use of a GPU is highly recommended, especially for training. If you still want to use your CPU, please refer to [INSTALLATION_CPU.md](INSTLATTION_CPU.md)

0. Prerequisite installations
   ~~~
   sudo apt install g++ cmake make git 
   ~~~
1. Create a new conda environment
   ~~~
   conda create --name CenterNet python=3.6
   ~~~

   And activate the env
   ~~~
   conda activate CenterNet
   ~~~
2. Install Pytorch 1.2.0
   ~~~
   conda install pytorch=1.2.0 torchvision -c pytorch
   ~~~
   Open `miniconda3/envs/CenterNet/lib/python3.6/sites-packages/torch/nn/functional.py` or `Anaconda3/envs/CenterNet/lib/python3.6/sites-packages/torch/nn/functional.py` (if you are using Anaconda).
   Find the line with `torch.batch_norm` and replace the `torch.backends.cudnn.enabled` with `False`.
   
   
