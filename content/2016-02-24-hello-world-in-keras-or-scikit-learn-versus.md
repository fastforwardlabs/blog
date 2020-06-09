---
author: Mike
author_link: https://twitter.com/mikepqr
date: "2016-02-24T18:58:10Z"
feature: true
preview_image: http://68.media.tumblr.com/a4cf05aa664f57b54fe5021ce966f5d6/tumblr_inline_o30qnzlyxi1qcg73w_540.png
redirect_from:
- /post/139921712388/hello-world-in-keras-or-scikit-learn-versus
tags:
- hello world
- deep learning
- code
title: '"Hello world" in Keras (or, Scikit-learn versus Keras)'
popular: true
---

<h5>This article is <a
href="https://github.com/fastforwardlabs/keras-hello-world">available as a
notebook on Github</a>. Please refer to that notebook for a more detailed
discussion and code fixes and updates.</h5>

<p>Despite all the recent excitement around deep learning, neural networks have a reputation among non-specialists as complicated to build and difficult to  interpret.</p><p>And while interpretability remains an issue, there are now high-level neural network libraries that enable developers to quickly build neural network models without worrying about the numerical details of floating point operations and linear algebra.</p><p>This post compares keras with scikit-learn, the most popular, feature-complete classical machine learning library used by Python developers.</p>

<p>Keras is a high-level neural network library that wraps an API similar to scikit-learn around the Theano or TensorFlow backend. Scikit-learn has a simple, coherent API built around <code>Estimator</code> objects. It is carefully designed and is a good description of machine learning workflow with which many engineers are already comfortable.</p>

<p>Let&rsquo;s get started by importing the libraries we&rsquo;ll need: scikit-learn, keras and some plotting features.</p>

```python
>>> %matplotlib inline
>>> import seaborn as sns
>>> import numpy as np
>>> from sklearn.cross_validation import train_test_split
>>> from sklearn.linear_model import LogisticRegressionCV
>>> from keras.models import Sequential
>>> from keras.layers.core import Dense, Activation
>>> from keras.utils import np_utils
```

<h2>Iris data</h2><p>The famous <a href="https://archive.ics.uci.edu/ml/datasets/Iris">iris dataset</a> is a great way of demonstrating the API of a machine learning framework. In some ways it&rsquo;s the &ldquo;Hello world&rdquo; of machine learning.</p><p>The data is simple, and it&rsquo;s possible to get high accuracy with an extremely simple classifier. Using a neural network here would be like using a sledghammer to crack a nut. But this is fine for us; we want to show the code required to get from data to working classifier, not the details of model design.</p><p>The iris dataset is built into many machine learning libraries. We like the copy in seaborn because it comes as a labelled dataframe that can be easily visualized. Let&rsquo;s load it and look at the first 5 examples.</p>

```python
>>> iris = sns.load_dataset("iris")
>>> iris.head()
```

<figure data-orig-width="450" data-orig-height="183" class="tmblr-full"><img src="http://68.media.tumblr.com/d7c32a4d56195a39fb609287cbf9987c/tumblr_inline_o30ql2XBMK1qcg73w_540.png" alt="image" data-orig-width="450" data-orig-height="183"/></figure><p>For each example (i.e., flower), there are five pieces of data. Four are standard measurements of the flower&rsquo;s size (in centimeters), and the fifth is the species of iris. There are three species: setosa, verscicolor and virginica. Our job is to build a classifier that, given the two petal and two sepal measurements, can predict the species of an iris. Let&rsquo;s do a quick visualization before we start model building (always a good idea!):</p>

```python
>>> sns.pairplot(iris, hue='species')
```

<figure data-orig-width="811" data-orig-height="721" class="tmblr-full"><img src="http://68.media.tumblr.com/a4cf05aa664f57b54fe5021ce966f5d6/tumblr_inline_o30qnzlyxi1qcg73w_540.png" alt="image" data-orig-width="811" data-orig-height="721"/></figure><h2>Munge and split the data for training and testing</h2><p>First we need to pull the raw data out of the <code>iris</code> dataframe. We&rsquo;ll hold the petal and sepal data in an array <code>X</code> and the species labels in a corresponding array <code>y</code>.</p>

```python
>>> X = iris.values[:, 0:4]
>>> y = iris.values[:, 4]
```

<p>Now we split <code>X</code> and <code>y</code> in half. As is standard in supervised machine learning, we&rsquo;ll train with half the data, and measure the performance of our model with the other half. This is simple to do by hand, but is built into scikit-learn as the <code>train_test_split()</code>function.</p>

```python
>>> train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, random_state=0)
```

<h2>Train a scikit-learn classifier</h2><p>We&rsquo;ll train a logisitic regression classifier. Doing this, with built-in hyper-paramter cross validation, requires one line in scikit-learn. Like all scikit-learn <code>Estimator</code> objects, a <code>LogisticRegressionCV</code> classifier has a <code>.fit()</code> method that takes care of the gory numerical details of learning model parameters that best fit the training data. So that method is all we need to do:</p>

```python
>>> lr = LogisticRegressionCV()
>>> lr.fit(train_X, train_y)
```

<h2>Assess the classifier using accuracy</h2><p>Now we can measure the fraction of of the test set the trained classifer classifies correctly (i.e., accuracy).</p>

```python
>>> pred_y = lr.predict(test_X)
>>> print("Test fraction correct (Accuracy) = {:.2f}".format(lr.score(test_X, test_y)))
# Test fraction correct (Accuracy) = 0.83
```

<h2>Now do something very similar with Keras</h2><p>Scikit-learn makes building a classifier very simple:</p><ul><li>one line to instantiate the classifier</li>
    <li>one line to train it</li>
    <li>and one line to measure its performance</li>
</ul><p>It&rsquo;s only a little bit more complicated in keras.</p><p>First a bit of data-munging: scikit-learn&rsquo;s classifiers accept string labels, e.g. <code>"setosa"</code>. But keras requires that labels be one-hot-encoded. This means we need to convert data that looks like</p>

```python
setosa
versicolor
setosa
virginica
...
```

<p>to a table that looks like</p>

```
setosa versicolor virginica
     1          0         0
     0          1         0
     1          0         0
     0          0         1
```

 <p>There are lots of ways of doing this. We&rsquo;ll use a keras utility and some numpy.</p>

```python
>>> def one_hot_encode_object_array(arr):
    '''One hot encode a numpy array of objects (e.g. strings)'''
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

>>> train_y_ohe = one_hot_encode_object_array(train_y)
>>> test_y_ohe = one_hot_encode_object_array(test_y)
```
<h2>Build the neural network model</h2>

<p>Building the model is the only aspect of using keras that is substantially more code than in scikit-learn.</p><p>Keras is a neural network library. As such, while the number of features/classes in your data provide constraints, you can determine all other aspects of model structure. This means that instaniating the classifier requires more work than the one line required by scikit-learn.</p>

<p>In this case, we&rsquo;ll build an extremely simple network: 4 features in the input layer (the four flower measurements), 3 classes in the ouput layer (corresponding to the 3 species), and 16 hidden units because (from the point of view of a GPU, 16 is a round number!)</p>

```python
>>> model = Sequential()
>>> model.add(Dense(16, input_shape=(4,)))
>>> model.add(Activation('sigmoid'))
>>> model.add(Dense(3))
>>> model.add(Activation('softmax'))
>>> model.compile(loss='categorical_crossentropy', optimizer='adam')
```

<p>But now we&rsquo;ve instantiated the keras model, we have an object whose API is almost identical to a classifier in scikit-learn. In particular, it has <code>.fit()</code> and <code>.predict()</code> methods. Let&rsquo;s <code>fit</code>:</p>

```python
>>> model.fit(train_X, train_y_ohe, verbose=0, batch_size=1)
```

<p>For basic use, the only syntactic API difference between a compiled keras model and a sklearn classifier is that keras&rsquo;s equivalent of the sklearn <code>.score()</code> method is called <code>.evaluate()</code>. By default it returns whatever loss function you set when you compile the model, but we can ask it to return the accuracy too. In this case, the second number it returns is exactly what you&rsquo;d get from <code>.score()</code> in sklearn.<br/></p>

```python
>>> loss, accuracy = model.evaluate(test_X, test_y_ohe, show_accuracy=True, verbose=0)
>>> print("Test fraction correct (Accuracy) = {:.2f}".format(accuracy))

# Test fraction correct (Accuracy) = 0.99
```

<p>As you can see, the test accuracy of the neural network model is better than that of the simple logistic regression classifier.</p><p>While reassuring, this misses the point: a neural network model is overkill for this problem. But note that using a batteries-included, high-level library like keras requires only marginally more code to build, train, and apply a neural network model than a traditional model.</p><h2>What&rsquo;s next</h2><p>There&rsquo;s a point where the high-level keras approach does not provide the flexibility needed to build a complex or novel neural network model, but fortunately most work won&rsquo;t reach that level of complexity.</p><p>We built an extremely simple feed-forward network model. To learn more, have a look at <a href="https://github.com/wxs/keras-mnist-tutorial/blob/master/MNIST%20in%20Keras.ipynb">this MNIST tutorial</a>, which demonstrates a slighty more complex use case: the MNIST handwritten digits data. This data requires the complexity a neural network model can afford, with performance improved via a deeper model with some <a href="https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf">dropout</a> (an approach to regularization in neural networks).</p><p>keras also has layers that allow you to build models with:</p><ul><li><a href="http://deeplearning.net/tutorial/lenet.html">convolutional neural networks</a>, which give state-of-the-art results for computer vsion problems</li>
    <li><a href="http://karpathy.github.io/2015/05/21/rnn-effectiveness/">recurrent neural networks</a>, which are particularly well suited to modelling language and other sequence data.</li>
</ul><p>In fact, one key strength of neural networks (along with sheer predictive power) is their composability. Using a high-level library like keras, it only takes a few seconds of work to create a very different network. Models can be built up like legos. Sure, the computer then has to grind through training on a GPU, and that&rsquo;s still relatively expensive. But while the computer slaves away, you get to have fun.</p><p>- Mike</p>
