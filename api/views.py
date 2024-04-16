from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Country
from django.http import Http404
from .serializers import CountrySerializer,CountryPostSerializer
from .serializers import CountryUpdateSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



    def retrieve(self, request, pk=None):
        try:
            country = self.get_object()
            serializer = self.get_serializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            country = self.get_object()
            country.delete()
            return Response({"message": "Country deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Country.DoesNotExist:
            return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)


# views.py

class CountryCreateAPIView(APIView):
    queryset = Country.objects.all()
    serializer_class = CountryPostSerializer
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
class CountryDetailAPIView(APIView):
    def get_object(self, country_id):
        try:
            return Country.objects.get(pk=country_id)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, country_id):
        country = self.get_object(country_id)
        serializer = CountrySerializer(country)
        return Response(serializer.data)


class CountryUpdateAPIView(APIView):
    queryset = Country.objects.all()
    serializer_class = CountryUpdateSerializer
    lookup_field = 'Country_id'
    def get_object(self, country_id):
        try:
            return Country.objects.get(pk=country_id)
        except Country.DoesNotExist:
            raise Http404

    def put(self, request, country_id):
        country = self.get_object(country_id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



