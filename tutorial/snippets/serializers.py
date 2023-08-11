from rest_framework import serializers
from snippets.model import Snippet, LANGUAGE_CHOICES ,STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(required=False,allow_blank=True,max_length=100)
    code=serializers.CharField(style={'base_template':'textarea.html'})
    lanuage=serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
    style= serializers.ChoiceField(choices=STYLE_CHOICES,default='firendly')
    
    
    def create(self, validate_data):
        """
        create and return a new snippeet instance ,given the validate data
        _summary_

        Args:
            validate_data (_type_): _description_
        """
        return Snippet.objects.create(**validate_data)
    def update(self, instance , validate_data):
        """
        update and return an existing  anipprt instance ,given the validate data

        Args:_summary_
            instance (_type_): _description_
            validate_data (_type_): _description_
        """
        instance.title=validate_data.get('title',instance.title)
        instance.code=validate_data.get('code',instance.code)
        instance.linenos=validate_data.get('linenos',instance.linenos)
        instance.language-validate_data.get('language',instance.language)
        instance.style=validate_data.get('style',instance.style)
        instance.save()
        return instance
        