# AI Assisted Shell Scripting

- No additional notes is required. Everything is covered as part of the video.
- Use the self hosted LLM model to write the script
- That is AI Assisted Shell Scripting
- The shell commands changes rarely hence there is no way LLM Model will provide an outdated commands
- Prompt Engineering is Important
    - make sure latest commands
    - make sure latest OS
    - make sure secured shell scripts
 
  - AI Pair Programming - Write your code with AI to avoid mistakes. Like writing the code along with a senior watching your code.
 
  - Visual Studio Code --> Install Github Copilot Extension (AI Pair Programming  and AI Chat features )
 
  - Select some piece of line and right click to select explain from copilot
 
  - OTHER AI TOOLS similar to Github Copilot
 
  - cursor AI tools - AI Code Editor
  


# Deepseek AI with CHATBOX.AppImage

- Deepseek AI R1
- R1 model is open
- Can make API calls as well
- OpenAI01 --> API calls

  Q. How to run Deepseek AI ?
  - download ollama and install it. Please refer day-3 for more details.
  - pull the deepseek model and run it 
  ```
  # ollama pull deepseek-r1:1.5b
  # ollama run deepseek-r1:1.5b
  # lsof -i -P -n | grep <process_name>
  # ss -lptn | grep <PID>
  
  # curl http://localhost:11434 --> by default ollama starts on 11434 port number
  NOTE: 1.5b refer to parameters on which these models were trained. 1.5b means 1.5 billion parameters.
  ```

  ```
  # Download https://chatboxai.app/
  # chmod +x Chatbox......AppImage
  # sudo app install libfuse2
  # ./chatbox.AppImage --no-sandbox OR Directly run after providing +x permission
  # GUI Launch: Alternatively, after making it executable, you can double-click the file in your file manager to run it.

  # Settings --> Model Provider --> Ollama --> Add the UI , deepseek-r1:1.5b as model --> Apply & Save
  # New Chat --> Search Model --> Select deepseek-r1:1.5b
  NOTE: Above 2 steps may change depends on the version of chatbox.AppImage 
  ```
  
    libfuse --> allows user space application to interact with the file system. 
  - Open settings and select deepseek-r1 model with the localhost URL
  - Now you can use a chatGPT based UI interface to connect with deepseek-r1.
