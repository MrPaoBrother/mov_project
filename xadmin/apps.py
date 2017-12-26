# -*- coding:utf8 -*-

from django.apps import AppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _
import xadmin


class XAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'xadmin'
    verbose_name = _("管理员")

    def ready(self):
        self.module.autodiscover()
        setattr(xadmin, 'site', xadmin.site)
