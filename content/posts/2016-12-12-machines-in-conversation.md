---
author: Gridspace
author_link: https://www.gridspace.com/
date: "2016-12-12T17:47:22Z"
post_type: Guest Post
preview_image: http://68.media.tumblr.com/692d44e33b12223b1e7fb77bb122ec99/tumblr_inline_oi327sddi71ta78fg_540.png
redirect_from:
- /post/154383131913/machines-in-conversation
title: Machines in Conversation
aliases:
  - /2016/12/12/machines-in-conversation.html
---

![](http://68.media.tumblr.com/692d44e33b12223b1e7fb77bb122ec99/tumblr_inline_oi327sddi71ta78fg_540.png)

##### We at Fast Forward Labs have long been interested in speech recognition technologies. This year’s <a href="https://www.oreilly.com/ideas/an-overview-of-the-bot-landscape">chatbot craze</a> has seen growing interest in machines that interface with users in friendly, accessible language. Bots, however, only rarely understand the complexity of colloquial conversation: many practical customer service bots are trained on a very constrained set of queries (”I lost my password”). That’s why we’re excited to highlight <a href="https://www.gridspace.com/">Gridspace</a>, a San Francisco-based startup that provides products, services, and an <a href="https://api.gridspace.com/scripts/try">easy-to-use API</a> focused on making human-to-human conversation analyzable by machines. Gridspace Co-Founders <a href="https://www.linkedin.com/in/evan-macmillan-60716b71">Evan Macmillan</a> and <a href="https://www.linkedin.com/in/scodary"> Anthony Scodary</a> share their thoughts and demo their API below. Catch them this week at the <a href="http://www.slt2016.org/">IEEE Workshop on Spoken Language Technology</a> (SLT) in San Diego!

When most people think about speech systems, they think about virtual assistants like Siri and Alexa, which parse human speech intended for a machine. Extracting useful information from human-to-machine speech is a challenge. Virtual assistants must decode speech audio with a high degree of accuracy and map a complex tree of possible natural language queries, called an ontology, to distinguish one-word differences in similar yet distinct requests.

But compared to processing human-to-human speech, current virtual assistants have it easy! Virtual assistants work with a restricted set of human-to-machine speech requests (i.e. “Call Mom!” or “Will it rain tomorrow?”) and process only a few seconds of speech audio at a time. Virtual assistants also get the benefit of relatively slow and clear speech audio to process. After all, the user knows she is only speaking with a machine.

Today, most of our spoken conversations don’t involve machines, but they soon could. A big hurdle to making machines capable of processing more types of conversation, specifically natural conversations we have with other people, is called natural language understanding (NLU).The jump between NLU for human-to-machine conversations to NLU for long human-to-human conversations is non-trivial, but it’s a challenge we chose to tackle at Gridspace.

## Gridspace Sift API

The <a href="https://api.gridspace.com/scripts/try">Gridspace Sift API</a> provides capabilities specifically tailored to long-form, human-to-human speech. The transcription and speech signal analysis pipeline has been trained on tens of thousands of hours of noisy, distorted, and distant speech signals of organic, colloquial human speech. The downstream natural language processing capabilities, which perform tasks like phrase matching, <a href="https://www.cs.princeton.edu/~blei/papers/Blei2012.pdf">topic modelling</a>, entity extraction, and classification, were all designed to accept noisy transcripts and signals.

The following examples can all be run in the <a href="https://api.gridspace.com/scripts/try">Sift hosted script browser environment</a>, in which the full API (and handling of asynchronous events like speech or telephone calls) is accessed through short snippets of javascript.

For example, let’s say we want to call restaurants to get the wait times. You could prompt restaurants to enter the wait time into a keypad, but you’ll likely  have a low success rate. However, by using natural human recordings and allowing the restaurants to respond with natural language, a response rate of over 30% is achievable. This response rate could be even higher if you exclude restaurants that operate an IVR (interactive voice response) system. In the JavaScript sketch below (the full example can be viewed and run <a href="https://api.gridspace.com/scripts/try#waittimes">here</a>), we call a list of restaurants, greet whoever answers the phone, and then ask for a wait time:

```javascript
gs.onStart = function() {
  var waitTimes = {}
  for (var restaurant in NUMBERS) {
    var number = NUMBERS[restaurant];
    console.log(restaurant);
    console.log(number);
    var conn = gs.createPhoneCall(number);
    var trans = "";
    for (var j = 0; j &lt; MAX_TRANS; j++) {
      console.log("Try " + j);
      if (j == 0) {
        console.log("Saying hello...");
        newTrans = conn.getFreeResponse({"promptUrl": "http://apicdn.gridspace.com/examples/assets/hi_there.wav"});
      } else {
        console.log("Asking for the wait time...");
        newTrans = conn.getFreeResponse({"promptUrl": "http://apicdn.gridspace.com/examples/assets/wait_time.wav"});
      }
      if (newTrans) {
        trans += newTrans + " ";
        if (j &gt; 1 || trans.indexOf('minute') != -1 || trans.indexOf('wait') != -1) {
          break;
        }
      }
    }
    console.log("Saying thank you...");
    conn.play("http://apicdn.gridspace.com/examples/assets/thanks.wav");
    waitTimes[restaurant] = trans;
    conn.hangUp();
  }
  console.log(waitTimes);
}
```

As soon as we hear the word ‘minute’, we thank them and hang up. The results of each restaurant are simply printed to the console.

<figure data-orig-width="582" data-orig-height="171" class="tmblr-full"><img src="http://68.media.tumblr.com/5fc1eb13a3557ad08a4f13da6137c81a/tumblr_inline_oi32mhT1hZ1ta78fg_540.png" alt="image" data-orig-width="582" data-orig-height="171"/></figure>

In our experiments, about one in three restaurants provide a response, but this basic  example can be easily improved upon (and we encourage you to try!).

One glaring problem is the crudeness of the parser (we simply look for the word ‘minute’ and call it a day). In the next example (the full sketch is <a href="https://api.gridspace.com/scripts/try#statusUpdate">here</a>), we listen in on a simulated conference call, wherein status updates for different employees are extracted.

```javascript
const QUERIES = ["~~'status' then ~~'{name:employee}' then (~~'good' or ~~'bad' or ~~'late' or ~~'complete')"];
const BEEP = 'http://apicdn.gridspace.com/examples/assets/alert.wav';

gs.onIncomingCall = function(connection) {
  connection.joinConference('Conference', {
    onScan: function(scan, conversation) {
      for (var i = 0; i < QUERIES.length; i++) {
        var topMatch = scan[i][0];
        if (!topMatch) {continue;};
        var match = topMatch['match'];
        conversation.playToAll(BEEP);
        console.log("Status update: " + match);
        if (topMatch.extractions) {
          console.log("For employee: " + topMatch.extractions[0].value);
        }
        console.log("\n");
      }
    },
    scanQueries: QUERIES,
  });
};
```

In this example, instead of simply looking for exact words, we scan for approximate matches for status reports and names. This fuzzy natural language extraction allows for soft rephrasing and extraction of general concepts like numbers, names, dates, and times. Even if the conversation lasts for hours, each time a status update is detected, a sound is played, and the employee status is parsed. This entire behavior is implemented in just a couple lines of JavaScript.

In the <a href="https://api.gridspace.com/scripts/try">Sift API hosted script environment</a>, you’ll find a wide array of other examples including <a href="https://api.gridspace.com/scripts/try#politicalsurvey">automated political polling</a>, <a href="https://api.gridspace.com/scripts/try#callgrading">deep support call analysis</a>, <a href="https://api.gridspace.com/scripts/try#weather">an FAA weather scraper</a>, and <a href="https://api.gridspace.com/scripts/try#ivrSystem">interactive voice agents</a>. Each example is only a couple dozen lines long and demonstrates a broad spectrum of speech analysis capabilities.

While there is still much work to done in the area of conversational speech processing, we are excited about what is already possible. Human-to-human speech systems can now listen, learn and react to increasingly complex patterns in long-form conversational speech. For businesses and developers, these advancements in speech processing mean more structured data and the opportunity to build new kinds of voice applications.

– Evan Macmillan and Anthony Scodary, Co-Founders, Gridspace
