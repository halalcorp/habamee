from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^404/$', views.NotFoundPage.as_view(), name='404'),
    url(r'^about/$', views.about, name='about'),# views.AboutPage.as_view(), name='about'),
    url(r'^programs/$', views.getprograms, name='programs'), #views.ProgramsPage.as_view(), name='programs'),
    url(r'^apply/$', views.NotFoundPage.as_view(), name='apply'),#ApplyPage.as_view(), name='apply'),
    url(r'^blog/$', views.NotFoundPage.as_view(), name='blog'),#views.BlogPage.as_view(), name='blog'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
