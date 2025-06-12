# AI Assisted Shell Scripting

- No additional notes is required. Everything is covered as part of the video.


# Deepseek AI with CHATBOX.AppImage

- Deepseek AI R1
- R1 model is open
- Can make API calls as well
- OpenAI01 --> API calls

  Q. How to run Deepseek AI ?
  - download ollama and install it 
  # ollama pull deepseek-r1:1.5b
  # ollama run deepseek-r1:1.5b
  # lsof -i -P -n | grep <process_name>
  # ss -lptn | grep <PID>
  
  # curl http://localhost:11434 --> by default ollama starts on 11434 port number
  NOTE: 1.5b refer to parameters on which these models were trained. 1.5b means 1.5 billion parameters.

  # Download https://chatboxai.app/
  # chmod +x Chatbox......AppImage
  # sudo app install libfuse2
  # ./chatbox.AppImage --no-sandbox OR Directly run after providing +x permission
  # GUI Launch: Alternatively, after making it executable, you can double-click the file in your file manager to run it.

  # Settings --> Model Provider --> Ollama --> Add the UI , deepseek-r1:1.5b as model --> Apply & Save
  # New Chat --> Search Model --> Select deepseek-r1:1.5b

  
    libfuse --> allows user space application to interact with the file system. 
  - Open settings and select deepseek-r1 model with the localhost URL
  - Now you can use a chatGPT based UI interface to connect with deepseek-r1.
