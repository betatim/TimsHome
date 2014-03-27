title: Science

Have you noticed that the universe is full of matter and surprisingly
little antimatter? Why this is so is one of the main questions the
scientists of the [LHCb experiment][lhcb] hope to answer. I am one of
them.

I have been a [CERN][] research fellow since October 2012. Along
side my research, I spend a significant amount of time designing and
implementing pattern recognition algorithms. This code will be used in
the real time processing of the experiment's data, so performance is
key. I also think about how we can record as much data as possible.

[CERN]: http://cern.ch

I am leading the team working on the reconstruction and simulation
software for the upgrade [Vertex Locator][velo] (VELO) and am one of
the editors of the [Technical Design Report][velotdr]. We use
simulations to find the best design of the VELO, as well as optimising
the performance of the reconstruction software.

When running at full steam the detectors produce around 2 TB/s of
data, unfortunately we can not afford to record all of this. Reducing
the data volume is the job of the trigger system which processes the
data in real time. To do this it classifies data as "interesting" or
"boring". The more information it has when making this decision the
better.

A successful trigger system will be better than the sum of its
parts. I work on evaluating what the different parts of the experiment
have to offer and how to best combine them. All the while keeping in
mind what research we want to do, as this dictates what is
"interesting" and what is "boring".

Before coming to CERN I was a particle physics graduate student with
[The University of Manchester][man]. My research focused on properties
of [top quarks][topquark] using the vast data set from the [D0
detector][d0] at Fermilab's [Tevatron][tev] near Chicago. I defended
my thesis in December 2012

[topquark]: http://en.wikipedia.org/wiki/Top_quark
[d0]: http://www-d0.fnal.gov/public/index.html
[tev]: http://en.wikipedia.org/wiki/Tevatron
[man]: http://www.hep.manchester.ac.uk/


##Publications

Here is a list of my top publications and other science related
documents. My PhD thesis is linked to at the bottom as well. Take a look at the
[full list of my publications][inspire] on INSPIRE.

[inspire]: https://inspirehep.net/author/profile/T.Head.1

###LHCb VELO Upgrade Technical Design Report

[PDF][velotdr]

I am the team leader for the simulation and reconstruction software project
and was responsible for the Module layout and Performance chapters of the report.

###Measurement of Leptonic Asymmetries and Top Quark Polarization in tt̅ Production

[Phys.Rev. D87 (2013) 011103][afb]

I performed the whole analysis: writing the code to select events,
compare simulation to data and perform the statistical
analysis. Wrote the final paper and shepherded the paper through
internal collaboration review.

###Measurement of spin correlation in tt̅ production using dilepton final states

[Phys.Lett. B702 (2011) 16-23][spin]

I wrote the code to select events, compare simulation to data and
perform the statistical analysis, edited the paper and shepherded the
paper through internal collaboration and journal review.
 
###Measurement of spin correlation in tt̅ production using a matrix element approach

[Phys.Rev.Lett. 107 (2011) 032001][spinmatrix]

I prepared the data and Monte Carlo samples, planned analysis
strategies and lead discussions with theorists. Created the final
figures used in the paper.


###Evidence for spin correlation in tt̅ production

[Phys.Rev.Lett. 108 (2012) 032004][spincombo]

I took part in planning and discussions in our four person team on
extending our previous analysis to this new final state, lead
interactions with theorists. I created the final figures used in the
paper.


###A measurement of the WZ and ZZ production cross sections using leptonic final states in 8.6 fb<sup>-1</sup> of pp̅ collisions

[arXiv:1201.5652][wzzz]

This analysis uses a multivariate classifier to identify electrons
which I proposed and implemented, with efficiency gains of ~10% per
electron over previous algorithms. These are the most precise WZ and
ZZ cross section measurements at sqrt(s)=1.96TeV to date.

###Thesis: Top Quark Spin Correlations and Leptonic Forward-Backward Asymmetries at D0

[inspire entry][thesis]

A summary of all my work as a PhD student, my thesis. Only print it
off if you need a door stop, otherwise read it on your screen.

[lhcb]: http://lhcb-public.web.cern.ch/lhcb-public/
[thesis]: http://inspirehep.net/record/1222578
[spin]: http://arxiv.org/abs/1103.1871
[spinmatrix]: http://arxiv.org/abs/1104.5194
[spincombo]: http://arxiv.org/abs/1110.4194
[wzzz]: http://arxiv.org/abs/1201.5652
[afb]: http://arxiv.org/abs/1207.0364
[velotdr]: http://cds.cern.ch/record/1624070
[velo]: http://en.wikipedia.org/wiki/LHCb#The_VELO