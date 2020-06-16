---
author: Ade
author_link: https://twitter.com/Adewunmi
date: "2019-06-26T00:00:00Z"
feature: false
post_type: newsletter
preview_image: /images/editor_uploads/2019-06-07-135738-helloquence_51716_unsplash.jpg
published: true
title: The trouble with unexplainable algorithms
aliases:
  - /2019/06/26/the-trouble-with-unexplainable-algorithms.html
---

Thanks to a mix of technology-driven disruption and savvy competitors, the business environment is an increasingly challenging one. Staying competitive requires a better understanding of customers’ behaviour and preferences. It also requires the ability to optimise internal processes to more efficiently support both these things. This is a big reason that so many organisations are investing in machine learning.

And yet the use of machine learning in organisations has not been universally welcomed by customers and service users. In fact, in some areas, there’s been a growing push back -- or ‘techlash,’ as it has been dubbed. People have expressed concern about a range of things: the breadth of data being collected and the [terms](https://www.nbcnews.com/tech/security/millions-people-uploaded-photos-ever-app-then-company-used-them-n1003371) of its use, as well as the types of decisions being recommended or made by the algorithms trained on this data. The sources of concern vary, but a lack of trust is the common denominator.

### The trust deficit
One corollary of this trust deficit is an increasingly adversarial relationship between organisations and their service users and customers. Lately, I have been thinking about this a lot. It was definitely on my mind when I read about the [legal action](https://www.theguardian.com/technology/2019/may/21/office-worker-launches-uks-first-police-facial-recognition-legal-action) that Ed Bridges has brought against the South Wales police for violating his privacy through their facial recognition trial. Bridges, who is a private citizen, is doing this with the support of [Liberty HQ](https://www.libertyhumanrights.org.uk/news/press-releases-and-statements/liberty-client-takes-police-ground-breaking-facial-recognition) . This is the first case of its kind in the UK, and it comes hard on the heels of San Francisco city legislature’s [decision](https://text.npr.org/s.php?sId=723193785) to ban the use of facial recognition by police and city agencies. Oakland and Massachusetts are also considering similar legislation:

_“Big Sister is watching us," [says Senate Majority Leader, Cynthia Creem], "and yet we don't even know how those pictures are being used ... The system that they're using now raises issues of due process and significant issues with regards to civil liberties." _[(NPR.org)](https://text.npr.org/s.php?sId=723193785)

These are widely reported examples of techlash, but they’re on the same spectrum as smaller scale adversarial action against algorithmically-driven decision-making. This latter behaviour was a topic of discussion in a recent [episode](https://www.listennotes.com/podcasts/sleepwalkers/poker-face-bSmrcn6E1H4/) of the tech podcast, Sleepwalkers. [Lisa Talia Moretti](https://www.gold.ac.uk/institute-management-studies/staff/moretti-lisa/), a guest on the show, [spoke](https://lnns.co/0lIJtPjDcOf/371) about students who figured out that a certain selection algorithm prioritised applications from students from universities such as Harvard, Oxford, or Cambridge. They started writing the names of these universities in white text (so human recruiters couldn’t pick up on it) on their CVs, in order to dupe the algorithm.

![](/images/editor_uploads/2019-06-07-135738-helloquence_51716_unsplash.jpg)
##### Image Source:  [Helloquence](https://unsplash.com/@helloquence?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)

Screening out applications from certain candidates may well have been the intent of the organisation(s) using this algorithm. If so, it’s surprising that the human recruiters _didn’t_ immediately pick up on the fact that applications from less desirable candidates were getting through - in which case, they could have simply screened them out at a subsequent stage or been explicit about their preference for candidates from certain universities. My suspicion is that this _wasn’t_ their intention, and that the emergent selection bias or preference was simply a quirk of the algorithm that was left unexplored and unaddressed.

However this state of affairs came about, the low-level adversarial behaviour it has triggered is corrosive - slowly transforming a potentially positive engagement into a grudge interaction.

### Building trust, making friends 
So how _do_ organisations go about (re)building trust and - by extension - resetting the dynamic between themselves and their users/customers? There are some really obvious choices namely, clarity and honesty about the way any collected data will be used, and taking steps to protect that data. In this context, being honest is often a matter of being upfront about business models (in the case of commercial entities) as well as governance and decision-making policies (especially in the case of government), and not trying to sneakily change models and policies through privacy policy updates. 

However, achieving the requirement for clarity is a tougher challenge. There are a number of reasons for this, but I will simply touch on two: 

* Explaining how complex systems interact with the various features of a large dataset - in a way that’s easy for time-poor, non-experts to grasp - is hard.
* Sometimes,(especially in the case of so-called ‘black box’ models) organisations don’t know quite how their algorithms arrive at the results that they do. 

These problems are related: explaining the workings of a system you don’t really understand is a tall order. That’s why attaining this understanding should be a critical area of focus for organisations that use machine learning. Thankfully, approaches for doing this are becoming more mature; this was the focus of our [Interpretability](https://blog.fastforwardlabs.com/2017/08/02/business-interpretability.html) research report.  Understanding the way systems work also paves the way for better, and more considered, trust-building conversations with end-users. (If you’re curious about what this looks like in practice, I recommend reading [this blog post](https://www.projectsbyif.com/blog/learning-through-making-understanding-what-young-people-think-about-ai-and-data-privacy/) about “designing to expose the seams of [automated decision making].” It’s based on a collaboration between the design agencies [Comuzi](https://comuzi.xyz/#) and [Projects by If](https://www.projectsbyif.com/).) 

With the advent of the [General Data Protection Regulation](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (GDPR), there has  been a lot of focus on explainability as a regulatory requirement. There is great benefit for organisations in recognising the value of interpretability and explainability as tools for building trust with customers.