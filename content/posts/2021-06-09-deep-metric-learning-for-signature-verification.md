---
title: "Deep Metric Learning for Signature Verification"
date: 2021-06-09T08:48:00 
preview_image: /images/hugo/ff20_blog2_preview_img-1622115845.jpg
post_type: 
published: false
# external_url: 
---

By *[Victor](https://twitter.com/vykthur)* and *[Andrew.](https://www.linkedin.com/in/andrew-r-reed/)*

In our [previous blog post](/2021/05/27/pre-trained-models-as-a-strong-baseline-for-automatic-signature-verification.html), 
, we discussed how pretrained models can serve as strong baselines for the task of signature verification. Essentially, using representations learned by models trained on the ImageNet task allowed us to obtain a 74.3% accuracy when attempting to correctly classify signature pairs as genuine or skilled forgeries. 

However, several intuitions suggest that we might be able to improve on this. First, given that the pretrained model was trained on data (natural images), which does differ from our task of signature images, it makes sense that some sort of fine tuning would be useful in adapting the pretrained model weights to our data distribution.

Second, the pretrained model is based on a classification objective - correctly classify 1 million images into 1000 different classes. While this objective yields semantic representations that have proven to be useful, our primary task of verification does require something more precise. Essentially, we want an objective focused on capturing the similarities/dissimilarities between two data points. To achieve this goal, we can turn to metric learning - learning a distance metric designed to satisfy the objective of making representations for similar objects close and representations for dissimilar objects far apart in some metric space. 



## What is Metric Learning

A simple description of metric learning is any machine learning model structured to learn a distance measure over samples. The intuition here is that if the model is designed to learn a distance function for similar/dissimilar objects, we can use it for applications such as signature verification that rely on this property. 

The metric learning objective can be formulated in several ways depending on how the training dataset is structured. 

![](/images/hugo/metricblog/datapoints.png)
##### Figure 1. Data used to train a metric learning model may be structured as pairs, triplets or quadruplets. This in turn influences how the loss function is designed.  

Commonly, sets of training examples are structured as either pairs or triplets of images from which a distance function is learned. Despite the differences in problem formulation, the high level metric learning workflow remains consistent:

- Define a dataset of train samples (2, 3, 4 data points in each sample, depending on loss function)
- Extract representations for each datapoint in a given sample using a trainable embedding model. The exact architecture of this embedding model might vary depending on the data e.g. a CNN architecture might be used for metric learning on images while an RNN architecture might be useful for sequences.
- Measure the similarity between data points in each sample using a distance function (like Euclidean)
- Calculate a loss based on the observed vs expected distances between data points. E.g. for data points we know to be similar i.e. expected small distance, we have a very little or no loss if their observed distance is indeed low.
- Backpropagate the loss through the embedding network so the model learns to produce similar representations for similar examples and distant representations for dissimilar examples

In the following sections, we will consider a few metric learning techniques.




## Contrastive Loss
Contrastive loss (also known as pairwise ranking loss) is a metric learning objective function that operates with pairs of training data examples - positive pairs (examples that belong to the same class) and negative pairs (examples that belong to different classes). 

The contrastive loss function is set up such that we minimize the distance between embeddings for positive pairs, and maximize the distance between embeddings for negative pairs. After each pass through the network, we ideally want to update the weights of our embedding model such that the above condition is satisfied. Contrastive loss can be implemented using a Siamese network architecture for the embedding model. This model takes in two inputs and uses a shared trunk network that produces two embeddings for each input. 


Note that a Siamese network is not required to implement metric learning with contrastive loss. In theory, you could design a custom training loop where a forward pass through the embedding model is used to get embeddings for each data point in the sample pair, loss is computed and the model weights updated. The Siamese architecture which avoids manually implementing multiple forward passes, simplifies implementation and is widely used.


In our signature verification task, we construct positive pairs consisting of an anchor signature and an alternative, genuine signature from the same author. We then construct negative pairs composed of an anchor signature and a forged signature authored by a different individual. 

Note that the forged signature may be unskilled (i.e the forger knows nothing about the original) or skilled (i.e. the forger has access to what the origin signature looks like and actively attempts to mimic it). Clearly, it is easier to detect unskilled forgeries compared to skilled forgeries ,which are hard to detect even for humans. As we construct training pairs for a model to learn from, we want it to be particularly good at solving the hard version of the problem - distinguishing skilled forgeries.  
In the contrastive loss setting, negative pairs consisting of unskilled forgeries are termed easy negatives, while those consisting of skilled forgeries are termed hard negatives. 





![](/images/hugo/metricblog/contrastive_loss.png)
##### Figure 2. Contrastive loss is used to minimize the distance between genuine signature pairs (top) and maximize distance between negative pairs (bottom)



![](/images/hugo/metricblog/contrastive_train.png)
##### Figure 3. During training, we expect that loss updates will cause the model to update its weights such that positive pairs are closer and negative pairs are farther apart.
 

Contrastive loss is defined as:

where D is the calculated distance between embeddings for each datapoint in the pair, and m is a constant value of margin. In the case of positive pairs, the loss becomes positive only when we have a positive distance between vector representations. In the case of negative pairs, the loss is positive only when the distance between vectors is less than the margin. The margin value is a hyperparameter that serves as an upper threshold to constrain the amount of loss attributed to “easy to classify” pairs. A simple way to think about the function of the margin is that if the network produces representations that are distant “enough” for a given pair, there is no need to continue focusing training efforts on that example [^1]. 

While contrastive loss is useful, it has a limitation. For points in a negative pair, contrastive loss will push them far apart without any knowledge of the broader embedding space. For example, imagine we have 10 classes; each time we see class 1 and 2, we want to push them far apart; a result of this is that 1 might now become farther from 2 on the average but might overlap with other classes such as class 3, 4, 5 etc. 

Triplet loss addresses this issue by using triplets in each training sample - an anchor, a positive (same class) and a negative (different class) data point. This way, with each gradient update we learn to minimize anchor + positive distance whilst also ensuring that the anchor is also far from the negative point.


## Triplet Loss 


![](/images/hugo/metricblog/triplet_train.png)
##### Figure 4. A triplet model is trained with triplets such that the distance between the anchor and positive is minimized while the distance between the anchor and negative is maximized.

![](/images/hugo/metricblog/triplet_train.png)
##### Figure 5 - A triplet network architecture where triplet loss is used to learn a mapping such that anchor/positive representations are closer than anchor/negative representations.

The triplet loss function aims to learn a distance between representations such that the anchor-to-positive distance is less than the anchor-to-negative distance. Similar to contrastive loss, a margin value is imposed on the anchor-to-negative distance so that once negative representations have enough distance between them no further effort is taken to increase distance between them. With this understanding, triplet loss is formally defined as:

where DP is the anchor-to-positive distance and DN is the anchor-to-negative distance. With this loss formulation, we can create three different types of triplet combinations based on how we sample:
- Easy triplets: result when DN > DP + m. Here, the sampled anchor-to-negative distance is already large enough so loss is 0 and the network has nothing to learn from.
- Hard triplets: result when DN < DP. In this case, the anchor-to-negative distance is less than the anchor-to-positive distance, meaning high loss to backpropagation through the network.
- Semi-hard triplets: result when DP < DN < DP + m. Semi-hard triplets occur when the negative example is more distant to the anchor than the positive example, but the distance is not greater than the margin, therefore resulting in a positive loss. [1]

Based on the above, we can see that different approaches for selecting triplets (also called triplet mining approaches) are not equally informative. More importantly, if we prescriptively mine the right types of triplets that are informative, we can increase the overall efficiency of learning. Ideally, we want to focus on hard and semi-hard triplets - a luxury we were not afforded in the contrastive, pairwise learning setup. 

### From Offline to Online Triplet Mining

![](/images/hugo/metricblog/onlinetraining.png)
##### Figure 6. In online triplet mining, triplets are constructed during training. We get embeddings 

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



![](/images/hugo/metricblog/quadruplet_train.png)
##### Figure 7: Quadruplet loss 

At this point, it is clear that a good loss function should attempt to learn similarity using information from each training sample. Contrastive loss learns from pairs of images (positive, negative).  Triplet loss achieves even better performance by simultaneously learning  from carefully selected image triplets (anchor, positive, negative) within a batch. But what if we could simultaneously learn from even more samples within a batch? It turns out that existing research has explored this. 

In their work, Chen et 2017 [2][3] introduce the quadruplet loss, where each training sample consists of 4 data points (anchor, positive, negative1, negative2) where negative2 is dissimilar to all other data points.  They minimize the distance between anchor and positive while simultaneously maximizing distance between anchor and negative1 as well as negative1 and negative2.

Elezi et al [5] take this even one step further and propose the group loss which aims to simultaneously learn from all samples within a minibatch as opposed to a pair, triplet or quadruplet. To create the mini-batch, they sample from a fixed number of classes, with samples coming from a class forming a group. Thus, each mini-batch consists of several randomly chosen groups, and each group has a fixed number of samples. An iterative, fully-differentiable label propagation algorithm is then used to build feature embeddings which are similar for samples belonging to the same group, and dissimilar otherwise. The overall effect of this group loss formulation is to enforce embedding similarity across all samples of a group while promoting, at the same time, low-density regions amongst data points belonging to different groups.

One trend we can observe from these loss functions is that the more data points from multiple classes we use to update our gradients, the better our model is able to capture the global structure of the embedding space. In theory, quadruplet loss and group loss represent the state of the art in metric learning loss functions, but they introduce multiple parameters that can be challenging to implement and tune. Even when this is done correctly, the expected increase in performance (~1 - 4%) may be hard to reproduce, especially due to the stochastic nature of DNN training. In practice (as we will see in the experiment section), triplet loss (with online learning) is efficient, high performing and hence the recommended approach.



 

## Our Experimentation

### Dataset 

To evaluate a metric learning approach on our signature verification task, we experimented with contrastive and triplet loss. We first constructed an experimental setup consistent with the design from our pre-trained baseline experiment. Using the CEDAR dataset, we withheld signatures for 11 of the 55 authors as a test set and used the other 44 as a training set.   


![](/images/hugo/metricblog/cedardataset.png)
##### Figure 8. The CEDAR dataset used for our signature verification experiments.

Note that depending on the loss function, the strategy for constructing the eventual training dataset which the network learns from might differ. In our contrastive loss experiments, we generated a total of 36,432 pairs (xx positive pairs, xx hard negative pairs).  For our triplet loss experiments, given that we use the online triplet mining approach, we structure the dataset as a classification problem; each signer and each forgery is treated as a class, making for a total of 88 classes with 24 samples (2112 total)  each in the training set. Amongst other limitations, the CEDAR dataset is small; as we see later on, this makes it challenging to train a performant neural network from scratch.

To evaluate each model, we construct a set of pairs of positives and negatives (see Figure X for examples of skilled and unskilled forgeries in our test set) and report maximum accuracy and equal error rate. Except where mentioned, the performance scores we report are based on a test set of positives and skilled forgeries (hard negatives). Additional discussion on evaluation metrics is provided in our previous post.

![](/images/hugo/metricblog/hardnegatives.jpg)
##### Figure 9. Examples of skilled forgeries where the forger has access to the genuine signature and attempts to replicate it. We refer to such pairs as hard negatives. All performance scores reported are based on a test set containing this type of negatives.

![](/images/hugo/metricblog/easynegatives.jpg)
##### Figure 10. Examples of unskilled forgeries where the forger does not have access to the genuine signature and may provide a random signature instead. We refer to such pairs as easy negatives.


### Contrastive Loss Training and Evaluation
For contrastive loss, a siamese network was assembled using an embedding model composed of a frozen ResNet50 backbone with a series of 3 trainable layers appended to the network head (1 GlobalAveragePooling 2D layer and 2 Dense layers with 128 activations each). This approach allowed us to fine tune the already effective pre-trained ResNet50 feature extractor on our signature verification dataset using contrastive loss.

Through several training iterations, we found that introducing intermediate dropout and L2 regularization to our custom network head allowed us to achieve 78.2% max accuracy on the test set - an improvement of 11 percentage points over the pretrained ResNet50 baseline (67%)!

While these results are promising, there are several considerations to take into account when using contrastive loss. First, contrastive loss requires us to construct and train on an exhaustive list of genuine/forged examples. For our dataset, this means training on 36,432 sample pairs each epoch despite the fact that many of those pairs may not actually contribute any loss (and therefore learning) to the network because they are “easy” positives or negatives.

Figure 11. A 3D plot of embeddings produced by the trained siamese network for three authors signatures. Genuine vs. forged examples are appropriately placed into separable regions as seen by groupings of circles vs. diamonds.

Second, contrastive loss is limited in its ability to learn global, contextual feature representations. Figure 11 above depicts embeddings generated from the trained siamese network for genuine and forged signature examples from three authors. We observe that the network has correctly separated genuine vs. forged examples into separate regions which is precisely what contrastive loss aims to accomplish. However, the model has not captured the relative similarity of signatures from the same author (which can hurt generalization to new signature datasets). Ideally, we desire a model that produces embeddings that are separable across authors and discriminative between genuine/forged classes. For example, we would like to see that all signatures from Author 3 appear in the same general region, and within that region, signatures maintain separation between genuine and forged. Because contrastive loss is formulated by looking only at pairs of images, it cannot preserve a contextual understanding of author classes and simply just learns discriminative features between genuine and forged. This shortcoming is solved by triplet loss (as we will see), and therefore the remainder of our exploration focused on this superior loss function.


#####  Figure XYZ. A 3D plot of embeddings produced by the trained siamese network for three authors signatures. Genuine vs. forged examples are appropriately placed into separable regions as seen by groupings of circles vs. diamonds.

Second, contrastive loss is limited in its ability to learn global, contextual feature representations. Figure XYZ above depicts embeddings generated from the trained siamese network for genuine and forged signature examples from three authors. We observe that the network has correctly separated genuine vs. forged examples into separate regions which is precisely what contrastive loss aims to accomplish. However, the model has not captured the relative similarity of signatures from the same author (which can hurt generalization to new signature datasets). Ideally, we desire a model that produces embeddings that are separable across authors and discriminative between genuine/forged classes. For example, we would like to see that all signatures from Author 3 appear in the same general region, and within that region, signatures maintain separation between genuine and forged. Because contrastive loss is formulated by looking only at pairs of images, it cannot preserve a contextual understanding of author classes and simply just learns discriminative features between genuine and forged. This shortcoming is solved by triplet loss (as we will see), and therefore the remainder of our exploration focused on this superior loss function.

### Triplet Loss Training and Evaluation
We constructed several model architectures (see Table 1 below) and trained them using the Triplet Semi Hard loss implemented in the Tensorflow addons library [5].  Each model has a similar set of final layers (two conv2D layers followed by a Dense layer and an L2 Normalization layer with size 256). We found that adding an L2 Normalization layer after our output embeddings (as suggested in [2]) was useful in constraining the embeddings to a hypersphere conducive for cosine similarity. Each model was trained with the Adam optimizer (lr=0.001), with a learning rate decay of 0.7 ever 10 steps, and trained for 25 epochs.  

Figure 12. Maximum accuracy vs model size for multiple model architectures, evaluated on the signature verification task. 
 



#### Effect of Model Choices
Training multiple models allowed us to explore the impact of design choices which a datasciencist must navigate when applying metric learning in practice.  

**Impact of a Metric Loss Formulation** 
We see that fine tuning a pretrained model using the triplet loss leads to a 81.8% maximum accuracy for our best model. This is a significant improvement from a pretrained ResNet50 baseline performance of 74.3%.

**Impact of Pretrained Features** 
In our previous experiments, we saw that a pretrained model could be a strong baseline without any finetuning. To evaluate how much of the performance increase we see in our metric learning experiments is attributable to the use of pre trained features (vs the triplet loss function), we trained a vanilla baseline CNN,  as well as models constructed from intermediate layers of a pretrained ResNet and VGG16 model.
- Base CNN - 68%, 1.68 million parameters 
- Base UNet - 71.5%, 1.29 million parameters
- Small ResNet50 Skip initialized at skip connection layer conv4_block6_add - 81.8%, 9.2 million parameters. (Best performance) 
- Smaller ResNet50 Skip initialized at skip connection layer conv3_block4_add - 76.1%, 2.18 million parameters. 
- Full ResNet50  - Full ResNet50 fine tuned on the triplet metric learning objective -  76.4%  24.79 million.

Overall, we find that the following useful insights
Fine tuning with pre-trained features (e.g Smaller ResNet50 vs Baseline CNN and Baseline UNet) yields better results compared to training a model from scratch. 
A UNet like architecture for models of comparable size yields better performance for our task (Base UNet vs Base CNN).


**Impact of Skip Connections**
Skip connections in CNNs have been shown to improve the loss surface [7] for deep networks making them easier to train and yielding performance.
We find that fine tuning a full ResNet50 model (which has skip connections) achieves better performance (76.4%) compared to fine tuning a VGG16 model (67.4%) 

**Intermediate model vs Full Model** 
When applying transfer learning, the data scientist must decide how much of the pretrained model is useful to their task - i.e what features to include, what features to freeze and what features to finetune. 
- We found that we got the best performance when we constructed an intermediate model from ResNet50 (Small ResNet50 skip, 35MB) and fine tuned it vs fine tuning the entire ResNet50. 
- Furthermore we found that when we constructed this intermediate model using the output of a skip connection vs a conv2D layer, the results were better. Our intuition is that the later layers  in a pretrained ResNet50 model contain high level features (e.g eyes, wheels, doors) that are not relevant to our task and dataset (which are mostly lines and texture in a signature) and can introduce noise. More importantly, an intermediate model is faster to train, significantly smaller, and hence easier to deploy (e.g. as a microservice with limits on file sizes). Note that Smaller ResNet50 is competitive (76.1% on hard negatives, 95% on easy negatives) but only 8.5mb in file size.

Notes on training with triplet loss:
- Ensure a large enough batch size is selected when training with the online triplet loss (on the minimum, batch size should be greater than the number of classes). This ensures each batch contains enough samples such that a valid semi hard triplet can be sampled. A NaN loss value during training might indicate that your current  batch size is too small.
- Ensure the distance metric used in the loss function is the same distance metric that will be used during evaluation/test time. E.g. If cosine distance is used in the loss function during training, it should also be used when comparing the similarity of two signatures at test time. For example, a model trained with an L2 distance function will show reduced accuracy when evaluated with cosine distance. 
- Modifying the margin parameter can be used to improve the performance of each model. .e.g. If loss does not decrease during training, it might indicate that it is challenging to find good triplets (e.g. negatives are too hard and yield similar embeddings) ; in this case decreasing the margin parameter can be useful.


## Debugging a Metric Learning Model - Does it Do What We Think it Does?

So far, we have built several models with competitive results. However, it is important to verify that the model is in fact achieving its goals (similar signatures close together, dissimilar signatures far apart) and that it is doing this for the right reasons. 

To this end, we explored several sanity check approaches to help us build trust and confidence in the model’s behaviour. Sanity checks help us confirm expected behaviours and question any unexpected or unusual observations.

### Dimensionality Reduction + Visualization 
First, we have used dimensionality reduction techniques (UMAP) to visualize embeddings for each signature in our test set. We expect that signatures from the same author are clustered together; we also expect that skilled forgeries are close to originals but separated from the cluster of the associated genuine signature.

Figure 13. Visualization of UMAP embeddings (2 dimensions) for signatures in our test set. In general, we see that embeddings for forgeries are in the same region as their corresponding genuine signatures but still separated.

### Visualization of distance metrics
In this sanity check, we construct image pairs (positive and negative) pairs and compute the distance between embeddings produced by our model, for each pair. We expect that the density of distances between positive pairs is close to zero (with some variation to account for user error), but more spread out toward 1 for negative pairs.  


Figure 14 Density plot of the cosine distances between embeddings (produced by multiple models) for positive and hard negative pairs in our test set.  

Figure 15 Density plot of the cosine distances between embeddings (produced by multiple models) for positive and easy negative pairs in our test set.  

### Gradient Visualization of Class Activation Maps
We can also utilize gradient based approaches [10] to inspect “what aspects of the input are most influential/relevant to the output”. These approaches have been used in debugging classification models to identify what pixels in the input image drive a specific class prediction. For example we want to see that pixels around the head and ears of a husky dog are the relevant regions as opposed to a snow background when predicting the husky class.  A well known approach in this area is GradCam [11] which visualizes the gradient of the class score (logit) with respect to the feature map of the last convolutional unit of a DNN model. 
We can adapt it to our use case by visualizing the gradient of the entire output embedding with respect to the feature map of a preselected convolutional layer in our metric learning model. What this visualization gives us is some intuition on the region within the input signature that our layer finds influential while producing embeddings. Ideally, we want to see a concentration around the actual lines and strokes of the signature and possible focus on parts of written letters that might have high variance (e.g. attention to how users might round their g’s in a unique way).

Note, that methods like GradCam are not exactly principled, but subject to interpretation based on domain knowledge.

 

Figure 16: GradCam visualization for the last 4 convolutional layers for signatures from our test set.

## Limitations

In this work, we show that fine tuning a pretrained model on a metric learning loss (contrastive and triplet loss) can improve performance. However there are a few limitations with our experiment set up that are worth noting:


- **Dataset Limitations**: While our training setup is designed such that we evaluate the models on signatures from individuals not represented in the training set, we recognize that the CEDAR dataset is small and does not cover properties of signatures (e.g. different writing styles, languages etc) that may occur in real world documents but are not covered in the CEDAR dataset. Training and evaluation on additional datasets is strongly recommended prior to production use. 

- **Data Augmentation**: We used the CEDAR dataset as is, without exploring augmentations or transformations. For example, it may be useful to experiment with scale or rotation transforms to ensure the model is invariant to these changes.


- **Reproducibility**: Deep Neural networks can have multiple sources of randomness that can make it challenging to reproduce the exact results we report. These may include hardware properties, weight initialization, etc. In our experiments, we attempt to minimize this by fixing the seeds for numpy and tensorflow; we still observe slight variations across each run (~3 percentage points), however, the relative order of results stays consistent.  


- **Model Tuning**: In our experiments, while we explored the impact of metric loss finetuning,  pretrained features, skip connections over a small set of presets, there are still many parameters that can be tuned. These include margin parameter, learning rate, model architecture (e.g. use of models designed to learn multiscale features) etc.  


- **Other Loss Function**s: While we have focused on contrastive and triplet loss, there are other valid and perhaps less complicated ways of fine tuning a pretrained model that yields good distance metrics. For example, we can explore a cross entropy loss that learns to predict a class (genuine, skilled forgery, unskilled forgery) given a pair of images.  The reader is encouraged to review this paper for further insight on how cross entropy loss compares with other metric learning losses [9]. 


Naturally, these limitations are opportunities for future work and experiments.


## Summary and Conclusion

Metric learning helps us train a model that yields representations of similarity adapted to our task and dataset.  In this post we have covered several loss functions for metric learning (contrastive loss, triplet loss, quadruplet loss and group loss). We also report on a set of experiments training a model for signature verification on the CEDAR dataset. We learned that:

- Pre-trained models can be strong baselines for the signature verification. When the problem is easy (i.e unskilled forgery), we see that a pretrained VGG16 model yields 89.5% accuracy and 74.3% when the problem is hard (skilled forgeries).
- Triplet loss achieves better performance compared to contrastive loss and learns a better overall structure of the embedding space. 
- Triplet loss (with online triplet mining) is more efficient to train compared to contrastive loss i.e. training time to reach maximum accuracy. It does not require the manual construction of training triplets (as required in contrastive loss) and uses intelligent sampling to select informative triplets. This is very useful when running experiments to explore a large hyperparameter space. As an example, we found that fine tuning a ResNet50 model with triplet loss was completed in 3 minutes while a contrastive loss model needed 8 hours to reach max accuracy.
With respect to implementation, we found the Tensorflow addons implementation of triplet loss [6] to be useful.  
- While triplet loss is great, its application is limited to scenarios where labels exist. To implement intelligent construction of triplets (especially semi hard negatives), we need labels for each class.  On the other hand, we can still apply contrastive loss to unlabelled datasets by leveraging pseudo labels  - e.g. Existing research [8] shows that k-means assignments can be used as pseudo-labels to learn visual representations.
- Fine tuning an intermediate model can not only result in a reduced model size but also improved accuracy. Our experiments suggest that for the task of signature verification, fine tuning a subset of the ResNet50 model resulted in a smaller model size compared to fine tuning the entire ResNet50 model. 
- A good practice is to use the same distance metric across training and test. L2 distance is more computationally efficient compared to cosine distance, making it the better choice in production. L2 similarity measures are also well supported by libraries designed for fast approximate nearest neighbor search e..g Annoy, FAISS, ScaNN.  Also note that computing L2 distance on  normalized embeddings (recall our L2 normalization layer earlier), yields the equivalent of cosine distance. 




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
