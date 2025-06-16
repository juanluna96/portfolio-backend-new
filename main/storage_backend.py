# apps/core/storage_backends.py
import os
from django.conf import settings
from django.core.files import File

if not settings.DEBUG:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        location = 'media'
        default_acl = 'public-read'

    media_storage = MediaStorage()
else:
    media_storage = None  # Django usará el almacenamiento por defecto (FileSystemStorage)