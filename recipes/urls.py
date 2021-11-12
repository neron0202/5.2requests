from django.urls import path
from calculator.views import get_omlet, get_pasta, get_buter

urlpatterns = [
    path('omlet/', get_omlet),
    path('pasta/', get_pasta),
    path('buter/', get_buter)
    # здесь зарегистрируйте вашу view-функцию
]
