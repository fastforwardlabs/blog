---
date: "2017-10-26T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/2017/10/Screen_Shot_2017_10_09_at_9-1507556105313.33
published: true
title: Neuroscience-inspired AI
---

Pioneers in artificial intelligence (AI) have worked across multiple related fields, including computer science, AI, neuroscience, and psychology - but as each of these areas of research have grown in complexity and disciplinary boundaries have solidified, collaboration has become less commonplace. In [*Neuroscience-Inspired Artificial Intelligence*](https://www.ncbi.nlm.nih.gov/pubmed/28728020), the co-founder of Google DeepMind [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis), alongside other renowned neuroscientists, argues to revive collaborative efforts.

The (human) brain is a living case-in-point that human-level general AI is possible, but building it is a daunting task. The search space is vast and sparsely populated; biological intelligence provides a guide. Neuroscience can validate AI techniques that exist already: if known algorithms are found to be implemented in the brain, they are likely an integral component of general intelligence systems. 

Neuroscience also provides a rich source of inspiration for new types of algorithms and architectures; a set of recent papers ([Stachenfeld et al.](https://deepmind.com/blog/hippocampus-predictive-map/), [Constantinescou at al.](https://www.ncbi.nlm.nih.gov/pubmed/27313047)) suggests there are types of data representations sufficiently flexible and abstract as to support the remarkable human capacity of generalizing experiences to novel situations — a tough nut many AI researchers are looking to crack (i.e., [transfer](https://en.wikipedia.org/wiki/Transfer_learning) / [one-](https://en.wikipedia.org/wiki/One-shot_learning) or [zero-shot](https://www.quora.com/What-is-zero-shot-learning) learning) — and that a mechanism for constructing these (abstract) representations from sensory experience exists.

### A Nobel-prized story of the hippocampus
It's Nobel season, and in 2014, Edvard and May-Britt Moser, alongside John O'Keefe, were [awarded](https://www.nobelprize.org/nobel_prizes/medicine/laureates/2014/press.html) the Nobel Prize in Physiology or Medicine for their discovery of a set of cells in the hippocampus (a brain structure deep inside the mammalian brain) thought to help us orient and navigate in space. Drivers of black-cabs in London, required to memorize some 25,000 streets and thousands of landmarks, for example, have a [larger than usual hippocampus](https://www.wired.com/2011/12/london-taxi-driver-memory/); their brains have adapted to the unique demands of their jobs.

Stachenfeld and colleagues show that the hippocampus does more than encode locations in space. Instead, it encodes "[successor representations](https://www.nature.com/articles/s41562-017-0180-8)," information about likely *future* locations given your current location.

### Successor representations in decision making
Think about how you choose your route to work (or the next move in a game of chess or Go). You need to estimate the likely future reward of your decision in order to make a smart decision now. This is tricky, because the number of possible scenarios increases exponentially, the further you peek into the future. [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/), the Go playing champ built by Google DeepMind, uses advanced tree search ([Monte Carlo tree search](http://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/)) to simulate the future in order to make smart decisions in the now.

Rats - capable of strategic, reward-maximizing decisions - are unlikely to use such computationally expensive methods. Successor representations offer a computationally less expensive yet flexible mechanism. They are a kind of look-up table that contains information about likely future states (e.g., locations) given the current state (i.e., where you *will* be, given where you are now). Combined with information about (future) reward, successor representations enable reward-maximizing decisions without expensive simulation. They also enable quick adaptation to changes in reward (a novel food source, for example) - while adaptations to changes in space (e.g., a new obstacle) will be slower.

Stachenfeld and colleagues offer empirical evidence for the existence of successor representations in the rat's hippocampus *and* for the existence of a low-dimensional decomposition of successor representations in the [entorhinal cortex](https://en.wikipedia.org/wiki/Entorhinal_cortex) (the main interface between the hippocampus and neocortex). The authors show that these low-dimensional decompositions of the successor representations lend themselves to the discovery of subgoals, a hallmark of efficient planning and *the* foundation for hierarchical, increasingly abstract representations of tasks required for the generalization of knowledge to novel scenarios. 

![](/images/2017/10/Screen_Shot_2017_10_09_at_9-1507556105313.33)

##### Comparing model predictions (B) to reality (A) (i.e., the firing rates of cells recorded in the hippocampus of a rat). As the rat is trained to run in a preferred direction along a narrow track, initially symmetric place cells (red) begin to skew (blue) predicted in theory (B) and demonstrated in practice (A).

### From rats to humans, from spatial navigation to abstract reasoning
This isn't isolated to rats; humans also use these decompositions of successor representations during strategic planning and decision making, as [Constantinescou and colleagues](https://www.ncbi.nlm.nih.gov/pubmed/27313047) show. What's more, successor representations and their decompositions are used not only during spatial navigation, but also during *abstract* reasoning; abstract reasoning capabilities piggyback on representations evolved for spatial reasoning tasks. 

Taken together, successor representations and their decompositions provide us with a clue as to how the brain computes abstract representations from sensory inputs that allow us (human and non-human animals) to generalize our experiences to novel situations, thus showing that the collaboration between neuroscience, psychology, and AI could be a very fruitful one indeed.