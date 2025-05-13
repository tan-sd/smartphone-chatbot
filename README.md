## 📋 Requirements

Before running this project, ensure the following are installed on your **host machine**:

### 🧠 Ollama (LLM Runtime)
- [Download and install Ollama](https://ollama.com/download)
- Start the model server before using the chatbot:
  ```bash
  ollama run llama3
  ```

### 🐳 Docker
- [Install Docker](https://www.docker.com/products/docker-desktop)
- Ensure Docker is running:
  ```bash
  docker --version
  ```
---
## 📦 Build and Run

1. Build the Docker image:
```bash
docker build -t smartphone-chatbot .
```

2. Run the container:
```bash
docker run -p 8501:8501 smartphone-chatbot
```
