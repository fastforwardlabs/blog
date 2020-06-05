---
author: Miriam
author_link: https://twitter.com/meereve
date: "2016-08-22T18:02:08Z"
feature: true
post_type: Whitepaper
preview_image: http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160816_1754_reloaded_latent_784_500_500_50_round_65536_morph_4730816952.gif
redirect_from:
- /post/149329060653/under-the-hood-of-the-variational-autoencoder-in
tags:
- code
- deep learning
- probabilistic programming
title: Under the Hood of the Variational Autoencoder (in Prose and Code)
---

##### The <a href="https://arxiv.org/abs/1312.6114">Variational</a> <a href="https://arxiv.org/abs/1401.4082">Autoencoder</a> (VAE) neatly synthesizes unsupervised deep learning and variational Bayesian methods into one sleek package. In <a href="http://blog.fastforwardlabs.com/2016/08/12/introducing-variational-autoencoders-in-prose-and.html">Part I</a> of this series, we introduced the theory and intuition behind the VAE, an exciting development in machine learning for combined generative modeling and inference—<a href="http://shakirm.com/slides/DLSummerSchool_Aug2016_compress.pdf">“machines that imagine and reason.”</a>

<p>To recap: VAEs put a probabilistic spin on the basic autoencoder paradigm—treating their inputs, hidden representations, and reconstructed outputs as probabilistic random variables within a directed graphical model. With this <a href="https://xkcd.com/1236/">Bayesian</a> perspective, the encoder becomes a variational <em>inference network</em>, mapping observed inputs to (approximate) posterior distributions over latent space, and the decoder becomes a <em>generative network</em>, capable of mapping arbitrary latent coordinates back to distributions over the original data space.</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/vae.4.png" title="A variational autoencoder" style="width:80.0%"/></div>
<p>The beauty of this setup is that we can take a principled Bayesian approach toward building systems with a rich internal “mental model” of the observed world, all by training a single, cleverly-designed deep neural network.</p>
<p>These benefits derive from an enriched understanding of data as merely the tip of the iceberg—the observed result of an underlying causative probabilistic process.</p>
<p>The power of the resulting model is captured by Feynman’s famous <a href="http://archives-dc.library.caltech.edu/islandora/object/ct1:483">chalkboard quote</a>: “What I cannot create, I do not understand.” When trained on MNIST handwritten digits, our VAE model can parse the information spread thinly over the high-dimensional observed world of pixels, and condense the most meaningful features into a structured distribution over reduced latent dimensions.</p>
<p>Having recovered the latent manifold and assigned it a coordinate system, it becomes trivial to walk from one point to another along the manifold, creatively generating realistic digits all the while:</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160816_1754_reloaded_latent_784_500_500_50_round_65536_morph_4730816952.gif" title="Generatively morphing digits"/></div>
<p>In this post, we’ll take a look under the hood at the math and technical details that allow us to optimize the VAE model we sketched in <a href="http://fastforwardlabs.github.io/2016/08/12/introducing-variational-autoencoders-in-prose-and.html">Part I</a>.</p>
<p>Along the way, we’ll show how to implement a VAE in <a href="http://tensorflow.org/">TensorFlow</a>—a library for efficient numerical computation using data flow graphs, with key features like <a href="http://alexey.radul.name/ideas/2013/introduction-to-automatic-differentiation/">automatic differentiation</a> and parallelizability (across clusters, CPUs, GPUs…and <a href="https://cloudplatform.googleblog.com/2016/05/Google-supercharges-machine-learning-tasks-with-custom-chip.html">TPUs</a> if you’re lucky). You can find (and tinker with!) the full implementation <a href="https://github.com/fastforwardlabs/vae-tf/tree/master">here</a>, along with a couple <a href="https://github.com/fastforwardlabs/vae-tf/tree/master/out">pre-trained models</a>.</p>
<!--more-->
<h2 id="building-the-model">Building the Model</h2>
<p>Let’s dive into code (Python 3.4), starting with the necessary imports:</p>
```python
import functools

from functional import compose, partial
import numpy as np
import tensorflow as tf
```

<p>One perk of these models is their modularity—VAEs are naturally amenable to swapping in whatever encoder/decoder architecture is most fitting for the task at hand: <a href="https://arxiv.org/abs/1502.04623">recurrent</a> <a href="https://arxiv.org/abs/1511.06349">neural</a> <a href="https://arxiv.org/abs/1412.6581">networks</a>, <a href="https://arxiv.org/abs/1411.5928">convolutional</a> and <a href="https://arxiv.org/abs/1503.03167">deconvolutional</a> networks, etc.</p>
<p>For our purposes, we will model the relatively simple <a href="http://yann.lecun.com/exdb/mnist/">MNIST</a> dataset using densely-connected layers, wired symmetrically around the hidden code.</p>

```python
class Dense():
    """Fully-connected layer"""
    def __init__(self, scope="dense_layer", size=None, dropout=1.,
                 nonlinearity=tf.identity):
        # (str, int, (float | tf.Tensor), tf.op)
        assert size, "Must specify layer size (num nodes)"
        self.scope = scope
        self.size = size
        self.dropout = dropout # keep_prob
        self.nonlinearity = nonlinearity

    def __call__(self, x):
        """Dense layer currying, to apply layer to any input tensor `x`"""
        # tf.Tensor -&gt; tf.Tensor
        with tf.name_scope(self.scope):
            while True:
                try: # reuse weights if already initialized
                    return self.nonlinearity(tf.matmul(x, self.w) + self.b)
                except(AttributeError):
                    self.w, self.b = self.wbVars(x.get_shape()[1].value, self.size)
                    self.w = tf.nn.dropout(self.w, self.dropout)
    ...
```

<p>We can initialize a <code>Dense</code> layer with our choice of <code>nonlinearity</code> for the layer nodes (i.e. neural network units that apply a nonlinear activation function to a linear combination of their inputs, as per line <code>18</code>).</p>
<p>We’ll use <a href="https://arxiv.org/abs/1511.07289">ELUs</a> (Exponential Linear Units), a <a href="http://www.picalike.com/blog/2015/11/28/relu-was-yesterday-tomorrow-comes-elu/">recent advance</a> in building nodes that learn quickly by avoiding the problem of vanishing gradients. We wrap up the class with a <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/layers.py#L26-L38">helper function</a> (<code>Dense.wbVars</code>) for compatible random initialization of weights and biases, to further accelerate learning.</p>
<p>In TensorFlow, neural networks are defined as numerical computation graphs. We will build the graph using partial function composition of sequential layers, which is amenable to an arbitrary number of hidden layers.</p>
```python
def composeAll(*args):
    """Util for multiple function composition

    i.e. composed = composeAll([f, g, h])
         composed(x) # == f(g(h(x)))
    """
    # adapted from https://docs.python.org/3.1/howto/functional.html
    return partial(functools.reduce, compose)(*args)
```

<p>Now that we’ve defined our model primitives, we can tackle the VAE itself.</p>
<p>Keep in mind: the TensorFlow computational graph is cleanly divorced from the numerical computations themselves. In other words, a <code>tf.Graph</code> wireframes the underlying skeleton of the model, upon which we may hang values only within the context of a <code>tf.Session</code>.</p>
<p>Below, we initialize class <code>VAE</code> and activate a session for future convenience (so we can initialize and evaluate tensors within a single session, e.g. to persist weights and biases across rounds of training).</p>
<p>Here are some relevant snippets, cobbled together from the <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/vae.py">full source code</a>:</p>

```python
class VAE():
    """Variational Autoencoder

    see: Kingma &amp; Welling - Auto-Encoding Variational Bayes
    (https://arxiv.org/abs/1312.6114)
    """
    DEFAULTS = {
        "batch_size": 128,
        "learning_rate": 1E-3,
        "dropout": 1., # keep_prob
        "lambda_l2_reg": 0.,
        "nonlinearity": tf.nn.elu,
        "squashing": tf.nn.sigmoid
    }
    RESTORE_KEY = "to_restore"

    def __init__(self, architecture, d_hyperparams={}, meta_graph=None,
                 save_graph_def=True, log_dir="./log"):
        """(Re)build a symmetric VAE model with given:

         * architecture (list of nodes per encoder layer); e.g.
           [1000, 500, 250, 10] specifies a VAE with 1000-D inputs, 10-D latents,
           &amp; end-to-end architecture [1000, 500, 250, 10, 250, 500, 1000]

         * hyperparameters (optional dictionary of updates to `DEFAULTS`)
        """
        self.architecture = architecture
        self.__dict__.update(VAE.DEFAULTS, **d_hyperparams)
        self.sesh = tf.Session()

        if not meta_graph: # new model
            handles = self._buildGraph()
            ...
            self.sesh.run(tf.initialize_all_variables())
```

<p>Assuming that we are building a model from scratch (rather than restoring a <a href="https://www.tensorflow.org/versions/r0.9/how_tos/meta_graph/index.html">saved</a> <code>meta_graph</code>), the key initialization step is the call to <code>VAE._buildGraph</code> (line <code>32</code>). This internal method constructs nodes representing the placeholders and operations through which the data will flow—<em>before</em> any data is actually piped in.</p>
<p>Finally, we unpack the iterable <code>handles</code> (populated by <code>_buildGraph</code>) into convenient class attributes—pointers not to numerical values, but rather to nodes in the graph:</p>
```python
        ...
        # unpack handles for tensor ops to feed or fetch
        (self.x_in, self.dropout_, self.z_mean, self.z_log_sigma,
         self.x_reconstructed, self.z_, self.x_reconstructed_,
         self.cost, self.global_step, self.train_op) = handles
```

<p>How are these nodes defined? The <code>_buildGraph</code> method encapsulates the core of the VAE model framework—starting with the encoder/inference network:</p>
```python
    def _buildGraph(self):
        x_in = tf.placeholder(tf.float32, shape=[None, # enables variable batch size
                                                 self.architecture[0]], name="x")
        dropout = tf.placeholder_with_default(1., shape=[], name="dropout")

        # encoding / "recognition": q(z|x)
        encoding = [Dense("encoding", hidden_size, dropout, self.nonlinearity)
                    # hidden layers reversed for function composition: outer -&gt; inner
                    for hidden_size in reversed(self.architecture[1:-1])]
        h_encoded = composeAll(encoding)(x_in)

        # latent distribution parameterized by hidden encoding
        # z ~ N(z_mean, np.exp(z_log_sigma)**2)
        z_mean = Dense("z_mean", self.architecture[-1], dropout)(h_encoded)
        z_log_sigma = Dense("z_log_sigma", self.architecture[-1], dropout)(h_encoded)
```

<p>Here, we build a pipe from <code>x_in</code> (an empty placeholder for input data <span class="math inline">\(x\)</span>), through the sequential hidden encoding, to the corresponding distribution over latent space—the variational approximate posterior, or hidden representation, <span class="math inline">\(z \sim q_\phi(z|x)\)</span>.</p>
<p>As observed in lines <code>14</code> - <code>15</code>, latent <span class="math inline">\(z\)</span> is distributed as a multivariate <a href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2465539/figure/fig1/">normal</a> with mean <span class="math inline">\(\mu\)</span> and diagonal covariance values <span class="math inline">\(\sigma^2\)</span> (the square of the “sigma” in <code>z_log_sigma</code>) directly parameterized by the encoder: <span class="math inline">\(\mathcal{N}(\mu, \sigma^2I)\)</span>. In other words, we set out to “explain” highly complex observations as the consequence of an unobserved collection of simplified latent variables, i.e. independent Gaussians. (This is dictated by our choice of a conjugate spherical Gaussian prior over <span class="math inline">\(z\)</span>—see <a href="http://blog.fastforwardlabs.com/2016/08/12/introducing-variational-autoencoders-in-prose-and.html">Part I</a>.)</p>
<p>Next, we sample from this latent distribution (in practice, <a href="https://arxiv.org/abs/1312.6114">one draw is enough</a> given sufficient minibatch size, i.e. &gt;100). This method involves a trick—can you figure out why?—that we will explore in more detail later.</p>
```python
        z = self.sampleGaussian(z_mean, z_log_sigma)
```

<p>The sampled <span class="math inline">\(z\)</span> is then passed to the decoder/generative network, which symmetrically builds back out to generate the conditional distribution over input space, reconstruction <span class="math inline">\(\tilde{x} \sim p_\theta(x|z)\)</span>.</p>

```python
        # decoding / "generative": p(x|z)
        decoding = [Dense("decoding", hidden_size, dropout, self.nonlinearity)
                    for hidden_size in self.architecture[1:-1]] # assumes symmetry
        # final reconstruction: restore original dims, squash outputs [0, 1]
        decoding.insert(0, Dense( # prepend as outermost function
            "reconstruction", self.architecture[0], dropout, self.squashing))
        x_reconstructed = tf.identity(composeAll(decoding)(z), name="x_reconstructed")
```

<p>Alternately, we add a placeholder to directly feed arbitrary values of <span class="math inline">\(z\)</span> to the generative network (to fabricate realistic outputs—no input data necessary!):</p>

```python
        # ops to directly explore latent space
        # defaults to prior z ~ N(0, I)
        z_ = tf.placeholder_with_default(tf.random_normal([1, self.architecture[-1]]),
                                         shape=[None, self.architecture[-1]],
                                         name="latent_in")
        x_reconstructed_ = composeAll(decoding)(z_)
```

<p>TensorFlow automatically flows data through the appropriate subgraph, based on the nodes that we fetch and feed with the <code>tf.Session.run</code> method. Defining the <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/vae.py#L190-L196">encoder</a>, <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/vae.py#L198-L209">decoder</a>, and <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/vae.py#L211-L214">end-to-end VAE</a> is then trivial (see linked code).</p>
<p>We’ll finish the <code>VAE._buildGraph</code> method later in the post, as we walk through the nuances of the model.</p>
<h2 id="the-reparameterization-trick">The Reparameterization Trick</h2>
<p>In order to estimate the latent representation <span class="math inline">\(z\)</span> for a given observation <span class="math inline">\(x\)</span>, we want to sample from the approximate posterior <span class="math inline">\(q_\phi(z|x)\)</span> according to the distribution defined by the encoder.</p>
<p>However, model training by <a href="http://mathworld.wolfram.com/MethodofSteepestDescent.html">gradient descent</a> requires that our model be differentiable with respect to its learned parameters (which is how we propagate the gradients). This presupposes that the model is deterministic—i.e. a given input always returns the same output for a fixed set of parameters, so the only source of stochasticity are the inputs. Incorporating a probabilistic “sampling” node would make the model itself stochastic!</p>
<p>Instead, we inject randomness into the model by introducing input from an auxiliary random variable: <span class="math inline">\(\epsilon \sim p(\epsilon)\)</span>.</p>
<p>For our purposes, rather than sampling <span class="math inline">\(z\)</span> directly from <span class="math inline">\(q_\phi(z|x) \sim \mathcal{N}(\mu, \sigma^2I)\)</span>, we generate Gaussian noise <span class="math inline">\(\epsilon \sim \mathcal{N}(0, I)\)</span> and compute <span class="math display">\[z = \mu + \sigma \odot \epsilon\]</span> (where <span class="math inline">\(\odot\)</span> is the element-wise product). In code:</p>

```python
    def sampleGaussian(self, mu, log_sigma):
        """Draw sample from Gaussian with given shape, subject to random noise epsilon"""
        with tf.name_scope("sample_gaussian"):
            # reparameterization trick
            epsilon = tf.random_normal(tf.shape(log_sigma), name="epsilon")
            return mu + epsilon * tf.exp(log_sigma) # N(mu, sigma**2)
```

<p>By “reparameterizing” this step, inference and generation become entirely differentiable and hence, learnable.</p>
<h2 id="cost-function">Cost Function</h2>
<p>Now, in order to optimize the model, we need a metric for how well its parameters capture the true data-generating and latent distributions. That is, how likely is observation <span class="math inline">\(x\)</span> under the joint distribution <span class="math inline">\(p(x, z)\)</span>?</p>
<p>Recall that we represent the global encoder and decoder parameters (i.e. neural network weights and biases) as <span class="math inline">\(\phi\)</span> and <span class="math inline">\(\theta\)</span>, respectively.</p>
<p>In other words, we want to simultaneously tune these complementary parameters such that we maximize <span class="math inline">\(log(p(x|\phi, \theta))\)</span>—the log-likelihood across all datapoints <span class="math inline">\(x\)</span> under the current model settings, after marginalizing out the latent variables <span class="math inline">\(z\)</span>. This term is also known as the model <em>evidence</em>.</p>
<p>We can express this marginal likelihood as the sum of what we’ll call the <em>variational</em> or <em>evidence lower bound</em> <span class="math inline">\(\mathcal{L}\)</span> and the <em>Kullback-Leibler (KL) divergence</em> <span class="math inline">\(\mathcal{D}_{KL}\)</span> between the approximate and true latent posteriors: <span class="math display">\[ log(p(x)) = \mathcal{L}(\phi, \theta; x) + \mathcal{D}_{KL}(q_\phi(z|x) || p_\theta(z|x)) \]</span></p>
<p>Here, the <!-- The --> KL divergence can be (<a href="http://mathworld.wolfram.com/RelativeEntropy.html">fuzzily</a>!) intuited as a metric for the misfit of the approximate posterior <span class="math inline">\(q_\phi\)</span>. We’ll delve into this further in a moment, but for now the important thing is that it is non-negative by definition; consequently, the first term acts as a <em>lower bound</em> on the total. So, we maximize the lower bound <span class="math inline">\(\mathcal{L}\)</span> as a (computationally-tractable) proxy for the total marginal likelihood of the data under the model. (And the better our approximate posterior, the tighter the gap between the lower bound and the total model evidence.)</p>
<p>With some <a href="https://arxiv.org/abs/1312.6114">mathematical wrangling</a>, we can decompose <span class="math inline">\(\mathcal{L}\)</span> into the following objective function: <span class="math display">\[ \mathcal{L}(\phi, \theta; x) = \mathbb{E}_{z \sim q_\phi(z|x)}[log(p_\theta(x|z))] - \mathcal{D}_{KL}(q_\phi(z|x) || p_\theta(z)) \]</span> (Phrased as a cost, we optimize the model by minimizing <span class="math inline">\({-\mathcal{L}}\)</span>.)</p>
<p>Here, the perhaps unfriendly-looking first term is, in fact, familiar! It’s the probability density of generated output <span class="math inline">\(\tilde{x}\)</span> given the inferred latent distribution over <span class="math inline">\(z\)</span>—i.e. the (negative) expected <em>reconstruction error</em>. This loss term is intrinsic to perhaps every autoencoder: how accurately does the output replicate the input?</p>
<p>Choosing an appropriate metric for image resemblance is hard (but that’s another <a href="https://arxiv.org/abs/1512.09300">story</a>). We’ll use the binary <a href="http://neuralnetworksanddeeplearning.com/chap3.html#the_cross-entropy_cost_function">cross-entropy</a>, which is commonly used for data like MNIST that can be modeled as <a href="http://mathworld.wolfram.com/BernoulliDistribution.html">Bernoulli trials</a>. Expressed as a static method of the <code>VAE</code> class:</p>

```python
    @staticmethod
    def crossEntropy(obs, actual, offset=1e-7):
        """Binary cross-entropy, per training example"""
        # (tf.Tensor, tf.Tensor, float) -&gt; tf.Tensor
        with tf.name_scope("cross_entropy"):
            # bound by clipping to avoid nan
            obs_ = tf.clip_by_value(obs, offset, 1 - offset)
            return -tf.reduce_sum(actual * tf.log(obs_) +
                                  (1 - actual) * tf.log(1 - obs_), 1)
```

<p>The second term in the objective is the KL divergence of the prior <span class="math inline">\(p\)</span> from the (approximate) posterior <span class="math inline">\(q\)</span> over the latent space. We’ll approach this conceptually, then mathematically.</p>
<p>The KL divergence <span class="math inline">\(\mathcal{D}_{KL}(q||p)\)</span> is defined as the relative entropy between probability density functions <span class="math inline">\(q\)</span> and <span class="math inline">\(p\)</span>. In information theory, entropy represents information content (measured in nats), so <span class="math inline">\(\mathcal{D}_{KL}\)</span> quantifies the information gained by revising the candidate prior <span class="math inline">\(p\)</span> to match some “ground truth” <span class="math inline">\(q\)</span>.</p>
<p>In a related vein, the KL divergence between posterior and prior beliefs (i.e. distributions) can be conceived as a measure of “<a href="http://ilab.usc.edu/surprise">surprise</a>”: the extent to which the model must update its “worldview” (parameters) to accomodate new observations.</p>
<p>(Note that the formula is asymmetric—i.e. <span class="math inline">\(\mathcal{D}_{KL}(q||p) \neq \mathcal{D}_{KL}(p||q)\)</span>—with <a href="http://www.inference.vc/how-to-train-your-generative-models-why-generative-adversarial-networks-work-so-well-2/">implications</a> for its use in generative models. This is also why it is not a true metric.)</p>
<p>By inducing the learned approximation <span class="math inline">\(q_\phi(z|x)\)</span> (the encoder) to match the continuous imposed prior <span class="math inline">\(p(z)\)</span>, the KL term encourages robustness to small perturbations along the latent manifold, enabling smooth interpolation within and between classes (e.g. MNIST digits). This reduces “spottiness” in the latent space that is often observed in autoencoders without such regularization.</p>
<p>Mathematical bonus: we can strategically choose certain conjugate priors over <span class="math inline">\(z\)</span> that let us analytically integrate the KL divergence, yielding a closed-form equation. This is true of the spherical Gaussian we chose, such that <span class="math display">\[ {-\mathcal{D}}_{KL}(q_\phi(z|x) || p_\theta(z)) = \frac{1} 2 \sum{(1 + log(\sigma^2) - \mu^2 - \sigma^2)} \]</span> (summed over the latent dimensions). In TensorFlow, that looks like this:</p>

```python
    @staticmethod
    def kullbackLeibler(mu, log_sigma):
        """(Gaussian) Kullback-Leibler divergence KL(q||p), per training example"""
        # (tf.Tensor, tf.Tensor) -&gt; tf.Tensor
        with tf.name_scope("KL_divergence"):
            # = -0.5 * (1 + log(sigma**2) - mu**2 - sigma**2)
            return -0.5 * tf.reduce_sum(1 + 2 * log_sigma - mu**2 -
                                        tf.exp(2 * log_sigma), 1)
```

<p>Together, these complementary loss terms capture the trade-off between expressivity and concision, between data complexity and simplicity of the prior. Reconstruction loss pushes the model toward perfectionist tendencies, while KL loss (along with the addition of auxiliary noise) encourages it to explore sensibly.</p>
<p>To elaborate (building on the <code>VAE._buildGraph</code> method started above):</p>

```python
        # reconstruction loss: mismatch b/w x &amp; x_reconstructed
        # binary cross-entropy -- assumes p(x) &amp; p(x|z) are iid Bernoullis
        rec_loss = VAE.crossEntropy(x_reconstructed, x_in)

        # Kullback-Leibler divergence: mismatch b/w approximate posterior &amp; imposed prior
        # KL[q(z|x) || p(z)]
        kl_loss = VAE.kullbackLeibler(z_mean, z_log_sigma)

        # average over minibatch
        cost = tf.reduce_mean(rec_loss + kl_loss, name="cost")
```

<p>Beyond its concise elegance <!-- elegant concision  -->and solid grounding in Bayesian theory, the cost function lends itself well to intuitive metaphor:</p>
<p>Information theory-wise, the VAE is a terse game of Telephone, with the aim of finding the <em>minimum description length</em> to convey the input from end to end. Here, reconstruction loss is the information “lost in translation,” while KL loss captures how overly “wordy” the model must be to convey the message through an unpredictable medium (hidden code imperfectly optimized for the input data).</p>
<p>Or, framing the VAE as a lossy compression algorithm, reconstruction loss accounts for the fidelity of (de)compression while KL loss penalizes the model for using a sub-optimal compression scheme.</p>
<h2 id="training">Training</h2>
<p>At last, our VAE cost function in hand (after factoring in optional <a href="http://cs231n.github.io/neural-networks-2/#regularization"><span class="math inline">\(\ell_2\)</span>-regularization</a>), we finish <code>VAE._buildGraph</code> with optimization nodes to be evaluated at each step of SGD (with the <a href="https://arxiv.org/abs/1412.6980">Adam</a> optimizer)…</p>

```python
        # optimization
        global_step = tf.Variable(0, trainable=False)
        with tf.name_scope("Adam_optimizer"):
            optimizer = tf.train.AdamOptimizer(self.learning_rate)
            tvars = tf.trainable_variables()
            grads_and_vars = optimizer.compute_gradients(cost, tvars)
            clipped = [(tf.clip_by_value(grad, -5, 5), tvar) # gradient clipping
                    for grad, tvar in grads_and_vars]
            train_op = optimizer.apply_gradients(clipped, global_step=global_step,
                                                 name="minimize_cost") # back-prop
```

<p>…and return all of the nodes we want to access in the future to the <code>VAE.__init__</code> method where <code>buildGraph</code> was called.</p>

```python
        return (x_in, dropout, z_mean, z_log_sigma, x_reconstructed,
                z_, x_reconstructed_, cost, global_step, train_op)
```

<p>Using SGD to optimize the function parameters of the inference and generative networks simultaneously is called <em>Stochastic Gradient Variational Bayes</em>.</p>
<p>This is where TensorFlow really shines: all of the gradient backpropagation and parameter updates are performed via automatic differentation, and abstracted away from the researcher in the <code>train_op</code> (essentially) one-liner on line <code>48</code>.</p>
<p>Model training (with optional cross-validation) is then as simple as feeding minibatches from dataset <code>X</code> to the <code>x_in</code> placeholder and evaluating (“fetching”) the <code>train_op</code>. Here are some relevant chunks, excerpted from the <a href="https://github.com/fastforwardlabs/vae-tf/blob/master/vae.py#L216-L295">full class method</a>:</p>

```python
    def train(self, X, max_iter=np.inf, max_epochs=np.inf, cross_validate=True,
              verbose=True, save=False, outdir="./out", plots_outdir="./png"):
        try:
            err_train = 0
            now = datetime.now().isoformat()[11:]
            print("------- Training begin: {} -------\n".format(now))

            while True:
                x, _ = X.train.next_batch(self.batch_size)
                feed_dict = {self.x_in: x, self.dropout_: self.dropout}
                fetches = [self.x_reconstructed, self.cost, self.global_step, self.train_op]
                x_reconstructed, cost, i, _ = self.sesh.run(fetches, feed_dict)

                err_train += cost

                if i%1000 == 0 and verbose:
                    print("round {} --&gt; avg cost: ".format(i), err_train / i)

                if i &gt;= max_iter or X.train.epochs_completed &gt;= max_epochs:
                    print("final avg cost (@ step {} = epoch {}): {}".format(
                        i, X.train.epochs_completed, err_train / i))
                    now = datetime.now().isoformat()[11:]
                    print("------- Training end: {} -------\n".format(now))
                    break
```

<p>Helpfully, TensorFlow comes with a built-in <a href="https://www.tensorflow.org/versions/r0.10/how_tos/summaries_and_tensorboard/index.html">visualization dashboard</a>. Here’s the computational graph for an end-to-end VAE with two hidden encoder/decoder layers (that’s what all the <code>tf.name_scope</code>-ing was for):</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/tensorboard.png" title="TensorBoard" style="max-width: 398px !important"/><h2 id="wrapping-up">Wrapping Up
</h2><p>The future of deep latent models lies in models that can reason about the world—“understanding” complex observations, transforming them into meaningful internal representations, and even leveraging these representations to make decisions—all while coping with scarce data, and in semisupervised or unsupervised settings. VAEs are an important step toward this future, demonstrating the power of new ways of thinking that result from unifying variational Bayesian methods and deep learning.</p>
<p>We now understand how these fields come together to make the VAE possible, through a theoretically-sound objective function that balances accuracy (reconstruction loss) with variational regularization (KL loss), and efficient optimization of the fully differentiable model thanks to the reparameterization trick.</p>
<p>We’ll wrap up for now with one more way of visualizing the condensed information encapsulated in VAE latent space.</p>
<p><a href="http://blog.fastforwardlabs.com/2016/08/12/introducing-variational-autoencoders-in-prose-and.html">Previously</a>, we showed the correspondence between the inference and generative networks by plotting the encoder and decoder perspectives of the latent space in the same 2-D coordinate system. For the decoder perspective, this meant feeding linearly spaced latent coordinates to the generative network and plotting their corresponding outputs.</p>
<p>To get an undistorted sense of the full latent manifold, we can sample and decode latent space coordinates proportionally to the model’s distribution over latent space. In other words—thanks to variational regularization provided by the KL loss!—we simply sample relative to our chosen prior distribution over <span class="math inline">\(z\)</span>. In our case, this means sampling linearly spaced percentiles from the <a href="http://work.thaslwanter.at/Stats/html/statsDistributions.html#other-important-presentations-of-probability-densities">inverse CDF</a> of a spherical Gaussian.<a href="#fn1" class="footnoteRef" id="fnref1"><sup>1</sup></a></p>
<p>Once again, evolving over (logarithmic) time:</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160816_1813_latent_784_500_500_2_explore_ppf30_16.0.500x500.slower47.gif" title="Decoder's undistorted view of latent space, over training"/></div>
<p>Interestingly, we can see that the slim tails of the distribution (edges of the frame) are not well-formed. Presumably, this results from few observed inputs being mapped to latent posteriors with significant density in these regions.</p>
<p>Here are a few resulting constellations (from a single model):</p>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160805_1646_reloaded_latent_784_500_500_2_round_131072_explore_ppf_30.png" title="Generative view of latent space: 30x30"/></div>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160805_1646_reloaded_latent_784_500_500_2_round_131072_explore_ppf_60.png" title="Generative view of latent space: 60x60"/></div>
<div class="figure">
<img src="http://fastforwardlabs.github.io/blog-images/miriam/imgs_code/160805_1646_reloaded_latent_784_500_500_2_round_131072_explore_ppf_100.png" title="Generative view of latent space: 100x100"/></div>
<p>Theoretically, we could subdivide the latent space into infinitely many points (limited in practice only by the computer’s floating point precision), and let the generative network dream up infinite constellations of creative variations on MNIST.</p>
<p>That’s enough digits for now! Keep your eyes out for the next installment, where we’ll tinker with the vanilla VAE model in the context of a new dataset.</p>
<p>– Miriam</p>
<div class="footnotes">
<hr><ol><li id="fn1"><p>Thanks Kyle McDonald (<span class="citation">@kcimc</span>) and Tom White (<span class="citation">@dribnet</span>) for noting this!<a href="#fnref1">↩</a></p></li>
</ol></div> </div>
