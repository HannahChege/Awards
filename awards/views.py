# from django.shortcuts import render, redirect
# from django.http  import HttpResponse
# import datetime as dt
# from django.contrib.auth import login, authenticate
# from .forms import NewProjectForm,ProfileForm,CommentsForm
# from django.contrib.auth.decorators import login_required
# from .models import Project,Profile
# from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import  MoringaMerch
# from .serializer import MerchSerializer
# # Create your views here.

# @login_required(login_url='/accounts/login/')
# def award(request):
#     projects = Project.objects.all()
#     for x in projects:
#         print(x.image.url)
#     profiles = Profile.objects.all()
#     return render(request,'index.html',{"projects":projects, "profiles":profiles })

# @login_required(login_url='/accounts/login/')
# def new_project(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.profile = current_user.profile
#             image.user = current_user

#             image.save()
#         return redirect('award')

#     else:
#         form = NewProjectForm()
#     return render(request, 'new_project.html', {"form": form})



# def search_results(request):

#    if 'username' in request.GET and request.GET["projects"]:
#        category = request.GET.get("projects")
#        searched_categories = Projects.search_image(category)
#        message = f"{category}"

#        return render(request, 'all-task/search.html',{"message":message,"projects": searched_categories})

#    else:
#        message = " Found 0 images for the search term"
#        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Profile"

    projects = Project.get_project_by_id(id= user_id).order_by('-posted_time')
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html',{'title':title, "projects":projects,"profiles":profiles})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    profile=Profile.objects.get(user=request.user)
    image= Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = ProfileForm()
    return render(request, "edit_profile.html", {"form":form,"image":image}) 
 

def add_comment(request, project_id):
   images = get_object_or_404(Image, pk=project_id)
   if request.method == 'POST':
       form = CommentsForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.user = request.user
           comment.image = images
           comment.save()
   return redirect('awards')


class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)   