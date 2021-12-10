---
title: "Exploring the I3D architecture: understanding the core concepts of video classification"
date: 2021-12-09
author: Daniel Valdez Balderas
author_link: 
preview_image: /images/hugo/i3d_architecture-1639073974.png
post_type: Post
---

Video understanding aims to extract useful information from video. There are many tasks associated with video understanding, including video classification, action detection, video captioning, and action forecasting. Perhaps the simplest and most fundamental of those tasks is video classification. 

Video classification is typically used to decide what kind of event is happening in a video. This is done by assigning a set of scores to the video, each corresponding to a different class. One popular application of video classification is human action recognition, where the classes correspond to actions, and the scores measure how likely it is that the action is being performed in the video.

There are many ways to perform video classification. Within deep learning, the approaches can be broadly divided into two categories, depending on the type of operation used: convolution or attention. Those operations can also be combined in hybrid architectures. The use of  convolutions is inspired by the fact that those operations excel at extracting features from still images, and video consists of images. The use of attention, on the other hand, is motivated by the fact that video is sequential data – and attention is highly effective for processing sequences like natural language.

Here we describe a convolution-based architecture called Two-Stream Inflated 3D ConvNet, or I3D. I3D produced state-of-the art results in 2017. TODO SAY WHY. Though not a recent architecture, I3D is interesting because its simplicity allows shedding light on a conceptual aspect of video understanding, namely the relationship between space (the image-like aspect) and time (the sequence-like aspect) of video. 

Architecture Overview

In essence, I3D is built by converting a deep learning image classifier into a video classifier. This is done in three steps:

Inflation of convolutions. This step takes an image classifier based on 2-dimensional (2D) convolutions, and expands the convolutions from 2 to 3 dimensions. The rationale is that, if 2D convolutions are effective feature extractors for images, then 3-dimensional (3D) convolutions might produce useful features for videos. 
Creation of 2 streams. This step simply duplicates the architecture created in step 1, producing a two-branch architecture. One branch is used to process video frames. The other is used to process optical flow.
Blending. The two branches of the network are trained independently for classification. At test time, they are run separately and their logits added to perform the classification.

The following figure illustrates the two streams of the I3D architecture. On the left is the image stream, and on the right is the flow stream. The input to the image stream consists of all of the K frames that make up the video. The flow stream consists of K optical flow maps, one per each of the K-1 pairs of consecutive frames, plus one between either the first or last frame and a dummy frame. The flow maps are computed using a third-party algorithm which is not part of the deep learning architecture.

The two branches are trained independently of each other in a supervised manner, both for video classification. At test time, the logits of each branch are added before the softmax function that produces the final classification scores.


Illustration of the Two-Stream Inflated 3D ConvNet, or I3D. Image adapted from the original paper.



N-Dimensional Convolutions

One way to think about the dimensionality of convolutions, in the context of deep learning, is to consider the dimensions as the number of directions along which the convolution kernel is slided. This is in contrast with the dimension of the data structure holding the kernel itself. We’ll elaborate on this shortly, by reviewing the well-known 2D convolutions as a starting point, and then expanding on to 3D convolutions.


2 Dimensions

Though usually displayed in two dimensions, color images are typically stored in 3D data structures: two dimensions for space, and one dimension for the color channels. The shape of the data structure is typically represented by a triad of numbers (H, W, C) where H and W are the image height and width, corresponding to the spatial dimension, and C is the number of color channels (e.g., 3 for the RGB image format). Images will typically be processed by a series of convolution and pooling operations, each of which produces a new feature map. Those maps, like images, are also stored in data structures with size (H_l, W_l, C_l)

The following figure illustrates a 2D convolution. The kernel has dimension (k_h=3, k_w=3, C=3). 


Illustration of a 2D convolution. The kernel size in this case is k_h=3, k_w=3, C=3. Image from this blog.

2D convolutions are performed using a kernel (or filter). Kernels, like images and other feature maps, are stored in 3D data structures whose size is represented by another triad, namely (k_h, k_w, C). Here, k_h and k_w are the spatial dimensions of the kernel, and C has the same meaning as above, namely the number of color channels in the image.

Typically the kernel spatial dimensions are smaller than the image height and width: k_h < H and k_w < W. When this is the case, it is necessary to apply the kernel multiple times through the image, in order to extract all the relevant information. In doing that, the kernel can be said to be striding along two dimensions, namely the height and the width of the image. This is what makes the convolution 2D.

Good explanations of 2D convolutional neural networks can be found here.


3 Dimensions

When we go from image to video, we go from 3D to 4D data structures for both the input data and the kernels. The additional dimension corresponds, of course, to time. Being an image, each video frame is stored in a 3D data structure. And when multiple frames are put together to make up a video, a 4D data structure results. The shape of the structure holding the video will now consist of a quadruple: (T, H, W, C), where T is the number of frames in the video, and H, W, and C are the same as above, namely height, width and number of channels. The kernel will now also be stored in a 4D data structure: (k_t, k_h, k_w, C) where k_t is the temporal size of the kernel, and k_h, k_w, C are the same as above, namely the spatial size of the kernel and the number of color channels, respectively. 

Note that, in an analogous manner to the spatial dimensions (k_h, k_w) of the kernel being smaller than the spatial dimensions (H, W) of the frames, the temporal dimension of the kernel is also, in general, smaller than the temporal dimension of the data structure holding the video. This means that, in order to extract useful information from all the video, the kernel needs to be slided along 3 different dimensions: two spatial, and one temporal. And this makes the convolution 3D.


TODO. Replace this figure, borrowed from here, with a better figure, which more clearly shows the difference between temporal and channel directions.

Receptive Field

The size of the receptive field for a feature (in a convolutional neural network) is the size of the region in the input (to the network) that influences the value of that feature. 
For instance, in the simple case of a 2D image as input to a single-layer convolutional neural network with kernel size (k_h, k_w), the receptive field of that layer is identical with the size of the kernel (k_h, k_w) (the color channel dimension is omitted as it does’t impact the receptive field). This is so because, by definition, the feature is produced by a linear combination of the image values in a region of the size of the kernel. 

With an increasing number of layers in the network, the size of the receptive field increases. This is the case because every convolution is combining features which were themselves a combination of features.

In the context of convolutional neural networks, the size of the receptive field (for a layer) can be thought of as the size of the region in the input (to the network) that influences the value of a feature in the layer. It is related to the size of the kernels that are applied. For instance, in the simple case of a 2D image as input to a single-layer convolutional neural network, the receptive field of that layer is identical with the size of the filter. This is so because every feature that is produced by the convolutional layer is affected by the k_h * k_w * C  values from the image that the kernel uses to produce its output.

If the results of the convolution are further put through a pooling operation, the features produced would have a larger field of view, because they would be affected by the results of multiple kernel operations, which combined cover a larger regions of the image than a single kernel operation. A more detailed description can be found here 

In general, as one goes deeper in a convolutional neural network, the field of view increases. For image classification, for instance, the field of view eventually covers the full image, as in the most general case the output (e.g., the probability of a category class) should depend on the full image.

The factors impacting the field of view are the size and stride of convolutional and pooling operations. For images, when performing object detection, for example, it makes sense that the two spatial dimensions are treated equally. This ensures that an object continues to be detected even if it is rotated by an arbitrary angle. This capacity is typically encoded in a network by setting the vertical and horizontal sizes of kernels and strides to the same value. 

Spatial vs Temporal

This means that the vertical direction and the horizontal direction are treated in the same way. However, for video, there is no reason why the kernel and stride sizes in the temporal direction should have the same size as those of the spatial dimension. Spatially, we want to ensure that the algorithm detects a pair of hands. And we might achieve this by having a field of view of, say 300 pixels (if that's the size of the hand in the image). For action recognition, we'd like to be able to detect, e.g., that the hands are clapping. The temporal size of the field of view can be measured in physical time, e.g., seconds. In order to detect, say, clapping hands, the relevant time frame might be seconds. At 25 frames per second, this means that the temporal size of the field of view would be on the order of 25. This example illustrates the fact that for video processing, the spatial and temporal dimensions are not symmetric, and neural network designers need to explore and tune their architectures for optimal size of the field of views, which impacts the size of convolutional kernels and strides.

Another type of 3D input data is that produced by magnetic resonance imaging. In that case, the third dimension is spatial (like the first two dimensions) rather than temporal like in the case of video.

When it comes to video, however, there is no reason to keep the size 

For 2D convolutions, it makes sense that the stride 

Cite 3D convolutions
https://towardsdatascience.com/understanding-1d-and-3d-convolution-neural-network-keras-9d8f76e29610
It is called 2D because the "kernel slides along 2 dimensions on the data as shown in the following image"


BACKBONE

like Inception V1, 

WEIGHT INITIALIZATION

Not only is the I3D architecture inspired by image classifiers, but the value of their pre-trained weights are used as the initial point for training the video classifiers. 


COMPARISON TO OTHER ARCHITECTURES

The paper compares I3D to four other architectures. All but one of them use as backbone a common image classifier, namelyInception V1, pre-trained on ImageNet. Using a common backbone, the comparison between architectures is expected to shed light on the aspects of the architecture morphology that benefit video classification the most, rather than on the backbone itself.

ARCH. 1: 2D ConvNet Only
“The high performance of image classification networks
makes it appealing to try to reuse them with as minimal
change as possible for video. This can be achieved by using
them to extract features independently from each frame then
pooling their predictions across the whole video [15]. This
is in the spirit of bag of words image modeling approaches
[19, 22, 33]; but while convenient in practice, it has the issue
of entirely ignoring temporal structure (e.g. models can’t
potentially distinguish opening from closing a door).”

ARCH. 2: ConvNet+LSTM
“add a recurrent
layer to the model [5, 37], such as an LSTM, which can
encode state, and capture temporal ordering and long range
dependencies. We position an LSTM layer with batch normalization
(as proposed by Cooijmans et al. [4]) after the
last average pooling layer of Inception-V1, with 512 hidden
units. A fully connected layer is added on top for the
Classifier”

...
LSTMs on features from the last layers of ConvNets can
model high-level variation, but may not be able to capture
fine low-level motion which is critical in many cases. It is
also expensive to train as it requires unrolling the network
through multiple frames for backpropagation-through-time”
….
This can be addressed by The Old III: TwoStream
Networks”


ARCH. 3: 3D ConvNets
“3D ConvNets seem like a natural approach to video modeling,
and are just like standard convolutional networks, but
with spatio-temporal filters
they directly create hierarchical representations
of spatio-temporal data. One issue with these
models is that they have many more parameters than 2D
ConvNets because of the additional kernel dimension”

ARCH. 4: Two Stream Networks: 1 image, 10 optical flow frames, all into 2D conv net
“TO overcome the above mentioned limitations of LSTMs on the last layers of conv nets (Daniel’s addition: like hand clapping, by the last layers, the conv nets recognize a human, but cannot distinguish hands in a lot of detail, therefore can miss clapping), 
this method models short temporal snapshots
of videos by averaging the predictions from a single
RGB frame and a stack of 10 externally computed optical
flow frames, after passing them through two replicas of an
ImageNet pre-trained ConvNet. The flow stream has an
adapted input convolutional layer with twice as many input
channels as flow frames (because flow has two channels,
horizontal and vertical), and at test time multiple snapshots
are sampled from the video and the action prediction is averaged.
This was shown to get very high performance on
existing benchmarks, while being very efficient to train and
test.”




Datasets


asdf

Name
Year
Classes
Clips per Class
Length (sec)
Size GB
Total Clips
UCF101
2013
101
100-150
4-18
7
13,320
kinetics400
2017
400
250-1000


460
306,245
kinetics600
2018
600
450-1000
10
720
480,000
kinetics700_2020
2020
700
700
10
950
635,200


asdf



Other Resources

https://towardsdatascience.com/understanding-the-backbone-of-video-classification-the-i3d-architecture-d4011391692




