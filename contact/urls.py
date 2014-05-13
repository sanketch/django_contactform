from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_contactform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'contact.views.contact', name="contact"),
    url(r'^thanks/$', 'contact.views.thanks', name="thankyou"),
)
