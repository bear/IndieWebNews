# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, Response, request, jsonify, current_app, render_template, g
from iwn.extensions import cache
from iwn.articles import mention


main = Blueprint('main', __name__)

@main.route('/')
@cache.cached(timeout=1000)
def index():
    return render_template('home.jinja')

@main.route('/static/<path:path>')
def static_proxy(path):
    return main.send_from_directory('static', path)

@main.route('/about')
def testing():
    return render_template('about.jinja')

@main.route('/domain/<domain>')
def domain(domain):
    """Locate the given domain in our database and
    render an info page for it.
    """
    current_app.logger.info('domain [%s]' % domain)
    g.domain = current_app.palala.domain(domain)
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
    g.post = current_app.palala.post(postid)
    if g.post is None:
        return Response('', 404)
    else:
        return render_template('post.jinja')

@main.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')
        # vouch  = request.form.get('vouch')

        current_app.logger.info('submit [%s] [%s]' % (source, target))

        r = mention(source, target)
        if r is None:
            response             = jsonify({ "error": "submitted URL cound not be found within target URL"})
            response.status_code = 400
        else:
            response                     = jsonify(r)
            response.status_code         = 201
            response.headers['location'] = 'http://indieweb.news/posts/{domain}/{postid}'.format(**r)
        return response
    else:
        return render_template('submit.jinja')

@main.route('/webmention', methods=['POST'])
def webmention():
    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')
        # vouch  = request.form.get('vouch')

        current_app.logger.info('webmention [{source}] [{target}]'.format(source=source, target=target))

        if '/publish' in target:
            return mention(source, target)
