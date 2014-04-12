from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='base_bootstrap.html'), name='home'),
    url(r'^products/', include('products.urls')),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),

                            )