import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from insta.models import Like

register = template.Library()

@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"


@register.simple_tag
def is_following(profile, profile_to_check):
    return profile.following.filter(user_id=profile_to_check.user_id).exists()

#addcss filter
# custom filters to add css in django forms
@register.filter(name='addClass')
def addClass(field, css):
   return field.as_widget(attrs={"class":css})

#Adds the given class to the class attribute of the given field.

@register.filter(name='addID')
def addID(field, css):
   return field.as_widget(attrs={"id":css})

@register.filter(name='parse_hashtags')
def parse_hashtags(field):
    hashtags_arr = re.findall(r"#(\w+)", field)
    for hashtag in hashtags_arr:
        html_tag = "<a href='/explore?hashtag=" + hashtag + "'>#" + hashtag + "</a>"
        field = field.replace("#" + hashtag, html_tag)
    return field


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''






