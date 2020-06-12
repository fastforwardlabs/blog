---
author: Grant
author_link: https://twitter.com/grantcuster
date: "2017-01-03T15:00:00Z"
interview_with: Aditya
interview_with_link: https://twitter.com/whaleandpetunia
preview_image: https://68.media.tumblr.com/3eefb9d8c2e3d798ca6dcead23017de9/tumblr_inline_oj7sj2BjWG1ta78fg_540.png
redirect_from:
- /post/155350468038/learning-to-use-react
title: Learning to Use React
---

![](https://68.media.tumblr.com/3eefb9d8c2e3d798ca6dcead23017de9/tumblr_inline_oj7sj2BjWG1ta78fg_540.png)

##### React and Redux helped us keep application state manageable in our probabilistic programming prototypes

For every topic we research at Fast Forward Labs, we create prototypes to show how the technology can be applied to make great products. Finite, stand-alone projects, our prototype web applications are great opportunities to experiment with new front-end tech.

In our latest [report on probabilistic programming](https://twitter.com/FastForwardLabs/status/811294428287602688), I used the [React javascript library](https://facebook.github.io/react/) to create the interface with [Redux](http://redux.js.org/) for managing the data state of UI components. This setup was extremely helpful in prototyping: by keeping the application state in one place with Redux, it was much easier to switch components in and out as the prototype direction changed. The setup (which also involved Webpack, Babel and learning ES6 syntax features) did feel overwhelming at times, though new tools and tutorials made the process much smoother than my experience using React on the previous [Text Summarization](http://blog.fastforwardlabs.com/2016/04/11/new-tools-to-summarize-text.html) prototype. Once everything was rolling, it was the most enjoyable front-end coding experience I’ve ever had.

When [Aditya](https://twitter.com/whaleandpetunia), our Data Visualization and Prototyping Intern, started with us this fall, I asked him to get familiar with React and Redux (and Webpack, and ES6 features…) in preparation for future products. Now that he’s experimented with it, we decided to document what has been useful and not so useful in the process.

– [Grant](https://twitter.com/grantcuster)

## The Process

**Grant:** First I sent Aditya some helpful resources:

*   [How to Build a Todo App Using React, Redux, and Immutable.js](https://www.sitepoint.com/how-to-build-a-todo-app-using-react-redux-and-immutable-js/)
*   [Getting Started with Redux](https://egghead.io/lessons/javascript-redux-the-single-immutable-state-tree?course=getting-started-with-redux) 
*   [React Starter Kit](https://facebook.github.io/react/downloads.html)

**Aditya:** I was familiar with Javascript but had never used a Front-end framework, so first read the React documentation, and proceeded fairly quickly to the sitepoint tutorial. The sitepoint tutorial (about Redux) really tripped me up because it used a lot of unfamiliar syntax. A web search for alternate intros to Redux just ended up confusing me more.

Fortunately I found the [egghead videos by Dan Abramov](https://egghead.io/lessons/javascript-redux-the-single-immutable-state-tree?course=getting-started-with-redux), which make no assumptions about the learner’s prior knowledge, and explain things like ES6 syntax that might throw off new learners.

**Grant:** While I later realized it was too much to drop on Aditya all at once, I suggested the [sitepoint tutorial](https://www.sitepoint.com/how-to-build-a-todo-app-using-react-redux-and-immutable-js/) as a starting point because I like how it shows how Redux works across an entire React app. Abramov’s Egghead videos are great, but I got impatient with them because I wanted to incorporate Redux into the React app straight away. The sitepoint article helped me figure out how to structure Redux to adapt it into the prototype I was working on – but that was after I had gone through several other tutorials and banged my head against the code in various ways.

**Aditya:** Eventually, I realized that my confusion had little to do with the tutorials themselves. I really needed to go back and iron out my understanding of React before jumping into Redux. I realized this as I came across Abramov’s [You might not need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367), where he stresses the importance of learning to think in React before attempting to learn Redux. I took a step back to introspect and indeed found that my React knowledge hadn’t really seeped in yet.
![](https://68.media.tumblr.com/47d4c4e1a11b3b20c4b1475cedc128df/tumblr_inline_oj7slkRzhE1ta78fg_540.png)

##### When the creator of Redux [encourages you to think carefully about whether you need to use it](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367), it’s best to listen to him.

**Grant:** From the beginning I debated whether to introduce React alone or together with Redux. In retrospect, I should have started with React alone. I was anxious to get Redux in early because adopting it had made my own React development process simpler and more enjoyable. Especially when dealing with APIs (thanks in large part to Soham Kamani’s [A simplified approach to calling APIs with Redux](http://www.sohamkamani.com/blog/2016/06/05/redux-apis/)), Redux helped me maintain a readily understandable model of what was happening where – versus the spaghetti-ish ComponentDidMount situation I found myself in with React. (Note: You can have a perfectly reasonable set-up without Redux if you structure your React app well, which I’m not convinced I did. The point is, the opinionated structure of Redux was super helpful for developing and maintaining a manageable set-up.)

That’s my rationalization for introducing Redux at the start. But as Aditya points out, it was too many new moving parts at once! Much better to get a handle on React first -- and even work with the messiness Redux helps reduce -- than have the whole system dropped on you all at once. I knew this in principle, but this process was a good reminder.

**Aditya:** [Thinking in React](https://facebook.github.io/react/docs/thinking-in-react.html) was a great resource to deepen my understanding. It teaches concepts by showing one the processes used to design a React app: I like this approach because it can be overwhelming to read scores of definitions with no idea how they ultimately interplay to form the grand picture. ‘Thinking in React’ helped me break down the development process into discrete steps that made the fundamental concepts easier to understand.

Take, for example, the concepts of [props](https://facebook.github.io/react/docs/components-and-props.html) and [states](https://facebook.github.io/react/docs/state-and-lifecycle.html) in React. Both were well defined in the standard documentation, but when I started making a simple app on my own, I was a bit confused. What part of my app would be a state? What would be a prop? Should I write the parent component first or begin with the leaves? We might say I knew the words but not the grammar. ‘Thinking in React’ introduced a framework to help think about their code architecture.

I’m very impressed by the React documentation, and it’s still the primary source for most of my React-related questions. As it should be. There are a lot of third-party resources (most behind a paywall) that are so fragmented that learning these technologies can be jarring. Third-party resources should exist, and are even required in the ecosystem, but those who make technology are also responsible for explaining it to users. Kudos to the React community for not only making a great technology but also by giving a damn about good documentation. Providing a great number of examples (whether in codepens or code blocks), a way to quick start ‘hello-world’ programs (such as [Create React App](http://github.com/facebookincubator/create-react-app)), and a way to think about process is key to a good developer experience. It’s no coincidence that libraries, like D3.js and React, that provide that kind of an experience are so successful and widely adopted.

## Conclusions

**Grant:** There’s a lot of worry and excitement about the current state of Javascript development. I’m mainly excited. There is a pretty big learning curve to this stuff, but once you get going tools like React and Redux can make front-end development a lot more fun. They enabled me to much more quickly develop and experiment with different interface components in our probabilistic programming prototype. Sometimes I was surprised (in a good way!) by how different components worked in combination, and I took inspiration from those interactions to build out a feature or interaction I hadn’t planned on.

That said, there is definitely work to be done to help people with that learning curve. We touched on some starter materials in this post. One thing we didn’t discuss is the [React Starter Pack](https://facebook.github.io/react/docs/installation.html), which include the [Create React App](http://github.com/facebookincubator/create-react-app) command-line tool. One of the biggest headaches I had in my earlier attempts to get started with React was getting the development environment setup. The pipeline created within Create React App made it much easier to get up and running smoothly.

Even with all the great work being done, it can still be quite overwhelming to jump into. It helps me to read about others’ process and experiences (especially their mistakes and lessons learned). Hopefully this post is helpful to others.

**Aditya:** I think it's really important for people building these technologies to start thinking about documentation at a fundamental level. We are facing an avalanche of new technologies everyday and developers need to be mindful that not everyone comes to the table with the same stack or the same level of experience. What a Senior Software Engineer expects from documentation is probably going to differ from that of a college sophomore.

At Fast Forward Labs, we work on cutting edge machine learning technologies, but remain mindful that this radically new ecosystem, where knowledge is concentrated in the hands of a few, can lead to socio-economic inequalities. Lowering barriers to entry is critically important as the technology ecosystem evolves at an increasingly rapid clip.