import json
from rest_framework import serializers
from .models import Biography


class BiographySerializer(serializers.ModelSerializer):
    about_me = serializers.SerializerMethodField()
    stacks_description = serializers.SerializerMethodField()

    class Meta:
        model = Biography
        fields = '__all__'

    def _localize(self, value):
        """Return language-specific text if the field stores JSON, otherwise return as-is."""
        lang = self.context.get('language', 'en')
        try:
            parsed = json.loads(value)
            if isinstance(parsed, dict):
                return parsed.get(lang) or parsed.get('en') or value
        except (json.JSONDecodeError, TypeError, ValueError):
            pass
        return value or ''

    def get_about_me(self, obj):
        return self._localize(obj.about_me)

    def get_stacks_description(self, obj):
        return self._localize(obj.stacks_description)
