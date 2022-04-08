import os
from fileinput import filename

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import models
import boto3


class CreateCourseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title', 'subject', 'slug', 'overview', 'course_image')
    template_name = 'courses/create_course.html'
    permission_required = 'courses.add_course'
    login_url = reverse_lazy('users:login')
    raise_exception = False
    success_url = reverse_lazy('home:home')

    def upload_file(self, request):
        file = request.FILES['course_image']
        s3 = boto3.resource('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
        bucket = s3.Bucket('lms-pro')
        bucket.put_object(Key=filename, Body=file)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
