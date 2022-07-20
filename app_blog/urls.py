from django.urls import path
from app_blog.views import CreateRecordView, ListRecordView, UploadRecordView, RecordDetailView

urlpatterns = [
    path('create/', CreateRecordView.as_view(), name='create_url'),
    path('records/', ListRecordView.as_view(), name='records_url'),
    path('upload_record/', UploadRecordView.as_view(), name='upload_url'),
    path('record/<int:pk>', RecordDetailView.as_view()),
]
