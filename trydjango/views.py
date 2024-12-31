'''
To render html web pages
'''
import random

from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article

HTML_STRING = """
<h1>Hello World</h1>
"""

def home_view(request, *args, **kwargs):
    '''
    Take in a request
    Return HTML as a response
    '''

    name = "Justin"
    random_id = random.randint(0, 3)

    # from the database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    
    return HttpResponse(HTML_STRING)
