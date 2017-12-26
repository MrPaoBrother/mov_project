"""learn_xadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from spider_board import views
from data_show import views as data_show_views
import xadmin

xadmin.autodiscover()

from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'run', views.run),
    url(r"log$", views.log),
    # url(r"realtime_log", views.realtime_log),
    url(r"test", views.test),
    url(r"fresh", views.fresh),
    url(r'result/', views.result, name='views-result'),
    url(r'result_page/(?P<page>[0-9]+)/', views.result_page, name='views-result-page'),

]
