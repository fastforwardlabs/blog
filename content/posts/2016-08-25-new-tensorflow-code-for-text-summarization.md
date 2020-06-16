---
date: "2016-08-25T17:24:14Z"
preview_image: http://68.media.tumblr.com/ecc5db59efcfa474331c6a1d2ec84824/tumblr_inline_och5k95kSe1ta78fg_540.png
redirect_from:
- /post/149468760123/new-tensorflow-code-for-text-summarization
tags:
- natural language processing
- recurrent neural network
- deep learning
- summarization
title: New TensorFlow Code for Text Summarization
aliases:
  - /2016/08/25/new-tensorflow-code-for-text-summarization.html
---

<figure class="tmblr-full" data-orig-height="249" data-orig-width="529"><img src="http://68.media.tumblr.com/ecc5db59efcfa474331c6a1d2ec84824/tumblr_inline_och5k95kSe1ta78fg_540.png" data-orig-height="249" data-orig-width="529"/></figure><p>Yesterday, <a href="https://research.googleblog.com/2016/08/text-summarization-with-tensorflow.html">Google released</a> new TensorFlow <a href="https://github.com/tensorflow/models/tree/master/textsum">model code</a> for text summarization, specifically for generating news headlines on the Annotated English Gigaword dataset. We’re excited to see others working on summarization, as <a href="http://blog.fastforwardlabs.com/2016/04/11/new-tools-to-summarize-text.html">we did in our last report</a>: our ability to “digest large amounts of information in a compressed form” will only become more important as unstructured information grows. </p><p>The TensorFlow release uses <a href="http://arxiv.org/abs/1409.3215">sequence-to-sequence learning</a> to train models that write headlines for news articles. Interestingly, the models output abstractive - not extractive - summaries. Extractive summarization involves weighing words/sentences in a document according to some metric, and then selecting those words/sentences with high scores as proxies for the important content in a document. Abstractive summarization looks more like a human-written summary: inputting a document and outputting the points in one’s own words. It’s a hard problem to solve. </p><p>Like the <a href="https://github.com/facebook/NAMAS">Facebook NAMAS model</a>, the TensorFlow code works well on relatively short input data (100 words for Facebook; the first few sentences of an article for Google), but struggles to achieve strong results on longer, more complicated text. We faced similar challenges when we built <a href="http://fastforwardlabs.github.io/brief/">Brief</a> (our summarization prototype) and decided to opt for extractive summaries to provide meaningful results on long-form articles like those in the New Yorker or the n+1. We anticipate quick progress on abstractive summarization this year, given <a href="http://arxiv.org/abs/1509.00685">progress with recurrent neural nets</a> and this new release. </p><p>If you’d like to learn more about summarization, contact us (contact@fastforwardlabs.com) to discuss our research report &amp; prototype or come hear <a href="http://conferences.oreilly.com/strata/hadoop-big-data-ny/public/schedule/speaker/203745">Mike Williams’ talk</a> at Strata September 28! </p>
