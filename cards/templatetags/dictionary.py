from django import template

register = template.Library()

@register.filter
def keyvalue(dict, key):    
    if key in dict:
        return str(dict[key]).replace('First ', '')
    return ''

