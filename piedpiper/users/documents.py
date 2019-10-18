from django_elasticsearch_dsl import DocType, Index
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from .models import User
client = Elasticsearch(['es:9200'])

my_search = Search(using=client)

# define simple search here
# Simple search function
def search(title):
    query = my_search.query("match", title=title)
    response = query.execute()
    return response
