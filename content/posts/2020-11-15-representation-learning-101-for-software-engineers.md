---
title: "Representation Learning 101 for Software Engineers"
date: 2020-11-15T21:09:50
author: Victor Dibia
author_link: https://twitter.com/vykthur
preview_image: /images/hugo/representation_densenet.jpg
post_type: post
published: false
# external_url:
---

Deep Neural Networks (DNNs) have become a particularly useful tool in building intelligent systems that simplify cognitive _tasks_ for users. Examples include neural search systems that identify the most relevant results given a natural language or image query, and recommendation systems that provide personalized recommendations based on the user's profile.

For many of these systems, their performance is gated on the ability to create representations of data with semantic meaning - numbers that truly encode the meaning of each data point with respect to the _task_. For example, to enable customers find relevant clothes in our dataset that are similar to images of a picture they have (see Pinterest use case ), we need good measures of _relevance_ that compare the user's picture and all items in the database. To recommend relevant products to users based on their profile, we also need high quality measures of _relevance_ e.g. a measure of similarity between a user and all products.

DNN models are the tool of choice because they excel at building complex, distributed and semantically meaningful representations. However, across many real-world use cases, these models need to be carefully designed to fit the both the task and data - a field known as _representation learning_. This area of study is related to (and overlaps with) adjacent fields such as manifold learning (learn about the manifold hypothesis here [[5]](https://arxiv.org/abs/1310.0425)) and deep metric learning (see list of recent papers [here](https://github.com/kdhht2334/Survey_of_Deep_Metric_Learning).).

In this article, we will focus on discussing aspects of representation learning:

- What is representation learning and why?
- What are practical methods for representation learning?
- Example implementation using supervised representation learning for the task of semantic image search.

---

## Deep Representation Learning: What and Why!

<div style="border-bottom: 1px dashed grey; background-color:#E5E5E5; padding: 10px; margin-bottom:10px"> 
Generally speaking, a good representation is one that makes a subsequent learning task easier. The choice of representation will usually depend on the choice of the subsequent learning task.
<a target="_blank" href="https://www.deeplearningbook.org/contents/representation.html">[1](Bengio, Yoshua, Ian Goodfellow, and Aaron Courville. Deep learning, 2017)</a>.</div>

Based on the above, we can define deep representation learning as _training DDN models that yield numerical representations of data, suitable for solving a set of tasks_.

To build intuition on why representation learning is valuable, we can review the question of _how humans solve cognitive tasks_? In many cases, we rely on heuristics - a set of fairly simple rules relevant to the task. For example, to identify if an image is a cat, we might perform the following checks - does it have 4 legs, two pointy ears, fur, whiskers etc. Based on the answers to these questions, we might determine with some level of confidence that it indeed, is a cat.

<!-- For machines, this task is particularly complicated as there is usually no clear linear relationship between real world data (e.g. pixels within an image) and  -->

Similarly, a neural network that succeeds at this same task should allocate its capacity (layers) such that it successfully translates (or disentangles) raw input data (e.g. image pixels) into a set of representations (e.g. eyes, ears, legs, whiskers etc) that are useful for the task. Keep in mind that layers within a DNNs are stacked units of computation comprised of weights, and bias terms whose values are learned during training. Thus, an interesting realization here is that if we formulate our training objectively carefully, a DNN can yield representations that are then useful for a family of related tasks. Depending on the availability of labeled data, compute capacity and distribution of data, there are several strategies that are useful for learning representations.

<!-- Again, to build intuition on how DNNs achieve this goal of disentangling important aspects of data, let use briefly review the architecture of a DNN. DNNs for classification tasks typically consist of layers - stacked units of computation - which feed into a final linear classifier (e.g. a softmax classifier) to discriminate across task categories. To excel at these tasks, a network trained with some supervised learning objective results in a situatuion where the majority of the network's capacity (layers before the final linear classifier) is devoted to computing representations that improve the classifier. -->

## Methods for Representation Learning

### Supervised Learning

When we train a DNN on a supervised learning task (e.g. classification), the training objective naturally yields representations that are useful for solving the task. In practice, this approach takes two main forms:

- Generic Classification
  The approach assumes the availability of large labeled datasets. The most commmon example of this is the use of models pretrained on the imagenet dataset. Extensive experiments have shown that the representations learned by these pretrained models (layers before the final softmax classifier layer) yield representations that are suitable for many other image processing tasks.

![](/images/hugo/representation_densenet.png)

##### Figure 1:(a) Layer 2 in a pretrained DenseNet121 model shows neurons in this layer mostly respond to colors and simple textures. (b) Layer 202 contains neurons that respond to more complex, level concepts such as tree patterns and an eye. To visually explore more representations learned by pretrained models, see [here](https://victordibia.github.io/neuraldreams/#/).

- Metric Learning

<div style="border-bottom: 1px dashed grey; background-color:#E5E5E5; padding: 10px; margin-bottom:10px"> 
"Metric learning approaches aim to learn a good embedding space
such that the similarity between samples are preserved as distance between embedding vectors of the samples" <a target="_blank" href="https://arxiv.org/pdf/1811.12649.pdf">[9] (Zhai et al 2108 "Classification is a strong baseline for deep metric learning)</a>.
</div>

. The metric learning losses, such as contrastive loss [8](http://www.cs.utoronto.ca/~hinton/csc2535_06/readings/chopra-05.pdf) and triplet loss [[7]](https://link.springer.com/chapter/10.1007/978-3-319-24261-3_7), are formulated to minimize intra-class distances and maximize inter-class distances". For this we need special datasets of positive and negative example pairs.

Classification losses are widely adopted in
face verification applications [13, 22, 23] and achieve state-of-the-art performance.

Research shows it is valuable to use an L2 normalized softmax loss (as opposed to softmax) as this more explicitly optimize the features to have higher similarity score for positive pairs and lower similarity score for negative pairs [[4]](https://arxiv.org/pdf/1703.09507.pdf).

Some researches have also explored ensembling (training and combining results from multiple learnings) [[3]](https://arxiv.org/pdf/1801.04815.pdf) for even better perfromance but with drawbacks in system complexity and additional hyperparameters that need to be optimized.

The main drawback is that training a model from scratch requires a large amount of labelled data which is
[TODO .. notes from bengio talk, book]

### Self Supervised Learning (Pretext Tasks)

In this paradigm, the goal is to still train a supervised learning model, but find creative ways of automatically generating meaningful labels. Historically, this is done by designing pretext tasks - that's that if solved, yield semantically meaningful representations as a side effect. We can observe this across multiple areas:

- Next sentence prediction
  - Data: corpus of text in a given language
  - Objective: given a pair of sentences, does one follow the other?
- Image -

It is important to note that a good pretext task should be one which requires some bit of semantic understanding (or knowledge of important patterns) to solve.

If we construct pretext tasks that are inherently meaningful, then we can provide some signal (impose constraints) for the network to build notions of meaning. E.g learning to predict rotation, fill in missing sections of an image, remove noise.

Advances in these area is particularly exciting. Recent research shows that if we design the pretext task we, we can learn representations that achieve results close to supervised learning! For example, [SwAV[2]](https://arxiv.org/pdf/2006.09882.pdf) is only 1.2% below the performance of a fully supervised model.

### Unsupervised Learning

In some situations, it may be challenging to design good pretext tasks. For these situations, fully unsupervisedd methods are useful. For example an autoencoder used to reconstruct data, denoising autoencoder, VAE, GAN. While there is not pretext task, the training objective still requiress some level of semantic meaning. E.g. The intuition here

- Strictly unsupervised learning is uncertain. Intuition suggests that a generative model or an autencoder that generates cars etc typically need some level of knowledge to perform the task.

Requires a bit of data, might require the use of pretrained models to bootstrap the precess [6](https://arxiv.org/pdf/2009.04091.pdf). Some recent work include

![](/images/hugo/replearning.jpg)

---

While unsupervised methods in theory presents a litany of benefits - learning from limited labelled data, comparable performance to supervised methods, there are still challenges. You should use it when

- You have a good supervised baseline
- You have a tonne of unlabelled data (most poeople dont have it except you are a huge firm)
- You have sufficient expertise to design a careful evaluation framework to benchmark quality improvements.

## Evaluating Representation Learning

How do we know if we have good representations? It turns out that this is hard to mathematically quantify and historically has been evaluated based on task performance. For example, representations learning from unsupervised or self supervisedd methosd are evaluated by using them as input for a linear logistic regression classifier.

<!-- Yoshua bengio - it is really hard to implement .. so we default tos -->

<!-- ## Semantic Image Search with Supervised Pretrained Models -->

<!-- ## Case Studies

Pinterest - PinText
https://medium.com/pinterest-engineering/pintext-a-multitask-text-embedding-system-in-pinterest-b80ece364555

They use user interaction as a signal in learning relevant embeddings.
Custom embedding on their data
Standard embedddings dont work well.

https://medium.com/pinterest-engineering/hybrid-search-building-a-textual-and-visual-discovery-experience-at-pinterest-8527ba9728a9 -->

## References

[1] Bengio, Yoshua, Ian Goodfellow, and Aaron Courville. Deep learning. Vol. 1. Massachusetts, USA, MIT press, 2017. https://www.deeplearningbook.org/contents/representation.html

[2] Caron, Mathilde, et al. "Unsupervised learning of visual features by contrasting cluster assignments." Advances in Neural Information Processing Systems 33 (2020).

[3] Opitz, Michael, et al. "Deep metric learning with bier: Boosting independent embeddings robustly." IEEE transactions on pattern analysis and machine intelligence (2018).

[4] Ranjan, Rajeev, Carlos D. Castillo, and Rama Chellappa. "L2-constrained softmax loss for discriminative face verification." arXiv preprint arXiv:1703.09507 (2017).

[5] Fefferman, Charles, Sanjoy Mitter, and Hariharan Narayanan. "Testing the manifold hypothesis." Journal of the American Mathematical Society 29.4 (2016): 983-1049.

[6] Nguyen, Binh X., et al. "Deep Metric Learning Meets Deep Clustering: An Novel Unsupervised Approach for Feature Embedding." arXiv preprint arXiv:2009.04091 (2020).

[7] Hoffer, Elad, and Nir Ailon. "Deep metric learning using triplet network." International Workshop on Similarity-Based Pattern Recognition. Springer, Cham, 2015.

[8] Chopra, Sumit, Raia Hadsell, and Yann LeCun. "Learning a similarity metric discriminatively, with application to face verification." 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR'05). Vol. 1. IEEE, 2005.

[9] Zhai, Andrew, and Hao-Yu Wu. "Classification is a strong baseline for deep metric learning." arXiv preprint arXiv:1811.12649 (2018).

<!--
Semantic search is useful across many business application domains and data types.
Semantic search relies on the existence of a representation of eaech data item which encodes semantic meaning.

For example, the following problems can be cast as a semnatic search problem: identifying fraudulent signatures, recommending the right fashion content,

While this remains an interesting area, constructing the right representation remains a difficult challenge.

In general, deep neural networks are good candidates for use as feature extractors. If we recall that deep models are composed of "layers" of stacked computation units with weights and biases which are learned during training to support some objective; we can assume that if these weights are correctly selected to support this obejctive and this objective requires semantic inforation, we can assume these features become good at this sort of task. Furthermore, deep models are heirarchiccal (cite bertology where attention show behaviour of bert layers, and simonyan paper on visualizing convnets), where early layers learn low level functions and later laters laern more complex functions; thus we can make informed decisions on what layeers within the netowrk to use as feature extractors.

At this point, it is abundantly clear that the training paradigm and training objective are critical components in achieving a model for semantic feature extraction. In the next section, we catagorize the methods for building such a model into 3 main paradigms and provide an overview with examples. -->

<!--
Resources

http://www.offconvex.org/2019/03/19/CURL/
https://dl.acm.org/doi/10.1145/3331184.3331320'
https://arxiv.org/abs/1711.02209
https://app.wandb.ai/authors/swav-tf/reports/Unsupervised-Visual-Representation-Learning-with-SwAV--VmlldzoyMjg3Mzg

https://wandb.ai/authors/image-retrieval/reports/Towards-Representation-Learning-for-an-Image-Retrieval-Task--VmlldzoxOTY4MDI

https://github.com/ariG23498/G-SimCLR

https://github.com/google-research/simclr
https://www.inovex.de/blog/transfer-learning-siamese-networks/

https://arxiv.org/abs/2010.00578

https://arxiv.org/abs/2006.09882 Unsupervised Learning of Visual Features by Contrasting Cluster Assignments

Recommending What Video to Watch Next: A Multitask
Ranking System
https://www.youtube.com/watch?v=sr1KscMfBOY&ab_channel=ACMRecSys
https://daiwk.github.io/assets/youtube-multitask.pdf

Approximate nearest neighbor search in high dimensions – Piotr Indyk – ICM2018
https://www.youtube.com/watch?v=cn15P8vgB1A&feature=youtu.be&ab_channel=RioICM2018

Review of Metric Learning - https://arxiv.org/pdf/2003.08505.pdf -->
