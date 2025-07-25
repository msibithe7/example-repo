
python manage.py startapp sticky_notes_app

INSTALLED_APPS = [
  # ...
  'sticky_notes_app.apps.StickyNotesAppConfig',
]
Model Definition

# models.py
from django.db import models

class StickyNote(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()

python manage.py makemigrations
python manage.py migrate
Views and Forms

# views.py
from django.shortcuts import render, redirect
from .models import StickyNote
from .forms import StickyNoteForm

def create_sticky_note(request):
  if request.method == 'POST':
    form = StickyNoteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('sticky_notes_list')
  else:
    form = StickyNoteForm()
  return render(request, 'sticky_notes/create.html', {'form': form})

def read_sticky_note(request, pk):
  sticky_note = StickyNote.objects.get(pk=pk)
  return render(request, 'sticky_notes/read.html', {'sticky_note': sticky_note})

def update_sticky_note(request, pk):
  sticky_note = StickyNote.objects.get(pk=pk)
  if request.method == 'POST':
    form = StickyNoteForm(request.POST, instance=sticky_note)
    if form.is_valid():
      form.save()
      return redirect('sticky_notes_list')
  else:
    form = StickyNoteForm(instance=sticky_note)
  return render(request, 'sticky_notes/update.html', {'form': form})

def delete_sticky_note(request, pk):
  sticky_note = StickyNote.objects.get(pk=pk)
  sticky_note.delete()
  return redirect('sticky_notes_list')

# forms.py
from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
  class Meta:
    model = StickyNote
    fields = ('title', 'content')
URL Patterns

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available "
            "on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

# sticky_notes/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('admin/', admin.site.urls),
  path('sticky_notes/', include('sticky_notes_app.urls')),
]
Templates and Static Files

<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Sticky Notestitle>
head>
<body>
  <div id="content">
    {% block content %}{% endblock %}
  div>
body>
html>

<!-- create.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Create Sticky Noteh1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Createbutton>
  form>
{% endblock %}
<!-- read.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ sticky_note.title }}h1>
  <p>{{ sticky_note.content }}p>
{% endblock %}
<!-- update.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>Update Sticky Noteh1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Updatebutton>
  form>
{% endblock %}

/* style.css */
body {
  font-family: Arial, sans-serif;
}

#content {
  width: 80%;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static'),
]


python manage.py migrate
python manage.py runserver