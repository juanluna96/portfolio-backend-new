import coreapi
from rest_framework.schemas import AutoSchema


class ProjectListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field(
                name='language',
                required=True,
                location='query',
                description='The language abbreviation for filtering (e.g., "en").',
                type='string'
            ),
            coreapi.Field(
                name='search',
                required=False,
                location='query',
                description='Search term to filter projects by description or title.',
                type='string'
            ),
            coreapi.Field(
                name='order',
                required=False,
                location='query',
                description='Order by title, "asc" for ascending or "desc" for descending.',
                type='string'
            )
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields