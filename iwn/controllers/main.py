# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, Response, request, current_app, render_template, jsonify, g
from iwn.extensions import cache
from iwn.articles import mention


main = Blueprint('main', __name__)

@main.route('/')
@cache.cached(timeout=1000)
def index():
    return render_template('en-home.jinja')

@main.route('/about')
@cache.cached(timeout=1000)
def about():
    return render_template('en-about.jinja')

@main.route('/howto')
@cache.cached(timeout=1000)
def howto():
    return render_template('en-howto.jinja')

@main.route('/articles')
def articles():
    g.posts = current_app.iwn.current()
    return render_template('en-posts.jinja')

@main.route('/publish')
def publish():
    return render_template('en-howto.jinja')

@main.route('/static/<path:path>')
def static_proxy(path):
    return main.send_from_directory('static', path)

@main.route('/domain/<domain>')
def domain(domain):
    """Locate the given domain in our database and
    render an info page for it.
    """
    current_app.logger.info('domain [%s]' % domain)
    g.domain = current_app.iwn.domain(domain)
    if g.domain is None:
        return Response('', 404)
    else:
        return render_template('domain.jinja')

@main.route('/post/<postid>')
def domainPosts(postid):
    """Locate the requested domain / postid in our database
    and render an info page for it.
    """
    current_app.logger.info('post [%s]' % postid)
    g.post = current_app.iwn.post(postid)
    if g.post is None:
        return Response('', 404)
    else:
        return render_template('post.jinja')

@main.route('/webmention', methods=['POST'])
def webmention():
    current_app.logger.info('webmention [%s]' % request.method)
    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')
        # vouch  = request.form.get('vouch')

        current_app.logger.info('webmention [{source}] [{target}]'.format(source=source, target=target))

        if '/publish' in target:
            r = mention(source, target)
            response                     = jsonify(r)
            response.status_code         = 201
            response.headers['location'] = 'https://indieweb.news/posts/{postid}'.format(**r)

            return response
