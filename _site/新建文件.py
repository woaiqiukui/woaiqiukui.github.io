# -*- coding: utf-8 -*
import datetime

module = """---
layout: post
title: {}
category: ['Learning']
---"""

filename_old = "{}-"

f = open('URL集合.txt')
urls = f.readlines()
i = 0
now=datetime.datetime.now()
delta=datetime.timedelta(days=1)
for url in urls:
    now += delta
    i += 1
    filename = filename_old.format(now.strftime("%Y-%m-%d")) + str(i) + '.md'
    file = open('_posts/' + filename,'a')
    file.write(module.format(i) + '\n\n')
    file.write(url + '\n\n')
    file.close
f.close()