from django import template
register = template.Library()


@register.filter(name='classify_spread')
def classify_spread(classify_first_id, show_id):
    if classify_first_id == show_id:
        return 'in'
    return ''

