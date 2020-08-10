from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','author','description','created_at')
        model = Post

        