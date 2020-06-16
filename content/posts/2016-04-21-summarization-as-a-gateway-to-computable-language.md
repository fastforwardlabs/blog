---
date: "2016-04-21T19:38:37Z"
feature: true
preview_image: http://68.media.tumblr.com/981136c87557be0df4c1d09c3b4ed8b2/tumblr_inline_o600ygq2OG1qcg73w_540.png
redirect_from:
- /post/143177754283/summarization-as-a-gateway-to-computable-language
tags:
- summarization
- product
- language processing
title: Summarization as a Gateway to Computable Language
aliases:
  - /2016/04/21/summarization-as-a-gateway-to-computable-language.html
---

<p>Analyzing unstructured text data such as news, emails, chats, narrative prose, legal documents, or transcribed speech is an extremely tough problem. Thanks to massive leaps in data engineering, we can just about store and retrieve this torrent of information. But we can&rsquo;t yet conduct the kind of rich and fast analyses that we take for granted with structured, quantitative data.</p>

<p>Our newly released <a href="http://blog.fastforwardlabs.com/2016/04/11/new-tools-to-summarize-text.html">summarization report</a> is a response to this problem in two senses.</p>

<figure data-orig-width="1125" data-orig-height="533" class="tmblr-full"><img src="http://68.media.tumblr.com/af5b628fd8b2a1c2f8c6676f0211d362/tumblr_inline_o600vklwhN1qcg73w_540.png" data-orig-width="1125" data-orig-height="533"/></figure>

##### Summaries make documents more manageable

<p>The first is the more obvious: by definition, summarization makes documents shorter and more manageable while retaining meaning. If you want to learn how to build automatically generated extractive summaries in your product, then the specific algorithms and prototypes we describe will definitely be interesting.</p>

<p>Summarization algorithms therefore have embedded within them a key component of one of the most fundamental problems in machine intelligence: how to extract and process the meaning of human language.</p>

<p>But the second way summarization is relevant to the problem of analyzing unstructured text is more general and, we think, more significant.</p>

<p>To automatically summarize text, a necessary first step is to vectorize it. That is, to rewrite it as a sequence of numbers that a computer can operate on. There are lots of ways to do this. The best (such as topic models or neural-network-based language embeddings such as skip-thoughts) are more than just counts of words. They do a good job of retaining the semantic meaning of the document in a way that is accessible to computers. We talk about them more in the report.</p>

<p>Done well, vectorization allows the subsequent steps of a summarization algorithm to find the key ideas in a document, which it can use to generate a summary. But vectorization is also the first step for the countless other tasks that, like summarization, implicitly involve the computer working with the meaning of a document.</p>

<figure class="tmblr-full" data-orig-height="776" data-orig-width="1125"><img src="http://68.media.tumblr.com/981136c87557be0df4c1d09c3b4ed8b2/tumblr_inline_o600ygq2OG1qcg73w_540.png" data-orig-height="776" data-orig-width="1125"/></figure>

##### The technologies we use to summarize documents have many other potential uses

<p>We&rsquo;re really excited about the summarization algorithms and prototypes we describe in the report, which are great solutions to a valuable specific task. But we&rsquo;re perhaps even more excited about the way in which they point to better approaches to simplification, translation, semantic search, document clustering, image caption generation, and even speech recognition.  In that sense, they open a gateway to a future in which machine intelligence can truly understand human language.</p>
