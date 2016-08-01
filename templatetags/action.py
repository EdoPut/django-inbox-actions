from django import template

register = template.Library()

@register.inclusion_tag('inbox-actions/action.html')
def potentialAction(target_url, action_name, action_description):
    return {
        'target': target_url,
        'name': action_name,
        'description': action_description,
    }
