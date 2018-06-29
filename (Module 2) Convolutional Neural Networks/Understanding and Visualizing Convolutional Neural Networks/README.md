## [Visualizing and Understanding Convolutional Networks (Zeiler and Fergus, 2013)](https://arxiv.org/abs/1311.2901)
* Small tranformations of the image have:  
   1.) in the first layer of convnet: dramatic effect;  
   2.) at the top feature layer of convnet: a lesser impact (can be considered quasilinear for translation & scaling);  

* Higher layers generally produce more discriminative features.  

* ImageNet feature extractor is really powerful (just 6 Caltech-256 images are needed to beat the leading method (in 2013) using 10 times as many images).  


## [Explaining and Harnessing Adversarial Examples (Goodfellow _et al._, 2014)](https://arxiv.org/abs/1412.6572) 
* __Adversarial examples__: inputs formed by applying small but intentionally worst-case perturbations to examples from the dataset, such that the perturbed input results in the model outputting an incorrect answer with high confidence.  

* A simple linear model can have adversarial examples if its input has sufficient dimensionality.
  Softmax regression is vulnerable to adversarial examples.

* __Fast gradient sign method__ of generating adversarial examples:
  x + eta => new_x (adversarial example)
  eta = eps * sign (gradientxJ(theta, x, y)).
  eps - a small constant (for example 0.007),
  theta - the parameters of a model,
  x - the input to the model,
  y - the targets associated with x (for machine learning tasks that have targets),
  J(theta, x, y) - the cost used to train the neural network.

* The authors found that above method reliably causes a wide variety of models to misclassify their input.

* Other simple methods of generating adversarial examples are possible. For example, authors of the paper also found that rotating x by a small angle in the direction of the gradient reliably produces adversarial examples.

* One reason that the existence of adversarial examples can seem counter-intuitive is that most of us have poor intuitions for high dimensional spaces. We live in three dimensions, so we are not used to small effects in hundreds of dimensions adding up to create a large effect. 

* RBF networks are naturally immune to adversarial examples, in the sense that they have low confidence when they are fooled.

* An intriguing aspect of adversarial examples is that an example generated for one model is often misclassified by other models, even when they have different architectures or were trained on disjoint training sets. Moreover, when these different models misclassify an adversarial example, they often agree with each other on its class.

* Another hypothesis about why adversarial examples exist is that individual models have strange quirks but averaging over many models can cause adversarial examples to wash out.

* Ensembles are not resistant to adversarial examples.

* Models that are easy to optimize are easy to perturb.

* Linear models lack the capacity to resist adversarial perturbation; only structures with a hidden layer (where the universal approximator theorem applies) should be trained to resist adversarial perturbation.

* The existence of adversarial examples suggests that being able to explain the training data or even being able to correctly label the test data does not imply that our models truly understand the tasks we have asked them to perform.


## [ImageNet Large Scale Visual Recognition Challenge (Russakovsky _et al._, 2014)](https://arxiv.org/abs/1409.0575)
* Some datasets for segmentation (useful for my research):  
    * MSRC Dataset (Criminisi, 2004)  
       - 591 images;  
       - 23 object classes;  
    * Stanford Background Dataset (Gould _et al._, 2009)  
       - 715 images;  
       - 8 classes;  
    * Berkely Segmentation Dataset (Arbelaez _et al._, 2011)  
       - 500 images annotated with object boundaries;  
    * PASCAL VOC Dataset (Everingham _et al._, 2010, 2014);  
    * COCO Dataset (Lin _et al._, 2014b)  
       - more than 328,000 images;  
       - with 2.5 million object instances manually segmented.  


## [Striving for Simplicity: The All Convolutional Net (Springenberg _et al._, 2014)](https://arxiv.org/abs/1412.6806)
* Why __pooling__ can help in CNNs?  
  1.) a __more invariant representation__ in CNN;  
  2.) the __spatial dimensionality reduction__ performed by pooling makes covering larger parts of the input in higher layers possible;  
  3.) the feature-wise nature of the pooling operation (as opposed to a convolutional layer where features get mixed) could make the optimization easier.  

* Pooling can be removed from a network without abandoning the spatial dimensionality reduction by 2 means:  
    1. remove each pooling layer and increase the stride of the convolutional layer that preceded it accordingly;  
       * _downside_:  
       significantly reduces the overlap of the convolutional layer that preceded the pooling layer;  
       it is equivalent to a pooling operation in which only the top-left feature response is considered and can result in less accurate recognition;  
    2. replace the pooling layer by a normal convolution with stride larger than one;  
      this can be seen as learning the pooling operation rather than fixing it;  
       * _downside_: increase of overall network parameters;  

* Max-pooling may not be necessary for training large-scale convolutional networks.  


## [Fractional Max-Pooling (Graham, 2014)](https://arxiv.org/abs/1412.6071)
* __MP2: 2x2 max-pooling__ - has been the default choice for building conv nets for a long time;
* Reasons for the popularity of MP2:  
  1.) it is fast, it quickly reduces the size of the hidden layers;  
  2.) it encodes a degree of invariance with respect to translations and elastic distortions.  

* Each layer of pooling is an opportunity to view the input image at a different scale;  
* With FMP we can view the input image at more scales => viewing images at the 'right' scale should make it easier to recognize tell-tale features that identify an object as belonging to a particular class.  

* __FMP: fractional max-pooling__ - a particular form of max-pooling;  
* The idea of FMP is to reduce the image by a factor alpha with 1 < alpha < 2;  
* To generate the pooling regions of FMP: use random or pseudorandom sequences;  
* Pooling regions can be either disjoint or overlapping;  
* Overlapping FMP seems to be better than disjoint FMP;  
* The authors of the paper have trained convolutional networks with fractional max-pooling on a number of popular datasets and found substantial improvements in performance.   

