---
author: Grant
author_link: https://twitter.com/GrantCuster
date: "2018-07-31T00:00:00Z"
feature: false
post_type: Newsletter
preview_image: /images/editor_uploads/2018-06-26-144942-Screen_Shot_2018_06_25_at_10_46_42_AM.png
published: true
title: Neural reinterpretations of movie trailers
---

In his latest project, artist and coder Mario Klingemann uses a neural network to match archival movie footage with the content of recent movie trailers. He regularly posts the resulting “neural reinterpretations” on [his Twitter](https://twitter.com/quasimondo). The results are technically impressive. They’re also a fascinating view into how to explore the creative possibilities of a machine learning technique.

Looking through Klingemann’s tweets you can trace his explorations:

![A screenshot from Klingemann's video of similar scene classification. A 3x3 grid shows several similar looking scenes. Some have planes, others are mostly blank, some have spare drawings of squares.]({{ site.github.url}}/images/editor_uploads/2018-06-26-144731-Screen_Shot_2018_06_25_at_10_45_15_AM.png)

##### Mario Klingemann's neural scene classifier grouping scenes it finds similar.

- Early in the explorations he posted [clusters of similar frames and clips in a 3x3 grid](https://twitter.com/quasimondo/status/1006485457713197056).
- He then experiments with compilations, like [scenes of water flowing (and other scenes the model thinks look similar to water)](https://twitter.com/quasimondo/status/1006570368751099904).
- Then he adds an element of interactivity, using [his webcam as the source against which to match the archival footage](https://twitter.com/quasimondo/status/1006835734223970304).
- He tries using the matches to create [new reaction gifs](https://twitter.com/quasimondo/status/1006996750429761536).

![On the left is a shot of Brad Pitt from Fight Club; on the right is a man holding a telephone with a similar expression from the archive footage.]({{ site.github.url}}/images/editor_uploads/2018-06-26-144942-Screen_Shot_2018_06_25_at_10_46_42_AM.png)

##### A neural reinterpretation of the Fight Club trailer, with the original footage on the left and the matched on the right.

- Then he moves into the trailer reinterpretations, with both stand-alone reinterpreted versions ([Fight Club](https://twitter.com/quasimondo/status/1010189455997784065)) and side-by-side versions ([Fight Club side-by-side](https://twitter.com/quasimondo/status/1010191619042238465)).
- He does [another version of the Fight Club trailer](https://twitter.com/quasimondo/status/1010983581475360768) using a tool that allows him to select from several algorithm-supplied suggestions: 

The movie trailer reinterpretations are a great showcase for the technique for a couple of reasons:

1. Trailers are made up of short clips. This gives the algorithm lots of shots at finding interesting matches (every cut is a new example). If it was instead focused on a 2 minute long continuous scene, you wouldn’t get to see nearly as many matches. Also the fact that the cuts are often timed to the music makes the reinterpreted content appear more connected to the audio of the trailer.

2. Films have a built up vocabulary of what different shots mean, like a close-up of a face to signal intense feelings. Film-makers employ these patterns consciously. As film watchers, we may not think about scene types explicitly, but we do build up associations and expectations with different framing, movements, and styles. The side-by-side reinterpretations make this referential language more visible by showing us two examples at a time, helping us notice the similarity the machine has identified. We can then often extrapolate even further into “ah, right, that’s another one of those 'vehicles rushing by' shots” that you normally don’t consciously note. This takes the trailers from technical demos into artistic territory.

![A screenshot of the video by Memo Atken. On the left is a blanket being scrunched up by hands; on the right is an image that looks like a painting of waves, where the shape of the waves matches the position of the hands and blanket.]({{ site.github.url}}/images/editor_uploads/2018-06-26-145050-Screen_Shot_2018_06_25_at_10_47_09_AM.png)

##### A still from "Learning to see: Gloomy Sunday" by Memo Atken

["Learning to see: Gloomy Sunday"](https://vimeo.com/260612034) by Memo Akten explores similarity in a different, fascinating way. He has a model trained on specific types of art that interpret his webcam photos and generate new images: for example, a sheet becomes waves. Like in the trailer reinterpretations, what takes this beyond technical demo is how suggestive the association can be. The machine's ability to identify similarity between a sheet and a wave gives us an understanding that we can then apply outside of the context of the video. It’s a suggestive analogy that opens out so that the viewer can build upon it and make their own connections.