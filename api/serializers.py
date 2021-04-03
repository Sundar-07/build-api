from rest_framework import serializers
from api.models import ProjectForm 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectForm
        fields = '__all__'


    def create(self, validated_data):
        """
        Create and return a new 'project data' instance, given the validated data.
        """
        return ProjectForm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'project data' instance, given the validated data.
        """
        
        instance.location           = validated_data.get('location', instance.location)
        instance.project_name       = validated_data.get('project_name', instance.project_name)
        instance.tower              = validated_data.get('tower', instance.tower)
        instance.floor              = validated_data.get('floor', instance.floor)
        instance.unit_status        = validated_data.get('unit_status', instance.unit_status)
        instance.unit_desc        = validated_data.get('unit_desc', instance.unit_desc)
        instance.created            = validated_data.get('created', instance.created)
        
        instance.save()
        return instance
