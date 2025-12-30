from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request,'index.html')

def tweet_list(reqeust):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(reqeust,'tweet_list.html',{'tweets':tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form=TweetForm()
    
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    
    return render(request,'tweet_form.html',{'form': form})

def tweet_delete(request,tweet_id):
        tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
        if request.method=='POST':
            tweet.delete()
            return redirect('tweet_list')
        return render(request,'tweet_delete.html',{'tweet':tweet})

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def tweets(reqeust):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(reqeust,'index.html',{'tweets':tweets})

def search(request):
    if request.method == 'POST':
        text = request.POST.get('search')
        tweets = Tweet.objects.filter(text__icontains=text)
        return render(request, 'index.html', {'tweets': tweets})

    return redirect('tweets')