from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from blog.models import *


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)
    catage = BlogCategory.objects.all()


    # Search
    if search_query:
        search_results = Page.objects.all().search(search_query)
        catage = catage.filter(name__contains=search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'category_results':catage,
        'search_results': search_results,
    })
