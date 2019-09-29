from django.urls import path

from . import views, admin, wish

urlpatterns = [
    #mysite
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('list/<str:last_evaluated_key>', views.list, name='list'),
    path('list_pagination', views.list_pagination, name='list_pagination'),
    path('page/<str:id>', views.page, name="page"),
    path('list_filter/cat/<str:cat>', views.list_filter_cat, name='list_filter_cat'),
    path('list_filter/tag/<str:tag>', views.list_filter_tag, name='list_filter_tag'),
    path('list_filter/keyword', views.list_filter_keyword, name='list_filter_keyword'),
    path('list/tag/<str:tag>', views.list_tag, name='list_tag'),
    path('list/cat/<str:cat>', views.list_cat, name='list_cat'),

    #admin
    path('admin/', admin.admin_index, name="admin_index"),
    path('admin/mysite/login', admin.admin_login, name="admin_login"),
    path('admin/mysite/logout', admin.admin_logout, name="admin_logout"),
    path('admin/mysite/list/<str:start_from>', admin.admin_list, name="admin_list"),
    path('admin/mysite/list/', admin.admin_list, name="admin_list"),
    path('admin/mysite/page/<str:id>', admin.admin_page, name="admin_page"),
    path('admin/mysite/page/', admin.admin_page, name="admin_page"),
    path('admin/mysite/save', admin.admin_save, name="admin_save"),
    path('admin/mysite/admin_search', admin.admin_search_keyword, name="admin_search_keyword"),
    path('admin/mysite/list_pagination/', admin.admin_list_pagination, name="admin_list_pagination"),

    path('wish/page', wish.page, name="wish_page"),
    path('admin/wish/save', wish.save, name="wish_save"),
    path('wish/page/<str:id>', wish.page, name="wish_page"),
    path('wish/list/', wish.list, name="wish_list"),
    path('wish/change_status', wish.change_status, name="wish_change_status"),
]
