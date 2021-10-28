from django.shortcuts import render

# Create your views here.

# FBV를 이용한 대문페이지 구현.
def landing(request):
    return render(request, 'single_pages/landing.html')

# FBV를 이용한 자기소개 페이지 구현.
def about_me(request):
    return render(request, 'single_pages/about_me.html')
