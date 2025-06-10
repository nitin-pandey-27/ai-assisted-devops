# 🐳 What is LLM ? 

- LLM Large Language Model
- https://aws.amazon.com/what-is/large-language-model/
        - 
- Backbone of Generative AI
- Can perform Text Based Output generation
- 2 types
- Local or Self Hosted
        - LLMs run within our local environment
        - Meta - llama
        - Deepseek -
        - Pros and Cons
            - Good Security
            - Need to setup & manage infrastrcuture 
  
- Cloud Hosted
        - Hosted by companies like OpenAI , Google (Gemini),
        - Requires API Keys / Token to connect with them and call the APIs
        - Pros and Cons
            - Not secured because its over internet
            - Costly in terms of API calls (Charges based on TOKENS - These TOKEN are the combination of TOTAL WORDS (Both input and output words)).
            - No need to setup and manage infrastrcuture

- Local LLM 
        - Use OLLAMA
        - ollama is repository of LLM Models.
        - It is like dockerhub for storing LLM models
        - Also, provides CLI to manage and install LLM Models
        - https://github.com/ollama/ollama

# 🐳 Dockerfile Generator

A GenAI powered tool that generates optimized Dockerfiles based on programming language input. This project uses Ollama with the Llama3 model to create Dockerfiles following best practices.

## 📋 Prerequisites

### Installing Ollama

1. **Download and Install Ollama**
   ```bash
   # For Linux
   curl -fsSL https://ollama.com/install.sh | sh

   # For MacOS
   brew install ollama
   ```

2. **Start Ollama Service**
   ```bash
   ollama serve

   ollama start
   ```

3. **Pull Llama3 Model. This will pull the model like #docker pull <image>. This command wont start the model like #docker start --image <some-image>**
   ```bash
   ollama pull llama3.2:1b
   ```

4. **Start Llama3 Model. This will start the model. Time it takes to start the model will differ based on the GPU availability. Once you start it you can use it as Text Based Gen AI**
   ```bash
   ollama run llama3.2:1b
   ```

## 🚀 Project Setup

1. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python3 generate_dockerfile.py
   ```

## 💡 How It Works

1. The script takes a programming language as input (e.g., Python, Node.js, Java)
2. Connects to the Ollama API running locally
3. Generates an optimized Dockerfile with best practices for the specified language
4. Returns the Dockerfile content with explanatory comments

## 📝 Example Usage

```bash
python3 generate_dockerfile.py
Enter programming language: python
# Generated Dockerfile will be displayed...
```

## 🏆 Troubleshooting
- Make sure Ollama service is running before executing the script.
- Ensure the correct model is downloaded.
- Adapt best practices for other programming languages as needed.
