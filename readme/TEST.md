# Testing your model

## For a single instrument class 

1. In `CenterNet_ROOT/src/lib/datasets/dataset` modify `instrument.py` like this `if split == 'test' : ...` : 

    <p align="center">  <img src='test_instrument.png' align="center" height="230px"> </p>


    The function is to specify the label file as the test file test.coco.json created before.



## For multiple classes 