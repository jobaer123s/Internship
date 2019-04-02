from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.parsers import JSONParser
from .models import Post
from django.db.models import Q
from .forms import applyForm
from django.contrib import messages
from rest_framework import generics
from .serializers import PostlistSerializer


def create(request):
    if request.method == 'GET':
        serializer=PostlistSerializer

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# class CreateView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = Post.objects.all()
#     serializer_class = PostlistSerializer
#
#     def perform_create(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         serializer.save()
#         messages.success( 'Post submission successful!')


# This function is for creating post from forms.py


def postCreate(request):

    return render(request, 'post.html')

#this function is for applying for intern  from forms.py

def apply(request,title):
    details = Post.objects.get(Posting_title=title)
    form = applyForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'Done!  You have successfully applied for this job')
        # return render(request, 'thanks.html')
    context={
        "form":form,
        'name': details
    }
    return render(request, 'apply.html',context)


#this function is for showing posts, and search query


def post_list(request):
    articles=Post.objects.all()
    query = request.GET.get("q")


    if query:
        articles = articles.filter(
        Q(Location__contains=query) |
        Q(Posting_title__contains=query) |
        Q(job_type__contains=query)

    )
    context = {'all_post':articles}
    return render(request, 'post_list.html',context)


#this function created for showing post detail

def detail(request, id):
    detail = Post.objects.get(id=id)
    context = {'detail':detail}
    return render(request, 'post_detail.html',context)


#this funcyion created for going contact page


def contact(request):
    return render(request, 'contact.html')
# def post_apply(request,title):
#     detail=Post.objects.all(Posting_title=title)
#     context={'name':detail}
#     return render(request, 'apply.html',context)


# def num_post(request):
#     post_numbers = Post.objects.all()
#     context = {'post_numbers':post_numbers}
#     return render(request, 'post_list.html', context)