from django import template

register = template.Library()


@register.simple_tag
def mediapath(object):
    if object.image and hasattr(object.image, 'url'):
        return object.image.url
    return f'/media/default.png'


@register.filter
def mediapath(object):
    if object.image and hasattr(object.image, 'url'):
        return object.image.url
    return f'/media/default.png'