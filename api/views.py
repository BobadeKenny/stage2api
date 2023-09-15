from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from api.models import Person
from api.serializers import PersonSerializer

# Create your views here.


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Person created", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PersonSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": f"Person {instance.name} updated"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": f"{instance.name} deleted"}, status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PersonSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
