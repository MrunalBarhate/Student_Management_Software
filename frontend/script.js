// FastAPI backend URL
const API_URL = "http://127.0.0.1:8000";


// ============================================================
// ADD STUDENT
// ============================================================

async function addStudent() {

    const name = document.getElementById("name").value;
    const course = document.getElementById("course").value;
    const marks = document.getElementById("marks").value;

    const response = await fetch(
        `${API_URL}/students?name=${encodeURIComponent(name)}&course=${encodeURIComponent(course)}&marks=${marks}`,
        {
            method: "POST"
        }
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


// ============================================================
// GET ALL STUDENTS
// ============================================================

async function getAllStudents() {

    const response = await fetch(
        `${API_URL}/students`
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


// ============================================================
// GET STUDENT BY ID
// ============================================================

async function getStudent() {

    const id = document.getElementById("studentId").value;

    const response = await fetch(
        `${API_URL}/students/${id}`
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


// ============================================================
// UPDATE STUDENT
// ============================================================

async function updateStudent() {

    const id = document.getElementById("updateId").value;
    const name = document.getElementById("updateName").value;
    const course = document.getElementById("updateCourse").value;
    const marks = document.getElementById("updateMarks").value;

    const response = await fetch(
        `${API_URL}/students/${id}?name=${encodeURIComponent(name)}&course=${encodeURIComponent(course)}&marks=${marks}`,
        {
            method: "PUT"
        }
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


// ============================================================
// DELETE STUDENT
// ============================================================

async function deleteStudent() {

    const id = document.getElementById("deleteId").value;

    const response = await fetch(
        `${API_URL}/students/${id}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}