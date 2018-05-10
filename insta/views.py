from django.shortcuts import render


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  # Only return posts from users that are being followed
  users_followed = request.user.profile.following.all()
  posts = Post.objects.filter(profile__in=users_followed).order_by('-posted_on')


  return render(request,'index.html',{"posts":posts})