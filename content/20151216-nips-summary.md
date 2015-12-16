Title: A Physicist at NIPS2015
date: 2015-12-16
slug: physics-does-nips

Last week I attended the second half of [NIPS 2015](//nips.cc). It was
great! I am an experimental particle physicist, not a professional
machine-learning guy. This was the first time I went to NIPS and it
was very different from big conferences I have experienced in particle
physics.

This post is a summary of my impressions, and a reading list of sorts.

<img alt="A physicist's view of NIPS" src="/images/inception-deep-learning.jpeg" title="A physicist's view of NIPS" style="width: 400px;">
<figcaption><em>A physicist's view of NIPS. Image Credit: Googler Mike Tyka’s </em><a href="https://photos.google.com/share/AF1QipPX0SCl7OzWilt9LnuQliattX4OUCj_8EP65_cTVnBmS1jnYgsGQAieQUc1VQWdgQ?key=aVBxWjhwSzg2RjJWLWRuVFBBZEN1d205bUdEMnhB" rel="nofollow">Inceptionism Library</a></figcaption>


## Conference format

NIPS takes place from Monday to Saturday. The first day is tutorials,
and the last two are dedicated to workshops. On all other days the
conference operates in single track mode. There are a few longer talks
each day but the majority of the time is dedicated to "spotlight"
talks. These are three minute long talks about a selected few of the
day's posters. Then there are the epic poster sessions each day.

The workshops are organised by "outsiders" (not conference
organisers), and there are a lot of them in parallel.

Overall about 3700 people attended the conference.


## Business

I was not just a tourist in machine-learning wonderland, I had to do
some work as well. I gave an invited talk at the [ALEPH
workshop](//yandexdataschool.github.io/aleph2015/) on Friday. In the
same workshop [Gilles](https://twitter.com/glouppe) talked about some
work we did together: [Pitfalls of evaluating a classifier's
performance in high energy physics
applications](https://github.com/glouppe/talk-aleph-workshop2015).

More physicists should go and give talks at NIPS. You can learn a lot,
make connections to people you would not otherwise meet, and have your
mind blown by the craze that is deep learning.

Particle physics (HEP) has hard and interesting problems to solve. Attracting
the skills of the machine learning community would be great. HEP would make
progress faster, and it would spark interesting research for the NIPS
community. Right now the barrier to entry to HEP is extremely high though.
We should work on fixing that.


## Posters, posters, posters

The first surprise was that how many poster sessions there are at NIPS
and how well attended they are.

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">4 nights in a row, 100 posters per night, from 7pm till 11pm, <a href="https://twitter.com/hashtag/nips2015?src=hash">#nips2015</a> poster session. <a href="https://t.co/NOxPzzwdhu">https://t.co/NOxPzzwdhu</a> <a href="https://t.co/VPS7abv3Yy">pic.twitter.com/VPS7abv3Yy</a></p>&mdash; Tim Head (@betatim) <a href="https://twitter.com/betatim/status/674786498076655616">December 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Given the conference format, it makes sense, but it was still surprising
for me. At most physics conferences the focus is on short talks in parallel
sessions.

I enjoyed having the opportunity to ask really dumb questions to the
poster presenters without having to reveal my ignorance to a room full
of experts. I tried to prepare for the two poster sessions I was in town
for by reading the abstracts for that session. It helped, but I would have
had to do a lot mroe studying for it to be really useful. Just walking around
and reading the introduction to each poster turned out to be quite a good
strategy. I usually ran out of posters before the session was over.


## Free stuff

The other big differnce was how many people from industry attended the
conference. Basically everywhere you saw someone wearing something branded
by Google DeepMind or FAIR.

There were also a lot of parties or dinners organised by companies. This
does not happen at physics conferences. I am sure if you wanted to you
could have eaten and drunk for free all week. Ideal for grad students?!?


> Below follows a collection of things I found interesting or want to
> investigate further. It is half todo list, and half recommendations.

## Workshops

There are a lot of them. Interesting thoughts about how to [organise coopetitions if the aim is to produce and share new knowledge](http://ciml.chalearn.org/). The [ALPEH Workshop](http://yandexdataschool.github.io/aleph2015/), not just because I gave a talk there ... [Bayesian optimisation](http://bayesopt.com/), we optimise everything! [Reasoning, attention, memory](http://www.thespermwhale.com/jaseweston/ram/), did not attend but looking forward to videos. [Transfer learning](https://sites.google.com/site/tlworkshop2015/), what if training and testing densities are not the same (also known as: my simulator is not perfect!!).


## Reading list

This is a unordered list of posters, talks or otherwise interesting things
that ended up on my reading list. [karpathy](https://twitter.com/karpathy)'s [machine-learning powered overview of the NIPS papers](http://cs.stanford.edu/people/karpathy/nips2015/).

* [Pointer
  networks](http://papers.nips.cc/paper/5866-pointer-networks), solve
  the travelling salesman problem, and other problems where the length
  of the output sequence is not known. Useful for track reconstruction?

* [Efficient and Robust Automated Machine Learning](http://papers.nips.cc/paper/5872-efficient-and-robust-automated-machine-learning), automatic machine learning made easy. [auto-sklearn](https://github.com/automl/auto-sklearn), let the machine tune itself.

* [Semi-supervised Learning with Ladder Networks](http://papers.nips.cc/paper/5947-semi-supervised-learning-with-ladder-networks), looked at the poster, listened to a talk, started reading the paper and still I am confused. Very interesting though as LHCb has huge amounts of unlabelled data.

* [Efficient Non-greedy Optimization of Decision Trees](http://papers.nips.cc/paper/5886-efficient-non-greedy-optimization-of-decision-trees) Decision trees are usually iduced in a greedy fashion. What are the advantages of this approach?

* [Convolutional Networks on Graphs for Learning Molecular Fingerprints](http://papers.nips.cc/paper/5954-convolutional-networks-on-graphs-for-learning-molecular-fingerprints), how to deal with graphs of unknown length and perform learning on them. They applied it to predicting properties of molecules, could be useful for track reconstruction?

* [Generalization in Adaptive Data Analysis and Holdout Reuse](http://papers.nips.cc/paper/5993-generalization-in-adaptive-data-analysis-and-holdout-reuse) "Thresholdout", differential privacy allows you to reuse your holdout set. How does this compare to nested cross-validation?

* [End-To-End Memory Networks](http://papers.nips.cc/paper/5846-end-to-end-memory-networks), I understand very little about what they do, but it got a lot of attention.

* [Hidden Technical Debt in Machine Learning Systems](http://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems), complicated pipelines of sophisticated algorithms incure technical debt, ya don't say!

* [Deep Convolutional Inverse Graphics Network](http://papers.nips.cc/paper/5851-deep-convolutional-inverse-graphics-network), how is it that humans can recognise a face in completely different lighting conditions and a new pose after seeing it only once? Take a look at Tenenbaum's [other submissions](http://papers.nips.cc/author/josh-tenenbaum-6308) as well and [this article](http://www.sciencemag.org/content/350/6266/1332.full) in Science.

* [Spatial Transformer Networks](http://papers.nips.cc/paper/5854-spatial-transformer-networks), a network module that cna larn to undo spatial transformations before classification. Presenting upside-down digits to your network? Plug in this module which will orientate them correctly and then classify them. Check out the [lasagne code](https://github.com/skaae/recurrent-spatial-transformer-code).

* Bunch of leftovers: [http://papers.nips.cc/paper/5653-a-recurrent-latent-variable-model-for-sequential-data](),
 [http://papers.nips.cc/paper/5883-consistent-multilabel-classification](),
 [http://papers.nips.cc/paper/5773-deep-generative-image-models-using-a-laplacian-pyramid-of-adversarial-networks](),
 [http://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend](),
 [http://papers.nips.cc/paper/5881-optimization-monte-carlo-efficient-and-embarrassingly-parallel-likelihood-free-inference]()

All accepted papers are listed here: [Advances in Neural Information Processing Systems 28](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-28-2015)