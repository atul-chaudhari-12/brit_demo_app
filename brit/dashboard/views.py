from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from products.models import Products


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

