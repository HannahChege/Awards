from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth import login, authenticate
from .forms import NewProjectForm,ProfileForm,VotesForm
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# # Create your views here.

@login_required(login_url='/accounts/login/')
def award(request):
    projects = Project.objects.all()
    for x in projects:
        print(x.image.url)
    profiles = Profile.objects.all()
    return render(request,'index.html',{"projects":projects, "profiles":profiles })

@login_required(login_url='/accounts/login/')
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
 

def get_project_by_id(request,id):
        project = Projects.objects.get(id=id)
        vote = Votes()
        if request.method == 'POST':

                vote_form = Votes(request.POST)
                if vote_form.is_valid():

                        design = vote_form.cleaned_data['design']
                        usability = vote_form.cleaned_data['usability']
                        content = vote_form.cleaned_data['content']
                        creativity = vote_form.cleaned_data['creativity']
                        rating = Likes(design=design,usability=usability,
                                        content=content,creativity=creativity,
                                        user=request.user,project=project)
                        rating.save()
                        return redirect('/')
        return render(request,'index.html',{"project":project,"vote":vote})


class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        return Response(serializers.data)   
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)  

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)   

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        



@login_required(login_url='/login')
def add_usability(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('award')

    return render(request, 'index.html')
    
@login_required(login_url='/login')
def add_design(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('award')
    else:
        form = DesignForm()

    return render(request, 'index.html',{'form': form})


@login_required(login_url='/login')
def add_content(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('award')

    return render(request, 'index.html')
