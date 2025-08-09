from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# a
#     return render(request, 'blog/index.html')

# create a post dictionary with title, image, slug, author, date, content
posts = [
    {
        'slug': 'hiking-in-the-mountains',
        'image': 'hiking.jpg',
        'author': 'John Doe',
        'date': '2025-01-01',
        'content': 'This is a post about hiking in the mountains.'
    },
    {
        'slug': 'programming-in-the-mountains',
        'image': 'programming.jpg',
        'author': 'Jane Doe',
        'date': '2025-01-02',
        'content': 'This is a post about programming in the mountains.'
    },
    {
        'slug': 'eating-in-the-mountains',
        'image': 'eating.jpg',
        'author': 'Adam Doe',
        'date': '2025-01-02',
        'content': 'This is a post about programming in the mountains.'
    },
    {
        'slug': 'sleeping-in-the-mountains',
        'image': 'sleeping.jpg',
        'author': 'Eve Doe',
        'date': '2025-01-02',
        'content': 'This is a post about programming in the mountains.'
    },
]

def starting_page(request):
    return render(request, 'blog/index.html')

def all_posts(request):
    return HttpResponse(posts)

def post_detail(request, slug):
    try:
        post = next(post for post in posts if post['slug'] == slug)
        return HttpResponse(post.get('content'))
    except StopIteration:
        return HttpResponse(f"No post found for slug: {slug}")