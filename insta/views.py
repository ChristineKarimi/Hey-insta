from django.shortcuts import render


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  #returns posts from users that are being followed only
  users_followed = request.user.profile.following.all()
  posts = Post.objects.filter(profile__in=users_followed).order_by('-posted_on')
    return render(request,'index.html',{"posts":posts})

@login_required
def profile(request, username):
  user = User.objects.get(username = username)
  if not user:
    return redirect('Home')
  profile = Profile.objects.get(user =user)
  title = f"{user.username}"
   return render(request, 'profiles/profile.html', {"title": title, "user":user, "profile":profile})    