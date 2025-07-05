from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from .services import StudentService
from .serializers import StudentSerializer

class StudentListCreateView(APIView):
    """Handles listing and creating students."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = StudentService.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            try:
                student = StudentService.create_student(serializer.validated_data)
                return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"detail": "Error creating student"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    """Handles retrieving, updating, and deleting a student."""
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        student = StudentService.get_student(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, student_id):
        student = StudentService.get_student(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            updated_student = StudentService.update_student(student_id, serializer.validated_data)
            return Response(StudentSerializer(updated_student).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_id):
        success = StudentService.delete_student(student_id)
        if success:
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
