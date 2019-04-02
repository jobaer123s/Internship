from rest_framework import serializers
from .models import Post


class PostlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ('Posting_title', 'Internship_discription', 'date', 'slug', 'Location','job_type','deadline')
        read_only_fields = ('slug', 'date')