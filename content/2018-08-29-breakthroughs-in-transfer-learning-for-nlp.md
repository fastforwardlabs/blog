---
author: Seth
author_link: https://twitter.com/shendrickson16
date: "2018-08-29T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/2018/07/task_dict_v-1532535013679.jpg
published: true
title: Breakthroughs in transfer learning for natural language processing
---

One of the most exciting parts of our jobs at Cloudera Fast Forward Labs is [our work](https://www.cloudera.com/products/fast-forward-labs-research/fast-forward-labs-research-reports.html) on applied machine learning research. Through this research we see and work with some of the most exciting developments in machine learning, deep learning, and AI, but - as with any field that has been overhyped - we sift through a lot of noise. By noise, we generally mean research that is too immature to be of practical use, or research that follows one or more of the [troubling trends in machine learning](https://arxiv.org/pdf/1807.03341.pdf). 

The research we get really excited about hits a sweet spot of delivering new capabilities that are of practical use to general data science teams. That’s why we’re particularly excited about developments in transfer learning, a technique that allows anyone from ML beginner to expert to deploy state-of-the-art models on challenging tasks like computer vision and NLP. Specifically, there have been several recent results which indicate that transfer learning will have huge impacts in NLP, similar to what we’ve observed in computer vision.

### Transfer learning makes deep learning accessible to everyone

Transfer learning exploits the idea that many machine learning tasks are related to each other, and so the skills required to do well on one task are often transferable to other tasks. This is similar to how humans who learn to throw a baseball do not need to completely re-learn the mechanics of throwing to also throw a football, or how skills developed in learning to speak one foreign language would also be useful in learning another foreign language. Consider some of the common tasks that we might be interested in doing in the field of computer vision:

![](/images/2018/07/task_dict_v-1532535013679.jpg)

##### Various computer vision tasks. Image credit: [Taskonomy](https://github.com/StanfordVL/taskonomy/tree/master/taskbank).

* Object detection - is there a tv in this image? A bed? A couch?
* Scene detection - what type of room is this?
* Semantic segmentation - locate objects in the image
* Depth estimation - estimate the depth of objects in a 2D image

Intuitively, we know that these tasks require similar capabilities. Being able to pick out which pixels belong to the same object, as in semantic segmentation, is undoubtedly useful in depth estimation, since pixels belonging to one object should have the same or similar depths. Training a single model to do well on any of these tasks from scratch is difficult and requires extensive expertise; however, once such a model exists, we can take that model and transfer the knowledge it contains to our related task, without having to go through the complex and [brittle process](http://www.fast.ai/2018/07/12/auto-ml-1/) of training a model from scratch. 

This gives way to a general strategy: for some family of related tasks, e.g. computer vision tasks, train a model from scratch on a generic task that has plentiful data. That trained model can be applied to related tasks with minimal changes, since it already has much of the general knowledge required for this family of tasks. In computer vision, this generic task has traditionally been training an object detection model on the Imagenet dataset, which is a highly curated dataset of over 14 million images. Classification models trained on Imagenet [tend to learn general features](https://arxiv.org/abs/1311.2901) like how to detect shapes, edges, and higher level objects that are almost always helpful in related computer vision tasks. Training these models from scratch is difficult, requiring both advanced hardware and expertise, but the important thing is that anyone can take the result and use it to do very cool things - for free!

Transfer learning is not a new idea, but it has grown in popularity and importance because of the deep learning boom. Deep learning and transfer learning are a good match for several reasons:
* Transfer learning needs tasks that share the same types of inputs, which is more common when working with raw/unstructured data (text, audio, images)
* Transfer learning eliminates need to train deep models from scratch, which is difficult, time consuming, and notoriously hard to reproduce
* Deep learning is generally extremely data hungry, but transfer learning enables application of deep learning models to small data

### Discovering NLP's Imagenet

Transfer learning helps solve some of the biggest and most prohibitive problems with deep learning, but it has, until recently, mostly been limited to the domain of computer vision. Fortunately, we’re starting to see some breakthroughs in transfer learning in the field of natural language processing. One of the keys to transfer learning is to identify a generic task, with plenty of quality data, that allows us to train from-scratch models that will then transfer well to related tasks. In computer vision this is the Imagenet task, but in NLP there wasn’t an obvious solution, until now. Several recent papers (including [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) and [Improving Language Understanding
by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)) have shown that language modeling - predicting the next word in a sequence of text - is well-suited as this generic task. They show that next-word prediction forces a model to learn long-term dependencies, hierarchical relations, and sentiment, which are all useful for other NLP tasks. They go on to present results where a pre-trained model is transferred to other tasks, and can beat well established benchmarks in natural language inference, question and answering, sentiment classification, and others. This led one NLP researcher to declare that [“NLP’s Imagenet moment has arrived.”](https://thegradient.pub/nlp-imagenet/)

Transfer learning has been extremely important in lowering the barrier to entry for deep learning in computer vision and there is no reason to think it won’t do the same for NLP. This is exciting, in particular because raw text is often the largest source of available data for many businesses. Nearly every organization can make use of better algorithmic tools for understanding natural language, and we seem to be on the cusp of a revolution in NLP!