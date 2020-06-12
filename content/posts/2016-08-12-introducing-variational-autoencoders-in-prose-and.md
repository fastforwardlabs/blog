---
author: Miriam
author_link: https://twitter.com/meereve
date: "2016-08-12T17:09:50Z"
feature: true
post_type: whitepaper
preview_image: http://fastforwardlabs.github.io/blog-images/miriam/160727_1340_explore.gray_del11_492x490.slower40.gif
redirect_from:
- /post/148842796218/introducing-variational-autoencoders-in-prose-and
tags:
- code
- deep learning
- probabilistic programming
title: Introducing Variational Autoencoders (in Prose and Code)
---

<p>Effective machine learning means building expressive models that sift out signal from noise—that simplify the complexity of real-world data, yet accurately intuit and capture its subtle underlying patterns.</p>
<p>Whatever the downstream application, a primary challenge often boils down to this: How do we represent, or even synthesize, complex data in the context of a tractable model?</p>
<p>This challenge is compounded when working in a limited data setting—especially when samples are in the form of richly-structured, high-dimensional observations like natural images, audio waveforms, or gene expression data.</p>
<p><strong>Cue the Variational Autoencoder</strong>, a fascinating development in unsupervised machine learning that marries probabilistic Bayesian inference with deep learning.</p>
<p>Benefiting from advances in both research communities, the Variational Autoencoder addresses these challenges by leveraging innovative deep learning techniques grounded in a solid Bayesian theoretical framework&hellip;and can be explained through mesmerizing GIFs:</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/160727_1340_explore.gray_del11_492x490.slower40.gif" title="Shameless GIF for your attention" style="max-width:60.0% !important"/></div>
<p>(Read on, and all will become clear&hellip;)</p>
<h2 id="intro">Intro</h2>
<p>Traditional <a href="http://www.deeplearningbook.org/contents/autoencoders.html"><em>autoencoders</em></a> are models (usually multilayer <a href="http://karpathy.github.io/neuralnets/">artificial neural networks</a>) designed to output a reconstruction of their input. Specifically, autoencoders sequentially deconstruct input data into hidden representations, then use these representations to sequentially reconstruct outputs that resemble the originals. Fittingly, this process of teasing out a mapping from input to hidden representation is called <a href="http://www.deeplearningbook.org/contents/representation.html"><em>representation learning</em></a>.</p>
<p>The appeal of this setup is that the model learns its own definition of a &ldquo;meaningful&rdquo; representation based only on the data—no human-derived heuristics or labels! This approach stands in contrast to the majority of deep learning systems in production today, which rely on expensive-to-obtain labeled data (&ldquo;This image is a kitten; this image is a panda.&rdquo;). Alternatives to such <em>supervised learning</em> frameworks provide a way to benefit from a world brimming with valuable raw data.</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/miriams-figure.png" title="A basic autoencoder" style="max-width:80.0% !important"/></div>
<p>Though trained holistically, autoencoders are often built for the part instead of the whole: researchers might exploit the data-to-representation mapping for <a href="https://arxiv.org/abs/1511.01432">semantic embeddings</a>, or the representation-to-output mapping for extraordinarily complex <a href="https://github.com/Newmu/dcgan_code">generative modeling</a></p>
<p>But an autoencoder with unlimited capacity is doomed to the role of a wonky, computationally-expensive Xerox machine. To ensure that the transformations to or from the hidden representation are useful, we impose some type of <a href="http://www.deeplearningbook.org/contents/regularization.html"><em>regularization</em></a> or constraint. As a tradeoff for some loss in fidelity, such impositions push the model to distill the most salient features from a cacophonous real-world dataset.</p>
<p><a href="https://arxiv.org/abs/1312.6114">Variational</a> <a href="https://arxiv.org/abs/1401.4082">Autoencoders</a> (VAEs) incorporate regularization by explicitly learning the joint distribution over data and a set of latent variables that is most compatible with observed datapoints and some designated prior distribution over latent space. The prior informs the model by shaping the corresponding posterior, conditioned on a given observation, into a regularized distribution over latent space (the coordinate system spanned by the hidden representation).</p>
<p>As a result, VAEs are an excellent tool for <a href="http://scikit-learn.org/stable/modules/manifold.html"><em>manifold learning</em></a>—recovering the &ldquo;true&rdquo; manifold in lower-dimensional space along which the observed data lives with high probability mass—and <a href="https://openai.com/blog/generative-models/"><em>generative modeling</em></a> of complex datasets like images, text, and audio—conjuring up brand new examples, consistent with the observed training set, that do not exist in nature.</p>
<p>Building on other <a href="http://blog.keras.io/building-autoencoders-in-keras.html">informative</a> <a href="https://jmetzen.github.io/2015-11-27/vae.html">posts</a>, this is the first installment of a guide to Variational Autoencoders: the lovechild of Bayesian inference and unsupervised deep learning.</p>
<p>In this post, we&rsquo;ll sketch out the model and provide an intuitive context for the math- and code-flavored follow-up. In Post II, we&rsquo;ll walk through a technical implementation of a VAE (in <a href="http://tensorflow.org/">TensorFlow</a> and Python 3). In Post III, we&rsquo;ll venture beyond the popular <a href="http://yann.lecun.com/exdb/mnist/">MNIST</a> dataset using a twist on the vanilla VAE.</p>
<h2 id="the-variational-autoencoder-setup">The Variational Autoencoder Setup</h2>
<p>An end-to-end autoencoder (input to reconstructed input) can be split into two complementary networks: an <em>encoder</em> and a <em>decoder</em>. The encoder maps input <span class="math inline">\(x\)</span> to a latent representation, or so-called <em>hidden code</em>, <span class="math inline">\(z\)</span>. The decoder maps the hidden code to a reconstructed input value <span class="math inline">\(\tilde x\)</span>.</p>
<p>Whereas a vanilla autoencoder is deterministic, a Variational Autoencoder is stochastic—a mashup of:</p>
<ul><li>a probabilistic encoder <span class="math inline">\(q_\phi(z|x)\)</span>, approximating the true (but intractable) posterior distribution <span class="math inline">\(p(z|x)\)</span>, and</li>
<li>a generative decoder <span class="math inline">\(p_\theta(x|z)\)</span>, which notably does not rely on any particular input <span class="math inline">\(x\)</span>.</li>
</ul><p>Both the encoder and decoder are artificial neural networks (i.e. hierarchical, highly nonlinear functions) with tunable parameters <span class="math inline">\(\phi\)</span> and <span class="math inline">\(\theta\)</span>, respectively.</p>
<p>Learning these conditional distributions is facilitated by enforcing a plausible mathematically-convenient prior over the latent variables, generally a standard <a href="https://www.statlect.com/probability-distributions/multivariate-normal-distribution">spherical Gaussian</a>: <span class="math inline">\(z \sim \mathcal{N}(0, I)\)</span>.</p>
<p>Given this conjugate prior, the encoder&rsquo;s job is to supply the mean and variance of the Gaussian posterior over each latent space dimension corresponding to a given input. Latent <span class="math inline">\(z\)</span> is sampled from this distribution, then passed to the decoder to be transformed back into a distribution over the original data space.</p>
<p>In other words, a VAE represents a <a href="http://blog.forty.to/2013/08/24/graphical-models-theory/">directed probabilistic graphical model</a>, in which approximate inference is performed by the encoder and optimized alongside an easy-to-sample generative decoder. For this reason, these complementary halves are also known as the <em>inference</em> (or <em>recognition</em>) <em>network</em> and the <em>generative network</em>. By reformulating this graphical model as a differentiable neural net with a single, pithy cost function (derived from the variational lower bound), the whole package can be trained by <a href="http://neuralnetworksanddeeplearning.com/chap1.html">stochastic gradient descent</a> (SGD) thanks to the <a href="http://karpathy.github.io/2016/05/31/rl/">&ldquo;amusing&rdquo; universe</a> we live in.</p>
<h2 id="bayes-meet-neural-networks">Bayes, Meet Neural Networks</h2>
<p>In fact, many developments in deep learning research can also be understood through a probabilistic, or <a href="http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Chapter1.ipynb">Bayesian</a>, lens. Some of these analogies are more theoretical, whereas others share a parallel mathematical interpretation. For example, <a href="https://arxiv.org/abs/1505.05424"><span class="math inline">\(\ell_2\)</span>-regularization</a> can be viewed as imposing a Gaussian prior over neural network weights, and <a href="http://arkitus.com/files/nips-15-weber-reinforced-inference.pdf">reinforcement learning</a> can be formalized through variational inference.</p>
<p>VAEs exemplify a case where this relationship is made explicit and elegant, and variational Bayesian inference is the guiding principle shaping the model&rsquo;s cost function and instrinsic architecture.</p>
<p>Why does this setup make sense?</p>
<p>In the Bayesian worldview, datapoints are observations drawn from some data-generating distribution: (observed) variable <span class="math inline">\(x \sim p(x)\)</span>. So, the <a href="http://yann.lecun.com/exdb/mnist/">MNIST</a> dataset of handwritten digits describes a random variable with an intricate set of dependencies among all 28*28 pixels. Each MNIST image offers a glimpse into one arrangement of 784 pixel values with high probability—whereas a 28*28 block of white noise, or the <a href="https://en.wikipedia.org/wiki/Jolly_Roger">Jolly Roger</a>, (theoretically) occupy low probability mass under the distribution.</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/mnist_%5B6%5D.png" title="MNIST digit" style="max-width:40.0% !important"/></div>
<p>It would be a headache to model the conditional dependencies <!-- among all 784 pixels. --> in 784-dimensional pixel space. Instead, we make the simplifying assumption that the distribution over these observed variables is the consequence of a distribution over some set of hidden variables: <span class="math inline">\(z \sim p(z)\)</span>. Intuitively, this paradigm is analogous to how scientists study the natural world, by working backwards from observed phenomena to recover the unifying hidden laws that govern them. In the case of MNIST, these latent variables could represent concepts like number identity and tiltedness, whereas more complex natural images like the <a href="http://www.cs.nyu.edu/~roweis/data/frey_rawface.jpg">Frey faces</a> could have latent dimensions for facial expression and azimuth.</p>
<p><em>Inference</em> is the process of disentangling these rich real-world dependencies into simplified latent dependencies, by predicting <span class="math inline">\(p(z|x) -\)</span> the distribution over one set of variables (the latent variables) conditioned on another variable (the observed data). (This is where <a href="https://xkcd.com/1236/">Bayes&rsquo; theorem</a> enters the picture.)</p>
<p>With this Bayesian frame-of-mind, training a generative model is the same as learning the joint distribution over the data and latent variables: <span class="math inline">\(p(x, z)\)</span>. This approach lends itself well to small datasets, since inference relies on the data-generating distribution rather than individual datapoints <em>per se</em>. It also lets us bake prior knowledge into the model by imposing simplifying <em>a priori</em> distributions over variables.</p>
<p>Classical (iterative, non-learned) approaches to inference are often inefficient and do not scale well to large datasets. With a few theoretical and mathematical tricks, we can train a neural network to do the dirty work of both variational inference <em>and</em> generative modeling&hellip;while reaping the additional benefits deep learning provides (universal approximating power, cheap test-time evaluation, minibatched SGD, advances like batch normalization and dropout, etc).</p>
<p>The next post in the series will delve into these theoretical and mathematical tricks and show how to implement them in <a href="https://www.tensorflow.org/">TensorFlow</a> (a toolbox for efficient numerical computation with data flow graphs).</p>
<h2 id="mnist">MNIST</h2>
<p>For now, we will take our VAE model for a spin using handwritten MNIST digits.</p>

```python
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import vae # this is our model - to be explored in the next post


IMG_DIM = 28
ARCHITECTURE = [IMG_DIM**2, # 784 pixels
                500, 500, # intermediate encoding
                50] # latent space dims
# (and symmetrically back out again)
HYPERPARAMS = {
    "batch_size": 128,
    "learning_rate": 1E-3,
    "dropout": 0.9,
    "lambda_l2_reg": 1E-5,
    "nonlinearity": tf.nn.elu,
    "squashing": tf.nn.sigmoid
}

mnist = input_data.read_data_sets("mnist_data")
v = vae.VAE(ARCHITECTURE, HYPERPARAMS)
v.train(mnist, max_iter=20000)
```

<p>Let&rsquo;s verify the model by eye, by plotting how well it parses random MNIST inputs (top) and reconstructs them (bottom):</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/160801_1234_reloaded_batch_784_500_500_50_round_20000_test.png" title="Inputs and reconstructions"/></div>
<p>Note that these inputs are from the test set, so the model has never seen them before. Not bad!</p>
<p>For latent space visualizations, we can train a VAE with 2-D latent variables (though this space is generally too small for the intrinsic dimensionality of real-world data). Picturing this compressed latent space lets us see how the model has disentangled complex raw data into abstract higher-order features.</p>
<p>We&rsquo;ll visualize the latent manifold over the course of training in two ways, to see the complementary evolution of the encoder and decoder over (logarithmic) time.</p>
<p>This is how the encoder/inference network learns to map the training set from the input data space to the latent space&hellip;</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/160805_1646_train_16.0.col256_qual100_del11_nodith.gif" title="Latent space encoding"/></div>
<p>&hellip;and <em>this</em> is how the decoder/generative network learns to map latent coordinates into reconstructions of the original data space:</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/160805_1646_explore_16.0.gray_del11_492x490.slower47.gif" title="Latent space decoding" style="max-width:90.0% !important"/></div>
<p>Here we are sampling evenly-spaced percentiles along the latent manifold and plotting their corresponding output from the decoder, with the same axis labels as above.</p>
<p>Looking at both plots side-by-side clarifies how optimizing the encoder and decoder in tandem enables efficient pairing of inference and generation:</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/tableau.1493x693.png" title="Latent space (encoder + decoder perspective)" style="max-width:95.0% !important"/></div>
<p>This tableau highlights the overall smoothness of the latent manifold—and how any &ldquo;unrealistic&rdquo; outputs from the generative decoder correspond to apparent discontinuities in the variational posterior of the encoder (e.g. between the &ldquo;7-space&rdquo; and the &ldquo;1-space&rdquo;). These gaps could probably be improved by experimenting with model hyperparameters.</p>
<p>Whereas the original data dotted a sparse landscape in 784 dimensions, where &ldquo;realistic&rdquo; images were few and far between, this 2-dimensional latent manifold is densely populated with such samples. Beyond its inherent visual coolness, latent space smoothness shows the model&rsquo;s ability to leverage its &ldquo;understanding&rdquo; of the underlying data-generating process to generalize beyond the training set.</p>
<p>Smooth interpolation within and between digits—in contrast to the spotty latent space characteristic of many autoencoders—is a direct result of the variational regularization intrinsic to VAEs.</p>
<h2 id="take-aways">Take-aways</h2>
<p>Bayesian methods provide a framework for reasoning about uncertainty. Deep learning provides an efficient way to approximate arbitrarily complex functions, and ripe opportunities to probe uncertainty (over parameters, hyperparameters, data, model architectures&hellip;).</p>
<p>While differences in language can obscure overlapping ideas, recent research has revealed not just the power of cross-validating theories across fields (interesting in itself), but also a productive new methodology through a unified synthesis of the two.</p>
<p>This research becomes ever more relevant as we seek to leverage today&rsquo;s most interesting real-world data, which is often high-dimensional and rich in structure, yet limited in number and wholly or partially unlabeled.</p>
<p>(<a href="http://edwardlib.org/">But</a> <a href="http://blog.shakirm.com/2015/11/talk-memory-based-bayesian-reasoning-and-deep-learning/">don&rsquo;t</a> <a href="http://videolectures.net/course_information_theory_pattern_recognition/">take</a> <a href="http://dustintran.com/blog/a-quick-update-edward-and-some-motivations/">my</a> <a href="http://twiecki.github.io/blog/2016/06/01/bayesian-deep-learning/">word</a> <a href="http://link.springer.com/book/10.1007/978-1-4612-0745-0">for</a> <a href="https://arxiv.org/abs/1604.01662">it</a><a href="https://blog.dominodatalab.com/an-introduction-to-model-based-machine-learning/">.</a>)</p>
<p>Variational Autoencoders are:</p>
<ul><li>A reminder that productive sparks fly when deep learning and Bayesian methods are not treated as alternatives, but combined.</li>
<li>Just the beginning of creative applications for deep learning.</li>
</ul><p>Stay tuned for more technical details (math and code!) in Part II.</p>
<p>- Miriam</p>
