# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, render_template
from iwn.extensions import cache


en = Blueprint('en', __name__)

@en.route('/en')
@cache.cached(timeout=1000)
def index():
    return render_template('en-home.jinja')

@en.route('/about')
def testing():
    return render_template('en-about.jinja')
