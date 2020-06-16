---
date: "2018-06-29T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2018-06-19-231235-Compressorhead___Fingers_on_Gibson_Flying_V_Bones_on_Fender_Precision_Bass___Musikmesse_Frankfurt_2013.jpg
published: true
title: 'Deep Learning Vendor Update: Hyperparameter Tuning Systems'
aliases:
  - /2018/06/29/deep-learning-vendor-update-hyperparameter-tuning-systems.html
---

In our [research reports](https://www.cloudera.com/products/fast-forward-labs-research/fast-forward-labs-research-reports.html), we cover "the recently possible," and what makes "the recently possible" possible. In addition to a detailed how-to guide of new machine learning capabilities, each of our reports contains a section on open source projects, commercial offerings, and vendors that help implement this new machine learning capability to realize the opportunities opened up by technological innovation. We like to keep an eye on the the technologies we research, of course. Our report on deep learning (for image classification) was published a few years ago, and we have seen noteworthy new developments.

Training neural networks requires a set of "hyperparameters" that guide the training process, and sometimes aspects of the network itself (such as the number of layers of the network or the number of nodes per layer). Hyperparameter tuning is important because hyperparameters have substantial effects on the quality of the trained model.

![Tuning hyperparameters is important to a neural net's performance](/images/editor_uploads/2018-06-19-231235-Compressorhead___Fingers_on_Gibson_Flying_V_Bones_on_Fender_Precision_Bass___Musikmesse_Frankfurt_2013.jpg)
##### Tuning hyperparameters is important to a neural net's performance (Image Credit: [Torsten Maue](https://commons.wikimedia.org/wiki/File:Compressorhead_-_Fingers_on_Gibson_Flying_V,_Bones_on_Fender_Precision_Bass_-_Musikmesse_Frankfurt_2013.jpg), Wikimedia Creative Commons [(Compressorhead)](https://innotechtoday.com/can-real-iron-man-sing-ironman/))

Hyperparameter tuning has generally been at least as much of an art as a science. Machine learning specialists select preliminary hyperparameters, train the model with those hyperparameters, and evaluate the performance and characteristics of the trained model. Then they adjust the hyperparameters (applying some educated guesses), retrain the model with those hyperparameters, and evaluate again. This process is repeated until the specialist is satisfied with the model.

Several new options promise to automate at least a part of the work of hyperparameter tuning, freeing up the personnel building the model, and possibly finding better hyperparameter settings than a human might. They generally work by automating the hyperparameter selection, model training and evaluation, and hyperparameter adjustment, searching for better model performance. These automated hyperparameter tuning packages include offerings from major cloud services providers (e.g., SageMaker from Amazon and Azure ML Studio from Microsoft) as well as smaller independent vendors (e.g., [Comet.ml](https://www.comet.ml/), [Weights & Biases](https://www.wandb.com/), and [SigOpt](https://sigopt.com/)). Afficionados of open source projects may enjoy [Hyperopt](https://github.com/hyperopt/hyperopt), a python library for "serial and parallel optimization over awkward search spaces." As anyone who has ever embarked on a quest for optimal hyperparameters can tell you, "awkward" is a good description of the process of searching for the optimal hyperparameters of neural networks.

For a thorough overview, Jesus Rodriguez rounds up automated hyperparameter tuners in a recent [Hackernoon article](https://hackernoon.com/hyperparameter-tuning-platforms-are-becoming-a-new-market-in-the-deep-learning-space-7106f0ac1689). Hyperparameter tuning is one of the more easily automated aspects of machine learning (in contrast to, for example, feature engineering). In most practical settings, careful feature engineering requires an understanding of the organization and business, data collection protocols, as well as data science tools and algorithms; it is hard to automate with out-of-the-box solutions. We welcome appropriate automation; automated hyperparameter tuning promises to cut down development time of neural networks and lead to better results.