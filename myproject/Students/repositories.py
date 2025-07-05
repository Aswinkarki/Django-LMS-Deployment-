from Students.models import Student


class StudentRepository:
    """Handles database queries for the Student model."""

    @staticmethod
    def create_student(data):
        """Create a new student record."""
        return Student.objects.create(
            student_name=data.get('student_name'),
            email=data.get('email'),
            contact_number=data.get('contact_number'),
            department=data.get('department'),
        )

    @staticmethod
    def get_student_by_id(student_id):
        """Retrieve a student by ID."""
        return Student.objects.filter(student_id=student_id, is_deleted=False).first()

    @staticmethod
    def get_all_students():
        """Retrieve all students."""
        return Student.objects.filter(is_deleted=False).order_by('-created_date')

    @staticmethod
    def update_student(student, data):
        """Update an existing student record."""
        for key, value in data.items():
            if value is not None:  # Prevent overwriting with None
                setattr(student, key, value)
        student.save()
        return student

    @staticmethod
    def delete_student(student):
        """Soft delete a student record."""
        student.is_deleted = True
        student.save()
