from memehaiti.serializers import GeneratedMemeSerializer
from rest_framework import generics
from memehaiti.models import GeneratedMeme
from rest_framework.response import Response
from rest_framework import status


class GeneratedMemeListAPIView(generics.ListCreateAPIView):
    queryset = GeneratedMeme.objects.all()
    serializer_class = GeneratedMemeSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer tous les memes générés depuis la base de données
            generated_memes = self.get_queryset()
            serializer = self.get_serializer(generated_memes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération des memes générés."},
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

class GeneratedMemeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneratedMeme.objects.all()
    serializer_class = GeneratedMemeSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer un meme généré spécifique depuis la base de données
            generated_meme = self.get_object()
            serializer = self.get_serializer(generated_meme)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GeneratedMeme.DoesNotExist:
            # Si le meme généré n'existe pas, renvoyer une réponse avec un message d'erreur
            return Response({"error": "Meme généré non trouvé."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération du meme généré."},
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