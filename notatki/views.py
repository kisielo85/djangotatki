from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Notatka
from .forms import addNoteForm, editNoteForm
from django.contrib.auth.models import User

def index(request):
    notatki = Notatka.objects.all()
    return render(request, "index.html", {'notatki': notatki})

def addNote(request):
    if request.method == 'POST':
        form = addNoteForm(request.POST)
        if form.is_valid():

            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author=request.user
            else:
                note.author = User.objects.get(username='default_user')
            note.save()
            
            return redirect('index')
    return render(request, 'add_note.html')

def viewNote(request, note_id):
    note = get_object_or_404(Notatka, pk=note_id)
    return render(request, 'view_note.html', {'n': note, 'next_n':note.next(), 'prev_n':note.previous()})

def deleteNote(request, note_id):
    note = get_object_or_404(Notatka, pk=note_id)
    if request.method == 'POST':
        print(note.title)
        note.delete()
    
    return redirect('index')

def editNote(request, note_id):
    note = get_object_or_404(Notatka, pk=note_id)
    if request.method == 'POST':
        form = addNoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, 'edit_note.html',{'n':note})