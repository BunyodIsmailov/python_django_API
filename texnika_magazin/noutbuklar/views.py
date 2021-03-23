from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class NoutbuklarView(APIView):
    def get(self, request, pk=None):
        if pk:
            article = Noutbuklar.objects.get(pk=pk)
            serializer = NoutbuklarSerializer(article, many=False)
        else:
            article = Noutbuklar.objects.all()
            serializer = NoutbuklarSerializer(article, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = NoutbuklarSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Noutbuklar '{article_saved.brend}' created successfully"})

    def put(self, request, pk):
        saved_article = get_object_or_404(Noutbuklar.objects.all(), pk=pk)
        data = request.data
        serializer = NoutbuklarSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Noutbuklar '{article_saved.brend}' update successfully"})



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
        return Response({"success": f"Aperatsion_tizim '{article_saved.type}' created successfully"})

    def put(self, request, pk):
        saved_article = get_object_or_404(Aperatsion_tizim.objects.all(), pk=pk)
        data = request.data
        serializer =  Aperatsion_tizimSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": f"Aperatsion_tizim '{article_saved.type}' update successfully"})
