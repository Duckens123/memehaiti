from memehaiti.serializers import CategorySerializer
from memehaiti.models import Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer toutes les catégories depuis la base de données
            categories = self.get_queryset()
            serializer = self.get_serializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération des catégories."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # Renvoyer une réponse avec un message d'erreur en cas de données invalides
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer une catégorie spécifique depuis la base de données
            category = self.get_object()
            serializer = self.get_serializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            # Si la catégorie n'existe pas, renvoyer une réponse avec un message d'erreur
            return Response({"error": "Catégorie non trouvée."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération de la catégorie."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # Renvoyer une réponse avec un message d'erreur en cas de données invalides
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)