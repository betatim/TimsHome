Title: Jupyterhub backed by Carina!
date: 2015-11-25
slug: jupyterhub-carina

This post explains how you can setup [jupyterhub][] to serve notebooks
from a computer owned by your visitors. Sounds confusing? Bare with
me.

In a traditional setup the person hosting the jupyterhub instance has
to provide the compute power for all users. This means you have to have
enough resources for that [Peter Norvig](http://norvig.com/) moment, when
a large number of users suddenly wants to execute Norvig's latest notebook.

However jupyterhub is extremely modular, so I wrote a replacement for
the authentication and process spawning parts that allow jupyterhub to
launch the notebooks on computing resources owned by the visitor. If every
user brings their own resources, you can never run out. Perfect scalability!


## The Code

If you know about [carina][] and [jupyterhub][] already, head stright
over to
[carina-jupyterhub](https://github.com/betatim/carina-jupyterhub) for
the code.


## Got Carina?

[Carina][carina] is _an easy-to-use, instant on, native container
environment_ made by [rackspace](http://www.rackspace.com/). With a few
clicks you can create a cluster and then launch [docker](//docker.com)
containers on that cluster.

Once the cluster is running you interact with it via a docker
endpoint. Jupyterhub already has a mechanism for spawning notebooks
in docker containers so with a bit of hacking we can use a different
docker endpoint for each user.


## How do I use it?

When users visit your jupyterhub instance they are greeted by a page
asking them to upload their carina credentials and type in a
username. The username is used to allow people to launch several
notebooks on one cluster if they wish. So maybe it should be a
notebook-name instead.

Once we have their credentials jupyterhub can launch the notebook
container on that cluster. Hook up a proxy route to it, et voila!

Sign up for a [carina][] account, download the credentials file for your cluster, and head on over to [http://172.99.78.68:8000/hub/login](http://172.99.78.68:8000/hub/login) to give it a go.


## Why?

I have been tinkering a lot recently with differnet approaches to
reusing and sharing research code. My current best idea is [project
everware][http://everware.xyz]: use a docker container to run your
research code and it becomes trivial for others to try it out without
ever having to install anything.

Everware provides a way for you to say "launch Tim's code in the cloud
and let me try it!". A very similar project is
[binder](//mybinder.org). The drawback of both is that the person
hosting the everware or binder instance has to provide all the
computing power. Which can be quite challenging if you use it for a
popular tutorial session, a notebook written by Peter Norvig, or an
analysis project based on LHC data.

All these require large amounts of computing, which is a nice way of
saying it costs a lot of money. So allowing your users to bring their
own computing power is pretty cool. Potentially your users already
have access to large amounts of computing via their university or
employer. In addition a lot of compute intensive research also
processes large amounts of data, so you want to run the computation
"close to" the data. Imagine having to transfer a few 100GB across the
network each time you launch your code.

In all these scenarios you want your users to be able to bring their
own computing power and privileges. [carina-jupyterhub](https://github.com/betatim/carina-jupyterhub) is a first attempt at making this possible.

[Try it](http://172.99.78.68:8000), [fork it](https://github.com/betatim/carina-jupyterhub#fork-destination-box), [star it](https://github.com/betatim/carina-jupyterhub/stargazers), tell me what is broken!

[jupyterhub]: //github.com/jupyter/jupyterhub
[carina]: //getcarina.com