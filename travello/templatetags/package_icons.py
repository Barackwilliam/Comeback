from django import template

register = template.Library()

ICON_MAP = {
    'guided': 'fa-route',
    'guide': 'fa-user-shield',
    'support crew': 'fa-users-cog',
    'hotel': 'fa-hotel',
    'park fees': 'fa-ticket-alt',
    'meals': 'fa-utensils',
    'airport': 'fa-shuttle-van',
    'camping': 'fa-campground',
    'flights': 'fa-plane-departure',
    'visa': 'fa-passport',
    'insurance': 'fa-shield-alt',
    'tips': 'fa-hands-helping',
    'personal gear': 'fa-hiking',
    'beverages': 'fa-coffee',
    'hotel nights': 'fa-hotel',
    'excursions': 'fa-binoculars',
}

@register.filter
def fa_icon(title):
    title_lower = title.lower()
    for key, icon in ICON_MAP.items():
        if key in title_lower:
            return icon
    return 'fa-circle'
