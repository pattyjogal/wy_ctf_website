from django.template import Library

register = Library()
@register.filter(name='score_total')
def score_total(user):
    total = 0
    challenges = user.completed_challenges.all()
    for challenge in challenges:
        total += challenge.points
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
