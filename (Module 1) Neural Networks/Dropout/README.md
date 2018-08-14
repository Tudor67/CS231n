# Dropout


## [Improving neural networks by preventing co-adaptation of feature detectors (Hinton _et al._, 2012)](https://arxiv.org/abs/1207.0580)
* Random "dropout":  
1.) gives big improvements on many benchmark tasks;  
2.) sets new records for speech and object recognition.

* Dropout can be seen as a very efficient way of performing model averaging with neural networks.

* Dropout forces the discriminative model to learn good features which are less co-adapted and leads to a better generalization.

* Using non-convolutional higher layers with a lot of parameters leads to a big improvement with dropout but makes things worse without dropout.


## [Dropout Training as Adaptive Regularization (Wager _et al._, 2013)](https://arxiv.org/abs/1307.1493)
* Authors' analysis shows that dropout regularization should be better than L2-regularization for learning weights for features that are rare (i.e., often 0) but highly discriminative, because dropout effectively does not penalize ßj over observations for which x(i, j) = 0.

* Remember that a problem with classic SGD is that it can be slow at learning weights corresponding to rare but highly discriminative features. This problem can be alleviated using stochastic descent rules from the AdaGrad family.


## [Dropout: A Simple Way to Prevent Neural Networks from Overfitting (Srivastava _et al._, 2014)](http://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf)

* Dropout: randomly drop units (along with their connections) from the neural network during training.
  This prevents units from co-adapting too much.

* Dropout is a general technique and is not specific to any domain.

* The central idea of dropout is to take a large model that overfits easily and repeatedly sample and train smaller sub-models from it.

* Applying dropout to a neural network amounts to sampling a "thinned" network from it. The thinned network consists of all the units that survived dropout.

* Dropout:  
  1.) Training: samples from an exponential number of different "thinned" networks;  
  2.) Test: use a single unthinned network (approximate the effect of averaging the predictions of all these thinned networks).

* Dropout significantly reduces overfitting and gives major improvements over other regularization methods. It can be interpreted as a form of model averaging.

* The idea of dropout is not limited to feed-forward neural nets and can be more generally applied to graphical models such as Boltzmann Machines.

* Dropout does break up co-adaptations (among hidden units), which is probably the main reason why it leads to lower generalization errors.

* Dropout automatically leads to sparse representations.

* Experimental results:  
  1.) Dropout improved generalization performance on all data sets compared to neural nets that did not use dropout;  
  2.) For extremely small data sets (100, 500) dropout does not give any improvements;  
  3.) The weight scaling method (at test time) is a fairly good approximation of the true model average.

* Drawbacks:  
  1.) Dropout increases training time. It takes 2-3 times longer to train than a standard neural net of the same architecture.

* Advices:  
  a.) It is to be expected that dropping units will reduce the capacity of a neural network.  
      If an n-sized layer is optimal for a standard neural net, a good dropout net should have at least n/p units.  
  b.) A dropout net should typically use 10-100 times the learning rate that was optimal for a standard neural net.  
      While momentum values of 0.9 are common for standard nets, with dropout values around 0.95 to 0.99 work quite a lot better.  
  c.) Max-norm regularization can prevent the network weights to grow very large (caused by large learning rate and momentum).  
      This constraints the norm of the vector of incoming weights at each hidden unit to be bound by a constant c (typical values of c: range(3, 4)).  
  d.) Typical values of __*p*__ (the probability of retaining a unit) are in the range 0.5 to 0.8.  
  e.) For hidden layers, the choice of __*p*__ is coupled with the choice of number of hidden units __*n*__.
