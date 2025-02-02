from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    # English fields
    question = models.TextField()
    answer = RichTextField(null=True)
    
    # Hindi translations
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    
    # Bengali translations
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)
    
    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)
    
    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Auto-translate on creation
            translator = Translator()
            for lang in ['hi', 'bn']:
                # Translate question
                q_field = f'question_{lang}'
                if not getattr(self, q_field):
                    setattr(self, q_field, translator.translate(self.question, dest=lang).text)
                # Translate answer
                a_field = f'answer_{lang}'
                if not getattr(self, a_field):
                    setattr(self, a_field, translator.translate(self.answer, dest=lang).text)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.question