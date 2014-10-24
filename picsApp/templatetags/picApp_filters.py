"""
    Amtex Training Project
    "Image Upload Program"
       
      Sandeep Jadoonanan
       October 24, 2014
"""

from django import template

register = template.Library()

@register.filter(name = "d_key")
def getDictionaryKey(d, k):
  if k in d.keys():
    return d[k]
  else:
    return "N/A"