---
author: Seth
author_link: https://twitter.com/shendrickson16
date: "2018-09-28T00:00:00Z"
feature: false
post_type: newsletter
preview_image: /images/editor_uploads/2018-09-19-194511-XOnSpark.png
published: true
title: Apache Spark gets a machine learning makeover
aliases:
  - /2018/09/28/apache-spark-gets-a-machine-learning-makeover.html
---

### Machine learning on Spark: an abridged history

[Apache Spark](https://spark.apache.org/) - the cluster computing framework 
that's been throwing shade at MapReduce since 2011 - has always been a bit 
remarkable, because it bridged the divide between data engineering and data 
science. One of the great promises of Spark was that it would be easy, 
trivial almost, to scale machine learning and data science to arbitrarily 
large data. Seven years later, Spark has made its place in data science, but 
perhaps not in the way we originally hoped.

Spark's big contribution was that it delivered a very elegant API for dealing 
with distributed collections of data, termed _Resilient Distributed Datasets_ 
(RDDs). Compared to alternatives at the time, it was simple to use that API 
to write certain machine learning algorithms, and since those algorithms were 
built on RDDs; you got fault tolerance and scale for free. It wasn't long 
until a machine learning library built on RDDs was born: [MLlib](https://spark.apache.org/docs/latest/ml-guide.html). 

Implementing performant, scalable machine learning algorithms in MLlib wasn't 
*quite* as easy as just expressing the logic using RDD transformations, but in 
some cases it worked quite well. Spark, and by extension MLlib, work well 
when algorithms can be expressed in parallel, independent tasks that each 
work on independent chunks of data. Accordingly, MLlib has seen success and 
adoption with linear models, K-means clustering, decision trees, and some 
others. But some algorithms, most notably deep learning, are difficult to 
express using Spark. 

In comparison to linear models, optimizing deep learning algorithms over 
distributed collections requires frequent communication between tasks. 
Further, deep learning is _slow_, if you don't use a framework that has been 
heavily optimized for that exact use case. Tensorflow, PyTorch, MXNet, etc. 
all leverage accelerated hardware and heavily optimized C/C++ code to achieve 
reasonable efficiency. All this is to say that Spark and deep learning aren't 
a very good match.  So why are we talking about it?

Deep learning needs data (big data!) and that data often needs to be accessed 
through or pre-processed by Spark. That data is also messy and is probably 
stored across many datasets in many different storage platforms. Spark makes 
reading, aggregating, and joining these datasets less awful. So even if Spark 
isn't heavily optimized for machine learning, the data that feeds these 
algorithms often goes through Spark first. This reality led many developers 
to ponder, "what if we could combine the heavily optimized ML/DL frameworks 
into Spark?" And with that, the family of XOnSpark libraries came to be.

![](/images/editor_uploads/2018-09-19-194511-XOnSpark.png)

But Spark hasn't made it very easy to combine these other libraries, most of 
which are written in a combination of Python and C++, with Spark. There are
three main shortcomings:

* Moving data between Spark processes (JVM) and Python processes is inefficient
* Spark task scheduling doesn't take GPUs into account
* Deep learning tasks need to constantly communicate gradient/weight updates between them, which is a Spark anti-pattern

### Project Hydrogen makes Spark play nice with other ML frameworks

To address each of these issues, the open source community for Spark is 
undertaking a new initiative, dubbed _Project Hydrogen_, which is 
broken up into three main chunks, each designed to solve one of these 
shortcomings:

* [Barrier scheduling](https://issues.apache.org/jira/browse/SPARK-24374)
* [Accelerator aware scheduling](https://issues.apache.org/jira/browse/SPARK-24615)
* [Data interchange using Apache Arrow](https://issues.apache.org/jira/browse/SPARK-24579)

The goal of Project Hydrogen is to make it easy and efficient to build deep learning workflows that can run end to end in Spark. This is exciting!

Spark and deep learning can't ignore each other, and that probably won't 
change any time soon. Because of the current complexities, it's best to avoid 
distributing deep learning training when possible. But we're excited to 
see investment into scaling deep learning with Spark. There are so many great 
libraries for doing heavily optimized machine learning - PyTorch, Tensorflow, 
XGBoost, LightGBM - that it's hugely beneficial to be able to scale these 
up with Spark.