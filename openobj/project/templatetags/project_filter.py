from django.templatetags.static import register
from django import template


@register.filter(name='classify_spread')
def classify_spread(classify_first_id):
    return True

