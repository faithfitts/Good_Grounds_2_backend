from django.urls import path
from .views.recipe_views import Recipes, RecipeDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('recipes/', Recipes.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
