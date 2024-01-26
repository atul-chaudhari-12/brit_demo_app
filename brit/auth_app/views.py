from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect, render

from auth_app.forms import UserAuthenticationForm

class LoginFormView(FormView):
    template_name = "login.html"
    form_class = UserAuthenticationForm

    def get_success_url(self):
        return "admin"
    
    def form_valid(self, form):
        # import ipdb; ipdb.set_trace()

        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        # import ipdb; ipdb.set_trace()

        return self.render_to_response(self.get_context_data(form=form))