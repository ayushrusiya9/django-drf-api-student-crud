from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'age',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
