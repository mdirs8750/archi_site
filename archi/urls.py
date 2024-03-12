# this urls file has been created by ourselves in application and this data is copied from projects urls.py first 4 lines
from django.contrib import admin

from django.urls import path


from .import views # importing views where functions made for rendering page

# IMPORT HERE THE STATIC AND SETTINGS FOR CATOGARY CONNECTIONS  OF IMAGES UPDATIONS
#FROM DJANGO.CONF.URLS.STATIC. IMPORT STATIC
from django.conf.urls.static import static 
#FROM DJANGO.CONF.IMPORT SETTINGS
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home, name="home"),
    path("test",views.test, name="test"),# this working signup model 
    #path('',views.newsignup, name="newsignup"),
    #path('',views.signup, name="signup"),
    #path('',views.nsignup, name="nsignup"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('about',views.about,name="about"),
    path('career',views.career, name='career'),

    # path('product',views.product, name='product'),
    
    path('testinghtml',views.testinghtml, name='testinghtml'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
