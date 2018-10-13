from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from .forms import UserUpdateForm,ProfileUpdateForm,NewProjectForm
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
# Create your views here.

@login_required(login_url='/accounts/login/')
def award(request):
    projects = Project.objects.all()
    for x in projects:
        print(x.image.url)
    profiles = Profile.objects.all()
    return render(request,'index.html',{"projects":projects, "profiles":profiles })


def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
            image.user = current_user

            image.save()
        return redirect('award')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})
def search_results(request):

   if 'username' in request.GET and request.GET["projects"]:
       category = request.GET.get("projects")
       searched_categories = Projects.search_image(category)
       message = f"{category}"

       return render(request, 'all-task/search.html',{"message":message,"projects": searched_categories})

   else:
       message = " Found 0 images for the search term"
       return render(request, 'search.html',{"message":message})


def add_comment(request, image_id):
   images = get_object_or_404(Image, pk=image_id)
   if request.method == 'POST':
       form = CommentsForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.user = request.user
           comment.image = images
           comment.save()
   return redirect('awards')