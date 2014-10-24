from django import template

register = template.Library()

@register.filter(name = "d_key")
def getDictionaryKey(d, k):
  if k in d.keys():
    return d[k]
  else:
    return "N/A"