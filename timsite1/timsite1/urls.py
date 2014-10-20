from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from MyData import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'datalist', views.DataListViewSet)
router.register(r'stringparameter', views.StringParameterViewSet)
router.register(r'integerparameter', views.IntegerParameterViewSet)
router.register(r'booleanparameter', views.BooleanParameterViewSet)
router.register(r'decimalparameter', views.DecimalParameterViewSet)
router.register(r'unitparameter', views.UnitParameterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timsite1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)'''