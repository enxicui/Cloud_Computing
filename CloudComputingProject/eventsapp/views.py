from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import EventsForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'eventsapp/home.html', context)

#  From: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'eventsapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


@login_required
def past_events(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'eventsapp/past_events.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

#  From: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['event_name', 'event_date', 'event_description', 'location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

@login_required
def about (request):
    return render(request, 'eventsapp/about.html')

@login_required
def post_new(request):
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date_created = datetime.now()
            post.save()
            return redirect('events-home')

    else:
        form = EventsForm()
    return render(request, 'eventsapp/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = EventsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return redirect('events-home')
    else:
        form = EventsForm(instance=post)
    return render(request, 'eventsapp/post_edit.html', {'form': form})


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'eventsapp/search_results.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

    # Code learned and edited from: https://wsvincent.com/django-search/

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(event_name__icontains=query) | Q(location__icontains=query) | Q(user__username__icontains=query)
        )
        return object_list
