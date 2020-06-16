---
author: Micha
author_link: https://github.com/mynameisfiber
date: "2015-10-26T16:20:07Z"
feature: true
preview_image: http://fastforwardlabs.github.io/report_images/ff03/neural_net_overview.png
redirect_from:
- /post/131957134308/hello-deep-learning
tags:
- deep learning
- neural networks
- caffe
- googlenet
- helloworld
- code
title: Hello Deep Learning
aliases:
  - /2015/10/26/hello-deep-learning.html
---

<figure data-orig-width="610" data-orig-height="420" class="tmblr-full"><img src="http://68.media.tumblr.com/eabecd03e32522e28f0f6012580b7c35/tumblr_inline_nwu59mZS4C1ta78fg_540.png" alt="image" data-orig-width="610" data-orig-height="420"/></figure><p><b><br/></b>Deep learning is a hot and fascinating research area, particularly when applied to classifying images. While researching the Fast Forward Labs <i>Deep Learning: Image Analysis</i> report, we played with a lot of very cool technology. In this blog post, we offer a guide to getting started with deep learning by using APIs from some of the most interesting deep-learning-as-a-service startups.<b><br/></b></p><p>These APIs accept images and/or video, and quickly classify objects, ideas, and items shown in the images and video. We used this capability to build <a href="http://pictograph.us">pictograph.us</a>, an app that allows you to visualize your Instagram photos by the contents of the photos.</p><p>We have many ideas for other applications, and wanted share some tips and code to help you get started working in this field as well. </p><p>If you want to get started with deep learning for both images and videos, check out our repo <a href="https://github.com/fastforwardlabs/hello_deep_learning">hello_deep_learning</a>.  There’s a nice <a href="https://github.com/fastforwardlabs/hello_deep_learning/blob/master/hello_deep_learning.ipynb">jupyter notebook</a> to get you started as quickly as possible.  We chose to focus on <a href="https://www.metamind.io/">MetaMind</a>, <a href="https://www.dextro.co/">Dextro</a>, <a href="http://cloudsightapi.com/">CloudSight,</a> and <a href="http://www.clarifai.com/">Clarifai</a> because their mature and robust APIs handle large numbers of images while maintaining high quality image predictions.</p><p>We strongly recommend starting with an API, because it’s still very challenging to install and configure the open source libraries. That said, if you want to dig a bit deeper, the <a href="https://github.com/BVLC/caffe/wiki/Model-Zoo">model zoo</a> has many pre-trained models you can load up into <a href="http://caffe.berkeleyvision.org">caffe</a>.  </p><p>Interested in image recognition? Check out the <a href="https://github.com/BVLC/caffe/wiki/Model-Zoo#googlenet-gpu-implementation-from-princeton">GoogLeNet</a>.  </p><p>Want to play with automatic video descriptions? Check out <a href="https://github.com/BVLC/caffe/wiki/Model-Zoo#translating-videos-to-natural-language">Translating Videos to Natural Language</a>.  </p><p>Want to play with face detection? Check out <a href="https://github.com/BVLC/caffe/wiki/Model-Zoo#vgg-face-cnn-descriptor">Face CNN descriptor</a>.  </p><p>All these models have been pre-trained and simply need to be loaded up into caffe, then you can start throwing data at them!</p><p>Finally, if you want to dig even deeper, we recommend <a href="http://keras.io/">keras</a>. It’s a very simple python library to start building your own neural models. But don’t mistake simplicity for lack of power: we’re using it to train new and interesting language models, and the simplicity enables us to focus on the algorithms and techniques.</p><p>With these services and libraries, you’ll be able to start identifying objects in images or videos in no time. Have a cool idea to build something using this new capability? Tell us at <a href="http://twitter.com/fastforwardlabs">@fastforwardlabs</a>!</p><p>-Micha</p>
