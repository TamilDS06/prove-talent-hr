from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import traceback
from versionOne.API.Serializer import CandidatedirectorySerializer
from versionOne.models import CandidateDirectory

class CandidateCreateAPIView(APIView):
    def post(self, request):
        try:
            serializer = CandidatedirectorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exceptions:
            result = {"status":False, "Message":f"create record failed!{exceptions.args}"}
            return Response(result) 
        

class CandidateUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            candidate = CandidateDirectory.objects.get(id=id)
            serializer = CandidatedirectorySerializer(candidate, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except CandidateDirectory.DoesNotExist:
            return Response({"status": False, "message": f"Record with ID {id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"status": False, "message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        


class CandidateListRetrieveAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:  # If primary key is provided, return specific record
            try:
                candidate = CandidateDirectory.objects.get(pk=pk)
                serializer = CandidatedirectorySerializer(candidate)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CandidateDirectory.DoesNotExist:
                return Response({"status": False, "Message": "Record does not exist"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"status": False, "Message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:  # If no primary key provided, return all records
            try:
                candidates = CandidateDirectory.objects.all()
                serializer = CandidatedirectorySerializer(candidates, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"status": False, "Message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class CandidateDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            candidate = CandidateDirectory.objects.get(pk=pk)
            candidate.delete()
            return Response({"status": "Success", "message": f"Record with ID {pk} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except CandidateDirectory.DoesNotExist:
            return Response({"status": "Error", "message": f"Record with ID {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status": "Error", "message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        