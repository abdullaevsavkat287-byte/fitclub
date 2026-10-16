
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "FitClub boshqaruv paneli"
admin.site.site_title = "FitClub Admin"
admin.site.index_title = "FitClub administratsiyasi"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("account/", include("accounts.urls")),
    path("membership/", include("memberships.urls")),
path("management/", include("management.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
