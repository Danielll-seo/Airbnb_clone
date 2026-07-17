from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Amenity
from .serilalizers import AmenitySerializer

class Amenities(APIView):
    
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Logic to create a new amenity
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        # Logic to update an existing amenity
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({"error": "Amenity not found"}, status=404)

        serializer = AmenitySerializer(amenity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        # Logic to delete an existing amenity
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({"error": "Amenity not found"}, status=404)

        amenity.delete()
        return Response({"message": "Amenity deleted successfully"}, status=200)

class AmenityDetail(APIView):

    def get(self, request, pk):
        # Logic to retrieve a specific amenity by its primary key
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({"error": "Amenity not found"}, status=404)

        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        # Logic to update a specific amenity by its primary key
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({"error": "Amenity not found"}, status=404)

        serializer = AmenitySerializer(amenity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        # Logic to delete a specific amenity by its primary key
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response({"error": "Amenity not found"}, status=404)

        amenity.delete()
        return Response({"message": "Amenity deleted successfully"}, status=200)