---
author: Grant
author_link: http://www.twitter.com/grantcuster
date: "2015-05-19T16:25:01Z"
preview_image: http://i.imgur.com/bJjtxok.png
redirect_from:
- /post/119368587133/designing-the-tech-graph
tags:
- design
- code
title: Designing the Tech Graph
---

<p>We launched a redesign of the <a href="http://i.imgur.com/p7kidae.png" target="_blank">Fast Forward Labs website</a> today. There are lots of parts of the design I’d like to write someday about but for this post I want to focus on the thinking behind the “Tech Graph” force-directed graph display in the Intro section.</p>

<img src="http://i.imgur.com/bJjtxok.png"/>

### Dramatizing Information Work

<p>The response I want the intro section to provoke is something like: “Wow, there is some really interesting work being done here that I would like to be involved with it.” To get to that response I needed to figure out how to represent and dramatize the work we do at Fast Forward Labs.</p>

<p>Like a lot of companies whose work is primarily writing and coding, our process is not inherently visually dramatic. It involves a lot of sitting in front of a computer, typing and thinking. There are definite design strategies that have emerged to add some weight and drama to information work. Frank Chimero has <a href="http://frankchimero.com/writing//web-tableaus/" target="_blank">a great post explaining the “web tableau” strategy</a>, where the digital work is presented on a device surrounded by physical objects signaling the type of work being done.</p>

<p>If we had followed the tableau strategy we could have shot a video of us at our office, typing on computers but also whiteboarding, engaging in lively discussion, and working on one of our office hacks such as installing programmable LED lights. That video would be silent and looped in the background of the intro section, and, if executed well, it would be effective.</p><p>I had a different strategy in mind, though. The tableau strategy reminds me of the debate over <a href="http://en.wikipedia.org/wiki/Skeuomorph" target="_blank">skeuomorphism</a> in design. Like skeuomorphism, the tableau strategy uses the familiar and concrete (in this case physical props) to help ease us into the new and abstract. I don’t think there is necessarily anything wrong with that strategy, but there is a risk that by tying your design to the familiar you may pass up opportunities to develop strategies with new and different strengths.</p>

### Visualizing Thinking with the Tech Graph

<p>In the case of the Tech Graph I wanted to see if, rather than staging the physical aspects of the information work we do, I could get closer to dramatizing the thinking process itself. I had a starting point in an internal document we had where we track topics we are interested in, and, after getting familiar with <a href="https://github.com/mbostock/d3/wiki/Force-Layout" target="_blank">D3.js’s force-directed graph layout</a> for our second prototype, I had an idea of how to make the brainstorming process more visually dramatic. Instead of shooting video of us at one of the office whiteboards I would try and show our digital whiteboarding in progress.</p>

<p>The first step was creating an internal tool where we could add topics and draw connections between them. Using D3.js, I created an internally editable force-directed graph.</p>

<img src="http://i.imgur.com/p7kidae.png"/><p>The graph has a pretty bare-bones feature set at the moment, topics and links can be created and deleted and that’s about about it. My goal is to keep adding and improving to the point where it becomes a useful brainstorming tool for us. I’m looking forward to exploring what kinds of features can aid our thinking process.</p>

<p>The visualization on the website, then, is a read-only version of our internally editable graph, with the appearance tweaked to fit with the rest of the site. There were some fun tricks that went into making it work in the design of the intro, such as:</p>
<ul><li>The node boxes are kept from overlapping too much with the center logo through the use of an invisible node fixed at the center. Its charge keeps the others from overwhelming the logo.</li>
<li>I wanted some movement to the graph, so Micha helped me work out an equation to keep the nodes rotating around the center, which we eventually reduced down to:
<code>new_x = current_x - current_y * rotation_speed; new_y = current_y + current_x * rotation_speed;</code>
</li><li>I tried several different optimizations to make the graph more efficient. I thought it would run quieter if it was all SVG, but, at least in Chrome, an SVG layer for the connecting lines and an HTML layer with transforms for the boxes seemed to do the best.</li>
</ul><p>By feeding our internal brainstorming into the intro our website, we give visitors a preview of our process. The tour of our process is continued in the Product section of the site, where topics that emerged from brainstorming are displayed in their final report and prototype form. We hope that by giving people this view into our process they’ll get excited about it and want to join in by working with us.</p>

### A Starting Point

<p>I’ve already had feedback from people wishing the intro graph was more interactive, and just as I have plans for our internal graph tool I have dreams of further developing the public facing version as well. I would love to allow people to draw their own connections and make their own topic suggestions, these suggestions could be sent to us and become part of our brainstorming process (and how cool would it be if the site kept track of your specific recommendations and showed them in the graph when you returned to the site!) I’m looking forward to exploring all of those options, though I am equally happy to have scoped this first version down to a manageable size and get it shipped out.</p>

<p>Thanks for reading and I’d love to hear your thoughts on <a href="http://fastforwardlabs.com" target="_blank">the site</a>, visualizing information work, or tools for doing thinking at <a href="http://twitter.com/grantcuster.com" target="_blank">@grantcuster</a>.</p>

<p>- Grant</p>
