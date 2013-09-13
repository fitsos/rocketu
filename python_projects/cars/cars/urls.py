from django.conf.urls import patterns, include, url
# from cars.models import CarChoice, Equipment

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('cars_app.views',
    # Examples:
    # url(r'^$', 'cars.views.home', name='home'),
    # url(r'^cars/', include('cars.foo.urls')),
    url(r'^choice/', 'see_cars', name='cars'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
