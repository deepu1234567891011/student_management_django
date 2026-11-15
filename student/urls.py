from django.urls import path
from . import views


urlpatterns=[
    
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('addd-department',views.add_department,name='add_department'),
    path('view-department',views.view_department,name='view_department'),
    path('edit-department/<int:id>/',views.edit_department,name='edit_department'),
    path('delete-department/<int:id>/',views.delete_department,name='delete_department'),
    path('add-student',views.add_student,name='add_student'),
    path('view-student',views.view_student,name='view_student'),
    path('update-student/<int:id>/',views.edit_student,name='edit_student'),
    path('delete-student/<int:id>/',views.delete_student,name='delete_student'),
    path('my-profile/',views.my_profile,name='my_profile'),
]
    
    