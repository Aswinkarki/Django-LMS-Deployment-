from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'student_id', 'student_name', 'email', 'contact_number', 'department', 
            'created_date', 'updated_date', 'is_deleted'
        ]


def validate(self, data):
    email = data.get('email', self.instance.email if self.instance else None)

    print(f"DEBUG: Validating email {email} for student. Current instance: {self.instance}")

    if email:
        query = Student.objects.filter(email=email)

        if self.instance:
            query = query.exclude(student_id=self.instance.student_id)

        print(f"DEBUG: Existing students with this email: {query.exists()}")

        if query.exists():
            raise serializers.ValidationError("A student with this email already exists.")

    return data




