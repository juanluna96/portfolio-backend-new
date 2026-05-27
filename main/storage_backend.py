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
        """
        En desarrollo: fuerza revalidación con el servidor en cada petición
        (no-cache) para que imágenes reemplazadas con el mismo nombre se
        reflejen inmediatamente sin necesidad de hard-refresh.
        """
        def url(self, name):
            url = super().url(name)
            # Añade timestamp del archivo como query param para busting de caché
            import time, os
            try:
                mtime = int(os.path.getmtime(self.path(name)))
            except (OSError, NotImplementedError):
                mtime = int(time.time())
            return f"{url}?v={mtime}"

media_storage = MediaStorage()