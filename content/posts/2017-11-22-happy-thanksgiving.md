---
author: Friederike
author_link: https://twitter.com/FSchueuer
date: "2017-11-22T00:00:00Z"
preview_image: /images/2017/11/cute_bot-1511369925891.jpg
published: true
title: Algorithmic Cookery & Happy Thanksgiving
aliases:
  - /2017/11/22/happy-thanksgiving.html
---

As you are preparing for your Thanksgiving meal, just *know* that a robotic arm is holding the spoon at the Institute for Culinary Education (ICE); progress is relentless. *"The Chef Watson cookbook is a revolutionary display of the creative collaboration of man and machine."* [Cognitive Cooking with Chef Watson](https://www.ice.edu/about-us/brand-at-ice/ibm-cognitive-cooking-with-chef-watson-partnership), culinary and *cognitive* creativity [at your fingertips](https://www.ibmchefwatson.com/community). Perhaps you should try the Acorn Squash Meat Roast ... with English Breakfast Tea.

Jeopardy! It is [so 2011](http://www.nytimes.com/2011/02/17/science/17jeopardy-watson.html). In 2017, there is (of course) [a neural network trained to generate recipes](https://www.dailydot.com/unclick/neural-network-recipe-generator/) developed by [Janelle Shane](http://aiweirdness.com/aboutme). Try the *Pears Or To Garnestmeam* or the *Shanked Whipping Peanuts*:

![](/images/2017/11/shanked_whipping_peanuts-1511370088418.jpg)

##### Image Credit: [The Daily Dot](https://www.dailydot.com/unclick/neural-network-recipe-generator/)

For the literary-minded, Janelle recommends training the neural network first on the works of your favorite author before feeding it recipes. Here is what happens when you use the works of H. P. Lovecraft:

> Bake at 350 degrees for 30 to 32 minutes. Test corners to see if done, as center will seem like the next horror of Second House.
> 
> Whip ½ pint of heavy cream. Add 4 Tbsp. brandy or rum to possibly open things that will never be wholly reported.

The algorithm adds a helpful note:

> NOTE:  As this is a tart rather than a cheesecake, you should be disturbed.

Indeed.

Eager to cook your own recipes with [char-RNNs](https://github.com/karpathy/char-rnn) (i.e., multilayer recurrent neural networks with a character-level language models)? The code is available [here](https://gist.github.com/nylki/1efbaa36635956d35bcc). Do androids dream of cooking electric pies?

If you've done your shopping already, take a quick picture of your haul and let the algorithm [im2recipe](http://im2recipe.csail.mit.edu/) serve you cooking instructions. The algorithm developers collected 1m cooking recipes and 800k food images, the largest publicly available collection of recipe data, and trained a neural network to find a joint embedding of recipes and images, a multi-modal embedding that puts words and images in the same multidimensional embedding space. This embedding allows to retrieve a recipe given an image and an image given a recipe. More importantly, it allows arithmetic with chicken pizza: 

```python
v(chicken_pizza) - v(pizza) + v(lasagna) = v(chicken_lasagna)
```

![](/images/2017/11/arithmetics_sm_image_1-1511372024415.png)

##### You can now compute your next meal (Image Credit: [MIT](http://im2recipe.csail.mit.edu/)).

In 2017, ["we can embed that"](https://arxiv.org/abs/1709.03856) truly is the new ["we can pickle that."](https://www.youtube.com/watch?v=yYey8ntlK_E) (Pro-tip: challenge it with your left-overs.)

In the days after Thanksgiving, perhaps try the algorithm for [personalized diet meal planning](https://www.theatlantic.com/science/archive/2015/11/algorithm-creates-diets-that-work-for-you/416583/) or [AVA](http://eatwithava.com/), your intelligent nutrition bot focused on your happiness. 

(You're welcome!)

Finally, you will be pleased to know that the Association for Computing Machinery (ACM) holds a yearly workshop with the appetizing title [*Multimedia for Cooking and Eating Activities*](https://dl.acm.org/citation.cfm?id=3106668&picked=prox&CFID=1003587697&CFTOKEN=19498186). We have high hopes for Thanksgiving 2018!

We, the entire team at Cloudera Fast Forward Labs, wish you a Happy Thanksgiving.

*Cover image credit: Photo by [Besjunior/Shutterstock](https://www.shutterstock.com/image-photo/futuristic-robot-concept-electrical-wire-hairstyle-434970346?src=T_7B6fTKy7ufDO77AVnNvg-1-50)*
