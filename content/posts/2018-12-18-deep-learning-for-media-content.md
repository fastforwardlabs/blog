---
author: Ryan
author_link: https://twitter.com/jqpubliq
date: "2018-12-18T00:00:00Z"
feature: false
post_type: newsletter
preview_image: /images/editor_uploads/2019-01-05-191614-Merlin_Flow.png
published: true
title: Deep Learning for Media Content
aliases:
  - /2018/12/18/deep-learning-for-media-content.html
---

Machine learning continues to make its way into the arts, most recently in film and TV.

In a [recent blog post](https://cloud.google.com/blog/products/ai-machine-learning/how-20th-century-fox-uses-ml-to-predict-a-movie-audience), data scientists at 20th Century Fox and technical staff at Google Cloud described the approach they are using to predict audiences for their movies. (The tone of the post is fairly self-promoting, befitting the subject matter and industries involved.)

Their product, [Merlin Video](https://datastudio.google.com/u/0/reporting/1Ss64x1ocKeeDdTcMVX3l4iQcr8gp9w-W/page/Hg2V), is a deep learning tool that analyzes movie trailer videos. It was based on a pre-trained model - Google's YouTube 8M video data set, which identifes objects in video, and tuned with movie trailers and marketing data from past movies. Fox released [a paper describing the technology in detail](https://arxiv.org/abs/1810.08189). They have been using Merlin - with success - for a year and a half.

![](/images/editor_uploads/2019-01-05-191614-Merlin_Flow.png)
##### Merlin's architecture [(image source)](https://cloud.google.com/blog/products/ai-machine-learning/how-20th-century-fox-uses-ml-to-predict-a-movie-audience)

Fox's software works to predict an *audience*, with clear implications for "testing" likely outcomes for certain types of films, which studios can use to market existing movies more effectively, and guide writers and directors toward making more commercially appealing stories. But can machines generate the stories themselves? Not yet - but this is not far off.

For a challenge, filmmaker [Oscar Sharp](http://www.thereforefilms.com/oscar-sharp.html) and creative technologist [Ross Goodwin](https://rossgoodwin.com/) used a neural network to create a screenplay. They created an [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) recurrent neural network called Benjamin. They trained Benjamin with science fiction screenplays and prompted it with data from a science fiction filmmaking contest. Benjamin produced a screenplay, and Sharp and Goodwin, with a cast and crew, made [a film, Sunspring](https://www.youtube.com/watch?v=LY7x2Ihqjmc) from the screenplay with impressive and interesting results.

Clearly, Benjamin is not ready for commercial film, but the resulting film is surprisingly coherent (acknowledging that human minds will go a long way to find order in chaos).

Still, it's clear there are useful applications of machine learning in entertainment, and we expect these products to improve, with interesting results.