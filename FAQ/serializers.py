from rest_framework import serializers
from .models import FAQ
class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields =  ['question', 'answer']

    def get_question(self, obj):
        return obj.get_translated_question(self.context.get('lang', 'en'))
        

    def get_answer(self, obj):
        return obj.get_translated_answer(self.context.get('lang', 'en'))
        