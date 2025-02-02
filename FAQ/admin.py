from django.contrib import admin
from .models import FAQ
from django.utils.html import strip_tags
import html

def clean_html(text):
    """Remove HTML tags and decode HTML entities."""
    decoded_text = html.unescape(text)  # Converts &quot; to ", &lt; to <, etc.
    cleaned_text= strip_tags(decoded_text)  # Removes <p>, <div>, etc.
    return cleaned_text.strip()

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    fieldsets = [
        ('English', {'fields': ['question', 'answer']}),
        ('Hindi', {'fields': ['question_hi', 'answer_hi']}),
        ('Bengali', {'fields': ['question_bn', 'answer_bn']}),
    ]
    
    my_list= ('clean_question', 'clean_answer')
    
    def clean_question(self, obj):
        return clean_html(obj.question)
    clean_question.short_description = 'Question (English)'
    
    def clean_answer(self, obj):
        return clean_html(obj.answer)
    clean_answer.short_description = 'Answer (English)'
    
    def save_model(self, request, obj, form, change):
        # Clean questions
        obj.question = clean_html(obj.question)
        # Clean answers
        obj.answer = clean_html(obj.answer)
        
        super().save_model(request, obj, form, change)
    

    