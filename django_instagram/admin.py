"""
Created on 15/dic/2013

@author: Marco Pompili
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .models import InstagramConfiguration
from .templatetags import instagram_client


csrf_protect_m = method_decorator(csrf_protect)

instagram_extra_content = {
    "client_id": instagram_client.DJANGO_INSTAGRAM_CLIENT_ID,
    "redirect_uri": instagram_client.DJANGO_INSTAGRAM_REDIRECT_URI
}


class InstagramAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Django Instagram Configuration'),
         {
             'fields': ('app_access_token',)
         }),
    )

    def has_add_permission(self, request):
        """
        Just let to add the configuration once.
        :param request:
        :return:
        """
        return not InstagramConfiguration.objects.exists()

    def add_view(self, request, form_url='', extra_context=None):
        """
        Add extra parameters from the settings (client_id, redirect_uri) into the add view.
        :param request:
        :param form_url:
        :param extra_context:
        :return:
        """
        return admin.ModelAdmin.add_view(self,
                                         request,
                                         form_url='',
                                         extra_context=instagram_extra_content)

    @csrf_protect_m
    @transaction.atomic
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Add extra parameters from the settings (client_id, redirect_uri) into the change_view.
        :param request:
        :param object_id:
        :param form_url:
        :param extra_context:
        :return:
        """
        return admin.ModelAdmin.change_view(self,
                                            request,
                                            object_id,
                                            form_url=form_url,
                                            extra_context=instagram_extra_content)


admin.site.register(InstagramConfiguration, InstagramAdmin)