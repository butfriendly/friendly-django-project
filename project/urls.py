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

    # Admin URLs
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Example:
    (r'', include(urls)),
)


## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

# @todo Fix pipeline
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.STATIC_URL, document_root='/Users/csc/src/friendly-django-project/static')#settings.STATIC_URL)
