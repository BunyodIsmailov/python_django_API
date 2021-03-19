from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class TelefonlarView(APIView):
    def get(self, request, pk=None):
        if pk:
            article = Telefonlar.objects.get(pk=pk)
            serializer = TelefonlarSerializer(article, many=False)
        else:
            article = Telefonlar.objects.all()
            serializer = TelefonlarSerializer(article, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = TelefonlarSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Article '{article_saved.brend}' created successfully"})

    def put(self, request, pk):
        saved_article = get_object_or_404(Telefonlar.objects.all(), pk=pk)
        data = request.data
        serializer = TelefonlarSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Article '{article_saved.brend}' update successfully"})



class Aperatsion_tizimView(APIView):
    def get(self, request, pk=None):
        if pk:
            article = Aperatsion_tizim.objects.get(pk=pk)
            serializer = Aperatsion_tizimSerializer(article, many=False)
        else:
            article = Aperatsion_tizim.objects.all()
            serializer = Aperatsion_tizimSerializer(article, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = Aperatsion_tizimSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Article '{article_saved.type}' created successfully"})

    def put(self, request, pk):
        saved_article = get_object_or_404(Aperatsion_tizim.objects.all(), pk=pk)
        data = request.data
        serializer =  Aperatsion_tizimSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Article '{article_saved.type}' update successfully"})
