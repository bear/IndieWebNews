IndieWeb News

[![Circle CI](https://circleci.com/gh/bear/indiewebnews.svg?style=svg)](https://circleci.com/gh/bear/indiewebnews)
[![Requirements Status](https://requires.io/github/bear/indiewebnews/requirements.svg?branch=master)](https://requires.io/github/bear/indiewebnews/requirements/?branch=master)
[![codecov.io](https://codecov.io/github/bear/indiewebnews/coverage.svg?branch=master)](https://codecov.io/github/bear/indiewebnews?branch=master)

An aggregator of IndieWeb articles and news

## FAQ

#### Wait! Isn't this the same thing as http://news.indiewebcamp.com ?!?

Kinda sorta yes - when I was thinking about what I could do to both use the Python based tools I've been working on for IndieWeb (Ronkyuu, Kaku and others) I looked at a lot of the sites and tools others had created and did not see anything dealing with aggregation of news and posts. I had not yet seen Aaron's site at all. Heck when I started working on this and others were asking "won't this get confused with the news site?" I thought they were talking about http://indiewebcamp.com/news and the weekly email!

So yea, I eventually figured it out and was seriously bummed out :/

But then Aaron nicely pointed out that the community doesn't have a Planet type site yet and I also realized that having a news aggregation site written in Python isn't exactly a bad thing...

So I renamed the repo (I have personal use for the name palala still) and this repo is the result.

## Local Development Environment

Currently I'm assuming an OS X environment as that is what I am using...

```
pyenv install 2.7.11
pyenv virtualenv 2.7.11 indiewebnews
make install-tests
````

Testing the webmention handler - this assumes that you have a `/etc/hosts` entry to make indieweb.news to 127.0.0.1

```
./sm.py http://webmention.tools/test1.html
```
