from drf_yasg import openapi

# --- Parameters para los endpoints ---

language_param = openapi.Parameter(
    name='language',
    in_=openapi.IN_QUERY,
    description='Abbreviation of the language (e.g., "en", "es").',
    type=openapi.TYPE_STRING,
    required=True,
)

category_id_param = openapi.Parameter(
    name='category',
    in_=openapi.IN_QUERY,
    description='ID of the category to filter by (optional).',
    type=openapi.TYPE_INTEGER,
    required=False,
)

category_name_param = openapi.Parameter(
    name='category',
    in_=openapi.IN_QUERY,
    description='Name of the category to filter by. Required.',
    type=openapi.TYPE_STRING,
    required=True,
)

# --- Puedes agrupar en listas si quieres para usar en tus views más fácil ---

category_list_by_language_params = [language_param]

categories_description_with_all_languages_params = [language_param, category_id_param]

category_projects_view_params = [language_param, category_name_param]
