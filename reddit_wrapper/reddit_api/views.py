from django.http import JsonResponse
from .models import RedditThread
import praw
from django.shortcuts import render,redirect

def get_articles(request):
    reddit = praw.Reddit(
        client_id="npPQfFTWSzbKfk_Gp0K6eQ",
        client_secret="bTKK4zt1VbhjrnTlOnAxMnUiCCsLLg",
        user_agent="web:Wrapper WebApp:v1.0 (by /u/Ambitious-Bobcat3226)",
    )
    subreddit = reddit.subreddit("python")
    threads = subreddit.new(limit=10)

    articles = []
    for thread in threads:
        article = RedditThread(
            title=thread.title,
            author=thread.author.name,
            created_utc=str(thread.created_utc),  # Convert to string
            url=thread.url,
        )
        article.save()
        articles.append({
            "title": article.title,
            "author": article.author,
            "created_utc": article.get_created_utc_datetime(),  # Convert to datetime
            "url": article.url,
        })

    return render(request, 'reddit_api/threads.html', {'articles': articles})
