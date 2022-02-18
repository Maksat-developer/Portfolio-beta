from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializers = WomenSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'post': serializers.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)

        except:
            return Response({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    return render(request, 'portfolio/about.html')


def services(request):
    return render(request, 'portfolio/services.html')


def works(request):
    return render(request, 'portfolio/works.html')

