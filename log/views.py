from django.shortcuts import render
from django.http import HttpResponse, Http404

from models import Entry

def index(request):
	return HttpResponse("Hello, world. You're at the log index.")
	
def entry_detail(request, key="1"):
	try:
		entry = Entry.objects.get(pk=key)
		return render(request, 'entry.html', {'entry' : entry})
	except Entry.DoesNotExist:
		raise Http404("Entry does not exist!")