# Scientific Research Seminar
Materials for the scientific research seminar of Data Mining master program of Computer Science faculty of the Higher School of Economics. Spreadsheets with all experiments are available [here](https://drive.google.com/open?id=1eEYORHcoE0r3T1hn4_mUFU9OfP4AZSNQ)

*National Research University - Higher School of Economics* &copy; 2019

## Task-1
- NonCNN Network in MNIST digit classification task

|  optimizer | epochs_max | layers | batch_size | activation | best_acc |
| --- | --- | --- | --- | --- | --- |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 8 | relu | 90,00 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 16 | relu | 95,26 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 32 | relu | 96,72 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 64 | relu | 96,92 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 128 | relu | 97,28 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 256 | relu | 97,18 |
|  ADAM (0.01) | 10 | 3 (512, 256, 10) | 512 | relu | 97,36 |
|  SGD(0.01) | 10 | 3 (512, 256, 10) | 512 | relu | 97,68 |
|  SGD(0.01) | 25 | 3 (512, 256, 10) | 512 | relu | 98,00 |
|  SGD(0.001) start from exp000 | 25 | 3 (512, 256, 10) | 512 | relu | 98,45 |
|  SGD(0.0003) start from exp001 | 25 | 3 (512, 256, 10) | 512 | relu | **98,51** |
|   |  |  |  |  |  |
|  SGD(0.01) | 25 | 3 (512, 256, 10) | 512 | sigmoid | 98,00 |
|  SGD(0.001) from exp002 | 25 | 3 (512, 256, 10) | 512 | sigmoid | 98,40 |
|   |  |  |  |  |  |
|  ADAM(0.01) | 25 | 9(512,1024,2048,1024,512,258,128,64,10) | 512 | relu | 11,00 |
|  ADAM(0.01) | 25 | 5(512,512,512,128,10) | 512 | relu | 97,80 |
|  SGD(0.001) from exp003 | 25 | 5(512,512,512,128,10) | 512 | relu | 98,16 |

## Task-2

- CNN Network in MNIST digit classification task

|  optimizer | epochs_max | layers | batch_size | best_acc |
| --- | --- | --- | --- | --- |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 16 | 97,03 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 32 | 98,11 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 64 | 98,55 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 128 | 98,87 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 256 | 99,05 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 512 | 99,06 |
|  ADAM (0.01) | 10 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 1024 | 99,23 |
|  SGD (0.01) | 250 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 1024 | 98,23 |
|  SGD (0.001) start from exp000 | 30 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 1024 | 99,23 |
|  SGD (0.0001) start from exp000 | 30 | conv(10x5x5) -> relu -> maxpool(2x2) -> conv(30x3x3) > relu -> maxpool(2x2) -> fc(100) -> fc(10) | 1024 | **99,23** |

## Task-3
Cat / Dog classifier using transfer learning technique
- Use ConvNet as feature extractor
- Fine-tune ConvNet

|  method | feature extractor | fune-tune |
| --- | --- | --- |
|  KNN | 0,78 | **0,98** |
|  SVM | 0,64 | 0,83 |
|  Decision Tree | 0,62 | 0,94 |
|  Random Forest | 0,75 | 0,97 |
|  Gradient Boosting | 0,69 | 0,96 |
|  MLP | **0,87** | 0,97 |

## Task-4
Use NN as feature extractor for audio files
- Audio commands
- Audio digits

|  method | commands | digits |
| --- | --- | --- |
|  KNN | 0,61 | **0,81** |
|  SVM | 0,31 | 0,53 |
|  Decision Tree | 0,20 | 0,47 |
|  Random Forest | 0,63 | 0,79 |
|  Gradient Boosting | 0,35 | 0,56 |
|  MLP | **0,78** | 0,78 |
