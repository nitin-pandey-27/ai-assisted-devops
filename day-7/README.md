## Create your First AI Agent with zero coding and zero cost

## What are AI Agents ?
```
AI Assistents
- They can create text output without performing tasks. Like ChatGPT.
- They also communicate with LLM

AI Agents
- They can perform tasks on your behalf. Like Git Copilot.
- You can have multiple AI Agents running at the same time that can execute tasks in parallel.
- 1 AI Agent can also act as a viewer for other AI Agents and its purpose will be to unblock any stuck AI Agent.
- They also communicate with LLM.
```

## AI Agents Framework ? 
```
- Github Copilot, bolt.new they are enterprise AI Agents and require some paid subscription
**- Agents like (Autogen, Crew AI, LargeGraph) are open source agents that can be integrated with Local LLMs. **

- We will use Crew AI with Local LLM for further AI Agents practice. 
```

## CREW AI 
```
- CREWAI - is known for Research and Reporting related tasks. 
- Develop 2 agents
- 1st Agent will perform Research
- 2nd Agent will summarise the research for the blog
- https://www.crewai.com/open-source

== Instal CREW AI and Create Agents - 11:09
# mkdir crewai
# python3 -m venv crewai
# source crewai/bin/activate
# pip3 install crewai
# cd crewai/bin
# crewai create crew devops-ai-project
# crewai create crew devops-ai-project
Creating folder devops_ai_project...
Cache expired or not found. Fetching provider data from the web...
Downloading  [####################################]  532309/25267
Select a provider to set up:
1. openai
2. anthropic
3. gemini
4. nvidia_nim
5. groq
6. huggingface
7. ollama
8. watson
9. bedrock
10. azure
11. cerebras
12. sambanova
13. other
q. Quit
Enter the number of your choice or 'q' to quit: 7
Select a model to use for Ollama:
1. ollama/llama3.1
2. ollama/mixtral
q. Quit
Enter the number of your choice or 'q' to quit: 1
API keys and model saved to .env file
Selected model: ollama/llama3.1
  - Created devops_ai_project/.gitignore
  - Created devops_ai_project/pyproject.toml
  - Created devops_ai_project/README.md
  - Created devops_ai_project/knowledge/user_preference.txt
  - Created devops_ai_project/src/devops_ai_project/__init__.py
  - Created devops_ai_project/src/devops_ai_project/main.py
  - Created devops_ai_project/src/devops_ai_project/crew.py
  - Created devops_ai_project/src/devops_ai_project/tools/custom_tool.py
  - Created devops_ai_project/src/devops_ai_project/tools/__init__.py
  - Created devops_ai_project/src/devops_ai_project/config/agents.yaml
  - Created devops_ai_project/src/devops_ai_project/config/tasks.yaml
Crew devops-ai-project created successfully!
(crewai) root@cyber:~/crewai#  ollama pull llama3.1
(crewai) root@cyber:~/crewai#  ollama run llama3.1


- A folder will be created "devops_ai_project" which contains all the files required to run the agents.yaml and tasks.yaml
- Main files are "devops_ai_project/config/agents.yaml" and "devops_ai_project/config/tasks.yaml"
- agents.yaml --> will define the agents. Can define multiple agents.
- tasks.yaml --> will include the tasks that will be performed by the agents. Each agent will have its own tasks.
- devops_ai_project/main.py --> you need to change the TOPIC and the OUTPUT. main.py also invokes the function in crew.py
- crew.py --> it includes all the functions as a class.

# crewai install  --> this will interact with LLM + create a file uv.lock 
# crewai run      --> 1st agent will interact with llama and 2nd agent will also interact with llama + it will generate report and report.md file in final outcome   

```


## CREW AI WITH META QUEST PROJECT FOR DOCUMENTATION 
```
# git clone https://github.com/crewAIInc/crewAI-examples.git
# cd crewAI-examples/meta-quest-example
# ls -lrth
total 668K
-rw-r--r-- 1 root root 2.0K Jun 15 23:26 README.md
drwxr-xr-x 3 root root 4.0K Jun 15 23:26 src
-rw-r--r-- 1 root root  577 Jun 15 23:26 pyproject.toml
-rw-r--r-- 1 root root 649K Jun 15 23:26 uv.lock
drwxr-xr-x 2 root root 4.0K Jun 15 23:27 knowledge

# cd knowledge  --> COPY the PDF files required in this location.

# cd ../src/meta_quest_knowledge/config --> Edit tasks.yaml and agents.yaml files to change the name of the expert.

# cd src/meta_quest_knowledge  --> Edit crew.py and replace sdk_expert at relevant location.

# cd crewAI-examples/meta_quest_knowledge --> Goto main project folder and execute
# pip install uv
# vi pyproject.toml  --> Edit meta_quest_Knowledge
# crewai install
# crewai run

```




