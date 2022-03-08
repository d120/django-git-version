import logging
from django import template
from git import Repo

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def current_commit(path):
    try:
        repo = Repo(path)
        commit = repo.commit()
        chash = commit.hexsha
        repo.__del__()
        return chash
    except Exception as e:
        logger.debug(f"Failed to find current commit for {path}")
        logger.debug(f"Exception was: {e}")
        return "no git?"


@register.simple_tag
def current_commit_short(path):
    return current_commit(path)[:8]
