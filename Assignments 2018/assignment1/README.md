# Assignment 1
Details about this assignment can be found [on the course webpage](http://cs231n.github.io/), under Assignment #1 of Spring 2018.

## Final results
| Classifier | Features | Learning rate | Regularization strength | Batch size | Number of iterations | Other hyperparameters | Training accuracy | Test accuracy |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| kNN | raw pixels | - | - | - | - | k = 10 | - | 33.86% |
| kNN | HOG + hue  | - | - | - | - | k = 13 | - | 44.31% |
| Softmax | raw pixels | 5.000000e-07 | 3.214286e+04 | 200 | 1500 | - | 31.52% | 32.08% |
| Softmax | HOG + hue  | 5.000000e-07 | 1.000000e+04 | 200 | 1500| - | 41.53% | 40.93% |
| SVM | raw pixels | 1.258925e-07 | 1.467799e+04 | 2000 | 1500 | - | 38.43% | 37.62% |
| SVM | HOG + hue  | 1.000000e-08 | 1.000000e+06 | 200 | 3000 | - | 41.50% | 41.11% |
| Two layer net | raw pixels | 1.000000e-03 | 1.000000e+00 | 200 | 50000 | lr_decay: 0.95, hidden_dim: 100| 55.41% | 51.71% |
| Two layer net | HOG + hue | 1.000000e-01 | 1.584893e-11 | 200 | 15000 | lr_decay: 0.95, hidden_dim: 100 | 64.85% | **57.83%** |
