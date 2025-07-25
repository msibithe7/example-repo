from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm

def create_sticky_note(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_sticky_note', pk=form.instance.pk)
    else:
        form = StickyNoteForm()
    return render(request, 'sticky_notes/create.html', {'form': form})

def read_sticky_note(request, pk):
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'sticky_notes/read.html', {'sticky_note': sticky_note})

def update_sticky_note(request, pk):
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=sticky_note)
        if form.is_valid():
            form.save()
            return redirect('read_sticky_note', pk=pk)
    else:
        form = StickyNoteForm(instance=sticky_note)
    return render(request, 'sticky_notes/update.html', {'form': form})

def delete_sticky_note(request, pk):
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    sticky_note.delete()
    return redirect('create_sticky_note')
