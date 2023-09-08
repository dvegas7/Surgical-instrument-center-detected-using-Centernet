# Testing your model

## For a single instrument class 

1. In `CenterNet_ROOT/src/lib/datasets/dataset` modify `instrument.py` like this `if split == 'test' : ...` : 

    <p align="center">  <img src='test_instrument.png' align="center" height="230px"> </p>


    The function is to specify the label file as the test file test.coco.json created before.


2. Go to `CenterNet_ROOT/src` and run `test.py`

    ~~~
    python test.py --exp_id coco_dla --not_prefetch_test ctdet --load_model path/to/your/model
    ~~~

    For example :

    ~~~
    python test.py --exp_id coco_dla --not_prefetch_test ctdet --load_model /CenterNet_ROOT/exp/ctdet/coco_dla/model_best.pth
    ~~~

    If set up correctly, the output with the above command should look like this :

    <p align="center">  <img src='dernier_screen.png' align="center" height="400px"> </p>

    To understand the test results and how they are calculated please refer to [Results](#results)






## For multiple classes 

1. In `CenterNet_ROOT/src/lib/datasets/dataset` modify the `.py` created before (in my case `tools.py`) like this `if split == 'test' : ...` : 

    <p align="center">  <img src='tools_test.png' align="center" height="230px"> </p>


2. Go to `CenterNet_ROOT/src` and run `test.py`

    ~~~
    python test.py --exp_id coco_dla --not_prefetch_test ctdet --load_model path/to/your/model
    ~~~

    For example :

    ~~~
    python test.py --exp_id coco_dla --not_prefetch_test ctdet --load_model /CenterNet_ROOT/exp/ctdet/coco_dla/model_best.pth
    ~~~

    If set up correctly, the output with the above command should look like this :

    <p align="center">  <img src='dernier_screen.png' align="center" height="400px"> </p>

    To understand the test results and how they are calculated please refer to [Results](#results)

## Results 


As you can see after running `test.py`. We obtain a series of average precision `AP` and average recall `AR` values. This is how the results are obtained :

If you want all the details of the calculation, check [Object-Detection-Metrics](https://github.com/rafaelpadilla/Object-Detection-Metrics) it's all explained there. I'll try to summarize the most important points to help understanding how these results are obtained. 

### Intersection over union (IOU)

It measures the overlap between the ground-truth bounding boxes (the hand-labeled bounding boxes) and the predicted bounding boxes by the model. It is the ratio between the Intersection and Union of the ground truth boxes with the predicted bounding boxes.

This images from [Object-Detection-Metrics](https://github.com/rafaelpadilla/Object-Detection-Metrics) illustrates  the `IOU` :

<p align="center">  <img src='iou.png' align="center" height="150px"> </p>


Another visual example from our dataset :

<p align="center">  <img src='iou2.png' align="center" height="300px"> <img src='iou3.png' align="center" height="300px"></p>


In green the hand-labelled bounding boxe and in red the predicted one. In practice, we try to get as close as possible to the value 1, but an `IOU>0.50` is already good. 

### Precision and Recall

Precision and Recall are fundamental metrics used to evaluate the performance of classification and detection systems, including object detection in computer vision. Before discussing precision and recall, it's important to understand some key terms:

- True Positive `TP` : The number of times the model correctly predicted the positive input sample. In this context each time an instrument has been detected and located in the image. 

- False Positive `FP` : These are incorrect positive predictions. In this context, a false positive happens when the model incorrectly detects an instrument that is not present in the image.

- True Negative `TN` : These are the correct negative predictions made by a system. Here, a true negative occurs when the system correctly identifies the absence of an instrumenet, i.e., when there is no object in the image, and the model correctly doesn't detect one.

- False Negative `FN` : The number of time the model incorrectly predicted the positive input as negative. In our case false negative occurs when the model fails to detect an instrument that is actually present in the image.

Note that here a detection made by the model is considered True Positive only if it satisfies the two conditions:

- The confidence score of the predicted bounding box should be greater than the confidence threshold (which is 0.6 here), signifying that we have found the object for which we were looking.

- The `IoU` between the predicted bounding box and the hand-labelled bounding box should be greater than the `IoU` threshold (which can take several different values ranging from 0.5 to 0.95).

<p align="center">  <img src='TP.png' align="center" height="300px"> </p>

Here's an example of a True positive, the `IOU` is above the treshold and the confidence level is higher than 0.6. 


Now, let's discuss about precision and recall:

1. Precision measures the accuracy of positive predictions made by a system. It's the ratio of true positive predictions to all positive predictions, showing how accurate the system's positive guesses are. The formula is :


$$ Precision = {TP \over TP + FP} $$


    

2. Recall answers whether your model guessed every time that it should be guessing. The higher the recall, the more positive samples are detected. It is the ratio of true positive predictions to the total number of actual positive cases. Recall is crucial when it's essential to capture all relevant instances. The formula is :

$$ Recall = {TP \over TP + FN} $$

### Precision-Recall Curve and Average Precision

From what we saw, we understand that a model with high precision and recall correctly identifies positive samples and captures a substantial portion of all positive samples. In contrast, a model with high precision but low recall accurately predicts positive samples but misses a significant number of them, leading to an increased count of false negatives.

With this in mind, the aim is to find the best score for precision and recall. 

The Precision-Recall curve is as crucial, if not more so, in evaluating the performance of an object detection model. A good object detector maintains high precision and recall even when we change the confidence threshold (the probability that a box contains an instrument). It means that as we find more instruments (recall increases), we shouldn't see a significant drop in precision.

We can also assess the performance of object detectors by calculating the area under the Precision-Recall curve `p`, known as `AUC` (Area Under the Curve). `AP` (Average Precision) is another helpful metric for comparing different detectors. `AP` is a number that tells us how well a detector performs. In practical terms, `AP` is the average precision calculated for all possible recall values ranging from 0 to 1. It helps us compare detectors more easily because `AP` provides a single numerical measure of performance.

$$ AP = \int_{0}^{1} p(r) dr $$

To fully understand the importance of Precision-Recall and `AP` we would use [rafaelpadilla](https://github.com/rafaelpadilla) repo [Object-Detection-Metrics](https://github.com/rafaelpadilla/Object-Detection-Metrics) which provides an excellent example. 

Considering this detection : 

<p align="center">  <img src='rpadilla1.png' align="center" height="300px"> </p>

There are 7 images with 15 ground truth objects represented by the green bounding boxes and 24 detected objects represented by the red bounding boxes. Each object is detected with a certain level of confidence and assigned a letter from A to Y. 

To make this clearer, we provide a table with the detection identifier letter and confidence level for each image. The last column tells you whether the detection is `FP` or `TP`, depending on the conditions mentioned above (here the `IOU` threshold is 0.3).


<p align="center">  <img src='rpadilla2.png' align="center" height="550px"> </p>

The Precision-Recall curve is created by calculating precision and recall values based on the accumulated True Positives `TP and False Positives (FP) detections. To do this, we start by arranging the detections in order of their confidence scores. Then, we compute precision and recall for each step as we accumulate detections with the formula above, as demonstrated in the table below. Note that for recall computation, the denominator term ("Acc TP + Acc FN" or "All ground truths") is constant at 15 since hand-labelled boxes are constant irrespective of detections:


<p align="center">  <img src='rpadilla3.png' align="center" height="550px"> </p>


Example : for the 6th line (image 1), Precision = TP/(TP+FP) = 2/(2+4) = 1/3 and Recall = TP/(TP+FN) = (2/15) = 0.133333

When we plot the Precision values with the Recall values we obtain the Precision-Recall curve as follow :

<p align="center">  <img src='rpadilla4.png' align="center" height="350px"> </p>


