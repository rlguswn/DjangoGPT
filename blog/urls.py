from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", views.PostIndex.as_view(), name='list'),
    # # 글 상세 조회
    path("detail/<int:pk>/", views.PostDetail.as_view(), name='detail'),
    # # 글 작성
    path("write/", views.PostWrite.as_view(), name='write'),
    # # 글 수정
    path("detail/<int:pk>/update/", views.PostUpdate.as_view(), name='update'),
    # # 글 삭제
    path("detail/<int:pk>/delete/", views.PostDelete.as_view(), name='delete'),
    # # 코멘트 목록 조회
    path("comment/", views.CommentList.as_view(), name='cm-list'),
    # # 코멘트 작성
    path("detail/<int:pk>/comment/write/", views.CommentWrite.as_view(), name='cm-write'),
    # # 코멘트 삭제
    path("detail/comment/<int:pk>/delete/", views.CommentDelete.as_view(), name='cm-delete'),
]
