# Lesta Start DevOps 2025 Test Task

A test task repository for the **Lesta Start DevOps 2025** program. This project demonstrates a simple application designed to showcase DevOps practices such as containerization, deployment, and automation.

## Prerequisites

- Docker (for containerized execution)
- Git (for cloning the repository)

Installing on Arch Linux (I use Arch, btw :)
```bash
pacman -S --needed git docker docker-compose docker-buildx
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/feelamee/lesta-start-devops-2025-test-task.git
cd lesta-start-devops-2025-test-task
```

### Run with Docker

```bash
docker compose up --build
```

### Test

```bash
curl http://localhost:5000/ping
curl http://localhost:5000/count
```
