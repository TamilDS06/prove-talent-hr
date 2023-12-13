from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Candidatedirectory
from versionOne.API.Serializer import CandidatedirectorySerializer
import traceback

# @api_view(['POST'])
# def create_candidate(request):
#     try:
#         if request.method == 'POST':
#             serializer = CandidatedirectorySerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             return Response(serializer.errors, status=400)
#         else:
#             result = {"status":False, "Message":"Method not allowed!!Create a recode failed!"}
#             return Response(result, status=400)
#     except Exception as exception:
#         print("Error occured while creating candidate record!", exception.args)
#         result = {"status":False, "Message":f"Create a recode failed!{traceback.format_exc()}"}
#         return Response(result, status=400)