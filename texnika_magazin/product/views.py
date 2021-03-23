from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Category, Brand
from .serializers import (CategorySerializer, BrandSerializer, )
from . import services
from rest_framework.exceptions import NotFound


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            category = Category.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound('category not found')
        return category

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs and kwargs["pk"]:
            return Response(services.get_category_by_id(kwargs['pk']), status=status.HTTP_200_OK)
        else:
            return Response(services.get_all_categories(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        instance.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)


# BREND


class BrandView(GenericAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            category = Brand.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound('category not found')
        return category

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs and kwargs["pk"]:
            return Response(services.get_brend_by_id(kwargs['pk']), status=status.HTTP_200_OK)
        else:
            return Response(services.get_all_brend(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        instance.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
