from elasticsearch_dsl import Document, Text, Keyword
from elasticsearch_dsl.connections import connections
from .models import Page
#from rangoapp.search_indexes import index_page

# Connect to the default cluster
connections.create_connection()

class PageIndex(Document):
    title = Text()
    url = Keyword()
    description = Text()
    category = Text()

    class Index:
        name = 'pages'

    def save(self, **kwargs):
        return super().save(**kwargs)

    @classmethod
    def create_index(cls):
        if not cls._index.exists():
            cls.init()

# Example function to index a page
def index_page(page):
    page_index = PageIndex(
        meta={'id': page.id},
        title=page.title,
        url=page.url,
        description=page.description,
        category=page.category.name if page.category else '',
    )
    page_index.save()

