from django.conf.urls.defaults import *
from spill_watch import views as spill_watch_views
from django.core.paginator import Paginator

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', spill_watch_views.index, name='index'),

    url(r'^companies/p/(?P<page>\d+)?', spill_watch_views.companies, name='companies_paginated'),
    url(r'^companies/(?P<company_id>\d+)?', spill_watch_views.company, name='company'),    
    url(r'^companies/?', spill_watch_views.companies, name='companies'),

    url(r'^incidents/p/(?P<page>\d+)?', spill_watch_views.incidents, name='incidents_paginated'),    
    url(r'^incidents/(?P<incident_id>\d+)?', spill_watch_views.incident, name='incident'),    
    url(r'^incidents/?', spill_watch_views.incidents, name='incidents'),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
