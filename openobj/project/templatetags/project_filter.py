from django import template

from project.models import Project

register = template.Library()


@register.filter(name='classify_spread')
def classify_spread(classify_first_id, show_id):
    if classify_first_id == show_id:
        return 'in'
    return ''


@register.filter(name='difficulty')
def difficulty(difficulty):
    for diff in Project.DIFF_TYPE:
       if diff[0] == difficulty:
           return diff[1]
    return difficulty


@register.filter(name='code_pattern')
def code_pattern(code_pattern):
    for code in Project.CODE_PATTER:
       if code[0] == code_pattern:
           return code[1]
    return code_pattern

@register.filter(name='repository')
def repository(repository):
    for rep in Project.REPOSITORY:
        if rep[0] == repository:
            return rep[1]
    return repository
