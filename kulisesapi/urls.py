from django.contrib import admin
from django.urls import path, include

#from account.api.views import registration_view
from api import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('show/', views.show_list),
                  path('showapi/', views.ShowsListView.as_view()),
                  path('show/<int:id>', views.show_detail),
                  path('director/', views.director_list),
                  path('director/<int:id>', views.director_detail),
                  #path('actor/', views.actor_list),
                  #path('actor/<int:id>', views.actor_detail),
                  path('theatre/', views.theatre_list),
                  path('theatre/<int:id>', views.theatre_detail),
                 # path('register/', registration_view, name="register"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
