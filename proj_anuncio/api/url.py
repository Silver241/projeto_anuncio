from rest_framework.urls import path
from api.views import perfil_views, user_views, minuta_views, anuncio_views, cartao_views, user_cartao_views, pagamento_views, fatura_views

urlpatterns = [
    # Perfil URLs
    path('perfis/', perfil_views.get_perfis, name='get_perfis'),
    path('perfis/create/', perfil_views.create_perfil, name='create_perfil'),
    path('perfis/update/<int:pk>/', perfil_views.update_perfil, name='update_perfil'),
    path('perfis/delete/<int:pk>/', perfil_views.delete_perfil, name='delete_perfil'),

    # User URLs
    path('users/', user_views.get_users, name='get_users'),
    path('users/create/', user_views.create_user, name='create_user'),
    path('users/update/<int:pk>/', user_views.update_user, name='update_user'),
    path('users/delete/<int:pk>/', user_views.delete_user, name='delete_user'),
    path('users/login/', user_views.login_user, name='login_user'),

    # Minuta URLs
    path('minutas/', minuta_views.get_minutas, name='get_minutas'),
    path('minutas/create/', minuta_views.create_minuta, name='create_minuta'),
    path('minutas/update/<int:pk>/', minuta_views.update_minuta, name='update_minuta'),
    path('minutas/delete/<int:pk>/', minuta_views.delete_minuta, name='delete_minuta'),

    # Anuncio URLs
    path('anuncios/', anuncio_views.get_anuncios, name='get_anuncios'), 
    path('anuncios/create/', anuncio_views.create_anuncio, name='create_anuncio'),
    path('anuncios/update/<int:pk>/', anuncio_views.update_anuncio, name='update_anuncio'),
    path('anuncios/delete/<int:pk>/', anuncio_views.delete_anuncio, name='delete_anuncio'),

    # Cartao URLs
    path('cartoes/', cartao_views.get_cartoes, name='get_cartoes'),
    path('cartoes/create/', cartao_views.create_cartao, name='create_cartao'),
    path('cartoes/update/<int:pk>/', cartao_views.update_cartao, name='update_cartao'),
    path('cartoes/delete/<int:pk>/', cartao_views.delete_cartao, name='delete_cartao'),

    # UserCartao URLs
    path('user_cartoes/', user_cartao_views.get_user_cartoes, name='get_user_cartoes'),
    path('user_cartoes/create/', user_cartao_views.create_user_cartao, name='create_user_cartao'),
    path('user_cartoes/update/<int:pk>/', user_cartao_views.update_user_cartao, name='update_user_cartao'),
    path('user_cartoes/delete/<int:pk>/', user_cartao_views.delete_user_cartao, name='delete_user_cartao'),

    # Pagamento URLs
    path('pagamentos/', pagamento_views.get_pagamentos, name='get_pagamentos'),
    path('pagamentos/create/', pagamento_views.create_pagamento, name='create_pagamento'),
    path('pagamentos/update/<int:pk>/', pagamento_views.update_pagamento, name='update_pagamento'),
    path('pagamentos/delete/<int:pk>/', pagamento_views.delete_pagamento, name='delete_pagamento'),

    # Fatura URLs
    path('faturas/', fatura_views.get_faturas, name='get_faturas'),
    path('faturas/create/', fatura_views.create_fatura, name='create_fatura'),
    path('faturas/update/<int:pk>/', fatura_views.update_fatura, name='update_fatura'),
    path('faturas/delete/<int:pk>/', fatura_views.delete_fatura, name='delete_fatura'),
]