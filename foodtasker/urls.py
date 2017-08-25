
from django.conf.urls import url
from django.contrib import admin
from foodtaskerapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^account/$', views.account_redirect, name='account-redirect'),
    url(r'^sign-in/$', auth_views.login,
        {'template_name': 'restaurant/sign_in.html'},
        name='sign-in'),
    url(r'^sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name='sign-out'),
    url(r'^restaurant/$', views.restaurant_home, name='restaurant-home'),
    url(r'^anadir-restaurante/$', views.anadir_restaurante, name='anadir-restaurante'),
    url(r'^(?P<id_restaurante>.+)/anadir-plato/$', views.anadir_plato, name='anadir-plato'),
    url(r'^enviando/$', views.ajax_enviar_restaurantes),
    url(r'^restaurants-bd/$', views.restaurants, name='restaurants-bd'),
    url(r'^platos-preferidos/$', views.mis_preferidos, name='platos-preferidos'),
    url(r'^sign-up/$', views.usuario_sign_up, name='sign-up'),
    url(r'^(?P<name>.+)/$', views.preferidos_por_usuario, name='usuario-preferidos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
