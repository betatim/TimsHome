Title: TIL: A Python module from which you can import anything
date: 2021-11-17
slug: python-module-import-anything

_[What is a TIL?](../til-explained)_

Today I learnt how to make a Python module from which you can import anything.

[Yuvi asked](https://twitter.com/yuvipanda/status/1460630086319702017) if you
can write a Python module that will allow anything to be imported from it. A bit
like `from idealmock import whatever, does_not_exist`.

I thought "how hard can it be?" and off I went to find out.

The answer is that it is not very hard to do. I first read about the [import
machinery of Python](https://docs.python.org/3/reference/import.html), learnt
a bit about [`importlib`](https://docs.python.org/3/library/importlib.html) and
in the end the solution had nothing to do with all that.

It is surprisingly simple:

```python
def __getattr__(name):
    pass
```

If you put this code in your module, say `blackhole.py` you can import
anything you want from it: `from blackhole import something, does_not_exist`
or you can import the whole module and then access anything you want:
`import blackhole; blackhole.something`.

It is pretty neat.

If you want to learn more about module level `__getattr__` and some real world
use cases checkout [PEP 562 -- Module `__getattr__` and `__dir__`](https://www.python.org/dev/peps/pep-0562/)
which has a nice trick for dealing with deprecated functions in it.
