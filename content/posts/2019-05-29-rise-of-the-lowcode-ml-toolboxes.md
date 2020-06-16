---
author: Justin
author_link: https://twitter.com/JustinJDN
date: "2019-05-29T00:00:00Z"
feature: false
post_type: newsletter
preview_image: /images/2019/05/markus_spiske_109588_unsplash-1556815976857.jpg
published: true
title: Rise of the Low-Code ML toolboxes
aliases:
  - /2019/05/29/rise-of-the-lowcode-ml-toolboxes.html
---

We've written previously about the rapid growth and adoption of ML tools in the [AutoML](https://blog.fastforwardlabs.com/2017/11/30/the-promise-of-automated-machine-learning-automl.html) family.  Specifically, we broke down AutoML into 4 categories:

* Citizen Data Science / ML
* Efficient Data Science / ML
* Learning to Learn
* Transfer Learning

Advancement has been especially rapid in tools designed to make Data Science/ML more efficient, and in learning to automate/optimize model architecture design.  While these frameworks and tools have continued to mature, their prominence has unveiled another set of challenges.  Even when using automation, building out useful, semi-custom deep learning models takes a lot of code!  Popular libraries like TensorFlow and Pytorch offer incredible power in that data scientists (who also happen to be experienced software developers) have the ability to tailor model architectures granularly to fit specific use cases.  However, all of that power comes at a cost, and that cost can include hundreds of lines of code--and all of the technical debt that comes with it.  Add in the need to programmatically implement many iterations of experiments, and one could easily end up maintaining a highly complex codebase simply to train, test, and experiment with a single deep learning model.

![](/images/2019/05/markus_spiske_109588_unsplash-1556815976857.jpg)
##### Photo by [Markus Spiske](https://unsplash.com/photos/xekxE_VR0Ec?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/code?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

To address this challenge, a new genre of ML capabilities has surfaced, pioneered by what we like to call 'Low-Code ML Toolboxes.' Projects like the Allen Institute's [AllenNLP](https://allennlp.org/tutorials), [fast.ai](https://www.fast.ai/) and Uber's [Ludwig] (https://uber.github.io/ludwig/) seek to abstract much of the programming complexity inherent to building deep learning models, while preserving the above-mentioned power of libraries such as Pytorch and TensorFlow.  These toolboxes are not limited to AutoML applications. As a result, they address codebase management challenges for many types of ML projects. 

These projects advertise themselves as a way to make deep learning much easier to accomplish and more accessible to the masses, and while this is technically true, it's important to point out that in this case we aren't talking about GUI-based approaches to ML/DL such as [Lobe](https://lobe.ai/), [KNIME](https://www.knime.com/) or even building lambda function-based models.  Instead, tools in this category seek to holistically reduce the programming load of data scientists by providing higher level text-based interface with which to specify a model's configuration.  

Both Ludwig and AllenNLP leverage the JSON format as a way to allow for custom configuration of a model architecture/approach, while still enforcing a standard structure, which is needed in order to provide abstraction.  Ludwig offers YAML as the primary user interface, which is then used to generate JSON model specifications.  AllenNLP uses jsonnet for the same purpose.  Ludwig does also feature a programmatic [API](https://uber.github.io/ludwig/api/), and many of AllenNLP's core capabilities can easily be integrated/extended to existing software projects.

Fast.ai takes a different approach, relying heavily still on its users to develop models directly in Python.  However, through both the library's built in functions, as well as the project's well documented DS practices, management of the codebase supporting a model is much simpler.

These projects are also showing high levels of adoption with the older AllenNLP [Github](https://github.com/allenai/allennlp) boasting over 100 contributors and 6,000 stars.  Ludwig, though only recently released, has nearly 4,500 stars at the time of this article and has strong support within Uber's extended AI community.  Because fast.ai is also paired with a human learning course, it also boasts a large community (over 13,000 stars and hundreds of contributors).

### Why low-code?

Increasing Data Scientist productivity is the primary benefit of low-code ML tools, but not the only one.  In addition to making it faster to experiment, these tools also seek to provide a repeatable and structured way to capture experiment results as well.  Both toolchains automatically log the details of each training run into a pre-specified directory/file hierarchy.  Once one is comfortable with this structure it's easy to pinpoint key moments in the experimentation process for further analysis or configuration.

In addition, since these low-code toolboxes are essentially built on top of well-maintained deep learning libraries (PyTorch and Tensorflow), it's easy to take advantage of other adjacent capabilities like [TensorBoard](https://github.com/tensorflow/tensorboard) to visualize/inspect models. 

### Possible Pitfalls

As discussed above, the developers of low-code ML tools make a lot of assumptions about how these tools will be used.  These assumptions are wide ranging, due to the level of abstraction provided.  One of the most important assumptions concerns how input data will be structured and preprocessed.  For example, Ludwig's standard toolchain expects data to be formatted into CSV, and currently only supports a limited number of datatypes and preprocessing functions.  While it is of course possible to extend the supported datatypes and preprocessing steps, you will need to write some code to do so.  Users who lack this skillset or become complacent during the experiment design process might run into trouble here.  

A primary component of many modern deep learning approaches is transfer learning (TL).  The benefits of this technique are plentiful and [well-documented](https://blog.fastforwardlabs.com/2018/08/29/breakthroughs-in-transfer-learning-for-nlp.html).  However, there is an inherent tradeoff to employing TL: it's sometimes impossible to know exactly on what and how someone else's model was trained, and thus very difficult to be sure if that model (or any derivative models) are fair, without inspection. Though the lack of automatic in-depth fairness analysis is not unique to the low-code toolboxes we are exploring, it's worth noting that just because experimentation and training processes are easier, one shouldn't assume the outputs are fair.

### Parting thoughts

There are *still* no tools which replace a solid conceptual foundation in ML and software development. However, for experienced practitioners, low-code toolboxes can help make the data science process much easier and faster.