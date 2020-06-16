---
author: Dean Gonsowski
author_link: https://twitter.com/dean_gonsowski
date: "2016-04-26T18:41:17Z"
post_type: Guest Post
preview_image: http://68.media.tumblr.com/ebfd0ddb6284c50fde7a72b87f40462d/tumblr_inline_o69786Qw561ta78fg_540.jpg
redirect_from:
- /post/143439945583/making-a-case-for-machine-learning-to-legal
tags:
- ediscovery
- data science
- whitepaper
- language processing
title: Making a Case for Machine Learning to Legal Departments
aliases:
  - /2016/04/26/making-a-case-for-machine-learning-to-legal.html
---

<figure data-orig-width="550" data-orig-height="394" class="tmblr-full"><img src="http://68.media.tumblr.com/ebfd0ddb6284c50fde7a72b87f40462d/tumblr_inline_o69786Qw561ta78fg_540.jpg" alt="image" data-orig-width="550" data-orig-height="394"/></figure>

##### Since we released our <a href="http://blog.fastforwardlabs.com/2016/04/11/new-tools-to-summarize-text.html">text summarization resources</a>, the legal technology community has shown <a href="https://twitter.com/MMBues/status/724939065645273089">interest</a> in leveraging summarization technology to support litigation document review, deposition digests, and contract analysis. Data scientist interest to use machine learning to mine legal document corpuses and support legal strategy was also one factor motivating our summarization research.

##### The time is therefore ripe for data scientists to apply new text analytics capabilities for legal use cases. But to be effective, data scientists must first understand how lawyers think: what problems they’re trying to solve, how their processes are structured, and, perhaps most importantly, what fears may hinder the adoption of new technologies.

##### <a href="https://www.kcura.com/">kCura</a> is an electronic discovery (e-Discovery) software company with long experience helping lawyers adopt tools to support litigation. This guest blog post from <a href="https://twitter.com/dean_gonsowski">Dean Gonsowski</a>, kCura’s VP of Business Development, provides tips to help data scientists explain the value of machine learning to lawyers.

<p>Electronic discovery software helps manage the exchange of electronically stored information, documents that could be used as evidence in various forms of litigation like investigations or contract reviews. It is not used exclusively by law firms or service providers though—today’s corporate counsel are facing constant pressure to reduce costs in litigation, especially when faced with numerous discovery requests. This trend is getting more challenging due to exponential data growth and content proliferation. <a href="https://www.emc.com/collateral/analyst-reports/idc-the-digital-universe-in-2020.pdf">IDC’s Digital Universe study</a> predicts the world&rsquo;s data will amount to 44 zettabytes by 2020, which will have a significant impact on the compliance and e-discovery needs of organizations on a global scale. Corporate legal departments are aware of the trend, but an often-heard challenge is understanding what tools are available to combat this data deluge. </p><p>Several years ago the Rand Institute of Civil Justice conducted a <a href="http://www.rand.org/content/dam/rand/pubs/monographs/2012/RAND_MG1208.pdf">study about litigant expenditures in e-discovery</a>, where it found that corporations spend just eight percent of their discovery costs on collecting the data, 19 percent on processing and normalizing the data, and a whopping 73 percent on mining or “reviewing” the data. Review may be the driving feature of e-discovery, the process of finding the documents that matter for a legal matter. By applying text analytics to this “review” phase, corporations can start driving greater savings across the entire e-discovery spectrum. </p><p>The report suggests that the increasing volume of digital records makes techniques leveraging machine learning the most cost-effective way to conduct review. Supervised or active machine learning, for instance, can be used to predict the responsiveness of documents using a labeled sample set. From my experience, most savvy practitioners see this type of machine learning as an obvious way to increase efficiencies in the review process, but a number of factors have limited adoption. As a result, there is a conspicuous “consumption gap” in legal technology, which emerges from the difference in the current use of technology versus its capabilities. A <a href="http://ediscoveryjournal.com/research?search=eDJ%202015%20PC-TAR%20Focus%20Report">2015 PC –TAR Focus Report</a> prepared by the eDJ Group noted that counsel and management often resist analytics technologies due to their limited knowledge of software capabilities, limitations, potential costs and applications. In other cases, the resistance is simply in the form of the refrain that the old ways are good enough.</p><p>Fortunately, data scientists’ practical experience deriving insight from data can help drive the adoption of machine learning in the legal department. Data scientists can use their experience  and wins to help legal departments grasp how data technologies can support experts to lead them to the right information. Corporate counsel will need to understand some basic data science to leverage predictive analytics in e-discovery, which can help the team get to the facts of a case faster. Data scientists have the practical responsibility of guiding their corporate legal departments toward informed text analytics strategies, helping them to positively view text analytics as a cost and time-saving solution.</p><p>As a data scientist, there are several ways you can help corporate counsel shift attitudes about machine learning and conquer the consumption gap:</p>

### 1.	Understand the technology

<p>According to the Coalition of Technology Resources for Lawyers (<a href="http://524.ada.myftpupload.com/wp-content/uploads/2014/07/Guidelines-Regarding-the-Use-of-Predictive-Coding.docx">CTRL</a>), there are a range of machine learning applications that can be deployed to facilitate e-discovery. Corporate counsel will hear the word “predictive coding,” which refers to either a passive or active supervised learning approach. Another common term is technology-assisted review (TAR), which in addition to predictive coding includes search, near-duplicate document detection, and email threading. The important point to share with your legal team is that machine learning and other text analytics tools help augment lawyers’ decisions. The tools do not need to take control of the process.</p>

### 2.	Prove the machine learning methodology can hold up in court

<p>While predictive coding and TAR has been around for several years, legal professionals do have a responsibility for a defensible case in court, and might be worried about judicial approval for these somewhat newer tools. Fortunately, you can explain the defensibility of analytics in e-discovery by referencing well-known court cases such as <a href="http://blog.kcura.com/relativity/blog/more-da-silva-3-takeaways-from-judge-pecks-rio-tinto-opinion"><i>Rio Tinto Plc v. Vale S.A.</i></a><i> </i>or more recent decisions such as <a href="http://blog.kcura.com/relativity/blog/case-law-update-the-uk-joins-the-u.s.-and-ireland-in-approving-tar"><i>Pyrrho Investments Ltd. v. MWB Property Ltd.</i></a><i>, </i>where judges in both the United States and the United Kingdom cited greater consistency, proportionality (putting in effort proportional to the stakes of the case) and cost savings as reasons for using an assistive coding method like TAR over a less-efficient manual review process.</p>

### 3.	Utilize available workflows

<p>Look for cases that would be a good fit for analytics. It’s best to leverage these type of tools from start to finish in a project. Techniques email threading, for example, can quicken review, as teams can identify and discard non-relevant email threads as they clean up their data. Understand the best practices and proven workflows for your legal team’s chosen technology, as your expertise in text analytics could be leveraged at the beginning of the adoption cycle and all the way through a case. </p>

### The Future

<p>Early adopters are using emerging text analytics technologies like predictive coding without too much fanfare, and these technologies will be the industry standard for attorneys in the future. The only remaining question is how soon practitioners cross the chasm and start embracing these technologies in the near term, and how they can be helped along the way. </p><p>- Dean Gonsowski</p>
