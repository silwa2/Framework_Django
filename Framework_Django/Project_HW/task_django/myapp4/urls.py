from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image, UserCreate

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
    path('user2/', UserCreate.as_view())
]

