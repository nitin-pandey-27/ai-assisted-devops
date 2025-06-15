## Docker Model Runner
```
- Important Links for Docker Model Runner 
- https://www.youtube.com/watch?v=uFaxKSEBr08&list=PLdpzxOOAlwvJ_qWyuqhbHteY84O1qr72a&index=10
- https://github.com/docker/hello-genai
- https://docs.docker.com/ai/model-runner/
- https://hub.docker.com/u/ai

Q. What is Docker Model Runner ?
ANS.
- It is used to run LLM models using Docker
- Similar to Ollama but can run the models with docker
- Models are pulled from Docker Hub the first time they're used and stored locally.
- They're loaded into memory only at runtime when a request is made, and unloaded when not in use to optimize resources.
- Since models can be large, the initial pull may take some time — but after that, they're cached locally for faster access.
- You can interact with the model using OpenAI-compatible APIs.

Q. How to start docker model runner ?
ANS.
- Enable DMR in Docker Desktop
- Enable DMR in Docker Engine
- Install Docker Engine as mentioned here "https://docs.docker.com/engine/install/ubuntu/"
# sudo apt-get update
# sudo apt-get install docker-model-plugin
# docker model
# docker model version
# docker model status
NOTE: The command is "docker model" for Docker Model Runner.

Q. How to pull a model and run the model ?
ANS.
- Select the model to run "https://hub.docker.com/u/ai"
# docker model pull ai/deepseek-r1-distill-llama    --> This will pull and start docker model 
# docker model run ai/deepseek-r1-distill-llama

- Example of pull command
#docker model pull ai/deepseek-r1-distill-llama
latest: Pulling from docker/model-runner Digest: sha256:2b06fa65d2c72af24838d07ebaa93e248ed9d1cadbabb68f0a784d038841fd9f
Status: Image is up to date for docker/model-runner:latest

Successfully pulled docker/model-runner:latest
Starting model runner container docker-model-runner...
Downloaded: 1964.86 MB

- Inspect a model 
# docker model inspect ai/deepseek-r1-distill-llama
- Check the logs
# docker model logs
- List the available models that can be run with the Docker Model Runner
# docker model list 



Q. Publish a model ?
ANS.
# Tag a pulled model under a new name
docker model tag ai/smollm2 myorg/smollm2
# Push it to Docker Hub
docker model push myorg/smollm2
# Download a model file in GGUF format, e.g. from HuggingFace
curl -L -o model.gguf https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf
# Package it as OCI Artifact and push it to Docker Hub
docker model package --gguf "$(pwd)/model.gguf" --push myorg/mistral-7b-v0.1:Q4_K_M
- Check all the commands at "https://docs.docker.com/reference/cli/docker/model/"

Q. How to  Integrate Docker Model Runner into your software development lifecycle ?
ANS.
- https://github.com/docker/hello-genai for running the model 
- Clone the repo - git clone https://github.com/docker/hello-genai.git
- Edit ".env" file and update "LLM_BASE_URL" and "LLM_MODEL_NAME"
- Start the environment "run.sh"



```
