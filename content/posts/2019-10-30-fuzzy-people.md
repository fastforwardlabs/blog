---
author: Chris
author_link: https://twitter.com/_cjwallace
date: "2019-10-30T00:00:00Z"
feature: false
post_type: NEWSLETTER
preview_image: /images/editor_uploads/2019-10-18-162954-bridge_fuzzy.png
published: true
title: Fuzzy People
aliases:
  - /2019/10/30/fuzzy-people.html
---

While preparing for a recent edition of the Federated Learning talk I often give at conferences, I encountered [this tweet](https://twitter.com/EliotAndres/status/1175101115966398464), which includes a demonstration of real-time multi-person segmentation on a smartphone.

Some useful terminology here: 
* Object _detection_ typically refers to identifying and localising objects (such as people!) in an image, and surrounding them with a bounding box.
* Object _segmentation_ labels each pixel of the image with a class (for instance: "person," "car," "cat," ...).

Segmenting multiple people in an image is substantially harder than segmenting a single person, because identifing the parts of the image that belong to each person essentially requires modeling each person's pose. Without understanding human poses, how would our function-approximating neural network know that an arm around a shoulder belongs to person one, rather than person two?

This technology working on a mobile device in real-time is impressive.

There is good reason to be concerned about the malicious or misguided use of facial recognition technology to invade personal privacy. However, there are many conceivable applications for computer vision in public spaces which do not require incidental privacy violation - monitoring road traffic, for example.

A potential use of the raft of face-swapping apps recently launched is protecting the identity of people in the background of video or photos, while maintaining the realism of the image.

This naturally raises the question: what is private?

If you know me well, you can probably recognise me with an obfuscated face, based on clothes and surroundings. The overt pixellation in the mobile demo appealed to me. Because vision so viscerally connects to our senses, it strikes me as a fascinating arena in which to test theoretical measures of privacy.

I managed to find a few older papers covering this idea - though given it's import, it feels under-explored.

### When in doubt, play.

Thanks to the ready availability of pre-trained models, TensorFlow.js, Observable notebooks, and some free time at a conference, I could reasonably straightforwardly construct a person pixellator, which you can try for yourself here: [Fuzzy People](https://observablehq.com/@cjwallace/fuzzy-people).

It can take an input image, such as this:

![](/images/editor_uploads/2019-10-18-162850-bridge_not_fuzzy.png)
##### Brooklyn Bridge with pedestrians  (image courtesy of [unsplash.com](https://unsplash.com/photos/AM23EReEsdc))

And output (an attempt at) a more private version:

![](/images/editor_uploads/2019-10-18-162954-bridge_fuzzy.png)
##### Brooklyn Bridge with fuzzy pedestrians

Since the picture is really intended to be of the Brooklyn Bridge and Manhattan skyline, we've done the pedestrians a favour and hidden their identities.

Clearly, it doesn't work perfectly.

Some experimentation reveals it to work best when the people are in the foreground, clearly separated, there are only a few of them, and the picture was taken in reasonable lighting and weather conditions.

Nonetheless, I'm impressed by how well it sometimes does work, given that it is running some quite sophisticated models entirely inside a web browser.

The pixellation technique used is simple: for each pixel that the model identifies as a person (the model here is a combination of a bounding box with COCO-SSD, and single person segmentation with BodyPix), replace it with a randomly selected pixel from within an adjustable region. At low noise, where the region the random pixel is selected from is small, people in the images are still human identifiable. As noise is increased, people progressively become less person-like and more static. 

Finding a less intrusive - but still highly private - means of masking people from images is left as an exercise to the research community.

The app is extremely early stage work, but I think credit is due to the open source community for providing pre-trained models to enable the creation of something that would have seemed magic a decade ago in a day or so of hacking. Certainly, we are past the point where some elements of computer vision can be considered as commodity: simply import the "detect person" function.

_A side-note on the pace of change in this space_:

Alas, much of my work is wasted. About a week after I made the notebook work, a multi-person version of BodyPix was released! While I confess to feeling slightly stung by having sunk a few hours into pixel manipulation to combine a bounding box model with a single-person segmentation model that has ultimately proved unnecessary, I'm excited to try out the new model. It certainly brings home the feeling of rapid progress in computer vision technology.