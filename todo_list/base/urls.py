from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLogin, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('tarefa/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('add_task/', TaskCreate.as_view(), name='task-create'),
    path('editar_tarefa/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('apagar_tarefa/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]