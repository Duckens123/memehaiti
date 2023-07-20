from memehaiti.serializers import CommentSerializer
from memehaiti.models import Comment
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer tous les commentaires depuis la base de données
            comments = self.get_queryset()
            serializer = self.get_serializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération des commentaires."},
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

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer un commentaire spécifique depuis la base de données
            comment = self.get_object()
            serializer = self.get_serializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            # Si le commentaire n'existe pas, renvoyer une réponse avec un message d'erreur
            return Response({"error": "Commentaire non trouvé."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération du commentaire."},
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