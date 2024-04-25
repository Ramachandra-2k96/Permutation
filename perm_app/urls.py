from django.urls import path
from perm_app.views import home,findPermutation
urlpatterns = [
	path('',home),
 	path('permutation',findPermutation),
]