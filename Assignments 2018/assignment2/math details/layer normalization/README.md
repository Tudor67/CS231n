# Layer Normalization

## [Layer Normalization (Ba _et al._, 2016)](https://arxiv.org/abs/1607.06450)
* Training deep neural networks is computationally expensive. One way to reduce the training time is to normalize the activations of the neurons.

* __Batch Normalization__:  
   1.) The effect of BN is dependent on the mini-batch size. It is less useful in complex networks which have a cap on the input batch size due to hardware limitations;  
   2.) Can't be applied to online learning tasks or to extremely large distributed models where the mini-batches have to be small;  
   3.) Does not perform exactly the same computation at training and test times;  
   4.) It is not obvious how to apply it to recurrent neural networks.

* __Layer Normalization__:  
   1.) The effect of LN is not dependent on the mini-batch size. The normalization is done separately over the feature vector corresponding to a single datapoint, not over the batch;  
   2.) Can be used in the pure online regime with batch size 1;  
   3.) Performs exactly the same computation at training and test times;  
   4.) It is straightforward to apply it to recurrent neural networks;  
   5.) It is very effective at stabilizing the hidden state dynamics in recurrent networks;  
   6.) Can substantially reduce the training time compared with previously published techniques.

* Both __Batch__ and __Layer Normalization__:  
   1.) Each neuron has its own adaptive scale and bias;  
   2.) Normalization is applied before the non-linearity.
