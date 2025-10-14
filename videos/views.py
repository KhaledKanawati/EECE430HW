from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all().order_by('MovieTitle')
    return render(request, 'videos/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'videos/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'videos/movie_form.html', {'form': form, 'action': 'Create'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'videos/movie_form.html', {'form': form, 'action': 'Update'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'videos/movie_confirm_delete.html', {'movie': movie})
