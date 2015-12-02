"""
Created on 13/mar/2014

@author: Marco Pompili
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class InstagramConfiguration(models.Model):
    class Meta:
        verbose_name = _(u"Django Instagram Configuration")
        verbose_name_plural = _(u"Django Instagram Configuration")

    app_access_token = models.TextField(
        _(u'Access token'),
        help_text=_(
            u'Click on "Get Access Token" and you will be redirected to \
            Instagram, then follow the instructions. Remember to log in with \
            the account that you want to show on the web page.'))
