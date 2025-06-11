from django.urls import path
from . import views

urlpatterns=[
    path('signin',views.signin,name="signin"),
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('guest',views.guest,name="guest"),
    path('services',views.services,name="services"),
    path('digital',views.digital,name="digital"),
    path('graveyard_upload',views.graveyard_upload,name="graveyard_upload"),
    path('staffdash',views.staffdash,name="staffdash"),
    path('signout',views.signout,name="signout"),
    path('firstlog',views.firstlog,name="firstlog"),
    path('upload_deceased',views.upload_deceased,name="upload_deceased"),
    path('graveyard_info',views.graveyard_info,name='graveyard_info'),
    path('memorial_upload',views.memorial_upload,name="memorial_upload"),
    path('search_graveyard',views.search_graveyard,name="search_graveyard"),
    path('page1',views.page1,name="page1"),
    path('search_memorial',views.search_memorial,name="search_memorial"),
    path('graveyard_name',views.graveyard_name,name="graveyard_name"),
    path('maintainance',views.maintainance,name="maintainance"),
    path('seework',views.pendingmaintainance,name="pendingmaintainance"),
    path('viewgrid',views.viewgrid,name="viewgrid"),
    path('update_maintainance',views.update_maintainance,name="update_maintainance"),
    path('upload_emp',views.upload_emp,name="upload_emp"),
    path('reserve',views.reserve,name="reserve"),
    path('search_deceased',views.search_deceased,name="search_deceased"),
    path('main_status',views.main_status,name="main_status")
]