# Assignment 1
Details about this assignment can be found [on the course webpage](http://cs231n.github.io/), under Assignment #1 of Spring 2018.

## Final results
| Classifier | Features | Number of iterations | Other hyperparameters | Training accuracy | Test accuracy |
| :---: | :---: | :---: | :---: | :---: | :---: |
| kNN | raw pixels | - | k = 10 | - | 33.86% |
| kNN | HOG + hue  | - | k = 13 | - | 44.31% |
| Softmax | raw pixels | 1500 | - | 31.52% | 32.08% |
| Softmax | HOG + hue  | 1500| - | 41.53% | 40.93% |
| SVM | raw pixels | 1500 | - | 38.43% | 37.62% |
| SVM | HOG + hue  | 3000 | - | 41.50% | 41.11% |
| Two layer net | raw pixels | 50000 | lr_decay: 0.95, hidden_dim: 100| 55.41% | 51.71% |
| Two layer net | HOG + hue | 15000 | lr_decay: 0.95, hidden_dim: 100 | 64.85% | **57.83%** |
