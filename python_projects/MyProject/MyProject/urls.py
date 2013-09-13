from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('MyApp.views',
    # Examples:
    # url(r'^$', 'MyProject.views.home', name='home'),
    # url(r'^MyProject/', include('MyProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r"^$", 'home'),
    url(r"^hello/(?P<name>[a-zA-Z]+)", "say_hello"),
    url(r"^counter", "counter"),
    url(r"^test", "test"),
    url(r"^ifelse/(?P<name>[a-zA-Z]+)?$", "ifelse"),
    url(r"^blackjack", "blackjack")
    
)
