from rest_framework import serializers
from .models import student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)

#     def create(self, validate_data):
#         return student.objects.create(**validate_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     # field level validataion  
#     def validate_roll(self, value):
#         if value > 200:
#             raise serializers.ValidationError('seat full')
#         return value
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name', 'roll', 'city']
    
    # def validate_roll(self, value):
#         if value > 200:
#             raise serializers.ValidationError('seat full')
#         return value