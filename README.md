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
1. Clone the repository:
```bash
git clone https://github.com/tan-sd/smartphone-chatbot.git
cd smartphone-chatbot
```

2. Build the Docker image:
```bash
docker build -t smartphone-chatbot .
```

3. Run the container:
```bash
docker run -p 8501:8501 smartphone-chatbot
```

Navigate to http://localhost:8501 in your browser to begin using the chatbot.
