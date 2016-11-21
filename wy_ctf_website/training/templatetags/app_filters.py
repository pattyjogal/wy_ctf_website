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

@register.filter(name='css_from_category')
def css_from_cat(category):
    colors = {
        'FR' : 'forensics-bg',
        'CR' : 'crypto-bg',
        'AL' : 'algo-bg',
        'LX' : 'linux-bg',
        'PW' : 'pwn-bg',
        'RE' : 'rev-eng-bg',
        'WB' : 'web-bg'
    }
    return colors[category]

@register.filter(name='rank_icon')
def rank_icon(num):
    color = ""
    icon = ""
    if num == 1:
        color = "#A57164"
        icon = "fa fa-circle-o-notch"
    if num == 2:
        color = "#BFC1C2"
        icon = "fa fa-circle-o"
    if num == 3:
        color = "#D4AF37"
        icon = "fa fa-circle"
    if num == 4:
        color = "#841B2D"
        icon = "fa fa-plus-circle"
    if num == 5:
        color = "#b9f2ff"
        icon = "fa fa-diamond"
    return '<i class="{}" aria-hidden="true" style="color: {}"></i>'.format(icon, color)
