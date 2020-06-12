---
author: Nisha
author_link: https://twitter.com/NishaMuktewar
date: "2019-06-26T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2019-06-12-143410-BigGANs.png
published: true
title: Seeing is not necessarily believing
---

Advancements in machine learning have evolved to such an extent that machines can not only understand the input data but have also learned to create it. Generative models are one of the most promising approaches towards this goal. To train such a model we first collect a large amount of data (be it images, text, etc.) and then train a model to generate data like it.

Generative Adversarial Networks (GANs) are one such class of generative models, that, given a training dataset, learn to 
generate new data with the same statistics as the training set. For instance, a GAN trained on images of dogs can help 
generate new images of dogs that at times may look authentic and have many realistic characteristics. GANs have progressed 
substantially in the last couple of years and have been applauded for their ability to generate high fidelity and diverse 
images. As such, applications of adversarial training have found their way into image translation, style transfer, and more - 
particularly data augmentation. 

So far these models have had limited success in such tasks for large-scale datasets like ImageNet, and that’s mainly because 
the models don’t generate sufficiently high quality samples. A recent model - [BigGAN](https://arxiv.org/abs/1809.11096), 
however, has generated photorealistic images of ImageNet data and has achieved considerable performance improvement when evaluating using traditional metrics like [Inception Score (IS)](https://arxiv.org/abs/1606.03498) and [Fréchet Inception Distance (FID)](https://arxiv.org/abs/1706.08500) compared to the previous 
state-of-the-art. What this means is that BigGANs are capable of capturing data distributions. And if this were true, one 
could then possibly use these generated samples for many downstream tasks, especially in situations where limited labeled data 
is available.

![](/images/editor_uploads/2019-06-12-143410-BigGANs.png)
##### Image source: [Large scale GAN training for high fidelity natural image synthesis - Brock et al., 2018](https://arxiv.org/pdf/1809.11096.pdf)

A recent [work](https://openreview.net/forum?id=rJMw747l_4) tested whether BigGANs can be really useful for data augmentation, or - more drastically - for data replacement of the original data distribution. The hypothesis the authors wanted to test was that if BigGANs were indeed capturing the data distribution, one could use the generated samples instead of (or in addition to) the original training set, to improve performance on classification. The authors conducted two simple experiments. First, they trained ImageNet classifiers, replacing the original training set with one produced by BigGAN. Second, they augmented the original ImageNet training set with samples from BigGAN. 

Replacing the original training data with BigGAN samples saw a substantial increase (120% and 384%) in the Top-1 and Top-5 classification errors when compared to the model performance on the original training set. Further, augmenting the training set improved the model performance only marginally, while at the expense of more training time. This suggests that **naively augmenting the dataset with BigGAN samples is of limited utility** and more work is required for BigGANs to be actually used in downstream tasks. It also further highlights the need to reflect on **better metrics that could be used to evaluate image synthesis models like GANs**. The current gold standard metrics - Inception Score (IS) and Fréchet Inception Distance (FID) for GAN model comparison could be misleading and are not predictive of data augmentation classification performance.