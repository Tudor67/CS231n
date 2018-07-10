import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_classes = W.shape[1]
  num_train = X.shape[0]
  max_score = np.max(X.dot(W))
  for i in range(num_train):
    scores = X[i].dot(W)
    scores = np.exp(scores - max_score)
    p = scores / np.sum(scores)
    
    loss -= np.log(p[y[i]])
    for j in range(num_classes):
      if j == y[i]:
        dW[:, y[i]] += (p[y[i]] - 1) * X[i]
      else:
        dW[:, j] += p[j] * X[i]
  
  # average
  loss /= num_train
  dW /= num_train
    
  # add regularization 
  loss += reg * np.sum(W * W)
  dW += 2 * reg * W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  max_score = np.max(scores)
  scores = np.exp(scores - max_score)
  
  p = scores / np.sum(scores, axis=1)[:, np.newaxis]
  
  loss_i = -np.log(p[range(num_train), y])
  loss = np.mean(loss_i) + reg * np.sum(W * W)
    
  mask = p
  mask[range(num_train), y] -= 1
  dW = np.dot(X.T, mask)
  dW /= num_train
  dW += 2 * reg * W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

