from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from django.forms import URLField

from main.models import Link, Tag

error_flag = 0

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
	tags = Tag.objects.all()

	return render_to_response('main/tags.html', {'tags': tags }, context)

def tag(request, tag_name):
	context = RequestContext(request)
	the_tag = Tag.objects.get(name=tag_name)
	link = the_tag.link_set.all()

	return render_to_response('main/index.html', 
			{'links': link, 'tag_name': '#' + tag_name}, context)

def add_link(request):
	context = RequestContext(request)
	error_flag = {}

	if request.method == 'POST':
		cur_url = request.POST.get("url", "")
		cur_tags = request.POST.get("tags", "").split()
		tag_list = []

		cur_title = request.POST.get("title", "")

		try:
			cur_url = URLField().clean(cur_url) 
		except ValidationError:
			error_flag['badurl'] = True 
			
		if error_flag == {}:
			for items in cur_tags:
				tag_list.append(Tag.objects.get_or_create(name=items)[0])

			bookLink = Link.objects.create(title=cur_title, url=cur_url)

			# Must create object and add due to many to many constraint
			for items in tag_list:
				#print(items)
				bookLink.tags.add(items)
			
	return redirect(index)


