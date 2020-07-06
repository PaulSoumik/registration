from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from registration import views
# SET THE NAMESPACE!
app_name = 'registration'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    ]




from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)