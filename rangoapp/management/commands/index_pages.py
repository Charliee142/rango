from .models import Page
from .search_indexes import index_page

def index_all_pages():
    pages = Page.objects.all()
    for page in pages:
        index_page(page)
