---
author: Shioulin
author_link: null
date: "2017-02-27T00:00:00Z"
feature: false
preview_image: /images/2017/02/mobileauth.png
title: Mobile Behavioural Authentication
---

As mobile devices become central to our personal and professional lives, their
security is more and more important. Passcodes in particular can be lost (or
forcibly surrendered) to law enforcement. Recent research has focussed on
behavioural authentication based on patterns of user interaction. This could
provide an unintrusive authentication method that operates during normal use.

![Mobile authentication](/images/2017/02/mobileauth.png)

##### Figure from [Touchalytics: On the Applicability of Touchscreen Input as a Behavioral Biometric for Continuous Authentication](https://arxiv.org/abs/1207.6231)

Research in this field addresses two problems. Is it possible to grant access
based on the way a user interacts with a phone? This is **gating interaction**.
And once access is granted, can a system continuously monitor use in the
background, requesting reauthentication through a gating system when suspicious
activity is detected? This is **continuous interaction**.

## Data Acquisition

To use touch dynamics for authentication, you first have to establish a
benchmark of normal user behavior. Current research does this by having
subjects type a fixed text or perform gestures on a smartphone. This is
repeated a few times to capture variation in behavior. Some researchers run
controlled experiments while others try to mirror real life usage scenarios. As
an example, [Tao Feng and
collaborators](http://ieeexplore.ieee.org/document/6459891/) recruited 40
subjects to perform common gestures such as zooming and spread.

The raw data obtained from the touch display can then be used directly or
massaged to obtain timing, spatial and motion features. The extracted features
are used to generate a unique user representation. Machine learning classifiers
are then used to authenticate a user. 
 
## Features

When a touch event occurs on a screen, the operating system records sensor
information, which can be accessed through the phone's API. The API also
reports timestamps, which can be manipulated to provide information on [dwell
and flight time](http://dl.acm.org/citation.cfm?id=2933015) (time the finger
stays on a virtual key, and time between presses), and spatial features such as
touch size, pressure, and position. Touch size and pressure are normalized
values and are usually used without manipulation. On the other hand, position
can be used raw or manipulated to provide information on speed, angle, and
distance. 

The phone's accelerometer and gyroscope provide yet more user-specific
information. The accelerometer measures movement in three dimensions, while the
gyroscope measures the rotation.

For gating authentication, many researchers use timing as the only feature, but
some combine timing with spatial and motion information. [Mario Frank and
collaborators](https://arxiv.org/abs/1207.6231) propose 30 features based on
strokes for continuous authentication. A stroke is a trajectory encoded as a
sequence of vectors with location, timestamp, pressure, area occluded by the
finger, orientation of the finger, and orientation of the phone. [Tao Feng and
collaborators](http://ieeexplore.ieee.org/document/6459891/) complement strokes
with zooming motions and finger motion sensor data from a digital glove. 

## Machine Learning

The collected features can then be used to train a machine learning system and
classify future users. [Gating](http://dl.acm.org/citation.cfm?id=2933015) and
[continuous](http://ieeexplore.ieee.org/document/7503170/) authentication
research use algorithms like clustering, decision trees, Support Vector
Machines (SVMs), and neural networks. For example, [Mario Frank and
collaborators](https://arxiv.org/abs/1207.6231) used SVMs and clustering,
specifically k nearest neighbor (kNN), as classifiers. During training, the
SVMs constructs a hyperplane to separate out the user and everyone else. The
hyperparameters of its radial basis function (a real-valued function which
measures distance) are tuned using standard crossvalidation techniques. The kNN
classifier looks at each new observation, finds the k nearest training
examples, and determines the label of the majority of those k neighbors. The
new observation is then assigned that label. SVM takes time to train but only
stores the decision hyperplane. kNN is quick, but but must store all training
observations and labels. Both storage and CPU are at a premium in a mobile
device, but experimental results show that the SVM generally outperforms the
kNN for this use case. 

## Metrics

False acceptance rate (FAR) and false rejection rate (FRR) are the usual
performance metrics for probabilistic authentication systems. FAR is the
fraction of intruders that are incorrectly authenticated. FRR is the fraction
of authentic users that are incorrectly rejected. A system with high FAR is
very insecure while one with high FRR is overly sensitive. In a continuous
authentication system, high FRR means that valid users need to reauthenticate
too often. 

The point where FAR and FRR are equal is known as the Equal Error Rate (ERR).
Ideally both FAR and FRR should be low. But when that's not possible, you can
tune the classifier to prioritise one or the other, depending on the
application. 

## What's next?

It's currently possible to build a touch-based authentication system with an
ERR of less than 5% (see reviews by [Teh et
al.](http://dl.acm.org/citation.cfm?id=2933015) and [Patel et
al.](http://ieeexplore.ieee.org/document/7503170/)). For gating authentication
purposes this is too high, but it could be appropriate for continuous
authentication. 

We think the most useful next step would be the release of large, public
datasets. Current datasets are small and mostly proprietary which makes
progress slow and difficult to measure. Large public datasets would likely
require collaboration between academia and device manufacturers. And it's time
to start thinking about performance not just in terms of accuracy but also
computational expense. If you think your phone's battery drains quickly today,
wait until you've got a neural network running in the background all the time!
Finally — and perhaps most interestingly — the trade off between usability,
security and privacy needs to be better understood from a product and user
point of view. 
