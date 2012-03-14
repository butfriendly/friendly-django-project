from django.conf import settings
from django.conf.urls.defaults import *
from foundation.urls import staticfiles_urlpatterns
from waffle.views import wafflejs
from project.example import urls

urlpatterns = []

# We attach the admin URLs if we detected the admin app
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin

    admin.autodiscover()

    urlpatterns = patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
    )

# We serve media files through Django in debug mode
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    # Use Waffle flags directly in JavaScript
    url(r'^waffle.js$', wafflejs, name='wafflejs'),

    # Example:
    (r'', include(urls)),
)
