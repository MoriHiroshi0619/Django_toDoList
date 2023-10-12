from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('tarefa/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('criar_tarefa/', TaskCreate.as_view(), name='task-create'),
    path('editar_tarefa/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('apagar_tarefa/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]