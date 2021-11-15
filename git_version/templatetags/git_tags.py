from django import template
from git import Repo

register = template.Library()

@register.simple_tag
def current_commit(path):
    try:
        repo = Repo(path)
        commit = repo.commit()
        chash = commit.hexsha
        repo.__del__()
        return chash
    except Exception:
        print(f"git_version - trouble with repo path {path}")
        return "no git?"

@register.simple_tag
def current_commit_short(path):
    return current_commit(path)[:8]
