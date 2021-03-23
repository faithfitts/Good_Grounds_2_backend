from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.recipe import Recipe
from ..serializers import RecipeSerializer, UserSerializer

# Create your views here.
class Recipes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = RecipeSerializer
    def get(self, request):
        """Index request"""
        # Get all the recipes:
        # recipes = Recipe.objects.all()
        # Filter the recipes by owner, so you can only see your owned recipes
        recipes = Recipe.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = RecipeSerializer(recipes, many=True).data
        return Response({ 'recipes': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['recipe']['owner'] = request.user.id
        # Serialize/create recipe
        recipe = RecipeSerializer(data=request.data['recipe'])
        # If the recipe data is valid according to our serializer...
        if recipe.is_valid():
            # Save the created recipe & send a response
            recipe.save()
            return Response({ 'recipe': recipe.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(recipe.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the recipe to show
        recipe = get_object_or_404(Recipe, pk=pk)
        # Only want to show owned recipes?
        if not request.user.id == recipe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recipe')

        # Run the data through the serializer so it's formatted
        data = RecipeSerializer(recipe).data
        return Response({ 'recipe': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate recipe to delete
        recipe = get_object_or_404(Recipe, pk=pk)
        # Check the recipe's owner agains the user making this request
        if not request.user.id == recipe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recipe')
        # Only delete if the user owns the  recipe
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['recipe'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['recipe'].get('owner', False):
            del request.data['recipe']['owner']

        # Locate Recipe
        # get_object_or_404 returns a object representation of our Recipe
        recipe = get_object_or_404(Recipe, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == recipe.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this recipe')

        # Add owner to data object now that we know this user owns the resource
        request.data['recipe']['owner'] = request.user.id
        # Validate updates with serializer
        data = RecipeSerializer(recipe, data=request.data['recipe'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
