# facturasieli/templatetags/custom_filters.py
from django import template
from facturasieli.models import Profile

register = template.Library()

@register.filter(name='has_any_role')
def has_any_role(user, roles):
    try:
        profile = Profile.objects.get(email=user.email)
        role_list = [role.strip() for role in roles.split(',')]
        return profile.has_role(role_list)
    except Profile.DoesNotExist:
        return False
