---
author: Grant
author_link: https://twitter.com/GrantCuster
date: "2018-03-28T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2018-03-09-211736-Screen_Shot_2018_03_08_at_3_52_58_PM.png
published: true
title: New creative possibilities with machine learning
---

Machine learning techniques are able to organize large amounts of unstructured data. Combined with dimensionality reduction techniques like t-SNE, this capability opens up new ways for us to interact with creative material including sounds, words, and ideas. In this section we highlight three of our favorite recent experiments.

![A screenshot of The Infinite Drum Machine. Showing the sample map with certain sounds like "Bag Plastic" highlighted and a drum sequencer at the bottom.](/images/editor_uploads/2018-03-09-203445-Screen_Shot_2018_03_08_at_3_21_16_PM.png)

[The Infinite Drum Machine](https://experiments.withgoogle.com/ai/drum-machine) is a Google Creative Lab experiment by Manny Tan and Kyle McDonald. It uses machine learning to cluster a large number of samples by similarity of sound. The user then selects clips, which can range from "gravel scoop tin cup" to "casino poker chip," from a sound map visualization created using t-SNE. The samples feed into a sequencer to create an uncanny drum machine.

Conceptually, the project works because it plays off the long history of hip-hop and electronic musicians using samples from surprising sources (one of Grant's favorite, kind of gross, examples is [Matmos' "A Chance to Cut is a Chance to Cure"](https://pitchfork.com/reviews/albums/5151-a-chance-to-cut-is-a-chance-to-cure/)). Sometimes machine learning systems give disappointing results because the system lacks context. In this case, the lack of context is a virtue. It frees the system up to make connections between sounds that humans, with their knowledge of each sound's source, might never make. It reminds us of first learning to draw, where you have to let go of your idea of what an apple looks like and draw the apple exactly as it appears in front of you.

Samples map well because each sound has a quantifiable (wave) form. Anything involving words gets more complicated. Do you compare on similarity of phoneme, grapheme, or meaning?

![A screenshot of an example from "Voyages in Sentence Space." It shows this example: 
"I went looking for adventure. I went out on a mission. I shouted awkwardly. I stared incredulously. I feel desperate. I never returned. I never returned."](/images/editor_uploads/2018-03-09-211736-Screen_Shot_2018_03_08_at_3_52_58_PM.png)

In [Voyages in Sentence Space](https://www.robinsloan.com/voyages-in-sentence-space/), Robin Sloan uses machine learning to explore the possibility space between sentences, which he calls "sentence gradients" (we love that metaphor). Instead of showing the whole map, it focuses on a specific journey from one sentence to another. As for how it does comparisons, Robin [tweeted about one illustrative example](https://twitter.com/robinsloan/status/969386860190433281) where, according to the model, '"thousand" is more like "three" than it is like "hundred" because of the "th."'

![A screenshot of Encartopedia. On the left is the Wikipedia article on Euclid. On the right is a visualization of the articles on Wikipedia and a line showing the user's journey through other articles to get to the Euclid article.](/images/editor_uploads/2018-03-09-213600-Screen_Shot_2018_03_08_at_4_32_10_PM.png)

[Sepand Ansari's](https://sepans.com/) [Encartopedia](http://encartopedia.fastforwardlabs.com/#/), which he made while working with us here at CFFL, looks at visualizing Wikipedia articles as an idea map, and plotting the user's journey through that space. It suggests how new capabilities can help us reflect on our thought process, by showing us how we move through an idea space.