---
title: "Deep Metric Learning for Signature Verification"
date: 2021-06-09T08:48:00 
preview_image: /images/hugo/ff20_blog2_preview_img-1622115845.jpg
post_type: 
published: false
# external_url: 
---

By *[Victor](https://twitter.com/vykthur)* and *[Andrew.](https://www.linkedin.com/in/andrew-r-reed/)*

In our [previous blog post](/2021/05/27/pre-trained-models-as-a-strong-baseline-for-automatic-signature-verification.html), we discussed how pretrained models can serve as strong baselines for the task of signature verification. Essentially, using representations learned by models trained on the ImageNet task allowed us to obtain a 67% accuracy when attempting to correctly classify signature pairs as genuine or skilled forgeries. 

However, several intuitions (based on existing research) suggest that we might be able to improve on this area. First, given that the pretrained model was trained on data (natural images) which does differ from our task of signature images, it does make sense that some sort of fine tuning would be useful in adapting the pretrained model weights to our data distribution.

Second, the pretrained model is based on a classification objective - correctly classify 1 million images into 1000 different classes. While this objective yields semantic representation that have proven to be useful, our primary task of verification does require something more precise. Essentially, we want an objective focused on capturing the similarities/dissimilarities between two data points. To achieve this goal, we can turn to metric learning - learning a distance metric designed to satisfy the objective of making representations for similar objects close and representations for dissimilar objects far apart in some metric space. 


## What is Metric Learning

> Metric learning is the task of learning a distance function over objects.  wikipedia.

A simple description of metric learning is any machine learning model structured to learn a distance measure over samples. The intuition here is that if the model is designed to learn a distance function for similar/dissimilar objects, we can use it for applications such as signature verification that rely on this property. 

The distance learning objective can be formulated in several ways depending on the shape of input to the network. Commonly, sets of training examples are structured as either pairs or triplets of images from which a distance function is learned. Despite the differences in problem formulation, the high level metric learning workflow remains consistent:

- Define a set of input elements where each element consists of a set of example images (2 or 3 depending on loss function)
- Extract representations for each example in a given element using a trainable embedding mode
- Measure the similarity between examples in the element using a distance function (like Euclidean
- Calculate a loss based on the observed vs expected distances between examples
- Backpropagate the loss through the embedding network so the model learns to produce similar representations for similar examples and distant representations for dissimilar examples

## Siamese Networks with Contrastive Loss
A siamese network is a neural network architecture that conceptually contains two or more identical subnetworks that share the same configuration and parameters. Consequently, while training the network, all parameter updates are mirrored between the subnets such that the subnets remain in sync with each other. In practice, this setup actually results in one trainable network that independently processes inputs one at a time as seen in the figure below.

Contrastive loss (also known as pairwise ranking loss) is a metric learning objective function that operates with pairs of training data examples in a siames network. In our signature verification problem, we construct positive pairs consisting of an anchor signature and an alternative, genuine signature from the same author. We then construct negative pairs composed of an anchor signature and a forged signature authored by a different individual. The objective of our contrastive loss function is to learn representations with a small distance between them for positive pairs, and a large distance for negative pairs, as seen in Figure XYZ below.


##### Figure XYZ - A siamese network architecture where contrastive loss is used to minimize distance for genuine signature pairs (top) and maximize distance for negative pairs (bottom)

To learn such a representation, we define contrastive loss as:

where D is the calculated distance between vector 1 and vector 2, and m is a constant value of margin. In the case of positive pairs, the loss becomes positive only when we have a positive distance between vector representations. In the case of negative pairs, the loss is positive only when the distance between vectors is less than the margin. The margin value is a hyperparameter that serves as an upper threshold to constrain the amount of loss attributed to “easy to classify” pairs. A simple way to think about the function of the margin is that if the network produces representations that are distant “enough” for a given pair, there is no need to continue focusing training efforts on that example [1]. 

While contrastive loss is useful, it has a limitation. For points in a negative pair, contrastive loss will push them far apart without any knowledge of the broader embedding space. For example, imagine we have 10 classes; each time we see class 1 and 2, we want to push them far apart; a result of this is that 1 might now become farther from 2 on the average but might overlap with other classes such as class 3, 4, 5 etc. 

Triplet loss addresses this issue by using triplets in each training sample - an anchor, a positive (same class) and a negative (different class) data point. This way with each gradient update we learn to minimize anchor + positive distance whilst also ensuring that the anchor is also far from the negative point.

## Triplet Networks with Triplet Loss 
Similar to siamese networks, triplet networks have three identical subnets with shared weights. As the design and corresponding loss function suggests, these networks operate on triplet example inputs defined by an anchor image, a positive image, and a negative image.


##### Figure XYZ - A triplet network architecture where triplet loss is used to learn a mapping such that anchor/positive representations are closer than anchor/negative representations.

The triplet loss function aims to learn a distance between representations such that the anchor-to-positive distance is less than the anchor-to-negative distance. Similar to contrastive loss, a margin value is imposed on the anchor-to-negative distance so that once negative representations have enough distance between them no further effort is taken to increase distance between them. With this understanding, triplet loss is formally defined as:

where DP is the anchor-to-positive distance and DN is the anchor-to-negative distance. With this loss formulation, we can create three different types of triplet combinations based on how we sample:

- Easy triplets: result when DN > DP + m. Here, the sampled anchor-to-negative distance is already large enough so loss is 0 and the network has nothing to learn from.
- Hard triplets: result when DN < DP. In this case, the anchor-to-negative distance is less than the anchor-to-positive distance, meaning high loss to backpropagation through the network.
- Semi-hard triplets: result when DP < DN < DP + m. Semi-hard triplets occur when the negative example is more distant to the anchor than the positive example, but the distance is not greater than the margin, therefore resulting in a positive loss[^1].

Based on the above, we can see that different approaches for selecting triplets (also called _**triplet mining**_ approaches) are not equally informative. More importantly, if we prescriptively mine the right types of triplets that are informative, we can increase the overall efficiency of learning. Ideally, we want to focus on hard and semi-hard triplets - a luxury we were not afforded in the contrastive, pairwise learning setup. 

### From Offline to Online Triplet Mining

To implement any of the triplet strategies, we need to obtain embeddings for our samples so as to determine their distances and how best to construct our triplet. An initial offline approach will be to obtain embeddings for our entire training set and then select only hard or semi hard triplets. Assuming we have a training set of size T : 

- Get all embeddings for all points in T
- Get all possible triplets T3   in T
- Identify valid triplets  (hard or semi hard) based on embeddings which are then used for training. 
 
This approach is inefficient as it requires that we have a decent embedding extractor prior to training and that we extract embeddings for the entire training set to generate triplets.

We can be more efficient about this by adopting  online triplet mining [2]. Here, we select our triplets during training (within each  training batch) as opposed to precomputing triplets prior to training. Assuming we have a batch of size B :

- Get embeddings for all points in B 
- Get all possible triplets B3 in B 
- Identify valid triplets (hard or semi hard) based on class labels which are then used for training.

As we will see later on, the ability to sample intelligently and introduce relative knowledge between three examples helps improve training efficiency and results in more contextually robust feature embeddings.


## Other Losses - Quadruplet Loss, Group Loss

At this point, it is clear that a good loss function should attempt to learn similarity using information from each training sample. Contrastive loss learns from pairs of images (positive, negative).  Triplet loss achieves even better performance by simultaneously learning  from carefully selected images triplets (anchor, positive, negative) within a batch. But what if we could simultaneously learn from even more samples within a batch? It turns out that existing research has explored this. 

Several papers have introduced  **quadruplet losses**[^2] [^3], where each training sample consists of 4 data points (anchor, positive, negative1, negative2) where negative2 is dissimilar to all other data points. They minimize the distance between anchor and positive while simultaneously maximizing distance between anchor and negative1 as well as negative1 and negative2.

Elezi et al [^5] take this even one step further and propose the **group loss** which aims to simultaneously learn from all samples within a minibatch as opposed to a pair, triplet or quadruplet. To create the mini-batch, they sample from a fixed number of classes, with samples coming from a class forming a group. Thus, each mini-batch consists of several randomly chosen groups, and each group has a fixed number of samples. An iterative, fully-differentiable label propagation algorithm is then used to build feature embeddings which are similar for samples belonging to the same group, and dissimilar otherwise. The overall effect of this group loss formulation is to enforce embedding similarity across all samples of a group while promoting, at the same time, low-density regions amongst data points belonging to different groups.

One trend we can observe from these loss functions is that the more data points from multiple classes we use to update our gradients, the better our model is able to capture the global structure of the embedding space. In theory, quadruplet loss and group loss represent the state of the art in metric learning loss functions, but they introduce multiple parameters that can be challenging to implement and tune. Even when this is done correctly, the expected increase in performance (~1 - 4%) may be hard to reproduce, especially due to the stochastic nature of DNN training. In practice (as we will see in the experiment section), triplet loss (with online learning) is efficient, high performing and hence the recommended approach.

 

## Our Experimentation

### Dataset 

To evaluate a metric learning approach on our signature verification task, we experimented with contrastive and triplet loss. We first constructed an experimental setup consistent with the design from our pre-trained baseline experiment. Using the CEDAR dataset, we withheld signatures for 11 of the 55 authors as a test set and used the other 44 as a training set.   





Note that depending on the loss function, the strategy for constructing the eventual training dataset which the network learns from might differ. In our contrastive loss experiments, we generated a total of 36,432 pairs (xx positive pairs, xx hard negative pairs).  For our triplet loss experiments, given that we use the online triplet mining approach, we structure the dataset as a classification problem; each signer and each forgery is treated as a class, making for a total of 88 classes with 24 samples (2112 total)  each in the training set. Amongst other limitations, the CEDAR dataset is small; as we see later on, this makes it challenging to train a performant neural network from scratch.

To evaluate each model, we construct a set of pairs of positives and hard negatives (skilled forgeries) and report accuracy at a fixed threshold.

### Contrastive Loss Training and Evaluation
For contrastive loss, a siamese network was assembled using an embedding model composed of a frozen ResNet50 backbone with a series of 3 trainable layers appended to the network head (1 GlobalAveragePooling 2D layer and 2 Dense layers with 128 activations each). This approach allowed us to fine tune the already effective pre-trained ResNet50 feature extractor on our signature verification dataset using contrastive loss.

Through several training iterations, we found that introducing intermediate dropout and L2 regularization to our custom network head allowed us to achieve 78.2% max accuracy on the test set - an improvement of 11 percentage points over the pretrained ResNet50 baseline (67%)!

While these results are promising, there are several considerations to take into account when using contrastive loss. First, contrastive loss requires us to construct and train on an exhaustive list of genuine/forged examples. For our dataset, this means training on 36,432 sample pairs each epoch despite the fact that many of those pairs may not actually contribute any loss (and therefore learning) to the network because they are “easy” positives or negatives.

#####  Figure XYZ. A 3D plot of embeddings produced by the trained siamese network for three authors signatures. Genuine vs. forged examples are appropriately placed into separable regions as seen by groupings of circles vs. diamonds.

Second, contrastive loss is limited in its ability to learn global, contextual feature representations. Figure XYZ above depicts embeddings generated from the trained siamese network for genuine and forged signature examples from three authors. We observe that the network has correctly separated genuine vs. forged examples into separate regions which is precisely what contrastive loss aims to accomplish. However, the model has not captured the relative similarity of signatures from the same author (which can hurt generalization to new signature datasets). Ideally, we desire a model that produces embeddings that are separable across authors and discriminative between genuine/forged classes. For example, we would like to see that all signatures from Author 3 appear in the same general region, and within that region, signatures maintain separation between genuine and forged. Because contrastive loss is formulated by looking only at pairs of images, it cannot preserve a contextual understanding of author classes and simply just learns discriminative features between genuine and forged. This shortcoming is solved by triplet loss (as we will see), and therefore the remainder of our exploration focused on this superior loss function.

### Triplet Loss Training and Evaluation
We constructed several model architectures and trained them using the Triplet Semi Hard loss implemented in the Tensorflow addons library [5].  Each model has a similar set of final layers (two conv2D layers followed by a Dense layer and an L2 Normalization layer with size 256). We found that adding an L2 Normalization layer after our output embeddings (as suggested in [2]) was useful in constraining the embeddings to a hypersphere conducive for cosine similarity and resulted in an increase of ~4 percentage points for our best model. Each model was trained with the Adam optimizer (lr=0.001), with a learning rate decay of 0.7 ever 10 steps, and trained for 25 epochs.


#### Effect of Model Choices

Training multiple models allowed us to explore the impact of multiple model design choices which a datasciencist must navigate when applying metric learning in practice.  


 

- Impact of a Metric Loss Formulation:  We see that fine tuning a pretrained model using the triplet loss leads to a X percent improvement in accuracy for our best model.
- Impact of Pretrained Features: In the previous post, we saw that a pretrained model could be a strong baseline without any finetuning. To evaluate how much of the performance increase we see is attributable to the use of pre trained features (vs the triplet loss function), we trained a vanilla CNN as well as models constructed from intermediate layers of a pretrained ResNet and VGG16 model.
  - Vanilla CNN () - X% perf. X million params 
  - Vanilla Unet ()
  - Intermediate ResNEt50 () - best performance
  - Full ResNet50  
- Impact of Skip Connections: Skip connections in CNNs have been shown to improve the loss surface [^7] for deep networks making them easier to train and yielding performance.  We find that fine tuning a resnet model (which has skip connections) achieves better performance compared to fine tuning a VGG16 model
- Intermediate model vs Full Model: When applying transfer learning, the data scientist must decide how much of the pretrained model is useful to their task - i.e what features to include, what features to freeze and what features to finetune. We found that we got the best performance when we constructed an intermediate model from ResNet50 and fine tuned it vs fine tuning the entire ResNet50. Furthermore we found that when we constructed this intermediate model using the output of a skip connection vs a conv2D layer, the results were better. Our intuition is that the later layers  in a pretrained ResNet50 model contain high level features (e.g eyes, wheels, doors) that are not relevant to our task and dataset (which are mostly lines and texture in a signature) and can introduce noise. More importantly, an intermediate model is faster to train, significantly smaller, and hence easier to deploy (e.g. as a microservice with limits on file sizes).

#### Tips on training with triplet loss

- Ensure a large enough batch size is selected when training with the online triplet loss (on the minimum, batch size should be greater than the number of classes). This ensures each batch contains enough samples such that a valid semi hard triplet can be sampled. If you see a NaN loss value during training, this is indicative of a small enough batch size.
- Ensure the distance metric used in the loss function is the same distance metric that will be used during evaluation/test time. E.g. If cosine distance is used in the loss function during training, it should also be used when comparing the similarity of two signatures at test time. For example, a model trained with an L2 distance function will show reduced accuracy when evaluated with cosine distance. 
- Modifying the margin parameter can be used to improve the performance of each model. .e.g. If loss does not decrease during training, it might indicate that it is challenging to find good triplets (e.g. negatives are too hard and yield similar embeddings) ; in this case decreasing the margin parameter can be useful.


## Limitations

In this work, we show that fine tuning a pretrained model on a metric learning loss (contrastive and triplet loss) can improve performance. However there are a few limitations with our experiment set up that are worth noting:


- Dataset Limitations: While our training setup is designed such that we evaluate the models on signatures from individuals not represented in the training set, we recognize that the CEDAR dataset is small and does not cover properties of signatures (e.g. different writing styles, languages etc) that may occur in real world documents but are not covered in the CEDAR dataset. Training and evaluation on additional datasets is strongly recommended prior to production use.
- Reproducibility: Deep Neural networks can have multiple sources of randomness that can make it challenging to reproduce the exact results we report. These may include hardware properties, weight initialization, etc. In our experiments, we attempt to minimize this by fixing the seeds for numpy and tensorflow; we still observe slight variations across each run (~3 percentage points), however, the relative order of results stays consistent.  
- Model Tuning: In our experiments, while we explored the impact of metric loss finetuning,  pretrained features, skip connections over a small set of presets, there are still many parameters that can be tuned. These include margin parameter, model architecture (e.g. use of models with multiscale features).  


Other Loss Functions: While we have focused on contrastive and triplet loss, there are other valid and perhaps less complicated ways of fine tuning a pretrained model that yields good distance metrics. For example, we can explore a cross entropy loss that learns to predict a class (genuine, skilled forgery, unskilled forgery) given a pair of images.  The reader is encouraged to review this paper for further insight on how cross entropy loss compares with other metric learning losses [9].

## Summary and Conclusion

Metric learning helps us train a model that yields representations of similarity adapted to our task and dataset.  In this post we have covered several loss functions for metric learning (contrastive loss, triplet loss, quadruplet loss and group loss). We also report on a set of experiments training a model for signature verification on the CEDAR dataset.

- Triplet loss achieves better performance compared to contrastive loss and learns a better overall structure of the embedding space. 
- Triplet loss (with online triplet mining) is more efficient to train compared to contrastive loss i.e. amount of epochs/training time to reach maximum accuracy (10x less time). It does not require the manual construction of training triplets (as required in contrastive loss) and uses intelligent sampling to select informative triplets. This is very useful when running experiments to explore a large hyperparameter space. With respect to implementation, we found the Tensorflow addons implementation of triplet loss [^6] to be useful.  
- While triplet loss is great, its application is limited to scenarios where labels exist. To implement intelligent construction of triplets (especially semi hard negatives), we need labels for each class.  On the other hand, we can still apply contrastive loss to unlabelled datasets by leveraging pseudo labels  - e.g. Existing research [^8] shows that k-means assignments can be used as pseudo-labels to learn visual representations.
- Fine tuning an intermediate model can not only result in a reduced model size but also improved accuracy. Our experiments suggest that for the task of signature verification, fine tuning a subset of the ResNet50 model resulted in a smaller model size compared to fine tuning the entire ResNet50 model.




## References

[^1]: https://gombru.github.io/2019/04/03/ranking_loss/  
[^2]: Schroff, Florian, Dmitry Kalenichenko, and James Philbin. "Facenet: A unified embedding for face recognition and clustering." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.
[^3]: Chen, Weihua, et al. "Beyond triplet loss: a deep quadruplet network for person re-identification." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017. 
[^4]: Proença, Hugo, Ehsan Yaghoubi, and Pendar Alirezazadeh. "A Quadruplet Loss for Enforcing Semantically Coherent Embeddings in Multi-Output Classification Problems." IEEE Transactions on Information Forensics and Security 16 (2020): 800-811.
[^5]: Elezi, Ismail, et al. "The group loss for deep metric learning." European Conference on Computer Vision. Springer, Cham, 2020. 
[^6]: TensorFlow Addons Losses: TripletSemiHardLoss https://www.tensorflow.org/addons/tutorials/losses_triplet 
[^7]: Li H, Xu Z, Taylor G, Studer C, Goldstein T. Visualizing the loss landscape of neural nets. arXiv preprint arXiv:1712.09913. 2017 Dec 28.
[^8]: Caron, Mathilde, et al. "Deep clustering for unsupervised learning of visual features." Proceedings of the European Conference on Computer Vision (ECCV). 2018. 
[^9]: Boudiaf, Malik, et al. "A unifying mutual information view of metric learning: cross-entropy vs. pairwise losses." European Conference on Computer Vision. Springer, Cham, 2020.
[^10]: Weinberger, Kilian Q., and Lawrence K. Saul. "Distance metric learning for large margin nearest neighbor classification." Journal of machine learning research 10.2 (2009).
