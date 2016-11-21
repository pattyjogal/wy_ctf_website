from django.template import Library

from wy_ctf_website.training.models import Challenge

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
def rank_icon(user):
    rank_quotient = score_total(user) / total_points()
    rank_assoc = 0
    if rank_quotient >= .85:
        rank_assoc = 5
    elif .85 > rank_quotient >= .75:
        rank_assoc = 4
    elif .75 > rank_quotient >= .60:
        rank_assoc = 3
    elif .60 > rank_quotient >= .40:
        rank_assoc = 2
    elif .40 > rank_quotient:
        rank_assoc = 1
    user.rank = rank_assoc
    user.save()
    num = rank_assoc
    color = ""
    icon = ""
    if num == 1:
        color = "#A57164"
        icon = "fa fa-circle-o-notch"
    elif num == 2:
        color = "#BFC1C2"
        icon = "fa fa-circle-o"
    elif num == 3:
        color = "#D4AF37"
        icon = "fa fa-circle"
    elif num == 4:
        color = "#841B2D"
        icon = "fa fa-plus-circle"
    elif num == 5:
        color = "#b9f2ff"
        icon = "fa fa-diamond"
    return '<i class="{}" aria-hidden="true" style="color: {}"></i>'.format(icon, color)


def total_points():
    points_total = 0
    for challenge in Challenge.objects.all():
        points_total += challenge.points
    return points_total
