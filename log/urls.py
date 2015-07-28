from django.conf.urls import url
from django.views.generic.list import ListView
from . import views
from models import Entry

urlpatterns = [
    url(r'^$', ListView.as_view(
		model=Entry,
		paginate_by='10',
		queryset=Entry.objects.all(),
		context_object_name='entries',
		template_name='entry_list.html')),
	url(r'^entries/([0-9]+)', views.entry_detail),
]