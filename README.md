# CenterNet-instrument

Detection of instrument centers using CenterNet: 
![alt text](readme/center.png)

## Disclaimer
This project is based on [CenterNet](https://github.com/xingyizhou/CenterNet) , created by [xingyizhou](https://github.com/xingyizhou). My work consists of modifications and additions to this repository, but it remains fundamentally based on the original author's work.

All credit for the original work and original contributions must be attributed to the original author. I claim no authority over the original repository, its goals, or its future versions.

If you are interested in the original repository or wish to contribute to it, please refer to the original repository by following the link above.
## Installation
All the installation instructions can be found in [INSTALLATION.md](readme/INSTALLATION.md) 

## Use CenterNet-instrument

Images and videos are supported for demo. 

First, download the models and put them in `CenterNet_ROOT/models/` (model_best_final by default)

For object detection on images/ video, go to `CenterNet_ROOT/src/` and run :

~~~
python demo.py ctdet --demo /path/to/image/or/folder/or/video --load_model ../models/model_best_final.pth
~~~

You can find example images in `CenterNet_ROOT/images/`

Example:

~~~
python demo.py ctdet --demo /path/to/image/or/folder/or/video --load_model ../models/model_best_final.pth
~~~

If set up correctly, the output with the above command should look like this :