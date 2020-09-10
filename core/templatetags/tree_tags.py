from django import template
from ..models import TreeMain

register = template.Library()

@register.inclusion_tag('tree/tag-tree.html')
def draw_menu(num): # Only one argument.
    """Converts a string into all lowercase"""
    return {"object": TreeMain.objects.filter(category__name=num)}
