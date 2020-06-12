---
author: Kathryn
author_link: https://twitter.com/HumeKathryn
date: "2016-12-08T17:22:58Z"
preview_image: http://68.media.tumblr.com/a97d30b7577d5fb32955853cb2ec7b17/tumblr_inline_ohvie7chq81ta78fg_540.png
redirect_from:
- /post/154210577998/dimensionality-reduction-and-intuition
tags:
- data science
- dimensionality
- data visualization
- t-sne
title: Dimensionality Reduction and Intuition
---

<figure data-orig-width="651" data-orig-height="513" class="tmblr-full"><img src="http://68.media.tumblr.com/a97d30b7577d5fb32955853cb2ec7b17/tumblr_inline_ohvie7chq81ta78fg_540.png" alt="image" data-orig-width="651" data-orig-height="513"/></figure>

> “I call our world Flatland, not because we call it so, but to make its nature clearer to you, my happy readers, who are privileged to live in Space."

<p>So reads the first sentence of Edwin Abbott Abbott’s 1884 work of science fiction and social satire, <i><a href="http://www.gutenberg.org/ebooks/201">Flatland: A Romance of Many Dimensions</a>.</i> At the time, Abbott used contemporary developments in the fields of geometry and topology (he was a contemporary of <a href="https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9">Poincaré</a>) to illustrate the rigid social hierarchies in Victorian England. A century later, with machine learning algorithms playing an increasingly prominent role in our daily lives, Abbott’s play on the conceptual leaps required to cross dimensions is relevant again. This time, however, the dimensionality shifts lie not between two human social classes, but between the domains of human reasoning and intuition and machine reasoning and computation.</p>

<p>Much of the recent excitement around artificial intelligence stems from the fact that computers are newly able to process data historically too complex to analyze. At Fast Forward Labs, we’ve been excited by new capabilities to use computers to <a href="http://pictograph.us">perceive objects in images</a>, extract the <a href="http://fastforwardlabs.github.io/brief/">most important sentences from long bodies of text</a>, and <a href="https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html">translate between languages</a>. But making complex data like images or text tractable for machines involves representing the data in high-dimensional vectors, long strings of numbers that encode the complexity of pixel clusters or relationships between words. The problem is these vectors become so large that it’s hard for humans to make sense of them: plotting them often requires a space of way more than the three dimensions we live in and perceive!</p><p>On the other hand, machine learning techniques that entirely remove humans from the loop, like <a href="http://www.automl.org/">automatic machine learning</a> and unsupervised learning, are still active areas of research. For now, machines perform best when nudged by humans. And that means we need a way to reverse engineer the high-dimensionality vectors machines compute in back down to the two and three dimensional spaces our visual systems have evolved to make sense of. </p><p>What follows is a brief survey of some tools available to reduce and visualize high-dimensional data. Send us a note at contact@fastforwardlabs.com if you know of others!</p><!--more-->


## Google’s Embedding Projector

<p>Yesterday, <a href="https://research.googleblog.com/2016/12/open-sourcing-embedding-projector-tool.html">Google open-sourced the Embedding Projector</a>, a web application for interactive visualization and analysis of high-dimensional data that is part of TensorFlow. The release highlights how the tool helps researchers navigate embeddings, or mathematical vector representations of data, which have proved useful for tasks like natural language processing. A popular example is to use embeddings <a href="https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/">to do “algebra” on words</a>, using the space between vectors as a proxy for semantic relationships like man:king::woman:queen. Embedding Projector includes a few dimensionality reduction techniques like Principal Component Analysis (<a href="https://en.wikipedia.org/wiki/Principal_component_analysis">PCA</a>) and t-SNE. Here’s an example of <a href="http://colah.github.io/posts/2014-10-Visualizing-MNIST/">using PCA on an image data set</a> (done before Google’s release).</p>

## t-SNE

<p><a href="https://en.wikipedia.org/wiki/Principal_component_analysis">t-Distributed Stochastic Neighbor Embedding</a> (t-SNE) is an increasingly popular non-linear dimensionality reduction technique useful for exploring local neighborhoods and finding clusters in data. As explained in <a href="http://distill.pub/2016/misread-tsne/">this post</a>, t-SNE algorithms adapt transformations to the structure of the input data they work on, and have a tuneable parameter called “perplexity” that “says (loosely) how to balance attention between local and global aspects of your data.” While the algorithms are powerful, their output representations must be read with care, as the perplexity parameter can create confusion. </p>

<img src="http://68.media.tumblr.com/9bed69a591a4f9f0796c5c312b2ec153/tumblr_inline_ohvl8uuV2H1ta78fg_540.png" alt="image" data-orig-width="1019" data-orig-height="258"/>

##### <a href="http://distill.pub/2016/misread-tsne/">Visualization</a> of how distance between clusters vary widely under different parameters on a t-SNE algorithm.

<p><a href="https://twitter.com/mtyka">Mike Tyka</a>, a machine learning artist, <a href="http://procedural-generation.tumblr.com/post/151619819088/mike-tyka-alt-ai-mike-tyka-has-been-working">has used t-SNE</a> to cluster images per similarity in Deep Dream’s neural network architecture. The resulting “map” reveals some interesting conclusions, showing, for example, that Deep Dream clusters violins near trombones. As the shapes of these two instruments differ to our eyes, their proximity in the neural network space may mean that Deep Dream uses the context of “people playing instruments” as a discriminatory feature for classification. </p>

## Topological Data Analysis

<p>Palo Alto-based <a href="https://www.ayasdi.com/">Ayasdi</a> uses theory from <a href="https://en.wikipedia.org/wiki/Topology">topology</a>, the study of geometrical properties that stay constant even when shapes are transformed, to help humans find patterns in large data sets. As CEO Gurjeet Singh explains in <a href="https://www.ayasdi.com/blog/compute/future_of_machine_intelligence/">this O’Reilly interview</a>, the two key benefits of using topology for machine learning are:</p><ul><li>The ability to combine results from different machine learning algorithms, while still maintaining guarantees about the underlying shapes or distributions</li><li>The ability to discover the underlying shape of data so you don’t assume it and, thereby, impact the parameters for an optimization problem</li></ul><p>Ayasdi’s product visualizes relationships in data as graphs, enabling users to visually perceive relationships that would be hard to uncover in the language of formal equations. We love the parallel insight that we, as humans, excel at what topologists call “deformation invariance,” the property that the letter A is still the letter A in different fonts. </p>

<img src="http://68.media.tumblr.com/13ece3e2298273b9ce09f11dd0538eb0/tumblr_inline_ohvmg3IZtG1ta78fg_540.png" alt="image" data-orig-width="572" data-orig-height="136"/>

##### Machines using an autoencoder to reconstruct digits with moderate deformation invariance, as we explained in <a href="http://blog.fastforwardlabs.com/2016/08/12/introducing-variational-autoencoders-in-prose-and.html">this blog post</a>.

## Data Visualization for the 3-D Web

<p>Finally, <a href="http://datavized.com/">Datavized</a> is working on a data analytics tool fit for the 3-D web. While they’ve yet to work on dimensionality reduction, they have embarked on projects to give consumers of data a more empathic, first-person interpretation of statistics and conclusions. We look forward to the release of their product in 2017!</p>

## Conclusion

<p>Our ability to represent rich, complex data, like images and text, in numbers required for mathematical functions on computers requires a Mephistophelean deal with the devil. These high-dimensional vectors are impossible to understand and interpret. But there’s been great progress in dimensionality reduction and visualization tools that enable us, in our Flatland, to make sense of the strange, cold world of machine intelligence. </p><p>- Kathryn</p>
