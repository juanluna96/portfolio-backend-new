from rest_framework.schemas import AutoSchema
import coreapi

class ContactSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        fields = super().get_manual_fields(path, method)

        # Definimos el parámetro de query 'language'
        fields.append(
            coreapi.Field(
                name='language',
                location='query',
                required=False,
                type='string',
                description='The language for the response message (defaults to "en").'
            )
        )

        # Definimos los parámetros de la solicitud (en el cuerpo) para el contacto
        fields.append(
            coreapi.Field(
                name='id',
                location='body',
                required=True,
                type='integer',
                description='ID of the contact'
            )
        )
        fields.append(
            coreapi.Field(
                name='name',
                location='body',
                required=True,
                type='string',
                description='Name of the contact'
            )
        )
        fields.append(
            coreapi.Field(
                name='email',
                location='body',
                required=True,
                type='string',
                description='Email of the contact'
            )
        )
        fields.append(
            coreapi.Field(
                name='message',
                location='body',
                required=True,
                type='string',
                description='Message from the contact'
            )
        )

        return fields
