# НИС: Методы интелектуального анализа данных. 
Домашние задания по научно исследовательскому семинару "Методы интелектуального анализа данных",
 проводимому на магистерской программе "Интеллектуальный анализ данных" Факультета компьютерных наук Высшей школы экономики.
&copy;2019

## Paper reading

* [FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search](https://arxiv.org/abs/1812.03443)


## Object detection using Tensorflow API

* Train face detector from scratch using
[TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
* Dataset: [WIDER FACE](http://shuoyang1213.me/WIDERFACE/)
* Detector specification
  * Backbone: MobileNetv2 with depth multiplier 0.5 0.25
  * Detection head: SSD
  * Input resolution: 128x128
  * Validation dataset: [here](https://drive.google.com/file/d/1cbazjRELfd4mGaNWQnQB7essJBM0BAe0/view?usp=sharing)

* Samples of [config files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs
) for different architectures
* [Description](https://github.com/tensorflow/models/tree/master/research/object_detection/protos
) of config parameters can be found in corresponding proto files

What is expected to be done: 
* Average precision (AP) on validation dataset should be higher than 0.5
* Investigate effect of different training parameters on accuracy:
  * with/without Feature Pyramid Network
  * focal loss VS hard negative mining
  * image augmentation
** optimization parameters: learning rate schedule, Adam, SGD
** Demonstrate results: describe what was done, show plots of loss and accuracy during training, show examples with correct predictions and incorrect

Pipeline
* Parse dataset
* Prepare training and validation data in suitable for TF Object detection format
* Setup config file
* Run training
* Make experiments


## GAN 

* Задание - натренируйте GANs на датасете MNIST, следуя указаниям в jupyter notebook файле. Задание можно выполнить либо на PyTorch (GANs-PyTorch.ipynb), либо на TensorFlow (GANs-TensorFlow.ipynb)
* Форма сдачи: сделайте презентацию, покажите сгенерированные изображения. Чем отличаются изображения, сгенерированные полно-связными (fully connected) и сверточными (convolutional) нейронными сетями и почему? 