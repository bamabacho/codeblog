from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r"^about/$", TemplateView.as_view(template_name='blog/about.html'),
    name='about'),
    url(r"^projects/$", TemplateView.as_view(template_name='blog/projects.html'),
    name='projects'),
    url(r"^contact/$", TemplateView.as_view(template_name='blog/contact.html'),
    name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)