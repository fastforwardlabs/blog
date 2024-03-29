---
date: "2015-07-16T19:43:26Z"
preview_image: http://68.media.tumblr.com/bbd3e0495730ede2d37c309aa574112f/tumblr_inline_nrlfopx9PL1ts2crc_540.jpg
redirect_from:
- /post/124262931473/fast-forward-labs-at-the-science-fair
tags:
- TimesOpen
title: Fast Forward Labs at the Science Fair
aliases:
  - /2015/07/16/fast-forward-labs-at-the-science-fair.html
---

<p>Last night was the New York Times&rsquo; Open Source Science Fair. It kicked off with a keynote speech by our own Hilary Mason.</p><figure data-orig-width="1024" data-orig-height="768" class="tmblr-full"><img src="http://68.media.tumblr.com/e66d787dfddf623b21818a329481f84e/tumblr_inline_nrlf88nLI11ts2crc_540.jpg" alt="image" data-orig-width="1024" data-orig-height="768"/></figure>

##### Photo by Chrys Wu: <a href="http://t.co/m7G7G3g1ih">http://t.co/m7G7G3g1ih</a>

<p>After a dinner meet-and-greet session, the attendees and exhibitors got down to business, showing off their open source software projects, science fair style.<br/></p><p>Fast Forward Labs was an exhibitor. Micha Gorelick impressed the crowd with our realtime stream analysis prototype, CliqueStream.</p><figure data-orig-width="4856" data-orig-height="2988" class="tmblr-full"><img src="http://68.media.tumblr.com/bbd3e0495730ede2d37c309aa574112f/tumblr_inline_nrlfopx9PL1ts2crc_540.jpg" alt="image" data-orig-width="4856" data-orig-height="2988"/></figure><p>CliqueStream visualizes the landscape of conversation on Reddit and Twitter, in realtime. This type and scale of analysis would generally be handled by a high-powered cluster and would take upwards of ten minutes to complete. But by using probabilistic algorithms, we are able to analyze the streaming data in realtime on a laptop.</p><p>The probabilistic modules underlying CliqueStream are used to distill stream data by counting it and later selectively &ldquo;forgetting&rdquo; it; this is the key to speedy analysis in small memory. These appropriately named modules are open source.</p><ul><li><a href="https://github.com/mynameisfiber/countmemaybe">CountMeMaybe</a><br/></li><li><a href="https://github.com/mynameisfiber/gocountme">GoCountMe </a>(implemented in Go)<br/></li><li><a href="https://github.com/mynameisfiber/fuggetaboutit">FuggetAboutIt</a></li></ul><p>CliqueStream was just one among many great open source projects at the Fair. Two of our favorites were the New York Public Library Labs&rsquo; book cover generator and MIT&rsquo;s App Inventor software.</p><ul><li>The New York Public Library Labs&rsquo; <a href="https://github.com/mgiraldo/tenprintcover-p5">10PRINT </a>book cover generation algorithm <a href="http://www.nypl.org/blog/2014/09/03/generative-ebook-covers">creates cover art</a> for digital books in its collection, many of which are public domain titles that never had cover art.<br/></li><li>MIT&rsquo;s <a href="http://appinventor.mit.edu/explore/">App Inventor</a> software is a teaching tool that allows kids to develop Android apps.<br/></li></ul><p>The Fast Forward Labs team had a great time learning about these and the other presenters&rsquo; work. Thanks to New York Times Labs for a great event!<br/></p>
