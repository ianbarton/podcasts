#!/usr/bin/env python
import listparser as lp

d = lp.parse("podcasts_opml.xml")

f = open('podcasts.org', 'w')
f.write('|-|-|\n')
f.write('|url|Title|\n')
f.write('|-|-|\n')
for podcast in d.feeds:
    f.write('|%s| %s|\n' % (podcast.url.encode('utf8'), podcast.title.encode('utf8')))
f.write('|-|-|\n')

f.close()
