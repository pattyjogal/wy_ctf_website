from django.template import Library

register = Library()
@register.filter(name='score_iter')
def score_iter(value):
    total = 0
    for score in value:
        total += score.value
    return total
