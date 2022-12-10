from django import template

register = template.Library()

@register.filter(name="teste")
def filter_teste(value,arg):
    return "{} + {} Qualquer coisa".format(value,arg)

@register.simple_tag
def tag_teste(*args):
    soma = 0
    
    for arg in args:
        soma += arg
    
    return soma