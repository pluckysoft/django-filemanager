from django.dispatch import Signal

filemanager_pre_upload = Signal(use_caching=False)
filemanager_post_upload = Signal(use_caching=False)

