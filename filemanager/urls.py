from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from filemanager.views import (BrowserView, DetailView, UploadView,
                               UploadFileView, DirectoryCreateView, RenameView,
                               DeleteView)

app_name= 'filemanager'

urlpatterns = [
    re_path(r'^$', BrowserView.as_view(), name='browser'),
    re_path(r'^detail/$', DetailView.as_view(), name='detail'),
    re_path(r'^upload/$', UploadView.as_view(), name='upload'),
    re_path(r'^upload/file/$', csrf_exempt(UploadFileView.as_view()), name='upload-file'),
    re_path(r'^create/directory/$', DirectoryCreateView.as_view(), name='create-directory'),
    re_path(r'^rename/$', RenameView.as_view(), name='rename'),
    re_path(r'^delete/$', DeleteView.as_view(), name='delete'),
]