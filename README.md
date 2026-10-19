# Spanish Learning Platform 🇪🇸

An interactive Spanish learning platform built for Greek speakers. Study through structured chapters, practice with chapter-based exams, and track your progress as you learn.

## Contributors

- **Aggelos Ladas** — Backend · [![Portfolio](https://img.shields.io/badge/Portfolio-24292f?style=flat-square&logo=googlechrome&logoColor=white)](https://www.aggelosladas.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aggelos-ladas-9057b1196/)
- **Stefanos Souroullas** — Frontend

## Screenshots

### Home
![Home page](Images/Screenshot_1.png)

### Lessons
Browse the available chapters and work through the material at your own pace.

![Lessons](Images/Screenshot_2.png)

### Exams
Practice what you've learned with chapter-based questions and exercises.

![Exams](Images/Screenshot_3.png)

### Progress
Keep track of completed chapters, exam scores, and learning progress.

![Progress](Images/Screenshot_4.png)

### Exam Results
Review your answers, check your score, and identify mistakes.

![Exam results](Images/Screenshot_5.png)

## Features

- **Structured lessons** — Learn Spanish through organized chapters.
- **Interactive exams** — Test your understanding with chapter-specific exercises.
- **Progress tracking** — Track completed chapters and exam performance.
- **Answer review** — Review your results and identify incorrect answers.
- **Persistent progress** — Return to your learning without starting over.
- **Greek interface** — Learn Spanish with explanations and navigation designed for Greek speakers.

## Tech Stack

- **Frontend:** React, Vite, Nginx
- **Backend:** Python, FastAPI, Uvicorn
- **Database:** SQLite
- **Containerization:** Docker and Docker Compose

## Getting Started

Docker Compose is the easiest way to run the application locally.

### Prerequisites

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine with Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/AggelosLadas/Spanish-Learning-Platform.git
cd Spanish-Learning-Platform
```

### 2. Build and start the application

```bash
docker compose up --build
```

This builds the frontend and backend images and starts the containers.

### 3. Open the application

Once the containers are running, visit:

**http://localhost:8080**

The frontend is available on port `8080`. The backend listens on port `8000` inside its container.

To check container status:

```bash
docker compose ps
```

To view application logs:

```bash
docker compose logs -f
```

### 4. Stop the application

Press `Ctrl+C` if running in the foreground, then run:

```bash
docker compose down
```

To start it again in the background:

```bash
docker compose up -d
```

To rebuild after making changes:

```bash
docker compose up -d --build
```

**Note:** Database persistence depends on your Docker volume configuration. Avoid removing volumes if you want to preserve existing data.

## Project Structure

```text
Spanish-Learning-Platform/
├── Images/
│   ├── Screenshot_1.png
│   ├── Screenshot_2.png
│   ├── Screenshot_3.png
│   ├── Screenshot_4.png
│   └── Screenshot_5.png
├── backend/
├── frontend/
├── docker-compose.yml
├── LICENSE.txt
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
