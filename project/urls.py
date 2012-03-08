from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from waffle.views import wafflejs
from project.example import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'', include(urls)),

    # Use Waffle flags directly in JavaScript
    url(r'^wafflejs$', wafflejs, name='wafflejs'),

    # Admin URLs
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEV:
    pass

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
