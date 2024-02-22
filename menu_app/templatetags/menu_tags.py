from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_items):
    menu_html = '<ul class="tree">'
    for item in menu_items:
        if item.parent is None:
            menu_html += '<li class="tree-item">'
            menu_html += '<input type="checkbox" id="{}">'.format(item.id)
            menu_html += '<label class="tree-item-label" for="{}"><a href="{}">{}</a></label>'.format(item.id, item.url, item.title)
            menu_html += draw_children(item, menu_items)
            menu_html += '</li>'
    menu_html += '</ul>'
    return mark_safe(menu_html)


def draw_children(parent, menu_items):
    children_html = ''
    children = [child for child in menu_items if child.parent == parent]
    if children:
        children_html = '<ul class="tree-submenu">'
        for child in children:
            children_html += '<li class="tree-submenu-item">'
            children_html += '<input type="checkbox" id="{}">'.format(child.id)
            children_html += '<label class="tree-submenu-item-label" for="{}"><a href="{}">{}</a></label>'.format(child.id, child.url, child.title)
            children_html += draw_children(child, menu_items)
            children_html += '</li>'
        children_html += '</ul>'
    return children_html
