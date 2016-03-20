# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import json
from flask import current_app


class IndieWebNews():
    def __init__(self, keyBase):
        self.keyRoot = '%sindienews-' % keyBase

    # execute the query
    def query(self, sql, args=()):
        cur  = current_app.dbStore.cursor()
        cur.execute(sql, args)
        rows = [dict(r) for r in cur.fetchall()]
        return rows

    # execute the query
    # return either a single dictionary item or a list of rows
    def run(self, sql, params=None):
        cur = current_app.dbStore.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        current_app.dbStore.commit()

    def domain(self, domain):
        d = { 'domain':    domain,
              'created':   None,
              'updated':   None,
              'postCount': 0,
              'posts':     [],
            }
        r = self.query('select * from domains where domain = "{domain}"'.format(domain=domain))
        if len(r) > 0:
            d['created']   = r[0]['created']
            d['updated']   = r[0]['updated']
            posts = []
            l    = self.query('select postid from posts where domain = "{domain}"'.format(domain=domain))
            for item in l:
                postid = item['postid']
                current_app.logger.info('post {postid}'.format(postid=postid))
                p = self.query('select * from posts where postid = "{postid}"'.format(postid=postid))
                d = {}
                if len(p) > 0:
                    for key in p[0].keys():
                        if key in ('comment', 'parsed'):
                            d[key] = json.loads(p[0][key])
                        else:
                            d[key] = p[0][key]
                print d
                posts.append(d)
            d['posts']     = posts
            d['postCount'] = len(posts)
        return d

    def post(self, postid):
        current_app.logger.info('post info [%s]' % postid)
        p = self.query('select * from posts where postid = "{postid}"'.format(postid=postid))
        d = {}
        if len(p) > 0:
            for key in p[0].keys():
                if key in ('comment', 'parsed'):
                    d[key] = json.loads(p[0][key])
                else:
                    d[key] = p[0][key]
        return d

    def domains(self):
        p = self.query('select * from domains')
        return p

    def current(self):
        posts = []
        l     = current_app.dbRedis.lrange('indienews-recent', 0, -1)
        current_app.logger.info('pulling current items %d' % len(l))
        for postid in l:
            current_app.logger.info('post {postid}'.format(postid=postid))
            p = self.query('select * from posts where postid = "{postid}"'.format(postid=postid))
            d = {}
            if len(p) > 0:
                for key in p[0].keys():
                    if key in ('comment', 'parsed'):
                        d[key] = json.loads(p[0][key])
                    else:
                        d[key] = p[0][key]
            print d
            posts.append(d)
        current_app.logger.info('%d items found' % len(posts))
        return posts
