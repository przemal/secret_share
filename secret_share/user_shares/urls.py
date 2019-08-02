from django.urls import path

from secret_share.user_shares.views import AddUserShareView
from secret_share.user_shares.views import UserShareView
from secret_share.user_shares.views import UserShareInfoDetailView

app_name = 'user_shares'
urlpatterns = [
    path('', AddUserShareView.as_view(), name='add'),
    path('<int:pk>', UserShareView.as_view(), name='get'),
    path('<int:pk>/info', UserShareInfoDetailView.as_view(), name='info'),
]
