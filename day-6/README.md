## AIOps 

- Use Traditional AI to analyse the data
- Use Generative AI for Anomaly detection
- Use AI Agents to rectify the anomalies

## Observability 

- Extensive use of AI for data analysis
- finding anamoly, rectifying the anomalies

## MLs

- Python script for writing the ML
- Always good to have historical data 
- Isolation Forest - Best for anomaly detection
- Random Forest

## Historical
- Logs --> Logstash/Fluentd --> Elastic --> Kibana metrics

Q> How do you get the pattern in the logs ? Or how do you get the anomaly detection. 
Ans. You can search for some error, warning etc. But to extract a pattern you needs to use AI. 
      AI Agent -> uses ML algorithm ( called Isolation Forest) -> will perform Anomaly Detection -> for Proactive approach

## Logs Reading 

```
1. Read the logs file
2. Seralize the data or Format the data (panda library from python)
    time | logs | string 

3. Create a for loop to go through the formatted logs (SIMPLE LOG ANAMOLY DETECTION)
    - use re (regular expression) for checking the logs in dd-mm-yyyy hh-mm-ss <Log-Level> <Some-Line> <Extra-line>
          <Log-Level> - INFO, WARN, ERROR, CRITICAL 
    - use panda for formatting the logs
    - use Counters to count the total number of occuring 
    - use threshould for the counters
    - detect anomaly
NOTE: This simple anamoly detection script just count the total number of occuring within some timeframe for some threshold
      However, its not calculating the response time for INFO, WARN, ERROR, CRITICAL etc.
      For raising the anamoly detection based on response time, you need AIOps.


4. Use AIOPs with Pandas, Numpy, IsolationForest.
    - pandas
    - numpy
    - isolationForest - it is a machine learning algorith
    - We will train the algorithm with the logs levels we have
```


## Isolation Forest 

```
IsolationForest **(Used for Anomaly Detection)**

Analogy: Imagine you're trying to find the one person wearing a red shirt in a crowd of people all wearing black. You don’t need to compare every detail — that red shirt stands out fast.

IsolationForest works similarly:
- It tries to "isolate" each data point by randomly splitting features.
- Unusual (outlier) data points get isolated faster because they are few and different.

Use case:
- Detect fraud
- **Identify unusual login patterns**
- Spot system failures

```

## Random Forest 

```
RandomForest **(Used for Classification and Prediction)**

Analogy: You ask 100 doctors to diagnose a patient. Most of them agree it’s the flu — you go with that.

- RandomForest works the same way:
-** Builds many decision trees.**
-** Each tree votes on the result.**
-** Majority wins = better accuracy.**

Use case:
- Spam detection
- Disease diagnosis
- **Customer churn prediction**
```

## JSON log File Example 
```
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from scipy.sparse import hstack
from datetime import datetime

# Step 1: Load JSONL logs
df = pd.read_json("app_logs.jsonl", lines=True)

# Step 2: Convert timestamp to numeric
df['@timestamp'] = pd.to_datetime(df['@timestamp'])
df['timestamp_num'] = df['@timestamp'].apply(lambda x: x.timestamp())

# Step 3: Encode categorical fields
df['level_enc'] = LabelEncoder().fit_transform(df['level'])
df['thread_enc'] = LabelEncoder().fit_transform(df['thread'])
df['class_enc'] = LabelEncoder().fit_transform(df['class'])

# Step 4: Vectorize message text
tfidf = TfidfVectorizer(max_features=100)  # limit features for performance
message_tfidf = tfidf.fit_transform(df['message'])

# Step 5: Combine all features (numerical + vectorized text)
from scipy.sparse import csr_matrix
numeric_features = csr_matrix(df[['timestamp_num', 'level_enc', 'thread_enc', 'class_enc']].values)
X = hstack([numeric_features, message_tfidf])

# Step 6: Fit IsolationForest
iso = IsolationForest(n_estimators=100, contamination=0.15, random_state=42)
df['anomaly'] = iso.fit_predict(X)

# Step 7: Display anomalies
anomalies = df[df['anomaly'] == -1]
print("\n🔍 Anomalies Detected:")
print(anomalies[['@timestamp', 'level', 'thread', 'class', 'message']])

```

## Steps 
```
# python3 -m venv aiops     # to start a venv
# source aiops/bin/activate # to move in venv
# python3 <script.py>
# pip install <module-1> <module-2> .....
# deactivate --> to move out of venv

```

