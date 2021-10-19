"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework.schemas import get_schema_view
from rest_framework import permissions, serializers, viewsets, routers
from rest_framework.renderers import OpenAPIRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from . import views
from rest_framework_swagger.views import get_swagger_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

 # schema_view = get_swagger_view(title='Jaseci API')
# schema_view = get_swagger_view(title='Pastebin API')
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# urlpatterns = patterns('',
#         url(r'^table/data/$', MyDataView.as_view(), name='table_data'),
#     )
# from .views import MyDataView

# urlpatterns = [
#     re_path(r'^doc(?P<format>\.json|\.yaml)$',
#             schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
#     path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
#          name='schema-swagger-ui'),  #<-- Here
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
#          name='schema-redoc'),  #<-- Here
#     path('admin/', admin.site.urls),
#     # path('user/', include('user_api.urls')),
#     # path('', include('jac_api.urls')),
#     # path('', include('obj_api.urls')),
#     # path('ui/', include('ui.urls')),
#     path('ui/', include('django.contrib.auth.urls')),
# ]




urlpatterns = [
    # url(r'^$', views.schema_view),
    # url(r'^', schema_view, name="docs"),
    # url(r'^users/', include(router.urls)),

    # url(r'^$', schema_view),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# path('docs/', schema_view),
#     path('admin/', admin.site.urls),
re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    # path('user/', include('user_api.urls')),
 path('schema_view', views.schema_view, name = 'schema_view'),
    # path('', include('jac_api.urls')),
    # path('', include('obj_api.urls')),
    # path('ui/', include('ui.urls')),
    path('ui/', include('django.contrib.auth.urls')),
# path('ss/<number>', views.student_show, name = 'student_show'),
 path('', views.student_show, name = 'student_show'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('json-example/data/', views.chart_data, name='chart_data'),
   # path('', views.MyView.as_view(), name='myview'),
path('main', views.addmain, name = 'main'),
path('Insert', views.Insertemp, name= 'Insertemp'),
path('addmerchant/<int:ss2>', views.addmerchant, name= 'addmerchant'),
path('addmanufacturer/<int:ss5>', views.addmanufacturer, name= 'addmanufacturer'),
path('addpartners/<int:ss>', views.addpartners, name= 'addpartners'),
path('viewmerchant', views.viewmerchant, name= 'viewmerchant'),
path('viewmanufacture', views.viewmanufacture, name= 'viewmanufacture'),
path('viewpartner', views.viewpartner, name= 'viewpartner'),
path('Edit/<int:id>',views.Editemp, name='Editemp'),
path('update/<int:id>',views.updateemp, name='updateemp'),
path('editmerchant/<int:id>',views.editmerchant, name='editmerchant'),
path('editmanufacture/<int:id>',views.editmanufacture, name='editmanufacture'),
path('updatemerchant/<int:id>',views.updatemerchant, name='updatemerchant'),
path('updatemanufacturer/<int:id>/<int:ss4>',views.updatemanufacturer, name='updatemanufacturer'),
path('updatemerchant/<int:id>/<int:ss3>',views.updatemerchant, name='updatemerchant'),
path('updatepartner/<int:id>/<int:ss1>',views.updatepartner, name='updatepartner'),
path('editpartners/<int:id>',views.editpartner, name='editpartner'),
]

urlpatterns += staticfiles_urlpatterns()