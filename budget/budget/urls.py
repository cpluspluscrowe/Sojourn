from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^budget/$',"check_manager.views.budget_sheet"),
     url(r'^budget/save/$',"check_manager.views.save_data"),
    url(r'^AddJS/$',"check_manager.views.add_js"),
    url(r'^users/add$',"person_manager.views.add_person"),
    url(r'users/save/$',"person_manager.views.save_person"),
                       )

