from django.core.paginator import Paginator
from django.conf import settings
 
def getPages(request, objectlist):
    currentPage = request.GET.get('page', 1)
    paginator = Paginator(objectlist, settings.EACHPAGE_NUMBER)
    objectlist = paginator.page(currentPage)
 
    return paginator, objectlist

def getAbsPages(request, objectlist):
    currentPage = request.GET.get('page', 1)
    paginator = Paginator(objectlist, settings.EACHPAGE_ABS_NUMBER)
    objectlist = paginator.page(currentPage)
 
    return paginator, objectlist