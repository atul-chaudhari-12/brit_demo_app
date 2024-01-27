from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import RedirectView

class VisiterRedirectionView(RedirectView):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('login')
        return redirect('dashboard')