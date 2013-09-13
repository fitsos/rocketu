from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('orm_app.views',
    # url(r'^$', 'home', name='home'),
    # url(r'^poll/(?P<poll_id>\d+)$', 'poll', name='poll'),
    # url(r'^poll/results/(?P<poll_id>\d+)$', 'poll_results', name='poll_results'),
    # url(r'^add_poll_answer$', 'add_poll_answer', name='add_answer'),
    # url(r'^add_poll$', 'add_poll', name='add_poll'),
    # url(r'^poll_question$', 'add_poll_question', name='poll_question'),
    # url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    # url(r'^add_polls', 'add_polls', name='add_poll'),
    # url(r'^admin/latest-poll', 'latest_poll', name='latest_poll_results'),
    # url(r'^Kontribute/', include('Kontribute.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'test', name='test'),
    url(r'^money/', 'money', name='money'),
)
