---
author: Varun
author_link: https://www.linkedin.com/in/varun-bhatnagar-74303437/
date: "2020-02-27T00:00:00Z"
feature: false
post_type: Post
preview_image: /images/editor_uploads/2020-02-28-180128-markus_spiske_FXFz_sW0uwo_unsplash.jpg
published: true
title: 'Privacy, data governance, and machine learning: the regulatory perspective'
aliases:
  - /2020/02/27/privacy,-data-governance,-and-machine-learning-the-regulatory-perspective.html
---

### Why do privacy and governance matter?

Data privacy has been a common conversation topic among the general public since the [Cambridge Analytica scandal](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal) in 2018. The data "breach," in which user information was hoovered up through a Facebook quiz and subsequently misrepresented as being used for academic purposes, resulted in over $5 billion in fines for Facebook. However, Facebook's infringements were, in fact, relatively narrow in scope (though nonetheless egregious) compared to the growing remit of privacy law. Enterprises with wide-spanning data practices should be wary when establishing data-gathering practices, particularly those practices which are covered by the [California Consumer Protection Act](https://oag.ca.gov/privacy/ccpa) (CCPA) and [EU General Data Protection Regulation](https://gdpr-info.eu/) (GDPR).

Companies have already begun complying with these regulations, primarily in the form of updated privacy notices. **However, precedence has yet to be set around how data governance (oversight of data flows both within and outside the company) is treated in this process. This article will deal with this intersection, and how it pertains to machine learning operations.**

![](/images/editor_uploads/2020-02-28-180128-markus_spiske_FXFz_sW0uwo_unsplash.jpg)
#####  Image credit: Photo by [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
### What laws are actually on the books? What are their implications to my business?

The new laws that directly pertain to company data usage are most prominently the GDPR and CCPA. Let's talk about each of them at a high level.

The GDPR requires companies that "process" (a purposefully broad term that covers just about anything you can do with data: collection, storage, transmission, analysis, etc.) any personal data of EU citizens must comply with a [19-point checklist](https://gdpr.eu/checklist/). One point on this checklist states: "it's easy for customers to request and receive all the information you have about them."

The CCPA mandate applies to any for-profit entity that collects consumers' personal data, which does business in California, and satisfies at least one of the following thresholds: a) has annual gross revenues in excess of $25 million; b) buys or sells the personal information of 50,000 or more consumers or households; or c) earns more than half of its annual revenue from selling consumers' personal information. This law stipulates, among other requirements, that consumers have the "right to know what personal information a business holds about a consumer and whether the business sells or discloses personal information to third parties."

One way to facilitate compliance would be to build a comprehensive data model, which lists viewing, editing, and administrative rights over data repositories. This data model would necessarily extend to all data-collecting and data-maintaining operations that an enterprise is pursuing.

### Does my machine learning algorithm fall under this law?

In a word, yes. Each of the regulations approach the topic differently:

The GDPR is much more exacting when it comes to setting standards for machine learning. Not only does it require companies to divulge all instances in which a customer's data is sold and processed, but it also states the consumer’s "right to an explanation." This notion of an explanation has yet to be determined; it is currently being [hotly debated](https://www.kdnuggets.com/2018/03/gdpr-machine-learning-illegal.html) by legal scholars. At the very least, it grants individuals "information about the existence of automated decision-making and about 'system functionality,' but no explanation about the rationale of a decision." In other words, consumers will be informed if their, say, credit decision was the result of an algorithm, but not the individual variables that contributed most to the decision.

The CCPA mostly focuses on consumer sovereignty around their data, whether that includes the sale, deletion, or correction of their personal data. One potential machine learning-related highlight of the legislation - [full text here](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180AB375) - includes the ban of any sort of price discrimination based on data: "A business shall not discriminate against a consumer because the consumer exercised any of the consumer’s rights under this title, including by charging different prices or rates for goods or services, including through the use of discounts or other benefits or imposing penalties." This sort of outcome could potentially be fostered unintentionally through a pricing model or inventory optimization algorithm. Lawyers are still debating the finer implications of the legislation, which was [written with the goal of being modified in the future](https://blog.ericgoldman.org/archives/2019/12/some-lessons-learned-from-the-california-consumer-privacy-act-ccpa-18-months-in-part-2-of-3.htm). Still, companies are still pursuing compliance activity regardless.

Compliance, in terms of data governance, starts with a well-built data model. This model should ideally cover not just the "golden record," but should also include how the golden record is being applied within business operations. For example, a telecommunications company may rely on an algorithm to predict customer churn. Normally, data models only extend to the golden record. However, for governance purposes, it is necessary to ensure that this usage is captured. More importantly, if a customer orders that their data is deleted, governance architects need to know exactly where data needs to be deleted, including within internal business-side operations. This includes machine learning algorithms, and companies can be held liable for this.

### Data governance and privacy: past, present, and future

Privacy law and ethics stretches back to the 1600s in the United States, when Governor William Bradford opened mail flowing between the US colonies and England to monitor insurrectionary forces in the Massachusetts Bay Colony. The Townshend Acts of 1768 allowed British tax agents to search colonist homes, and served as the motivation behind the Fourth Amendment within the Bill of Rights, which laid out the definition of a lawful search. Since then, innovations within postal services, telecommunications, and law enforcement have provoked conversations over what level of government snooping ought to be considered an overreach. However, these days, private institutions (as opposed to governments) are coming under the popular/regulatory microscope.

Regulators are beginning to take action to ensure a fair market and prevent market externalities. Companies like Facebook are now being observed to ensure the prevention of undue snooping. While consumers will emerge with more power, the laws in place have been structured so as to be quickly adaptable to technological change. Innovation within location, natural language, or health data analysis will necessarily compel further regulation. District/state attorneys across the nation are building up technical resources in order to build case precedence. In order to ensure compliance, companies are best served by improving their governance techniques. Software solutions such as SAP and Informatica will only go part way in achieving this level of compliance; human capital and change management best practices must also keep up with these changes.

The laws above have pressing implications for data governance practices, as well as activities peripheral to the governance function (e.g., AI & machine learning, automation, business intelligence). Data governance, before these laws were implemented, was primarily tied to core IT operations. However, with the advent of machine learning integration to corporate strategy, governance should now gradually be thought of as a strategic, legal, *and* technical function. Moreover, it is important for data governance to be conducted on a continual, iterative basis as data is generated in new and evolving ways. All traces of a data point, upon request of a consumer, need to be retrievable at the drop of a hat; thus, a hashing methodology will need to be built to facilitate this capability.

### Will the government actually enforce these rules?

[Yes](https://www.oag.ca.gov/privacy/privacy-enforcement-actions) and [yes](https://www.enforcementtracker.com/?).