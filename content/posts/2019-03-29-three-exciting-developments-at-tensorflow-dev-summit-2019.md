---
author: Chris
author_link: https://twitter.com/_cjwallace
date: "2019-03-29T00:00:00Z"
feature: false
post_type: newsletter
preview_image: '![](/images/editor_uploads/2019-05-09-205154-tensorflow.png)'
published: true
title: Three exciting developments at TensorFlow Dev Summit 2019
aliases:
  - /2019/03/29/three-exciting-developments-at-tensorflow-dev-summit-2019.html
---

The third annual TensorFlow Dev Summit was held. The entire first day of talks was live-streamed, and videos are available on the [TensorFlow YouTube channel](https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ). I stayed up late (from the UK) watching a few of the talks, and here’s an entirely idiosyncratic description of three things I find exciting. A broader [recap](https://medium.com/tensorflow/recap-of-the-2019-tensorflow-dev-summit-1b5ede42da8d) is provided by the TensorFlow team themselves.

### TensorFlow Federated

[TensorFlow Federated](https://www.tensorflow.org/federated/) is a library for federated learning. Given the title of our [last report](http://vision.cloudera.com/an-introduction-to-federated-learning/), you already know we think this is an exciting area. It was a group of Google researchers who coined the term “federated learning” with the release of the [Federated Averaging](https://arxiv.org/abs/1602.05629) algorithm for learning from decentralized data, so it makes sense that Federated Learning is getting the TensorFlow treatment.

The library includes both the high-level “Federated Learning” API designed for wrapping existing TensorFlow models, and a low-level “Federated Core” API, which is intended to the development of new federated learning algorithms.  The project is nascent, but particular attention has been paid to separating the various concerns of building a federated learning system. For instance, without some thought, it would easy to start entangling model operations and network communication. By providing high level abstractions, TensorFlow Federated allows experts in each area to contribute their respective knowledge, which could substantially lower the bar to entry for participating in federated learning research. The ability to wrap an existing Keras model is particularly appealing.

TensorFlow Federated currently includes only a simulated runtime (where all federated nodes actually live on the same, local, device), so it does not out-of-the-box “solve” federated learning. Eventually, other runtimes will be supported with the same API, meaning that the gap between researching novel federated approaches and deploying them to real federated networks is minimised.

### TensorFlow Probability

Likewise to federated learning, [probabilistic programming](https://blog.fastforwardlabs.com/2017/01/18/new-research-on-probabilistic-programming.html) is also something we’ve written about at Fast Forward Labs. Since our probabilistic programming report was released, the ecosystem has evolved. PyMC and Stan both continue to develop, but perhaps the most notable change has been the emergence of so-called “deep probabilistic programming” libraries. These libraries combine the ability of deep neural networks to learn complex functions with the probabilistic paradigm of computing with distributions. [Pyro.ai](http://pyro.ai/) runs atop PyTorch, and until recently, [Edward](http://edwardlib.org/) was the go-to library for TensorFlow.

[TF Probability](https://www.tensorflow.org/probability) takes a broader approach to probabilistic programming than Edward, introducing layers of abstraction into the “probprog” stack. At its base, it has complete interoperability with TensorFlow, which means all of TF’s linear algebra operations are available. On top of this is a set of “statistical building blocks” (their language): probability distributions and bijectors (composable transformations of random variables). There are also model building tools, including probabilistic programming language Edward2 - unsurprisingly, the successor to Edward - and a “probabilistic layers” component that can be used with high level APIs like Keras. Finally, there are a suite of probabilistic inference methods including Monte Carlo and Variational Inference.

The library has been evolving rapidly over the last year, but seems to be converging to a useful suite of tools. The TF Dev Summit [demo](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Probabilistic_Layers_Regression.ipynb) of TensorFlow Probability included a simple and compelling walk through of building a regression model then including aleatoric (observation noise) and epistemic (model) uncertainty. It is encouraging to see probabilistic programming continue to mature and gain traction with existing software ecosystems.

### Swift for TensorFlow

Anyone at CFFL will tell you this particular newsletter author has a bit of a soft spot for probabilistic programming. Despite developments in TF Probability, of all the developments announced at the TF Dev Summit, I find the progress in [Swift for TensorFlow](https://www.tensorflow.org/swift) (which has moved into beta) the most promising.

Swift is an open source language from Apple, first designed to provide a better development experience for iOS and OSX (but now also supporting Linux, less a few niceties like automatic test discovery). Chris Lattner, who implemented much of the Swift language while at Apple, is now working on bringing TensorFlow to Swift. However, this is not a simple wrapper around the existing TensorFlow codebase, but rather a re-imagining of what tools for machine learning can be. Swift for TensorFlow integrates automatic differentiation into the Swift language itself, allowing easy definition of performant custom operations. Swift is fast, expressive and has an advanced type system. At CFFL, we love Python, and the Swift for TensorFlow team have also provided an almost native experience for interoperability with Python.

The watch words are “differentiable computing,” and we eagerly await more demo applications in this ecosystem. One advantage to Swift, being designed as a replacement for C family languages is that it is not necessary to wrap C libraries for performant numerical code. This means one can move up and down the numerical computing stack in the same language, which is also great for pedagogy. Speaking of pedagogy, Jeremy Howard of Fast.ai has [noticed](https://www.fast.ai/2019/03/06/fastai-swift/) Swift too, and at the TF Dev Summit, it was announced that the next iteration of the Fast.ai course will include a Swift component from Chris Lattner himself.