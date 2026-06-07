from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShortURL
from .forms import ShortURLForm
from django.urls import reverse_lazy


#create URL
class ShortURLCreateView(LoginRequiredMixin, CreateView):
    model = ShortURL
    form_class = ShortURLForm
    template_name = "shortner/create_short_url.html"
    success_url = reverse_lazy("dashboard")
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#list urls
class ShortURLListView(LoginRequiredMixin, ListView):
    model = ShortURL
    template_name = "shortner/dashboard.html"
    context_object_name = "urls"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        urls = context["urls"]
        context["total_clicks"] = sum(url.click_count for url in urls)
        return context
    
#edit url
class ShortURLUpdateView(LoginRequiredMixin, UpdateView):
    model = ShortURL
    form_class = ShortURLForm
    template_name = "shortner/edit_short_url.html"
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        return ShortURL.objects.filter(user=self.request.user)

#delete url
class ShortURLDeleteView(LoginRequiredMixin, DeleteView,):
    model = ShortURL
    template_name = "shortner/delete_short_url.html"
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        return ShortURL.objects.filter(user=self.request.user)


def redirect_short_url(request, code):
    short_url = get_object_or_404(ShortURL, short_code= code)
    short_url.click_count += 1
    short_url.save()
    return redirect(short_url.original_url)

