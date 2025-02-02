from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer
class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        
        if not cached_data:
            faqs = FAQ.objects.all()
            serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 900)  # 15 minutes
        return Response(cached_data)