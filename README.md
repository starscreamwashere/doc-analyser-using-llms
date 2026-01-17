An AI-powered Health-Tech solution that analyzes medical reports (PDFs) to extract key health metrics and suggest wellness steps. Built with a modular microservices architecture.

## 🚀 Tech Stack
- **Backend:** FastAPI (Python), LangChain, Google Gemini AI
- **Frontend:** HTML5, CSS3, JavaScript (Nginx)
- **DevOps:** Docker, Docker Compose
- **Architecture:** Modular Service-Layer Pattern

## 🛠️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-link>

   Create a .env file in the backend/ directory using .env.example.
2.Start the application using Docker: docker-compose up --build
3.Access the UI at http://localhost and API docs at http://localhost:8000/docs.

🏗️ Architecture
The project follows a Modular Monolith approach:

Service Layer: Decouples business logic (PDF parsing, LLM calls) from API routes.
Dependency Injection: Used in FastAPI for scalable service management.
Containerization: Multi-stage Docker builds for production efficiency.

### Step 4: Initialize Git and Push to GitHub

1.  **Initialize locally:**
    ```bash
    git init
    git add .
    git commit -m "Initial commit: Professional Health-Tech AI Analyzer"
    ```

2.  **Verify `.env` is ignored:**
    Run this command: `git status`. You should **NOT** see `.env` listed in the files to be committed.

3.  **Create Repository on GitHub:**
    - Go to [GitHub](https://github.com/) and create a new repository named `medical-analyzer`.
    - Keep it **Public** (so the interviewers can see it).
    - **Do not** check "Initialize this repository with a README" (we already made one).

4.  **Connect and Push:**
    (Replace `<your-username>` with your actual GitHub name)
    ```bash
    git remote add origin https://github.com/<your-username>/medical-analyzer.git
    git branch -M main
    git push -u origin main
    ```

---
