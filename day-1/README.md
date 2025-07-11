# Day - 1 

## 1. Traditional AI in DevOps
Traditional AI relies on **structured data, pre-defined rules, and predictive models** trained on historical data. It excels at classification, forecasting, and anomaly detection.

### Example: Incident Detection & Prediction
- **Use Case:** Predicting system failures before they occur.
- **How It Works:**  
  - Uses **log-based anomaly detection** and **pattern recognition** (e.g., time-series forecasting).  
  - If CPU usage suddenly spikes beyond a threshold, AI predicts a potential issue.  
  - The system alerts DevOps teams to take preventive action.  
- **Limitations:**  
  - Works only on pre-trained scenarios.  
  - Cannot generate insights beyond structured input data.

 ### NOTES: 
 
**Predictive**
- **Trained on historical data OR Works only on pre-trained scenario**
- **Gives output based on historical data**
- **No thinking of its own without any historical data**
- **Cannot generate insights beyond structured input data**
- **Input could be - Only structured data**

**Use Case in DevOps** 
1. To predict events
2. For logs analysis
3. Observe pattern for incident management 
  

---

## 2. Generative AI in DevOps
Generative AI (Gen AI) leverages **large language models (LLMs)** to analyze, summarize, and even generate new content dynamically.

### Example: AI-Powered Incident Resolution & RCA
- **Use Case:** Automating root cause analysis (RCA) & remediation.  
- **How It Works:**  
  - **Understanding logs & metrics:** Gen AI processes unstructured log data, summarizes key issues, and suggests fixes.  
  - **Chat-based troubleshooting:** DevOps engineers can ask Gen AI:  
    _"Why did my Kubernetes pod crash?"_ → AI analyzes logs and suggests probable causes like OOM (Out of Memory) errors.  
  - **Auto-remediation:** AI suggests and even applies fixes (e.g., increasing memory limits in a YAML file).  
- **Advantages:**  
  - No need for extensive labeled training data.  
  - Can generate human-like explanations & solutions.  
  - Adaptable to new/unseen failure patterns.
 
   ### NOTES:
  - **Generative AI (Gen AI)  means it generates output based on some user input**
  - **It generates some output based on some user input. Input --> AI --> Output (Text,Image,Videos)**
  - **Input could be - some user written text, log files, any unstructured or structured data**
  - **Output could be text, images, videos**
  - **LLM - Large Language Model - if the output is text then it uses LLM**
  - **No training of historical data is required**
  - **Good for human intelligence and more user friendly**

---

## Key Differences Summary between Traditional AI and Generative AI 

| Feature            | Traditional AI                     | Generative AI                     |
|-------------------|--------------------------------    |--------------------------------|
| **Data Type**      | **Structured (logs, metrics)**    | **Structured + Unstructured (logs, docs, chat)**  |
| **Approach**       | **Predictive**, classification-based | **Generative**, contextual understanding |
| **Use Case**       | Detect anomalies, **forecast** failures | Explain failures, automate remediation |
| **Example**        | Alerts on high CPU usage       | Summarizes logs & suggests fixes |
| **Limitation**     | Requires **labeled datasets**     | May generate **incorrect suggestions** (hallucinations) |



---

## 3. Large Language Model
A Large Language Model (LLM) is an 
- **advanced AI system trained on vast amounts of text data**
- **to understand, generate, and process human language**. 

These models use **deep learning techniques**, particularly **transformers (like GPT, BERT, or LLaMA)**, to **recognize patterns, predict words, and generate human-like responses**.

**INPUT --> LLM --> Training**

NOTE: Input could be anything like google searches, some other algorithms etc. 
      Generative AI uses LLMs for text based output. 
      LLMs are trained with billions of input parameters like Traditional AI. 
      But Gen AI uses its own thinking based on the training before. 

**What is Prompt Engineering ?**
- LLM takes user input and generates text output
- The user input is known as prompt
- The efficient way to providing user input is prompt engineering
- Eg. These two user inputs will be treated differently by LLMs
- Generate a Kubernetes YAML manifest file
- Generate kubernetes manifests file with NGINX as image, Pod Security Policies, Security Context, Resource Limitation, Namespace, Node Affinity, Image Credentials, Liveness and Readiness Checks.


** What is AI Landscape for DevOps ?** 
- Landscape means the list of AI tools that are required for DevOps
- These are divided into 4 parts
    - AI Chatbots like ChatGPT, Deepseek, Iilama (AI Chatbots can take user input and give some output but can not execute the task)
    - AI Agents like Github Copilot, Bolt.new (AI Agents can perform the tasks. Agents can brainstrom and generate the plan as well. AI Agents can take user input and give some output and can also execute the task)
    - AI Assitants like Github Copilot, Perplexity, Cursor.ai 
    - Programming Lang. like Python, Fast API, Flask

---

**Practical using AI Agent**
1. Create a repo
2. Write shell script
3. Check CPU/Memory/Disk Space of a VM
4. If values <=60% then it should be healthy
5. Else Not healthy
6. Explain why its healthy and not healthy if pass an argument "healthy"
7. Create a good readme

