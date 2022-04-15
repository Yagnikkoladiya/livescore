from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
                  path('', views.Homepage, name='homepage'),
                  path('search/', views.search, name='search'),
                  path('live/', views.live, name='live'),
                  # path('scoreboard/', views.score_board, name='scoreboard'),
                  path('pointtable/', views.point_table, name='pointtable'),
                  path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                                      authentication_form=LoginForm), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='login'),
                       name='logout'),

                  path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                                form_class=MyPasswordChangeForm,
                                                                                success_url='/passwordchangedone/'),
                       name='passwordchange'),

                  path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name=
                                                                                    'app/passwordchangedone.html'),
                       name='passwordchangedone'),

                  path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                               form_class=MyPasswordResetForm),
                       name='password_reset'),

                  path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name=
                                                                                        'app/password_reset_done.html'),
                       name='password_reset_done'),

                  path('password_reset_confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                   'app/password_reset_confirm.html',
                                                                   form_class=MySetPasswordForm),
                       name='password_reset_confirm'),

                  path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name=
                                                                                                'app/password_reset_complete.html'),
                       name='password_reset_complete'),

                  path('registration/', views.ViewerRegistrationView.as_view(), name='Viewerregistration')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
