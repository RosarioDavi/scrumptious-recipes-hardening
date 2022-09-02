from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from mealplans.models import MealPlan
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class MealplanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "mealplans/list.html"
    paginate_by = 4
    context_object_name = "plans"


class MealplanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "mealplans/create.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("mealplans_detail")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mealplans_detail", pk=plan.id)


class MealplansDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "mealplans/detail.html"


class MealplansUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    fields = ["name"]
    template_name = "mealplans/edit.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy("mealplans_detail", args=[self.object.id])


class MealplansDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("mealplans_list")
