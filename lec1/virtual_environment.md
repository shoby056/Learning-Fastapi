
## 📘 Lecture 2: FastAPI Installation, Virtual Environment, Uvicorn & First API

### 1️⃣ Concept
To use FastAPI, we need to install:

- Python (3.9+ recommended)  
- Virtual Environment (isolated project space)  
- FastAPI library  
- Uvicorn (server to run FastAPI)  

**What is a Virtual Environment?**  
- A separate Python space for each project  
- Dependencies don’t mix  

**Example:**  
If you have Python 3.10 and 3.11, and one project needs 3.10, another needs 3.11 → Virtual Environment solves this.

---

### 2️⃣ Installation Steps

**Step 1: Create Virtual Environment**
```bash
# Create project folder
mkdir fastapi_project
cd fastapi_project

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate