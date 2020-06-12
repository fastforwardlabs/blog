---
author: Mike
author_link: http://twitter.com/mikepqr
date: "2017-10-02T20:00:00Z"
feature: true
preview_image: /images/2017/09/ff05.gif
published: true
title: 'Probabilistic programming: an annotated bibliography'
---

Earlier this year we launched a research report on [probabilistic
programming](http://blog.fastforwardlabs.com/2017/01/18/new-research-on-probabilistic-programming.html),
an emerging programming paradigm that makes it easier to describe and train
probabilistic models. The Bayesian probabilistic approach to model building and
inference has [many advantages in practical data
science](http://blog.fastforwardlabs.com/2017/01/30/the-algorithms-behind-probabilistic-programming.html),
including the ability to quantify risk (a superpower in industries like finance
and insurance) and the ability to insert institutional knowledge (which is
particularly useful when data is scarce). The rise of probabilistic programming
languages has made it a more practical technique for time-constrained working
data scientists.

![](/images/2017/09/ff05.gif)

If that sounds great to you, and you're looking to learn more, the first thing
you can do is — [work with us](https://www.cloudera.com/about/services-and-support/fast-forward-labs.html
)! We'll
be glad to discuss our report, relevant use cases in your industry,
and next steps to incorporate this approach into your data science work. 

But you might also enjoy this list of our favorite resources for learning how
to do Bayesian inference and build probabilistic programming systems. These are
the books, papers and tutorials we found most useful when conducting our
research.

### Practical books

If you're just starting out then we recommend either [Doing Bayesian Data
Analysis](https://sites.google.com/site/doingbayesiandataanalysis/) by John
Kruschke, or [Probabilistic Programming and Bayesian Methods for
Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
by Cameron Davidson-Pilon. 

Krushke's book uses R and Stan (and a language
called JAGS, that is really only used for teaching these days). Davidson-Pilon
uses Python and PyMC. Choose between these books based on your language
preferences. If you don't have a language preference, we at Fast Forward Labs
recommend Davidson-Pilon's book, which is available online, and in particular
[the PyMC3
edition](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers#pymc3)
(there are some important differences between PyMC3 and previous versions).

### Theoretical books

The practical books above cover the basics of the theoretical and mathematical
side, but if you'd like a deeper dive into why we do what we do, we recommend
[Data Analysis: A Bayesian
Tutorial](https://global.oup.com/academic/product/data-analysis-9780198568322?cc=us&lang=en&)
by Sivia and Skilling. It's a relatively short and extremely clear book. For an
even shorter introduction, we love [Brendon Brewer's lecture notes for STATS
331](https://www.stat.auckland.ac.nz/~brewer/stats331.pdf).

If your background is in economics or life sciences, you may prefer [Data
Analysis Using Regression and Multilevel/Hierarchical
Models](http://www.stat.columbia.edu/~gelman/arm/) by Gelman and Hill. If your
background is in physics or engineering, you may prefer [Principals of Data
Analysis](http://www.physik.uzh.ch/~psaha/pda/) by Prasenjit Saha (which is
available free online).

### Research

If you'd like a reading list of research papers, there is no better place to
start than the _excellent_ [annotated
bibliography](https://psyarxiv.com/ph6sw/) published last year by Alexander Etz
and colleagues. Their notes place the research in a historical and conceptual
context, so this is in a sense the _least_ technical document in this list. But
the papers they discuss are academic research, so you'll be grappling with some
big ideas, including our favorite

> The probability that a person is dead (i.e., data) given that a shark has
> bitten the person’s head off (i.e., theory) is 1. However, given that a
> person is dead, the probability that a shark has bitten this person’s head
> off is very close to zero".

If you're interested in the algorithmic and computational cutting edge
(Hamiltonian Monte Carlo, variational methods, etc.) then we have [a blog post
that links to a selection of important
papers](http://blog.fastforwardlabs.com/2017/01/30/the-algorithms-behind-probabilistic-programming.html).

### Tutorials and articles

Finally, here are a selection of shorter and/or use-case specific practical
articles we've found interesting and useful:

 - [Bayesian Survival Analysis in Python with
   PyMC3](http://austinrochford.com/posts/2015-10-05-bayes-survival.html), and
   indeed any of the [posts on Austin Rochford's
   blog](http://austinrochford.com/posts.html)
 - [Parameter estimation for text
   analysis](http://www.arbylon.net/publications/text-est.pdf) by Gregor
   Heinrich, which is first and foremost a great topic modeling tutorial, but
   almost accidentally a great introduction to Bayesian inference.
 - [Data analysis recipes: Fitting a model to
   data](https://arxiv.org/abs/1008.4686) by Hogg, Bovy and Lang, a deep
   article about an extremely simple problem (linear regression) that somehow
   also manages to be funny!