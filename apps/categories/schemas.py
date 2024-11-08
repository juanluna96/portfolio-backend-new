from rest_framework.schemas import AutoSchema
import coreapi
import coreschema

class CategoryListByLanguageSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == 'get':
            extra_fields = [
                coreapi.Field(
                    name='language',
                    required=True,
                    location='query',
                    schema=coreschema.String(
                        title='Language',
                        description='Abbreviation of the language (e.g., "en", "es").'
                    )
                )
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class CategoriesDescriptionWithAllLanguagesSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == 'get':
            extra_fields = [
                coreapi.Field(
                    name='language',
                    required=True,
                    location='query',
                    schema=coreschema.String(
                        title='Language',
                        description='Abbreviation of the language (e.g., "en", "es").'
                    )
                ),
                coreapi.Field(
                    name='category',
                    required=False,
                    location='query',
                    schema=coreschema.Integer(
                        title='Category',
                        description='ID of the category to filter by (optional).'
                    )
                )
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class CategoryProjectsViewSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == 'get':
            extra_fields = [
                coreapi.Field(
                    name='language',
                    required=True,
                    location='query',
                    schema=coreschema.String(
                        title='Language',
                        description='Abbreviation of the language (e.g., "en", "es"). Required.'
                    )
                ),
                coreapi.Field(
                    name='category',
                    required=True,
                    location='query',
                    schema=coreschema.String(
                        title='Category',
                        description='Name of the category to filter by. Required.'
                    )
                )
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
