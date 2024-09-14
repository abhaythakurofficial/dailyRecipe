from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from recipe.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('recipe/', include('recipe.urls')),  
    path('delete_recipe/<id>/', delete_recipe,name='delete_recipe'),  
    path('update_recipe/<id>/', update_recipe,name='update_recipe'),  
    path('login/', login_page,name='login'),  
    path('register/', register,name='register'),  
    path('logout/', logout_page,name='logout_page'),  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
