from django.urls import path
from .views import medicamentos_list
from .views import medicamentos_new
from .views import medicamentos_update
from .views import medicamentos_delete


urlpatterns = [
    path('', medicamentos_list),
    path('list/', medicamentos_list, name="medicamentos_list"),
    path('new/', medicamentos_new, name="medicamentos_new"),
    path('update/<int:id>/', medicamentos_update, name="medicamentos_update"),
    path('delete/<int:id>/', medicamentos_delete, name="medicamentos_delete"),
]