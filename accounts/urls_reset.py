from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', password_reset_complete, name='password_reset_complete'),

    # url(r'^user/password/reset/$', 
    #     'django.contrib.auth.views.password_reset', 
    #     {'post_reset_redirect' : '/user/password/reset/done/'},
    #     name="password_reset"),
    # (r'^user/password/reset/done/$',
    #     'django.contrib.auth.views.password_reset_done'),
    # (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
    #     'django.contrib.auth.views.password_reset_confirm', 
    #     {'post_reset_redirect' : '/user/password/done/'}),
    # (r'^user/password/done/$', 
    #     'django.contrib.auth.views.password_reset_complete'),
]
