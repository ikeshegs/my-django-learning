from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import redirect, render # type: ignore
from django.http import Http404

from .forms import ArticleForm
from .models import Article


# Create your views here.
def article_search_view(request):
    query_dict = request.GET    # This is a dictionary
    # query = query_dict.get('q') # <input type="text" name="q" />

    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    
    article_obj = None

    if article_obj is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        "object": article_obj
    }

    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    # print(dir(form))
    context = {
        "form": form
    }


    if form.is_valid():
        article_object = form.save()
        context["form"] = form

        # return redirect(article_object.get_absolute_url())
        return redirect("article-detail", slug=article_object.slug) # This is the same as the above line
    
        # context['object'] = article_object
        # context['created'] = True
    
    return render(request, "articles/create.html", context=context)

# def article_create_view(request):
#     form = ArticleForm()
#     # print(dir(form))
#     context = {
#         "form": form
#     }

#     if request.method == "POST":
#         form = ArticleForm(request.POST)    # Passing all the uncleaned data, making it available to the form class
#         context["form"] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')

#             article_object = Article.objects.create(title=title, content=content)

#             context['object'] = article_object
#             context['created'] = True
    
#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        # except Article.MultipleObjectsReturned:
        #     article_obj = Article.objects.get(slug=slug)
        except:
            raise Http404

    context = {
        "object": article_obj,
    }
    
    return render(request, "articles/detail.html", context=context)
