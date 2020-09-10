from django import template
from ..models import TreeMain

register = template.Library()


@register.simple_tag
def total_trees():
    print('template tag')
    return TreeMain.objects.count()

@register.simple_tag
def current_time(num):
    return TreeMain.objects.filter(category__name=num)

@register.filter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

@register.inclusion_tag('tree/tag-tree.html')
def tree_loop(num): # Only one argument.
    """Converts a string into all lowercase"""
    return {"object": TreeMain.objects.filter(category__name=num)}
