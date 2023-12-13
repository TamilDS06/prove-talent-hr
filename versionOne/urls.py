from django.urls import path
from versionOne.API.candidatedirAPI import CandidateCreateAPIView, CandidateUpdateAPIView, CandidateListRetrieveAPIView, CandidateDeleteAPIView

urlpatterns = [
    path('create-a-record/', CandidateCreateAPIView.as_view(), name = 'Create a candidate record'), # [POST] http://127.0.0.1:8000/v1/create-a-record/
    path('candidates-update/<int:pk>/', CandidateUpdateAPIView.as_view(), name='candidate-update'), # [PUT] http://localhost:8000/candidates-update/1/
    path('candidates-list/', CandidateListRetrieveAPIView.as_view(), name='candidate-list'),# [GET] http://localhost:8000/candidates-list/
    path('candidates-retrive/<int:pk>/', CandidateListRetrieveAPIView.as_view(), name='candidate-retrieve'), # [GET] http://localhost:8000/candidates-retrive/1/
    path('candidates/delete/<int:pk>/', CandidateDeleteAPIView.as_view(), name='candidate-delete'), # [DELETE] http://localhost:8000/candidates/delete/1/
]