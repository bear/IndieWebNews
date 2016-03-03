# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, current_app, jsonify
from flask_restful import Resource, Api


api     = Blueprint('api', __name__)
restApi = Api(api)

class PostList(Resource):
    def get(self):
        d             = current_app.iwn.current()
        print d
        r             = jsonify({ 'posts': d })
        r.status_code = 200
        return r

class DomainList(Resource):
    def get(self):
        d             = current_app.iwn.domains()
        r             = jsonify({ 'domains': d })
        r.status_code = 200
        return r

class Domain(Resource):
    def get(self, domain):
        d             = current_app.iwn.domain(domain)
        r             = jsonify(d)
        r.status_code = 200
        return r
class Post(Resource):
    def get(self, postid):
        post          = current_app.iwn.post(postid)
        r             = jsonify(post)
        r.status_code = 200
        return r

restApi.add_resource(PostList,   '/v1/posts')
restApi.add_resource(DomainList, '/v1/domains')
restApi.add_resource(Domain,     '/v1/domains/<domain>')
restApi.add_resource(Post,       '/v1/posts/<postid>')
