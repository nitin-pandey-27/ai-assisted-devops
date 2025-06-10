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

### Installing Ollama and select which MODEL to run

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

## 🚀 Project Setup or Setup of Python Environment 

1. **Create Virtual Environment. VENV are like VMs running on same host machine for Python. All the packages within a VENV will be separated from other VENV.**
   ```bash
   python3 -m venv venv
      - m venv - to start virtual environment
      - venv   - name of virtual environment 
   source venv/bin/activate  # On Linux/MacOS
      - venv - name of virtual environment
      - activate venv 
   # or
   .\venv\Scripts\activate  # On Windows
   ```

   ```bash
   python -m venv my_env
   This creates a directory my_env containing: A Python interpreter / A site-packages directory for installed libraries / Activation scripts for different shells

   source my_env/bin/activate
   Activating the Virtual Environment. Once activated, the environment's name appears in the terminal prompt, indicating that it is active. 
   Virtual environments are not portable. If moved to another location, they may break. It is recommended to recreate the environment instead
   Always activate the correct environment before working on a project to avoid dependency issues

   pip install <package_name>
   After activation, use pip to install packages:

   deactivate
   To exit the virtual environment, simply run


   rm -rf my_env
   To delete a virtual environment, deactivate it and remove its directory:
   
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
