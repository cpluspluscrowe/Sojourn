from django import template

#This gives me an instance of the Django template library so that one can add onto it
register = template.Library()

@register.filter(name = 'count')
def count(number):
    html = ""
    return(html)


