# apps/core/storage_backends.py
from django.conf import settings

if not settings.DEBUG:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        location = 'media'
        default_acl = 'public-read'
else:
    from django.core.files.storage import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        pass

media_storage = MediaStorage()