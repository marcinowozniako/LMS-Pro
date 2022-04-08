from django import views
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from courses.models import Course, Subject


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['courses'] = Course.objects.all()
        ctx['subject'] = Subject.objects.all()

        return ctx
