from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import redirect
from django.views import View
from expenses.views import (
    ExpenseCreateView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    RegistrationView,
)

class HomeRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("expense-list")

        return redirect("login")

urlpatterns = [

    path("", HomeRedirectView.as_view(), name="home"),

    path('admin/', admin.site.urls),

    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'expenses/',
        ExpenseListView.as_view(),
        name='expense-list'
    ),
    path(
        "expenses/create/",
        ExpenseCreateView.as_view(),
        name="expense-create",
    ),
    path(
        "expenses/<int:pk>/edit/",
        ExpenseUpdateView.as_view(),
        name="expense-update",
    ),
    path(
        "expenses/<int:pk>/delete/",
        ExpenseDeleteView.as_view(),
        name="expense-delete",
    ),
    path(
        "register/",
        RegistrationView.as_view(),
        name="register",
    ),
    
]