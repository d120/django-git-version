# django-git-version

A simple django app that uses [gitpython](https://gitpython.readthedocs.io/) to provide
templatetag(s) to display git version info from the current repo.

## Installation

First, install this package using `pip`

```
$ pip install django-git-version
```

then add `git_version` to `INSTALLED_APPS` in your Django `settings.py`:

```python
INSTALLED_APPS = (
    ...
    'git_version'
    ...
)
```

## Usage

Load the templatetag with

```django
{% load git_tags %}
```

and then use one of

```django
{% current_commit_short '.' %}
{% current_commit '.' %}
```

Where `'.'` is the path to the git repo
