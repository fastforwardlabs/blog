---
author: Noam
author_link: https://twitter.com/noamsf
date: "2016-05-03T14:51:14Z"
preview_image: http://68.media.tumblr.com/1d842739c4ecb115ce586049dd552f48/tumblr_inline_o6kjvaPgBs1ta78fg_540.jpg
redirect_from:
- /post/143792498983/probabilistic-programming-for-anomaly-detection
tags:
- code
- whitepaper
- probabilistic programming
- anomaly detection
title: Probabilistic Programming for Anomaly Detection
---

<figure data-orig-width="1440" data-orig-height="900" class="tmblr-full"><img src="http://68.media.tumblr.com/1d842739c4ecb115ce586049dd552f48/tumblr_inline_o6kjvaPgBs1ta78fg_540.jpg" alt="image" data-orig-width="1440" data-orig-height="900"/></figure><p>The Fast Forward Labs research team is developing our next prototype, which will demonstrate an application of probabilistic programming. Probabilistic programming languages are a set of high-level languages that lower the barrier to entry for Bayesian data analysis.<b><br/></b></p><p>Bayesian data analysis is often seen as the best approach to machine learning. Models derived by this process are highly interpretable, in contrast to other modern models like neural networks and support vector machines. Transparency like this is crucial in industries - such as healthcare and financial services - that have a legal or ethical duty to ensure safety or fairness.</p><p>On top of that transparency, the results of Bayesian modeling are complete probability distributions, which means their predictions come with meaningful confidence intervals. Confidence is an important part of interpretability, but is also a key ingredient for deciding whether to act on a prediction immediately or incur the cost of obtaining more data (as in active learning).</p><p>Interpretability and confidence have made Bayesian inference very popular in experimental science, where the explicit goal is interpreting a model in the context of data and obtaining more data can be expensive. But Bayesian inference was little used outside academia until recently: as it turns out, the practical engineering challenges of applying it in businesses are enormous. </p><p>Probabilistic programming languages are changing the game. The algorithms used in Bayesian inference are baked into these languages as primitives, and the syntax is optimized to permit precise and concise specification of complex models. Thanks to recent algorithmic advances, users don’t even have set tuning parameters: they simply state the structure of the model, feed in the data, and let the language take care of the rest.</p><p>To illustrate the power of probabilistic programming, we developed <a href="https://github.com/fastforwardlabs/anomaly_detection/blob/master/Anomaly%20Detection%20Post.ipynb">an iPython notebook</a> that shows how it simplifies and improves anomaly detection. In it, we show a traditional approach to anomaly detection, notice where that approach starts to fail, and show how probabilistic programming provides a more rigorous and robust approach.</p><p>- Noam </p>
