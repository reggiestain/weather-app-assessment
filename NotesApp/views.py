from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .forms import NoteCreate
from .models import NotesApp


def index(request):
    notes = NotesApp.objects
    return render(request, 'notes/index.html', {'notes': notes})


def create(request):
    note_form = NoteCreate(request.POST or None)
    if note_form.is_valid():
        note_form.save()
        messages.success(request, 'Note has been created successfully.')
        return redirect('/notes/index', {'success': 'Note was created successfully.'})
    return render(request, 'notes/create.html', {'note_form': note_form})


def edit(request, id):
    note = NotesApp.objects.get(id=id)
    return render(request, 'notes/edit.html', {'note': note})


def update(request, id):
    note_id = int(id)
    try:
        note = NotesApp.objects.get(id=note_id)
    except NotesApp.DoesNotExist:
        return redirect('/notes/index')
    note_form = NoteCreate(request.POST or None, instance=note)
    if note_form.is_valid():
        note_form.save()
        messages.success(request, 'Note has been updated successfully.')
        return redirect('/notes/index')
    return render(request, 'notes/edit.html', {'note': note})


def delete(request, id):
    note = NotesApp.objects.get(id=id)
    note.delete()
    messages.success(request, 'Note has been deleted successfully.')
    return redirect("/notes/index")
