from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Client,Project,User


class ClientSignUpForm(UserCreationForm):
    id = forms.IntegerField()
    client_name = forms.CharField(required=True)
    created_by = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.id = self.cleaned_data.get('id')
        user.client_name = self.cleaned_data.get('client_name')
        user.save()
        client = Client.objects.create(user=user)
        client.created_by = self.cleaned_data.get('created_by')
        client.save()
        return user


class ProjectSignUpForm(UserCreationForm):
    id = forms.IntegerField()
    project_name = forms.CharField(required=True)
    created_at = forms.CharField(required=True)
    created_by = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

        @transaction.atomic
        def data_save(self):
            user = super().save(commit=False)
            user.is_project = True
            user.is_staff = True
            user.id = self.cleaned_data.get('id')
            user.project_name = self.cleaned_data.get('project_name')
            user.save()
            project = Project.objects.create(user=user)
            project.created_by = self.cleaned_data.get('created_by')
            project.save()
            return user
