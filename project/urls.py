from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from waffle.views import wafflejs
from project.example import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Use Waffle flags directly in JavaScript
    url(r'^wafflejs$', wafflejs, name='wafflejs'),

    # Example:
    (r'', include(urls)),
)

# Admin URLs
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
    )

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Just serve the files within MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, view='django.views.static.serve', document_root=settings.MEDIA_ROOT)

    # Same as above, but also staticfiles finders are used to find statics
    urlpatterns += static(settings.STATIC_URL, view='django.contrib.staticfiles.views.serve', document_root=settings.STATIC_ROOT)
