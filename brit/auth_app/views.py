from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import RedirectView, View
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from auth_app.forms import UserAuthenticationForm
from auth_app.models import Products
from auth_app.serializers import ProductSerializer

class LoginFormView(FormView):
    template_name = "login.html"
    form_class = UserAuthenticationForm

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):        
        if self.request.user.is_authenticated:
            redirect_to = self.get_success_url()            
            return redirect(redirect_to)

        response = super().dispatch(request, *args, **kwargs)
        response["X-Frame-Options"] = "sameorigin"
        return response

    def get_success_url(self):
        return "dashboard"
    
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            auth_logout(self.request)
        return redirect('login') 
class AuthorizedDashboardView(TemplateView):
    template_name = "auth_dashboard.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.all()
        context["products_count"] = Products.objects.count()
        return context
    
class SummaryPageView(TemplateView):
    template_name = "summary_page.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Products.objects.count()
        return context
    

class ProductsViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer