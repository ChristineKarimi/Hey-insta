import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from gram.models import Like

register = template.Library()

@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"
