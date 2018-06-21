from django import template
from git import Repo

register = template.Library()

@register.simple_tag
def current_commit(path):
    repo = Repo(path)
    commit = repo.commit()
    chash = commit.hexsha
    repo.__del__()
    return chash

@register.simple_tag
def current_commit_short(path):
    return current_commit(path)[:8]
