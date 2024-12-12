from django import template

register = template.Library()


@register.filter
def active_comment(comment):
    return comment.filter(active=True)
