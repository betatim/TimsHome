TimsHome
========

This is the source of [Tim Head's blog](http://betatim.github.io). It is built
using the [Pelican](http://blog.getpelican.com/) blogging platform.


Requirements
------------

- make a new virtualenv, then run `pip install -r requirements`

- install `pandoc`

- Recent version of [IPython](http://github.com/ipython/ipython).  The
  liquid_tags plugin requires IPython 1.0.  Note that previously this
  could be built with the stand-alone nbconvert package.  That no
  longer works with the recent liquid_tags plugin.

- Recent version of [Pelican](http://github.com/getpelican/pelican).
  For the static paths (downloads, images, figures, etc.) to appear in
  the right place, Pelican 3.3+ must be used.
