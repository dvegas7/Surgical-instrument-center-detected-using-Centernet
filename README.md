# Surgical instrument center detected using Centernet

Detection of instrument centers using CenterNet: 
![alt text](readme/center.png)

## Disclaimer
This project is based on [CenterNet](https://github.com/xingyizhou/CenterNet) , created by [xingyizhou](https://github.com/xingyizhou). My work consists of modifications and additions to this repository, but it remains fundamentally based on the original author's work.

All credit for the original work and original contributions must be attributed to the original author. I claim no authority over the original repository, its goals, or its future versions.

If you are interested in the original repository or wish to contribute to it, please refer to the link above.
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
python demo.py ctdet --demo ../images/instrument1.jpg --load_model ../models/model_best_final.pth
~~~

If set up correctly, the output with the above command should look like this :

<p align="center">  <img src='readme/image_test1.png' align="center" height="300px"> </p>

Add --debug 2 to the previous command to visualize the heatmap output.

~~~
python demo.py ctdet --demo ../images/instrument2.jpg --load_model ../models/model_best_final.pth --debug 2
~~~

Output should look like this :
<p align="center">  <img src='readme/image_test2.png' align="center" height="300px"> <img src='readme/image_test_heatmap2.png' align="center" height="300px"></p>

If you want to have the coordinates (x,y) of the instruments centers add --debug 5 and the coordinates will be written in `CenterNet_ROOT/src/coordinates.txt`

~~~
python demo.py ctdet --demo ../images/instrument2.jpg --load_model ../models/model_best_final.pth --debug 5

~~~
## Training on your own dataset
If you want to use your own dataset to train CenterNet you can. All the details are in [TRAIN.md](readme/TRAIN.md)