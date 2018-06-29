# Transfer Learning
* Pretrain a ConvNet on a very large dataset and then use the ConvNet either as an initialization or a fixed feature extractor for the task of interest;
* ConvNet features:
   1. in early layers: more generic features;
   2. in later layers: more original-dataset-specific features.


## [DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition (Donahue _et al._)](https://arxiv.org/abs/1310.1531)
* In _CVPR_, 2013;  
* The philosophy of supervised transfer: one may view the trained model as an analog to the prior knowledge a human obtains from previous visual experiences, which helps in learning new tasks more efficiently.  
* A common deep learning knowledge: the first layers learn "low-level" features, whereas the latter layers learn semantic or "high-level" features.  

* DeCAF not only provides better within category clustering, but also clusters same category instances across domains. This indicates qualitatively that DeCAF removed some of the domain bias (in domain adaptation situation).  
* The authors demonstrate that by leveraging an auxiliary large labeled object database to train a deep convolutional architecture, they can learn features that have sufficient representational power and generalization ability to perform semantic visual discrimination tasks using simple linear classifiers, reliably outperforming current state-of-the-art approaches.  


## [How transferable are features in deep neural networks? (Yosinski _et al._)](https://arxiv.org/abs/1411.1792)
* In _NIPS_, 2014;  
* In case of many deep neural networks trained on natural images:  
   1. First-layer features: general in that they are applicable to many datasets and tasks;  
   2. Last-layer features: specific to a particular dataset or task;  

* Features must eventually transition from general to specific by the last layer of the network;  

* The transferability of features decreases as the distance between the base task and target task increases;  

* Initializing a network with transferred features from almost any number of layers can produce a boost to generalization that lingers even after fine-tuning to the target dataset;  

* In transfer learning, we first train a base network on a base dataset and task, and then we repurpose the learned features, or transfer them, to a second target network to be trained on a target dataset and task. This process will tend to work if the features are general, meaning suitable to both base and target tasks, instead of specific to the base task.

* Problems when you freeze a half of network and try to fine-tune the remaining layers:  
  The original network contained fragile co-adapted features on successive layers, that is, features that interact with each other in a complex or fragile way such that this co-adaptation could not be relearned by the upper layers alone. Optimization difficulties may be worse in the middle of a network than near the bottom or top.  

* Initializing with transferred features can improve generalization performance even after substantial fine-tuning on a new task, which could be a generally useful technique for improving deep neural network performance.  


## [CNN Features off-the-shelf: an Astounding Baseline for Recognition (Razavian _et al._)](https://arxiv.org/abs/1403.6382)
* In _CVPR_, 2015;  
* Recent results indicate that the generic descriptors extracted from the convolutional neural networks are very powerful;  
* These features can be used for different computer vision tasks;  

* __Fine-grained classification__: distinguish between sub-categories of a category such as the different species of flowers, dog breeds.  
* Fine-grained recognition datasets:  
   1. Caltech-UCSD Birds (CUB) 200-2011:  
       * 200 classes;  
       * 11,788 images: 5,994 for train and 5,794 for test.  
   2. Oxford 102 flowers dataset:  
       * 102 categories;  
       * each category contains 40 to 258 images;  
       * the dataset provides segmentation for all the images.  

* __Attribute detection__
* An attribute within the context of computer vision is defined as some semantic or abstract quality which different instances/categories share.  
* Attribute detection datasets:  
   1. UIUC 64 object attributes dataset:  
      * 3 categories of attributes:  
       * shape (e.g. is 2D boxy);   
       * part (e.g. has head);  
       * material (e.g. is furry).  
   2. H3D dataset:  
      * defines 9 attributes for a subset of the person images from PASCAL VOC 2007;  
      * the attributes range from "has glasses" to "is male".  

* OverFeat:  
   * a convnet trained for the image classification task of ILSVRC2013;  
   * won the localization task of ILSVRC2013.  
* A poselet describes a particular part of the human pose under a given viewpoint.  
