from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from Generator.models import Mathematics
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mathematics
        fields = ['question_text', 'answer', 'marks', 'difficulty_level']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Mathematics.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'maths', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paper/',include('Generator.urls')),
    path('', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]
