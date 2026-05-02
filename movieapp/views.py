from django.shortcuts import render
from .models import Slider, Advertisement, SocialLink, Trailer, TrailerItem, Celebrity, News, Tweet, MovieTheater, MovieTV

def home(request):
    context = {
        "sliders": Slider.objects.all(),
        "social_links": SocialLink.objects.all(),
        "theater_movies": MovieTheater.objects.all(),
        "tv_movies": MovieTV.objects.all(),
        "ads": Advertisement.objects.all(),
        "celebrities": Celebrity.objects.all(),
        "trailers": Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "news_list": News.objects.all(),
        "tweets": Tweet.objects.all(),
    }
    return render(request, "index.html", context)