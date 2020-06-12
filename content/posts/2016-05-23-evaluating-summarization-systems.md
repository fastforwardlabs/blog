---
author: Mohamed AlTantawy, Agolo
author_link: http://www.agolo.com/
date: "2016-05-23T17:09:13Z"
post_type: Guest Post
preview_image: http://68.media.tumblr.com/d879f22c1b7be3467b606c8aa8f7cfb6/tumblr_inline_o7n3a6bf5R1ta78fg_540.jpg
redirect_from:
- /post/144813278933/evaluating-summarization-systems
tags:
- whitepaper
- language processing
- summarization
- webinar
title: Evaluating Summarization Systems
---

<figure data-orig-width="1300" data-orig-height="863" class="tmblr-full"><img src="http://68.media.tumblr.com/d879f22c1b7be3467b606c8aa8f7cfb6/tumblr_inline_o7n3a6bf5R1ta78fg_540.jpg" alt="image" data-orig-width="1300" data-orig-height="863"/></figure>

##### We’re excited for tomorrow’s online discussion about automatic text summarization! You can <a href="https://textsummarizationwebinar.splashthat.com/">register here</a>.

##### During the event, Mohamed AlTantawy, CTO of <a href="http://www.agolo.com">Agolo</a>, will explain the tech behind their summarization tool. In this blog post, he describes how his team evaluates the quality of summaries produced by their system. Join us tomorrow to learn more and ask questions about the approach!

<p>Evaluating the quality of algorithmically created summaries is a very hard task. There are two main approaches to evaluating summaries: automatic and manual. While both approaches need human input, the automatic approach only needs human effort to build the reference summaries. Once we have the reference or gold standard summaries, there are metrics that can automatically determine the quality of the generated summaries by comparing them to the human created references. Automatic evaluation of summaries has been an active area of research for a long time and it is still far from being solved.<br/></p><p>At <a href="http://www.agolo.com">Agolo</a>, we are always tuning and improving our summarization engines. Without a systematic approach for evaluating our work, it would be impossible to measure our progress. In this blog post, will focus on the methods we use to evaluate our multi-document news summarizer. Some of the automatic evaluation methods discussed below do not lend themselves to evaluating some of our other systems, such as our engine for summarizing long-format reports or our domain-specific summarizers. This is due to the lack of a human-created gold standard. The widely different formats (and sometimes genres) of documents makes it hard to evaluate different summarization tasks on the same standard. For example, most of the highly adopted <a href="http://duc.nist.gov/">Document Understanding Conference (DUC)</a> datasets are newswire documents which make it unfit to evaluate the summaries of SEC filings. In these cases, we opt to use human evaluations with the goal of understanding and learning new evaluation methods to fully automate them.  </p>

### Rouge

<p><b></b></p><p>Since <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=cDF07aYAAAAJ&amp;citation_for_view=cDF07aYAAAAJ:u5HHmVD_uO8C">being introduced by Chin-Yew Ling in 2004</a>, Rouge has become the de facto metric for automatic summarization evaluation. Rouge stands for Recall-Oriented Understudy of Gisting Evaluation. It is a recall-based metric to automatically determine the quality of an algorithmically generated summary by comparing it to other gold-standard summaries created by humans. This metric measures content overlap between two summaries which means that the distance between two summaries can be established as a function of their vocabulary and how this vocabulary is used.</p><p>Rouge has a couple of limitations:</p><ul><li>To use Rouge, one has to use reference summaries that typically involve expensive human effort. Moreover, selecting content to serve as summaries is not a deterministic problem. Human inter-agreement is low when it comes to choosing sentences that best represent a document, let alone a group of documents. <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=cDF07aYAAAAJ&amp;citation_for_view=cDF07aYAAAAJ:eQOLeE2rZwMC">Lin and Hovy investigated</a> the DUC 2001 human assessment data and found that humans expressed agreement about 82% of the time in 5,921 total judgments on the single document summarization evaluation task.  <br/></li><li>Semantic equivalence is another problem. Two sentences may express the same meaning using different words. Such scenarios will be harshly penalized by Rouge. <a href="http://research.microsoft.com/apps/pubs/default.aspx?id=69253">ParaEval is another approach</a> to automatically evaluating summaries using paraphrases. <br/></li></ul>

### Readability

<p>Our summarization engines are mostly extractive. However, in many cases, we change the original sentences to make the summaries more readable. For example, coreference resolution is often used to replace pronouns and other references with their original entities, for example, the <a href="http://br.advfn.com/noticias/DJN/2016/artigo/70059200">following sentence</a>:<b><br/></b></p>

> “**The market** is maturing,” and opening retail stores in India helps “form the building blocks” for the firm in the country, **he** said.

<p>would change to:</p>

> “**India's smartphone market** is maturing,” and opening retail stores in India helps “form the building blocks” for the firm in the country, **Rushabh Doshi** said.

<p>As a result, we want to ensure that the modified sentence will not affect the readability of the summaries. The <a href="https://en.wikipedia.org/wiki/Gunning_fog_index">Gunning Fox Index</a> measures the readability of English writing. The index estimates the years of formal education needed to understand the text on a first reading. It is a linear equation of the average sentence length and percentage of complex words whose scale provides an estimate of grade level. Complex words are defined as words with three or more syllables. Text with a Fog Index value over 18 is generally considered unreadable.  </p><blockquote><p>Fog Index = 0.4 (average number of words per sentence + percent of complex words)</p></blockquote><p>For the purpose of this task, we are not interested in the absolute values of the Fox Index, but rather in the relative score of the modified text when compared to the original text. We ensure that that the difference in readability score between the original text and the modified text remains within a 10% scale. This method will become useful as we move from extractive to abstractive summaries.<br/></p>

### Speed and Complexity

<p>The speed of the summarization engine is another aspect that we continuously evaluate. As the amounts of text we summarize daily grows, we have to make to make sure that our engines will work efficiently and scale with big volume of data.<b><br/></b></p><p>Our summarization algorithm transforms the input text into high-dimensional sparse vectors, which can be efficiently analyzed in linear time O(n) to produce the final summaries. The theoretical analysis is borne out in our performance logs, which shows the processing time increasing linearly with respect to the size of the input documents. For examples, summarizing a little more than 7,500 words (7 news articles), takes less than half a second.<br/></p><figure data-orig-width="631" data-orig-height="302" class="tmblr-full"><img src="http://68.media.tumblr.com/b6ea78c28562d76d90e4da0165765860/tumblr_inline_o7n30giZIm1ta78fg_540.png" alt="image" data-orig-width="631" data-orig-height="302"/></figure><p>- Mohamed AlTantawy, Agolo</p>
