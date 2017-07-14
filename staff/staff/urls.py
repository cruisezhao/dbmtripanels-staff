"""staff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
from django.conf.urls import include
from common.apps.users.urls import staff_urlpatterns as user_urls
from . import views
from common.apps.orders import urls_staff as ordersurl
from common.apps.clients import url_staff as clientsurl
from common.apps.packages import urls_staff as packageurl
from common.apps.deployments import urls_staff as deployurl

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^users/', include((user_urls, 'users'))),
    # url(r'^crud/',  include('crudbuilder.urls')),
    #orders
    url(r'^orders/', include(ordersurl, namespace="orders")),
    url(r'^packages/', include(packageurl, namespace="packages")),
    #ticket
    url(r'^ticket/',include('helpdesk.urls')),
    url(r'clients/', include(clientsurl, namespace="clients"))
    url(r'^deployments/', include(deployurl, namespace="deployments")),
]
