---
title: "Evaluating QA: Metrics, Predictions, and the Null Response"
date: 2020-06-16T09:29:59
author: Melanie
author_link: https://www.linkedin.com/in/melanierbeck
preview_image: /images/hugo/shotwin-2020-06-16_09-31-48-1592314597.png
post_type: Notebook
external_url: https://qa.fastforwardlabs.com/no%20answer/null%20threshold/bert/distilbert/exact%20match/f1/robust%20predictions/2020/06/09/Evaluating_BERT_on_SQuAD.html
aliases:
  - /2020/06/16/evaluating-qa-metrics-predictions-and-the-null-response.html
---

A deep dive into computing QA predictions and when to tell BERT to zip it! In our last post, Building a QA System with BERT on Wikipedia, we used the HuggingFace framework to train BERT on the SQuAD2.0 dataset and built a simple QA system on top of the Wikipedia search engine. This time, we'll look at how to assess the quality of a BERT-like model for Question Answering.
