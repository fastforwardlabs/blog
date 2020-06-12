---
author: Ryan
author_link: https://twitter.com/micallefjd
date: "2019-12-24T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2019-11-05-200808-WikipediaLanguages.png
published: false
title: Bringing Information to Speakers of Less-common Languages
---

NLP has made major strides forward in the last year or two, and still has a lot of momentum. Now we're starting to see this research applied to universal translation that can reach broad audiences, including speakers of less-common languages.

![](/images/editor_uploads/2019-11-05-200808-WikipediaLanguages.png)

##### Wikipedia has content in many languages, but the content available in most languages is several orders of magnitude smaller than the most common languages.

New [pre-trained models](https://www.analyticsvidhya.com/blog/2019/03/pretrained-models-get-started-nlp/) are being released frequently, as well as improved versions of older models - including [smaller versions](https://medium.com/syncedreview/googles-albert-is-a-leaner-bert-achieves-sota-on-3-nlp-benchmarks-f64466dd583) suitable for mobile devices and high-performance applications.

These models are uniformly trained to work primarily or exclusively with text in English and a few other common languages like French, Spanish, or Chinese. These models are broadly useful for tasks *within* these popular languages. But they're *only* useful for single-language tasks in those languages. To bring text information to more of the world's population, though, we need translation models, which of course cover more than one language. 

There are a number of *bilingual* models trained to translate between two (usually popular) languages. This bilingual approach to inclusivity has two big problems. 

* First, to be able to share information *from* any language *to* any language we would need to include bilingual models for every language pair. The number of bilingual models necessary to translate among each language grows quickly. For example, to translate from and to any of one hundred languages we would need 4,950 bilingual models. Managing the training and deployment of thousands of models is a substantial pain.

* Second, models addressing less-common languages are more difficult to train. Less-common languages simply have less data with which to train. Training these models typically requires pairs of sentences in each language. Finding English-Spanish pairs is relatively straightforward compared to finding English-Estonian pairs - and finding Tamil-Basque pairs is even more daunting.

To address these problems, Google AI has released a [multilingual model](https://github.com/google-research/bert/blob/master/multilingual.md) trained on over a hundred languages, with more languages being added regularly. This is itself a great feat and important to speakers (well, writers) of less-common languages.

Part of what's interesting about this multilingual model is, of course, its scope, which makes model training and management simple. But the researchers also used some [clever techniques](https://arxiv.org/abs/1907.05019) to mitigate the lack of training data for the less-common languages. In building their model, they took pages from multi-task learning and transfer learning (both of which are techniques we have [studied here at Fast Forward Labs](https://clients.fastforwardlabs.com/)), and some creative strategies for amplifying the signal. The result is a model with solid performance on less-common resources without giving up much performance on more-common languages. And researchers at Google are [applying these techniques and others](https://arxiv.org/abs/1910.10683v2) to a higher quality set of training data that should improve performance in several NLP tasks, including translation.

These are great steps on the way to bringing ML to *everyone*, and we look forward to seeing what other techniques and data sources will help bring information to people who write in less-common languages.