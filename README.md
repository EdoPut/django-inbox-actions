django-inbox-actions
===================


With this templatetags library you can implement Actions in email messages.

The only email provider using Actions is Gmail but it is an open schema hosted at [schema.org][schema].

Available tags
--------------

- potentialAction: very generic tag
- resetPasswordAction: show the **Reset Password** text and link to reset password form

How to
------

## Django < 1.9

Add `django-inbox-actions` to the installed app list.

Load the required tag in your template

```
# load the required templatetag
{% load passwordResetAction %}

# use it

{% passwordResetAction http://domain.tld/resetPassword-iofhaohgihrviahrvjhwajh %}
```

## Django 1.9

There is an alternative method to load a template tag in Django 1.9 .

Using [DjangoTemplates][django_templates] you can register a custom tag without installing the custom app.


```python
TEMPLATES = [
    {
        'BACKEND'
        'OPTIONS': {
            'libraries': {
                # 
                'django-inbox-actions': 'django-inbox-actions.templatetags',
             }
        }
    },
]
```

And then load it in the template

```jinja2
{% load django-inbox-actions %}

{% django-inbox-actions.resetPasswordAction %}
```


[schema]: https://schema.org/
[django_templates]: https://docs.djangoproject.com/en/1.9/topics/templates/#django.template.backends.django.DjangoTemplates
