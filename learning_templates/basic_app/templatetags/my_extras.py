from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """_summary_
    This cuts all value of ""arg from the string!
    Args:
        value (_type_): _description_
        arg (_type_): _description_
    """
    return value.replace(arg, '')

# register.filter('cur', cut)