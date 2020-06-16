---
date: "2017-04-28T00:00:00Z"
interview_with: Eli Bressert
interview_with_link: https://twitter.com/astrobiased
post_type: Interview
preview_image: /images/2017/04/b1509_w11.jpg
title: Eli Bressert on Data-Driven Processes at Netflix
aliases:
  - /2017/04/28/eli-bressert-on-data-driven-processes-at-netflix.html
---

##### Despite their best intentions, companies often struggle to develop processes that provide data-driven decisions through partnership across the business. Netflix stands out as a company that excels at deeply integrating its data science teams into all aspects of the company. We spoke with [Eli Bressert](https://twitter.com/astrobiased), Manager, Data Engineering and Analytics at Netflix, to learn more about how they create the culture and processes to support and sustain that integration.

**Tell us about your background. What did you study?**

I started out studying philosophy as an undergrad in Utrecht, with a desire to understand the basic roots of human knowledge. Taking courses in the history and philosophy of science, I discovered Karl Popper ([known for his theory of falsifiability](https://plato.stanford.edu/entries/popper/) in scientific discourse) and Thomas Kuhn ([known for his work on scientific revolutions](https://plato.stanford.edu/entries/thomas-kuhn/)), who inspired me to shift into science. The transition was tough, as math programs are strong in the Netherlands, so I had to play catch up and teach myself partial differential equations. That catch up turned into a great benefit where I fell in love in maths as well (double majored in astro and maths). But it was worth it, and I ended up focusing in astrophysics. My thirst to get my hands dirty observing the cosmos led me to Hawaii, which houses[ 13 large telescopes on Maunakea](http://www.imiloahawaii.org/61/astronomical-observatories), one of the highest mountains in the world! It was crazy up there. There were nights with 10 -14 feet snow blizzards, and we had to brave the elements to put coolant in &nbsp;the telescopes. Thinking back to it always reminds me of the[ scene in The Empire Strikes Back](https://www.youtube.com/watch?v=CXmp1hLK0tY) where Luke Skywalker falls over sideways in the blizzard. &nbsp;At any rate, working with telescopes is intense – it’s being on the edge of physical human capability.

![X-ray image of a pulsar](/images/2017/04/b1509_w11.jpg)

##### An [X-ray image of a pulsar](http://chandra.harvard.edu/photo/2009/b1509/) Eli made while working at the Chandra Space Telescope.

**Astrophysics is a common gateway to data science: two members of the Fast Forward Labs research team followed the same path. How did you transition from astrophysics to data science?**

After Hawaii, my wife and I moved to Boston, where I worked on making images from the [Chandra Space Telescope](http://chandra.harvard.edu/about/axaf_mission.html) for popular news outlets like CNN or BBC News. This involved learning color theory to transform spectra we cannot physically perceive (gamma, x-ray, or infrared) into aesthetically pleasing palettes to make space images interpretable. I quickly realized that I could automate most of my work with Python, so my path to Python enlightenment began. In a span of six years I ended up writing two well known astronomy packages with my astro-partner-in-crime (Tom Robitaille), wrote my PhD thesis, and wrote the [O’Reilly book about SciPy and NumPy](http://shop.oreilly.com/product/0636920020219.do). And the final experience was the gateway drug that made me consider startups. The first startup that I worked with as an advisor was authorea.com, an online service to collaborate in LaTex and simplify the complexity of writing mathematical manuscripts. I loved the energy of the startup world, and joined the Insight Data Science program to give me a nudge into the professional world.

**We work closely with Insight, and[ have mentored fellows](http://blog.fastforwardlabs.com/2016/08/26/exploring-deep-learning-on-satellite-data.html) on deep learning projects. What aspect of the experience was most valuable for you?**

I had already spent years developing technical data science skills, so considered Insight to be means to accelerate my network to find a great job.[ Jake Klamka](https://www.linkedin.com/in/jakeklamka/) and his team are highly connected, and I wanted broad exposure to companies across the Bay Area. Moreover, the Insight program has an added benefit: the alumni cohorts usually become good friends and help each other grow collectively as their careers progress. I had the chance to learn from experienced practitioners like [Monica Rogati](https://twitter.com/mrogati) and [Hilary Mason](https://twitter.com/hmason) and ended up leading a research for Stitch Fix (see a [previous blog interview](http://blog.fastforwardlabs.com/2016/05/25/human-machine-algorithms-interview-with-eric.html) with Stitch Fix Chief Algorithms Officer [Eric Colson](https://twitter.com/ericcolson)).

**Many consider Netflix to be the poster child for a data-driven company. Is that fact or fiction?**

It’s fact: Netflix is incredibly data driven. Many people are shocked when they join the company because we don’t make any product changes without first analyzing data. We have multiple departments that use data in different ways. The platform team focuses on infrastructure and tools, Data Engineering &amp; Analytics focuses on data engineering, ETL, and analytics, which offers self-service tools to business teams so they can make decisions autonomously. The Science and Algorithms team focuses on predictive modeling, algorithm research/prototyping, and experimentation (A/B testing). The Product Analytics team has developed an [in-house A/B testing platform, Ignite](http://techblog.netflix.com/2016/04/its-all-about-testing-netflix.html), to get the right insights in front of the right people and provide easy-to-consume visualizations so users can view outputs on daily basis. I’m just mentioning a subset of how many teams are involved in the data space, so there’s a lot more!

![Slide reading "Maximizing value of data product" with three items: self-service tools, analytics, a/b testing](/images/2017/04/bressert-slide.png)

##### Key components for maximizing the value of a data product. From Eli’s talk [Data Over Matter](https://www.youtube.com/watch?v=pFly0N-hjYo).

**What’s are a few examples of data-driven product decisions?**

One example is customer retention. We track behaviors of customers on our site and test to see if different onboarding experiences, like creating profiles and suggesting movies users may enjoy, are correlated with longer term retention. Before going through with these onboarding changes, we performed A/B tests and really made sure what we changed would have an impact. A simple and illustrative example is the color of a button on the sign-up page. We might start with a hypothesis, drawn from color theory, that a green button will lead to more signups than a red button. If we identify a correlation to support this hypothesis, we’ll A/B test the various button colors, but won’t commit to the roll out until we feel there’s a causal relationship. This is a joint effort between DEA, engineers, PMs, and Science &amp; Algorithms team and more.

**Data science projects often fall short because they don’t deliver as much value as hoped for to the business. How do you make sure your data efforts stay relevant at Netflix?**

Data teams at Netflix are organized to make sure we’re very tightly aligned with the company at large. This keeps us efficient (so we don’t get lost on dead end projects) and helps us hone judgment on where to focus our attention and what kinds of questions to ask about our data. Many data science and engineering friends at other companies have told me that business people view them as holding purely technical, rather than strategic roles. Netflix is such a successful data company precisely because data has been built into the culture and operations from day one, and leadership exposes the data team to the big picture, strategic questions. We’ll then orient our work to start exploring questions that are relevant to Netflix in the near and long term future, running some lightweight experiments and even deep analyses to draft memos for the leadership team communicating our early conclusions. These memos can be immensely impactful as a vehicle to get leadership on board to make changes suggested by our analyses. It’s all about scaling multiple levels of communication: memos to tell the high-level, big-picture story, a dashboard to provide additional insights, and the ability for users to dig deeper into the analytics if they like to probe and question the results. 

![Slide reading "Netflix Culture: Freedom and Responsibility"](/images/2017/04/bressert-slide-culture.png)

##### Part of the Netflix culture is making sure people feel invested in their work and clear in their responsibilities. From Eli’s talk [Data Over Matter](https://www.youtube.com/watch?v=pFly0N-hjYo).

**Do you ever see tensions between different stakeholders on data teams? If so, how do you resolve them?**

I’ve seen some confusion arise when there’s redundancy between two teams or ambiguity regarding who is responsible for what. I think it’s really important to give teams a north star, a goal they are aiming towards, as opposed to micromanaging their every move directly. To attract strong talent, and keep passion alive, it’s important that people feel they really own their work, and are working towards a rewarding goal. We filter for passion in our interview process and only bring on folks who are completely enthusiastic and passionate for the specific role they’re taking on, be that data science, analytics, or engineering. That said, we also hire for diversity, with some people bringing 15 years of experience in data engineering, and others just out of a PhD program. Again, the key is to make sure everyone has their north star, and then let their specific talents filter,emerge and grow.

**What emerging machine learning capabilities are most exciting to you?**

I’m curious to see how research in Gaussian processes (which Ryan Adams does a good job[ introducing on Talking Machines](http://www.thetalkingmachines.com/blog/2016/1/28/openai-and-gaussian-processes)) develops. They used to be quite hard to scale, but I’ve seen a few papers recently that promise to change that. They’re extremely interpretable models that can used in many different ways. In deep learning, I’m most excited by game-playing algorithms like AlphaGo or[ Libratus](https://www.cmu.edu/news/stories/archives/2017/january/AI-beats-poker-pros.html) given how they replicate probabilistic and strategic thinking. There are so many problems that we couldn’t resolve deterministically that are being unlocked by new probabilistic techniques.

**You’re an avid reader, averaging a book per week. Any recent reads you’d recommend to others?**

I loved[ Liu Cixin’s The Dark Forest](https://en.wikipedia.org/wiki/The_Dark_Forest), the sequel to[ The Three-Body Problem](https://en.wikipedia.org/wiki/The_Three-Body_Problem). There’s some pretty hard physics in there, and I find Cixin’s environmentalist critique extremely intriguing: Is the [dark forest theory](https://www.quora.com/What-is-the-Dark-Forest-Theory-of-the-cosmos-which-is-a-response-to-the-Fermi-Paradox) really the reality that we’re facing in our Universe? Last but not least, the third book in the series (Death’s End) has one of the best descriptions of 4D space ever written in a sci-fi novel. A must read by all means!

##### For more on data science at Netflix be sure to check out Eli’s talk [Data Over Matter - Innovating the Next Generation of Data Products at Netflix](https://www.youtube.com/watch?v=pFly0N-hjYo).