from memehaiti.serializers import UserSerializer
from rest_framework import generics,permissions
from memehaiti.models import User
from rest_framework.response import Response
from rest_framework import status

class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Vérifie si l'utilisateur est authentifié
        is_authenticated = super().has_permission(request, view)
        
        # Vérifie si le jeton JWT est présent dans l'en-tête Authorization
        has_jwt = 'Authorization' in request.headers and 'Bearer' in request.headers['Authorization']
        
        return is_authenticated and has_jwt

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer tous les utilisateurs depuis la base de données
            users = self.get_queryset()
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération des utilisateurs."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = [IsAuthenticatedUser]


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            # Renvoyer une réponse avec un message d'erreur en cas de données invalides
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    permission_classes = [IsAuthenticatedUser]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            # Récupérer un utilisateur spécifique depuis la base de données
            user = self.get_object()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            # Si l'utilisateur n'existe pas, renvoyer une réponse avec un message d'erreur
            return Response({"error": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # En cas d'erreur, renvoyer une réponse avec un message d'erreur significatif
            return Response({"error": "Une erreur s'est produite lors de la récupération de l'utilisateur."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = [IsAuthenticatedUser]


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    permission_classes = [IsAuthenticatedUser]


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
    permission_classes = [IsAuthenticatedUser]
