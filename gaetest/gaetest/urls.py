from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gaetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^hello/$',views.greet),
    url(r'^admin/', include(admin.site.urls)),
)
