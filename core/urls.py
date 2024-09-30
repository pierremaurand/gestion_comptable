"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView

import comptabilite.views as compta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True,
         ) 
          , name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home', compta.compte_list , name="home"),
    path('compte/create/', compta.create_compte , name="compte_create"),
    path('compte/<int:compte_id>/', compta.view_compte, name='view_compte'),
    path('compte/<int:compte_id>/edit/', compta.edit_compte, name='edit_compte'),
    path('ecriture/', compta.ecriture_list, name='ecritures'),
    path('ecriture/create/', compta.create_ecriture, name='ecriture_create'),
    path('ecriture/<int:ecriture_id>/', compta.view_ecriture, name='view_ecriture'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)