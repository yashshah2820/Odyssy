from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from photologue.sitemaps import GallerySitemap, PhotoSitemap

sitemaps = {
            'photologue_galleries': GallerySitemap,
            'photologue_photos': PhotoSitemap,
            }

urlpatterns = [
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^api/people/', include('people.api.urls')),
    url(r'^committee/', include('committee.urls', namespace='committee')),
    url(r'^linkages/', include('linkages.urls', namespace='linkages')),
    url(r'^events/', include('events.urls', namespace='event')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^people/', include('people.urls', namespace='people')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^tag/', include('tag.urls')),
    url(r'^careers/', include('careers.urls')),
    url(r'^more/', include('more.urls', namespace='more')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^announcement/', include('announcement.urls', namespace='announcement')),
    url(r'^academic/', include('academic.urls', namespace='academic')),
    url(r'^admission/', include('admission.urls', namespace='admission')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^tender/', include('tender.urls', namespace='tender')),
    url(r'^office-orders/', include('office_orders.urls', namespace='office-orders')),
    url(r'^', include('basic.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
