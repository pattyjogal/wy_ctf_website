from django.template import Library

register = Library()
@register.filter(name='score_iter')
def score_iter(value):
    total = 0
    for score in value:
        total += score.value
    return total

@register.filter
def in_category(qs, category):
    return qs.filter(category=category)

@register.filter
def solved_problem_tag(user, challenge):
    print(user.completed_challenges.all())
    print(challenge)
    if challenge in user.completed_challenges.all():
        return 'success'
    else:
        return 'danger'
