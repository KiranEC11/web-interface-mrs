from django.shortcuts import render
# from .models import Enter_title
from .forms import TitleForm
from .MRS import Movie_recommender
import pandas as pd
# Create your views here.

def TitleView(request):
    if request.method =='POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            rec = Movie_recommender()
            
            title = form.cleaned_data['Title']
            recommendations = rec.recommender(title=title)
                    
            # context = {
            #         'table': recommendations.to_html(escape =False, classes="table table-bordered table-striped"),
            #             }
                    
                    
            # return render(request, 'recommendations.html', context)

             # Extract the recommended movie titles as a list
            movie_titles = recommendations['Recommended movies'].tolist()
            movie_description = recommendations['Overview'].tolist()
            movie_data = [(title,desc) for title,desc in zip(movie_titles,movie_description)]
            context = {
                'movie_data': movie_data,
            }

            return render(request, 'recommendations.html', context)

    else:
        form = TitleForm()
        context = {
                    'form': form,
                }
        return render(request, "enter_title_page.html", context)
    
