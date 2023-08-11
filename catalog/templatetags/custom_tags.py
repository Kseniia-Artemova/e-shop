from django import template

register = template.Library()


@register.simple_tag
def mediapath(string):
    if string:
        print(f'/media/{string}')
        return f'/media/{string}'


@register.filter
def mediapath(string):
    if string:
        return f'/media/{string}'