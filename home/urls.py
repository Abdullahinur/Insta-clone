from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Signup/$', core_views.signup, name='signup'),
    url(r'^UserLogin/$', views.user_login, name='userLogin'),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
