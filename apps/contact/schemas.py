from drf_yasg import openapi

# Parámetros en query (GET o POST)
contact_language_param = openapi.Parameter(
    name='language',
    in_=openapi.IN_QUERY,
    description='The language for the response message (defaults to "en").',
    required=False,
    type=openapi.TYPE_STRING
)

# Parámetros en body (POST)
contact_body_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["id", "name", "email", "message"],
    properties={
        'id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='ID of the contact'
        ),
        'name': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Name of the contact'
        ),
        'email': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Email of the contact'
        ),
        'message': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Message from the contact'
        ),
    }
)
