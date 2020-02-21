Title: Thoughts on collective thinking
date: 2020-02-22
slug: thoughts-on-collective-thinking

This post is about a tool to create a web of knowledge for your team. A tool to
help you to think things through together. A tool that helps keep everyone in
the loop. This tool is your issue tracker.

What features do you look for in an issue tracker for your team or whole company?
Think about it for a moment. Have you thought of three? Good.

Here are the top three items I look at when evaluating a system:
* how much screen real estate is given to reading and writing comments
* how well does the notification system work for power users
* how good is the automatic cross referencing support

There are many more things I care about but I either take them as a given for
any serious contender (full API access, markdown based message formatting)
or they are less important, after all not everything can be in the top three.

The issue tracker will become a primary tool for creating a collective memory
of why you did what you did in a project. In order for this to happen it has to
be a tool that helps your team to think things through together. When this
happens in your issue tracker you create a history of what got done, what didn't get
done and most importantly why.


## Screen real estate

The primary task people accomplish in an issue tracker is reading what other
people have written. In a team with ten active members you will spend nine tenths
of your time reading what other people have written. Only 10% of your time will
be writing new things. There are also other tasks to accomplish as a user of the
issue tracker but they all require you to first read or write something.

This means the user interface has to be optimised first for reading, second for writing,
and only then for labelling, triaging, tracking, progress reporting, sprint planning, and
all the other tasks people perform in an issue tracker.

Everyone agrees that the content of the top part of a webpage (above the fold) is
the most important part. This means when evaluating an issue tracker look at how
much of the content of an issue you can read after opening a ticket, without
first having to scroll.

Often the first items shown are status, assignee, priority, size, creation date,
parent or sub-tasks, deadlines and a whole host of other trivia about the issue
that does not help you with reading the content of the issue. All this information
does not help you to quickly scan the content of the issue.


## A notification system for power users

You might not know it yet but you will become a power user of your issue
tracker's notification system. It is the team's primary place to get thinking
done. A team of a few (or more) people does a lot of thinking. This means you
will receive a lot of notifications or have to find some other way of staying
on top of what is going on.

In order to create the collective memory and shared understanding of why and what is
being done you will receive notifications about things which you only have to
be aware of, not act on. Knowing what others are working on or discussing gives
you context. Having briefly seen issues that tell you that Jill and Jim are
working on the spine reticulator means when someone reports that it isn't working
anymore you have an idea where to start looking.

To deal with receiving a lot of notifications, most of which are there to keep
you in the loop you need to be able to decide from just the content of the
notification: can I act on this issue right now or is it something that will
require more than two minutes?

Most of the time acting on a notification means quickly scanning it and then
marking it as done. Minimising the number of clicks required to do this is
important.


## Forward and backward cross referencing

Someone with a lot of experience has "a web of knowledge". Lots of little bits
of information that have links between each other. Experience and knowledge is
not just a box of random, unconnected facts. It is a set of facts which are
related to each other.

To turn your issue tracker from a box of random issues with no context into a
web of knowledge you need to create links between them. This is why the hyperlink
got invented. Most issue trackers let you create forward links by referring to
other issues. This creates a link from A to B and A to C.

For your web of knowledge to really take off you also want to have links from
C to A and from B to A. Someone reading issue B should see that it was referred
to by other issues. A really good issue tracker automatically adds these backward
references.


## Things that don't matter

Things like tagging, assigning people, priorities, size estimates, sub-tasks,
boards, burn down charts, and so on are nice but less important than features
that help you accomplish the number one task you will be doing: reading what
other people have written.

These are nice to haves and create second order benefits. However they are not
very useful if you don't have the basics covered first.


## A recommendation

My current favourite issue tracker is the one that comes with GitHub
repositories. I don't get any money or other benefits for recommending them.

Before you turn away because your project is not a software project: people use
GitHub issues to organise a whole variety of projects, not just software based
ones. For example Mozilla used it to organise [the MozFest 2018 program](https://github.com/MozillaFestival/mozfest-program-2018).


## Conclusion

Your issue tracker is a very important tool for creating the web of
knowledge amongst your team. Most of your time is spent reading and writing,
how good is your issue tracker at helping you do that?
