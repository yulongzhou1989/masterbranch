from django.urls import path

from . import views, admin

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:last_evaluated_key>', views.list, name='list'),
    path('page/<str:id>', views.details, name="details"),
    path('admin/', admin.admin_index, name="admin_index"),
    path('admin/mysite/login', admin.admin_login, name="admin_login"),
    path('admin/mysite/logout', admin.admin_logout, name="admin_logout"),
    path('admin/mysite/list/<int:start_from>', admin.admin_list, name="admin_list"),
    path('admin/mysite/list/', admin.admin_list, name="admin_list"),
    path('admin/mysite/page/<str:id>', admin.admin_page, name="admin_page"),
    path('admin/mysite/page/', admin.admin_page, name="admin_page"),
    path('admin/mysite/save', admin.admin_save, name="admin_save"),
]
