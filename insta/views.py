from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

@login_required
def posts(request):
  if request.method == 'POST':
    form = PostForm(request.POST,files = request.FILES)
    if form.is_valid():
      post = Post(profile = request.user.profile, title = request.POST['title'], image = request.FILES['image'])
      post.save()
      return redirect('profile', kwargs={'username':request.user.username})
  else:
    form = PostForm()
  return render(request, 'post_picture.html', {"form": form})


def followers(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.followers.all

  title = "Followers"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})  
    