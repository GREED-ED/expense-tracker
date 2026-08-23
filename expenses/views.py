from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import FormView
from django.db.models import Sum
from django.utils import timezone
    
from .forms import ExpenseForm, RegistrationForm
from .models import Expense


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expenses/expense_list.html"
    context_object_name = "expenses"

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)

        category = self.request.GET.get("category")
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")

        if category:
            queryset = queryset.filter(category=category)

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        expenses = self.get_queryset()

        context["monthly_total"] = (
            expenses
            .filter(
                date__year=timezone.now().year,
                date__month=timezone.now().month,
            )
            .aggregate(total=Sum("amount"))["total"]
            or 0
        )

        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expenses/expense_form.html"
    success_url = reverse_lazy("expense-list")

    def form_valid(self, form):
        form.instance.user = self.request.user

        response = super().form_valid(form)

        messages.success(
            self.request,
            "Expense created successfully."
        )

        return response

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "expenses/expense_form.html"
    success_url = reverse_lazy("expense-list")

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Expense updated successfully."
        )

        return response

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "expenses/expense_confirm_delete.html"
    success_url = reverse_lazy("expense-list")

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            "Expense deleted successfully."
        )

        return super().delete(request, *args, **kwargs)


class RegistrationView(FormView):
    template_name = "registration/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("expense-list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        messages.success(
            self.request,
            "Account created successfully."
        )

        return super().form_valid(form)