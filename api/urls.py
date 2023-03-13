from api.views import LivroViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(f'livros', LivroViewSet)

urlpatterns = router.urls