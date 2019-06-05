from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

import os
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from settings import BASE_DIR

TEMPLATE_DIR = BASE_DIR+'/frontend/dist/static/'
PATH = '/static/'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^risks/', include('risks.urls', namespace='risks')),
    url(r'^fields/', include('risks.field_urls', namespace='fields')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]+ static(PATH, document_root=TEMPLATE_DIR)


urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]