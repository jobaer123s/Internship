from django.shortcuts import render
from  .models import amount,Stu_post
from post.models import Post
from django.db.models import Q

# this get all post from student model and do search query
def student(request):
    jh=amount.objects.all()
    list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        list = list.filter(
            Q(Location__contains=query) |
            Q(Posting_title__contains=query) |
            Q(job_type__contains=query)

        )


    context={'amount':jh,
             'list': list
             }
    return render(request, 'student.html',context)

# this get total number of posts by user and admin


def num_post(request):
    post_numbers = list.objects.all()
    context = {'post_numbers':post_numbers}
    return render(request, 'post_list.html', context)
