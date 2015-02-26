from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

from main.forms import TagForm, LinkForm
from main.models import Link, Tag

# Create your views here.
def index(request):
	# Get context of machine
	context = RequestContext(request)

	# Get Links
	links = Link.objects.all()

	return render_to_response('main/index.html', {'links':links}, context)

def tags(request):
	context = RequestContext(request)

	# Get all tags 
	tag = Tag.objects.all()

	return render_to_response('main/tags.html', {'tags': tags}, context)

def tag(request, tag_name):
	context = RequestContext(request)
	the_tag = Tag.objects.get(name=tag_name)
	link = the_tag.link_set.all()

	return render_to_response('main/index.html', 
			{'links': links, 'tag_name': '#' + tag_name}, context)

def add_link(request):
	context = RequestContext(request)

	if request.method == 'POST':
		url = request.POST.get("url", "")
		tags = request.POST.get("tags", "")
		title = request.POST.get("title", "")

		form = LinkForm(request.POST)

		if Link.objects.filter(url=url):
			print("URL exists in bookmarks")
			return index(request)

		if form.is_valid():
			form.url = url
			form.title = title
			form.tags = form.cleaned_data.get('tags')

			form.save(commit=True)
			return index(request)

		else: 
			print (form.errors)

	else:
		form = LinkForm()

	return render(request, 'main/index.html', {'form': form })

	return redirect(index)

def add_tag(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = TagForm(request.POST)

		if Tag.objects.filter(name=form.name):
			return index(request)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else: 
			print (form.errors)

	else:
		form = TagForm()

	return render(request, 'main/index.html', {'form': form })
