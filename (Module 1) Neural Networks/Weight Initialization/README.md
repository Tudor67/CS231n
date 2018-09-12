# Weight initialization
* In a neural network with a random initialization variance of the weights tends to increase when moving from the first to last layers. This can be considered a big problem for deep networks because the weights and its backpropagated gradients can explode or diminish.

* To solve the above problem some solution were proposed:  
1.) Xavier (also known as Glorot) initialization:  N(0, 2 / (n\_in + n\_out)).  
    It is used with saturating non-linearities (sigmoid, tanh).  
2.) Kaiming (also known as He) initialization:  N(0, 2 / n\_in).  
    It is used with non-saturating non-linearities (ReLU, Leaky-ReLU, PReLU).

* In practice, it is recommended to use ReLU non-linearities with Kaiming initialization (N(0, 2 / n\_in)).

* More details can be found in the original papers.

* Good links:
   * http://cs231n.github.io/neural-networks-2/#init
   * https://prateekvjoshi.com/2016/03/29/understanding-xavier-initialization-in-deep-neural-networks/
   * https://www.youtube.com/watch?v=s2coXdufOzE
   * https://www.youtube.com/watch?v=8krd5qKVw-Q


## [Understanding the difficulty of training deep feedforward neural networks (Xavier Glorot and Yoshua Bengio, 2010)](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf)
* Two things we want to avoid (from the evolution of activations):  
1.) Excessive saturation of activation functions (then gradients will not propagate well);  
2.) Overly linear units (they will not compute something interesting).

* The variance of the back-propagated gradients decreases as we go backward in the network.

* Sigmoid activations should be avoided when initializing from small random weights, because they yield poor learning dynamics, with initial saturation of the top hidden layers.

* It is helpful for learning to keep the layer-to-layer transformations such that both activations and gradients flow well.

* Xavier initialization is based on the assumption that the activations are linear.

* Xavier initialization better fits with saturating activation functions (sigmoid, tanh).

* The recommended initializations:  
1.) N(0, 1 / n\_in);  
2.) N(0, 2 / (n\_in + n\_out));  
3.) U(-sqrt(6 / (n\_in + n\_out)), sqrt(6 / (n\_in + n\_out))).


## [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification (Kaiming He _et al._, 2015)](https://arxiv.org/abs/1502.01852)
* A proper initialization method should avoid reducing or magnifying the magnitudes of input signals exponentially.

* Kaiming initialization allows for extremely deep models to converge (e.g. 30 conv/fc layers), while the Xavier method cannot.

* Kaiming initialization better fits with non-saturating activation functions (ReLU, Leaky-ReLU, PReLU).

* The recommended initialization:  
1.) N(0, 2 / n\_in).
