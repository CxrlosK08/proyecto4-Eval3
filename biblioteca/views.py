from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from biblioteca.models import Libro
from biblioteca.serializer import LibroSerializer

# Create your views here.
@api_view(['POST', 'PUT'])
def crear_libro(request):
    datos_libro_deserializado = LibroSerializer(data=request.data)

    if datos_libro_deserializado.is_valid():
        datos_libro_deserializado.save()
        return Response(datos_libro_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_libro_deserializado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_libros(request):
    try:
        listado_libros = Libro.objects.all()
        serializado = LibroSerializer(listado_libros, many=True)
        return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modificar_libro(request, id):
    try:
        libro_seleccioado = Libro.objects.get(pk=id)
        serializado = LibroSerializer(libro_seleccioado, data=request.data, partial=True)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_libro(request, id):
    try:
        libro_obtenido = Libro.objects.get(id=id)
        libro_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
