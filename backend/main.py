from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv
import os



# 1. LOAD ENVIRONMENT VARIABLES
load_dotenv()



# 2. CREATE FASTAPI APPLICATION
app = FastAPI()


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============================================================
# 3. GET SUPABASE CREDENTIALS
# ============================================================

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# ============================================================
# 4. CONNECT TO SUPABASE
# ============================================================

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# ============================================================
# 5. CREATE STUDENT - POST
# ============================================================

@app.post("/students")
def create_student(name: str, course: str, marks: int):

    try:

        # Data to be inserted into Supabase
        student = {
            "name": name,
            "course": course,
            "marks": marks
        }

        # Insert student into Supabase
        response = (
            supabase
            .table("students")
            .insert(student)
            .execute()
        )

        return {
            "message": "Student created successfully",
            "data": response.data
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "message": "Student creation failed",
            "error": str(e)
        }


# ============================================================
# 6. GET ALL STUDENTS - GET
# ============================================================

@app.get("/students")
def get_all_students():

    try:

        # Get all students from Supabase
        response = (
            supabase
            .table("students")
            .select("*")
            .execute()
        )

        return {
            "message": "Students retrieved successfully",
            "data": response.data
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "message": "Failed to get students",
            "error": str(e)
        }


# ============================================================
# 7. GET STUDENT BY ID - GET
# ============================================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    try:

        # Find student by ID
        response = (
            supabase
            .table("students")
            .select("*")
            .eq("id", student_id)
            .execute()
        )

        # Check if student exists
        if not response.data:
            return {
                "message": "Student not found"
            }

        return {
            "message": "Student found successfully",
            "data": response.data
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "message": "Failed to get student",
            "error": str(e)
        }


# ============================================================
# 8. UPDATE STUDENT - PUT
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    course: str,
    marks: int
):

    try:

        # New data
        student = {
            "name": name,
            "course": course,
            "marks": marks
        }

        # Update student in Supabase
        response = (
            supabase
            .table("students")
            .update(student)
            .eq("id", student_id)
            .execute()
        )

        # Check if student exists
        if not response.data:
            return {
                "message": "Student not found"
            }

        return {
            "message": "Student updated successfully",
            "data": response.data
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "message": "Student update failed",
            "error": str(e)
        }


# ============================================================
# 9. DELETE STUDENT - DELETE
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    try:

        # Delete student from Supabase
        response = (
            supabase
            .table("students")
            .delete()
            .eq("id", student_id)
            .execute()
        )

        # Check if student exists
        if not response.data:
            return {
                "message": "Student not found"
            }

        return {
            "message": "Student deleted successfully",
            "data": response.data
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "message": "Student deletion failed",
            "error": str(e)
        }