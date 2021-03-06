"""Geovis_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from basemap import views as basemap_views
from thematicdata import views as thematic_view


urlpatterns = [

    path('admin/', admin.site.urls),
    path('index/', basemap_views.index),
    # #  read_app_views
    url(r'^XXYL/(\d+)/(\d+)/(\d+)$', basemap_views.get_Tile),
    # #  basemap_app_views
    url(r'^(\d+)/(\d+)/(\d+)/(\d+)$', basemap_views.get_polyTile),
    # #  AQI_realtime
    url(r'^AQI/realtime/$', thematic_view.ditu),

]
