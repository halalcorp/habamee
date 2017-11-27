from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ProgramsPage(generic.TemplateView):
	"""docstring for ServicesPage"""
	template_name = "programs.html"
	#def __init__(self, arg):
	#	super(ServicesPage, self).__init__()
	#	self.arg = arg
		
class ApplyPage(generic.TemplateView):
	"""docstring for ApplyPage"""
	template_name = "apply.html"
	#def __init__(self, arg):
	#	super(ApplyPage, self).__init__()
	#	self.arg = arg

class BlogPage(generic.TemplateView):
		"""docstring for BlogPage"""
		template_name ="blog.html"
		#def __init__(self, arg):
	#	super(BlogPage, self).__init__()
	#	self.arg = arg
				