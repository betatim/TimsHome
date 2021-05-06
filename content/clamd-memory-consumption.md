Title: TIL: Limiting clamav memory usage
date: 2021-05-06
slug: clamav-memory-usage

Today I learnt how to limit [clamd's](https://www.clamav.net/) memory consumption.

The `clamd` process uses a lot of memory (about 1GB) because it loads the
complete database of virus definitions into memory. This allows it to be super
fast.

When deploying this to a kubernetes cluster we want to set a memory limit. I
naively set the limit to just over 1GB. This worked well for normal operations.
However once in a while the `clamd` process would get killed. It turns out
it would always get killed when reloading the database after an update.

This is due to the fact that during a database reload clamd will load the new
DB first and then drop the old one. This concurrent database reload strategy
allows it to keep scanning files while loading the new database. The drawback
is that it requires twice as much memory as during normal operations. As a
result the clamd process would keep getting killed.

Starting from
[ClamAV 0.103.0](https://blog.clamav.net/2020/09/clamav-01030-released.html)
you can set `ConcurrentDatabaseReload no` in your `/etc/clamav/clamd.conf`
to disable this behaviour.
