from .import views
from django.urls import path, include
from django.conf.urls import url
#from django.views.generic import TemplateView
from .models import blogdata
from .views import Home,My_posts,My_favorites

app_name = 'frontend'

# Authentication urls
urlpatterns  = [
				#Class Based Views
                    url(r'^home/',Home.as_view(),name='home'),
                    url(r'^my_posts/',My_posts.as_view(),name='my_posts'),
                    url(r'^my_favorites/',My_favorites.as_view(),name='my_favorites'),

                    #Function based Views
                    url(r'^user_profile/',views.user_profile,name='user_profile'),
                    url(r'^add_post/',views.add_post,name='add_post'),
                    url(r'^add_details/(?P<ref_id>\d+)$',views.add_details,name='add_details'),
                    url(r'^likes_dislikes/',views.likes_dislikes,name='likes_dislikes'),
                    url(r'^testing/',views.testing,name='testing'),
                ]


#For Static pages no need to write views we can use GENERIC VIEWS
#url(r'^dummy/',TemplateView.as_view(template_name="frontend/dummy.html"),name='dummy'),