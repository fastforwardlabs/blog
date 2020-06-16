---
author: Grant
author_link: https://twitter.com/GrantCuster
date: "2018-04-25T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2018-03-31-210319-hicat2.gif
published: true
title: 'JavaScript eats the world: deep learning and notebooks edition'
aliases:
  - /2018/04/25/javascript-eats-the-world-deep-learning-and-notebooks-edition.html
---

Google recently announced [TensorFlow.js](https://medium.com/tensorflow/introducing-tensorflow-js-machine-learning-in-javascript-bf3eab376db), an open-source library for running machine learning in the browser, and a successor to the deeplearn.js library. While the majority of machine learning work is unlikely to shift to JavaScript anytime soon, the examples included on the [TensorFlow.js site](https://js.tensorflow.org/) do a good job of showing the promise of machine learning models that run in the browser. 

![A short GIF of the Teachable Machines demo showing Grant raising his hand and the model responding with a GIF of a cat waving.](/images/editor_uploads/2018-03-31-210319-hicat2.gif)

##### Teachable Machine lets you train a model to help you wave at cats.

Our favorite example is [Teachable Machine](https://teachablemachine.withgoogle.com/), which walks you through a training process using images from your webcam to trigger response GIFs. It shows how training in the browser can help the model adapt to different contexts. For example, if you want your model to spot when a user raises their hand, a pre-trained model might have trouble if the user is sitting in a room surrounded by mannequins. Because you can train the Teachable Machine model with specific examples of both "raised hand" and "unraised hand," there's a good chance it will perform well in your weird mannequin room (a very specific situation). A related webcam-based example is the work [Oz Ramos](https://twitter.com/LearnWithOz) is doing to build a system for navigation using facial gestures, to help people with mobility impairments use the web.

Another advantage of having deep learning code running in the browser is that you can open up the code itself for people to interact with. Better JavaScript deep-learning tools mean more web-based interactive deep-learning explainers: explainers like [Minsuk Kahng's Deep Learning Tutorial](https://beta.observablehq.com/@minsukkahng/deep-learning-tutorial-with-deeplearn-js), which shows how to use deeplearn.js to build a model for the Iris dataset. Because all of the code for the system is exposed and editable, viewers cans tweak different parameters and easily view the results. 

![A screenshot form a section of Minsuk Kahng's Deep Learning Tutorial. It shows the model code and a slider for specifying the number of neurons in the hidden layer.](/images/editor_uploads/2018-03-31-210737-Screen_Shot_2018_03_30_at_4_59_56_PM.png)

##### Minsuk Kahng's deeplearning.js node lets you edit the code and immediately view the results.

Kahng's tutorial is built on the new JavaScript notebook site [Observable](https://beta.observablehq.com/@minsukkahng/deep-learning-tutorial-with-deeplearn-js). Made by D3.js creator Mike Bostock and others, Observable makes it easy to build interactive and modifiable JavaScript examples of all types. Along with sites like [Codepen](https://codepen.io/) and [Glitch](https://glitch.com/), Observable is leading a renaissance of interactive code examples and explainers. Grant has used Observable for [everything from using three.js for 2D data visualization to finding out how long it takes a browser to say different numbers out loud.](https://beta.observablehq.com/@grantcuster)