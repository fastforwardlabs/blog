---
author: Nisha and Victor
author_link: http://www.linkedin.com/in/melanierbeck
date: "2020-02-05T00:00:00Z"
feature: true
post_type: Featured Post
preview_image: /images/2020/02/ill-13.png
published: true
title: Deep Learning for Anomaly Detection
---

*The full **Deep Learning for Anomaly Detection** report [is now available](https://ff12.fastforwardlabs.com).* 

*You can also catch a replay of the webinar we reference below on demand [here](https://www.cloudera.com/about/events/webinars/deep-learning-for-anomaly-detection.html?utm_medium=cldr-properties&utm_source=blog&keyplay=ml&utm_campaign=FY21-Q1_CW_AMER_Webinar_2020-02-13%0A&cid=7012H000001OYfQ).*

---


In recent years, we have seen an unprecedented increase in the availability of data in a variety of domains: manufacturing, health care, finance, IT, and others. Applications leverage this data to make informed decisions. This comes with its own set of challenges (and opportunities) when things start to fail; for instance, what happens when a piece of equipment fails or a network suffers from a security vulnerability? Companies may lose customers, or fixing things could take a while (which in turn adds to the costs). In short, everything from the organization's bottom line to its reputation are at stake.

But what if we had the ability to reliably detect or identify when something goes wrong? This is the premise of anomaly detection, and the subject of our latest report.

Given the importance of the anomaly detection task, multiple approaches have been proposed and rigorously studied over the last few decades. The underlying strategy for most approaches to anomaly detection is to first model normal behavior, and then exploit this knowledge in identifying deviations (anomalies). This approach typically falls under the semi-supervised category and is accomplished across two steps in the anomaly detection loop. 

The first step, which we can refer to as the training step, involves building a model of normal behavior using available data. Depending on the specific anomaly detection method, this training data may contain both normal and abnormal data points or only normal data points. Based on this model, an anomaly score is then assigned to each data point that represents a measure of deviation from normal behavior.

![](/images/2020/02/ill-13.png)
##### Figure 1: Training - Modeling normal behavior

The second step in the anomaly detection loop - the test step - introduces the concept of threshold-based anomaly tagging. Given the range of scores assigned by the model, we can select a threshold rule that drives the anomaly tagging process - e.g., scores above a given threshold are tagged as anomalies, while those below it are tagged as normal.

![](/images/2020/02/ill-14.png)
Figure 2: Testing - Threshold-based anomaly detection

As data becomes high dimensional, it is increasingly challenging to effectively teach a model to recognize normal behavior. This is where deep learning approaches step in. The approaches discussed in our upcoming report typically fall under the encoder-decoder family, where an encoder learns to generate an internal representation of the input data, and a decoder attempts to reconstruct the original input based on this internal representation. While the exact techniques for encoding and decoding vary across models, the overall benefit they offer is the ability to learn the distribution of normal input data and construct a measure of anomaly respectively.

The forthcoming report and prototype from Cloudera Fast Forward Labs explores various such deep learning approaches and their implications. While deep learning approaches can yield remarkable results on complex and high dimensional data, there are several factors that influence the choice of approach when building an anomaly detection application. In our report we survey various approaches, highlight their pros and cons, and discuss resources and recommendations for setting up anomaly detection in a production environment, as well as technical and ethical considerations.

Want to learn more? Join us on Thursday, February 13th at 10:00am PST (1:00pm EST) for a live webinar on “Deep Learning for Anomaly Detection.” Nisha Muktewar and Victor Dibia of Cloudera Fast Forward Labs will be joined by Meir Toledano, Algorithms Engineer at Anodot.