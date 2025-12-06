from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    '''
    Full CRUD API for Student model:
    - GET /api/students/           -> list
    - POST /api/students/          -> create
    - GET /api/students/{id}/      -> retrieve (by id)
    - PUT /api/students/{id}/      -> full update
    - PATCH /api/students/{id}/    -> partial update
    - DELETE /api/students/{id}/   -> delete
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
