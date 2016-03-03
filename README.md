IndieWeb News

[![Circle CI](https://circleci.com/gh/bear/indiewebnews.svg?style=svg)](https://circleci.com/gh/bear/indiewebnews)
[![Requirements Status](https://requires.io/github/bear/indiewebnews/requirements.svg?branch=master)](https://requires.io/github/bear/indiewebnews/requirements/?branch=master)
[![codecov.io](https://codecov.io/github/bear/indiewebnews/coverage.svg?branch=master)](https://codecov.io/github/bear/indiewebnews?branch=master)

An aggregator of IndieWeb articles and news

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
