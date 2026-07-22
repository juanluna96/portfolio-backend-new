from drf_yasg import openapi

# Define los parámetros manualmente

language_param = openapi.Parameter(
    name='language',
    in_=openapi.IN_QUERY,
    description='The language abbreviation for filtering (e.g., "en").',
    required=True,
    type=openapi.TYPE_STRING
)

search_param = openapi.Parameter(
    name='search',
    in_=openapi.IN_QUERY,
    description='Search term to filter projects by description or title.',
    required=False,
    type=openapi.TYPE_STRING
)

order_param = openapi.Parameter(
    name='order',
    in_=openapi.IN_QUERY,
    description='Order by title, "asc" for ascending or "desc" for descending.',
    required=False,
    type=openapi.TYPE_STRING
)

# Agrupamos los parámetros en una lista (opcionalmente)
project_list_params = [language_param, search_param, order_param]
