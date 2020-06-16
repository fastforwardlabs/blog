---
author: Patrick Doupe
date: "2016-08-26T17:43:24Z"
post_type: Guest Post
preview_image: http://fastforwardlabs.github.io/blog-images/geo/empty_satellite_image.png
redirect_from:
- /post/149516029368/exploring-deep-learning-on-satellite-data
tags:
- deep learning
- code
title: Exploring Deep Learning on Satellite Data
aliases:
  - /2016/08/26/exploring-deep-learning-on-satellite-data.html
---

##### This is a guest post featuring a project Patrick Doupe, now a Senior Data Analyst at Icahn School of Medicine at Mount Sinai, completed as a fellow in the <a href="http://insightdatascience.com">Insight Data Science program</a>. In our partnership with Insight, we occassionally advise fellows on month-long projects and how to build a career in data science.

<p>Machines are getting <a href="http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html">better</a> at identifying objects in images. These technologies are used to do more than <a href="https://twitter.com/patrickdoupe/status/724820639924781056">organise your photos</a> or chat your family and friends with snappy augmented pictures and movies. Some companies are using them to better understand how the world works. Be it by improving <a href="http://www.wsj.com/articles/startups-mine-market-moving-data-from-fields-parking-lotseven-shadows-1416502993">forecasts on Chinese economic growth from satellite images of construction sites</a> or estimating <a href="http://www.forbes.com/sites/alexknapp/2015/04/22/satellite-data-and-a-i-will-be-deployed-to-predict-and-prevent-deforestation/#152c27947fdb">deforestation</a>, algorithms and data can help provide useful information about the current and future states of society.</p>
<p>In early 2016, I developed a prototype of a model to predict population from satellite images. This extends existing classification tasks, which ask whether something exists in an image. In my prototype, I ask how much of something not directly visible is in an image? The regression task is difficult; <a href="http://cs231n.github.io/neural-networks-2/">current advice</a> is to turn any regression problem into a classification task. But I wanted to aim higher. After all, satellite image appear different across populated and non populated areas.</p>
<p><img src="http://fastforwardlabs.github.io/blog-images/geo/populated_satellite_image.png" style="width: 256px; height: 256px" alt="image"/></p>
##### Populated region
<p><img src="http://fastforwardlabs.github.io/blog-images/geo/empty_satellite_image.png" style="width: 256px; height: 256px" alt="image"/></p>
##### Empty region
<p>The prototype was developed in conjuction with Fast Forward Labs, as my project in the <a href="http://insightdatascience.com">Insight Data Science</a> program. I trained convolutional neural networks on LANDSAT satellite imagery to predict Census population estimates. I also learned all of this, from understanding what a convolutional neural network is, to dealing with satellite images to building a website within four weeks at Insight. If I can do this in a few weeks, your data scientists too can take your project from idea to prototype in a short amount of time.</p>
<h2 id="landsat-landstats">LANDSAT-landstats</h2>
<p>Counting people is an important task. We need to know where people are to provide government services like <a href="http://www.theatlantic.com/health/archive/2016/02/nursing-shortage/459741/">health care</a> and to develop infrastructure like <a href="http://www.theage.com.au/national/education/victorias-schools-of-the-future-a-work-in-progress-20160321-gnn2ie">school buildings</a>. There are also constitutional reasons for a Census, <a href="https://www.youtube.com/watch?v=TK9Gq6SX3YU">which I&rsquo;ll leave to Sam Seaborn</a>.</p>
<p>We typically get this information from a Census or other government surveys like the American Community Survey. These are not perfect measures. For example, the inaccuracies are <a href="http://www.datacenterresearch.org/pre-katrina/articles/censustrust.html">biased against</a> those who are likely to use government services.</p>
<p>If we could develop a model that could estimate the population well at the community level, we could help government services better target those in need. The model could also help governments that facing resources constraints that prevent the running of a census. Also, if it works for counting humans, then maybe it could work for estimating other socio-economic statistics. Maybe even help <a href="https://code.facebook.com/posts/1676452492623525/connecting-the-world-with-better-maps/">provide universal internet access</a>. So much promise!</p>
<h2 id="so-much-reality">So much reality</h2>
<p>Satellite images are huge. To keep the project manageable I chose two US States that are similar in their environmental and human landscape; one State for model training and another for model testing. Oregon and Washington seemed to fit the bill. Since these states were chosen based on their similarity, I thought I would stretch the model by choosing a very different state as a tougher test. I&rsquo;m from Victoria, Australia, so I chose this glorious region.</p>
<p>Satellite images are also messy and full of interference. To minimise this issue and focus on the model, I chose the LANDSAT Top Of Atmosphere (TOA) annual composite satellite image for 2010. This image is already stitched together from satellite images with minimal interference. I obtained the satellite images from the <a href="https://earthengine.google.com">Google Earth Engine</a>. I began with low resolution images (1km) and lowered my resolution in each iteration of the model.</p>
<p>For the <a href="http://www.census.gov/geo/maps-data/data/tiger-line.html">Census estimates</a>, I wanted the highest spatial resolution, which is the Census block. A typical Census block contains between 600 and 3000 people, or about a city block. To combine these datasets I assigned each pixel its geographic coordinates and merged each pixel to its census population estimates using various Python geospatial tools. This took enough time that I dropped the bigger plans. Best get something complete than a half baked idea.</p>
<h2 id="a-very-high-level-overview-of-training-convolutional-neural-networks">A very high level overview of training Convolutional Neural Networks</h2>
<p>The problem I faced is a classic supervised learning problem: train a model on satellite images to predict census data. Then I could use standard methods, like linear regression or neural networks. For every pixel there is number corresponding to the intensity of various light bandwidths. We then have the number of features equal to the number of bandwidths by the number of pixels. Sure, we could do some more complicated feature engineering but the basic idea could work, right?</p>
<p>Not really. You see, a satellite image is not a collection of independent pixels. Each pixel is connected to other pixels and this connection has meaning. A mountain range is connected across pixels and human built infrastructure is connected across pixels. We want to retain this information. Instead of modelling pixels independently, we need to model pixels in connection with their neighbours.</p>
<p>Convolutional neural networks (hereafter, &ldquo;convnets&rdquo;) do exactly this. These networks are super powerful at image classification, with many models reporting better accuracy than humans. What we can do is swap the loss function and run a regression.</p>
<img src="http://fastforwardlabs.github.io/blog-images/geo/convnet-01-ffl.png" alt="Figure of Convolutional Neural Network showing the processing of an image of a horse" style="max-width: 360px"/>
##### Diagram of a simple convolutional neural network processing an input image. From Fast Forward Labs report on Deep Learning: Image Analysis
<h2 id="training-the-model">Training the model</h2>
<p>Unfortunately convnets can be hard to train. First, there are a lot of parameters to set in a convnet: how many convolutional layers? Max-pooling or average-pooling? How do I initialise my weights? Which activations? It&rsquo;s super easy to get overwhelmed. Micha suggested I use the well known VGGNet as a starting base for a model. For other parameters, I based the network on what seemed to be the current best practices. I learned these by following this winter&rsquo;s <a href="http://cs231n.github.io/neural-networks-2/">convolutional neural network course at Stanford</a>.</p>
<p>Second, they take a lot of time and data to train. This results in training periods of hours to weeks, while we want fast results for a prototype. One option is to use pre-trained models, like those available at the <a href="https://github.com/BVLC/caffe/wiki/Model-Zoo">Caffe model zoo</a>. I was writing my model using the <a href="http://keras.io">Keras</a> python library, which at present doesn&rsquo;t have as large a zoo of models. Instead, I chose to use a smaller model and see if the results pointed in a promising direction.</p>
<h2 id="results">Results</h2>
<p>To validate the model, I used data from on Washington and Victoria, Australia. I show the model&rsquo;s accuracy on the following scatter plot of the model&rsquo;s predictions against reality. The unit of observation is the small image-observation used by the network and I estimate the population density in an image. Since each image size is the same, this is the same as estimating population. Last, the data is quasi log-normalised[6]. Let&rsquo;s start with Washington</p>
<img src="http://fastforwardlabs.github.io/blog-images/geo/washington.png" alt="Washington State"/>
##### Washington State
<p>We see that the model is picking up the signal. Higher actual population densities are associated with higher model predictions. Also noticeable is that the model struggles to estimate regions of zero population density. The R<sup>2</sup> of the model is 0.74. That is, the model explains about 74 percent of the spatial variation in population. This is up from 26 percent in the four weeks achieved in Insight.</p>
<img src="http://fastforwardlabs.github.io/blog-images/geo/victoria.png" alt="Victoria"/>
##### Victoria
<p>A harder test is a region like Victora with a different natural and built environment. The scatter plot of model performance shows the reduced performance. The model&rsquo;s inability to pick regions of low population is more apparent here. Not only does the model struggle with areas of zero population, it predicts higher population for low population areas. Nevertheless, with an R<sup>2</sup> of 0.63, the overall fit is good for a harder test.</p>
<p>An interesting outcome is that the regression estimates are quite similar for both Washington and Victoria: the model consistently underestimates reality. In sample, we still have a model that underestimates population. Given that the images are unlikely to have enough information to identify human settlements at current resolution, it&rsquo;s understandable that the model struggles to estimate population in these regions.</p>
<table><thead><tr class="header"><th align="left">Variable</th>
<th align="right">A perfect model</th>
<th align="right">Washington</th>
<th align="right">Victoria</th>
<th align="right">Oregon (in sample)</th>
</tr></thead><tbody><tr class="odd"><td align="left">Intercept</td>
<td align="right">0</td>
<td align="right">-0.43</td>
<td align="right">-0.37</td>
<td align="right">-0.04</td>
</tr><tr class="even"><td align="left">Slope</td>
<td align="right">1</td>
<td align="right">0.6</td>
<td align="right">0.6</td>
<td align="right">0.86</td>
</tr><tr class="odd"><td align="left">R<sup>2</sup></td>
<td align="right">1</td>
<td align="right">0.74</td>
<td align="right">0.63</td>
<td align="right">0.96</td>
</tr></tbody></table><h2 id="conclusion">Conclusion</h2>
<p>LANDSAT-landstats was an experiment to see if convnets could estimate objects they couldn&rsquo;t &lsquo;see.&rsquo; Given project complexity, the timeframe, and my limited understanding of the algorithms at the outset, the results are promising. We&rsquo;re not at a stage to provide precise estimates of a region&rsquo;s population, but with improved image resolution and advances in our understanding of convnets, we may not be far away.</p>
<p>-Patrick Doupe</p>
