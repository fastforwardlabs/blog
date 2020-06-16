---
date: "2017-09-29T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/2017/09/Screen_Shot_2017_09_13_at_9-1505322932035.59
published: true
title: The Danger and Promise of Adversarial Samples
aliases:
  - /2017/09/29/the-danger-and-promise-of-adversarial-samples.html
---

Adversarial samples are inputs designed to fool a model: they are inputs created by applying perturbations to example inputs in the dataset such that the perturbed inputs result in the model outputting an *incorrect* answer with *high* confidence. Often, perturbations are so small that they are imperceptible to the human eye — they are inconspicuous.

Adversarial samples are a concern in a world where algorithms make decisions that affect lives: imagine an imperceptibly altered stop sign that the otherwise high-accuracy image recongnition algorithm of a self-driving car misclassifies as [a toilet](https://arxiv.org/abs/1707.03501). Curiously and concerningly, the same adversarial example is often misclassified by a variety of classifiers with different architectures trained on different subsets of data. Attackers can use their own model to generate adversarial samples to fool models they did not build.

![](/images/2017/09/Screen_Shot_2017_09_13_at_9-1505322932035.59)

##### Accessorize to a crime ([paper](http://dl.acm.org/citation.cfm?doid=2976749.2978392)), a pair of (physical) eyeglasses to fool facial recognition systems. Impersonators carrying out the attack are shown in the top row and corresponding impersonation targets in the bottom row (including Milla Jovovich). 

But adversarial samples are useful, too. They inform us about the inner workings of models by giving us an inuition for what aspects of model input matter for model output (cf. [influence functions](http://proceedings.mlr.press/v70/koh17a.html)). In case of adversarial examples, aspects of model input matter for model output that should *not* matter. Adversarial samples can help expose weaknesses of models. Combined with fast and efficient methods for generation of adversarial examples, such as the [Fast Sign](https://arxiv.org/abs/1412.6572), [Iterative](https://arxiv.org/abs/1607.02533), and [L-BFGS method](https://arxiv.org/abs/1312.6199), adversarial samples can help train neural networks to be [less vulnerable to adversarial attack](https://arxiv.org/abs/1412.6572). 

![](/images/2017/09/Screen_Shot_2017_09_13_at_10-1505322973486.02)

##### The model is fooled by the (distractor) sentence (in blue) ([paper](https://arxiv.org/abs/1707.07328)). 

Adversarial samples will inform the direction of research within the community. Adversarial samples are a consequence of [models being too linear](https://arxiv.org/abs/1412.6572). Linear models are easier to optimize but they lack the capacity to resist adversarial perturbation. Ease of optimization has come at the cost of models that are easily misled. This motivates the development of optimization procedures that are able to train models whose behavior is more locally stable ... and less vulnerable to attack.

![](/images/2017/09/Screen_Shot_2017_09_13_at_10-1505323059576.04)

##### Self-driving cars analyze images from varying distances and viewpoints. A recent [paper](https://arxiv.org/abs/1707.03501) shows that current methods for generation of adversarial samples generate samples that only fool models at certain distances and from certain viewing angels. Or maybe not ... that claim is [already being challenged](https://blog.openai.com/robust-adversarial-inputs/).