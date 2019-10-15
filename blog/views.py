from django.shortcuts import render

posts = [
	
	{
	'Title' : 'Blog post 1',
	'Author' : 'Prakhar',
	'Date_posted' : '15th October',
	'Content' : 'This is the first post.' 
	},

	{	
	'Title' : 'Blog post 2',
	'Author' : 'Prakhar',
	'Date_posted' : '15th October',
	'Content' : 'This is the second post.' 
	}

]

def home(request):
	context = {
	'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})