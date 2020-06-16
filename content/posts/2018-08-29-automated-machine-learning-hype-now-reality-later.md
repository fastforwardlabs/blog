---
author: Shioulin
author_link: https://twitter.com/shioulin_sam
date: "2018-08-29T20:00:00Z"
feature: false
post_type: Newsletter
published: true
title: 'Automated Machine Learning: Hype now, reality later?'
aliases:
  - /2018/08/29/automated-machine-learning-hype-now-reality-later.html
---

[Previously in our newsletter](https://blog.fastforwardlabs.com/newsletters/2017-11-08-client.html), we had framed automated machine learning around four notions:
* Citizen Data Science / ML: Automated machine learning will allow everyone to do data science and ML. It requires no special training or skills.
* Efficient Data Science / ML: Automated machine learning will supercharge your data scientists and ML engineers by making them more efficient.
* Learning to Learn: Automated machine learning will automate architecture and optimization algorithm design(architecture search).
* Transfer Learning: Automated machine learning will allow algorithms to learn new tasks faster by utilizing what they learned from mastering other tasks in the past.

Since then, the term *automated machine learning* has been strongly linked to Google's definition of **AutoML as a way for neural nets to design neural nets**, or - expressed technically - as a way to perform neural architecture search. Google's messaging asserts that AutoML will [make AI work for everyone](https://blog.google/technology/ai/making-ai-work-for-everyone/).  [Google Cloud's AutoML](https://cloud.google.com/automl/) beta products now allow one to custom vision, language and translation models with minimum machine learning skills. The product page states that under the hood, this capability is powered by Google's AutoML and transfer learning. But, [as pointed out by fast.ai](http://www.fast.ai/2018/07/23/auto-ml-3/), transfer learning and neural architecture search are two opposite approaches. Transfer learning assumes that neural net architectures generalize to similar problems (for example, features like corners and lines show up in many different images); neural architecture search assumes that each dataset needs a unique and specialized architecture. In transfer learning, you start with a trained model with an existing architecture and further tune the weights with your data; neural architecture search requires training multiple new architectures along with new weights. In practice, one does not need to use both techniques (yet?)! Transfer learning is currently the predominant approach since neural architecture search is **currently** computationally expensive. We very much agree with [fast.ai's assessment](http://www.fast.ai/2018/07/23/auto-ml-3/) that not everyone needs to perform neural architecture search, and the ability to perform such a search does not replace machine learning expertise. In fact, blindly using computation power to search for the best architecture seems to lead us further into the abyss of un-interpretable models.

On the flip side, if we go back in time to the pre-GPU era, one could argue that we are at the same place with neural architecture search as we were back then with deep learning. Sprinkle in the notion of [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35), and suddenly the idea of everyone designing neural nets for their particular needs looks like a reasonable trajectory!
