import json
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix, hstack

# === CONFIG ===
INPUT_TXT_FILE = "logs.txt"
OUTPUT_JSONL_FILE = "logs.jsonl"

# === STEP 1: Convert txt to JSONL with safe field names ===
def prepare_jsonl(txt_path, jsonl_path):
    with open(txt_path, "r") as infile, open(jsonl_path, "w") as outfile:
        for line in infile:
            try:
                log_entry = json.loads(line.strip())

                # Rename reserved keyword
                if "class" in log_entry:
                    log_entry["class_name"] = log_entry.pop("class")

                outfile.write(json.dumps(log_entry) + "\n")
            except json.JSONDecodeError:
                print(f"❌ Invalid JSON: {line.strip()}")

# === STEP 2: Detect anomalies with IsolationForest ===
def detect_anomalies(jsonl_path):
    df = pd.read_json(jsonl_path, lines=True)

    # Convert timestamp safely
    df['@timestamp'] = pd.to_datetime(df['@timestamp'], errors='coerce')
    df = df.dropna(subset=['@timestamp'])  # Drop rows with invalid timestamp
    df['timestamp_num'] = df['@timestamp'].apply(lambda x: x.timestamp())

    # Encode categorical features
    df['level_enc'] = LabelEncoder().fit_transform(df['level'])
    df['thread_enc'] = LabelEncoder().fit_transform(df['thread'])
    df['class_enc'] = LabelEncoder().fit_transform(df['class_name'])

    # TF-IDF on full message content
    tfidf = TfidfVectorizer(max_features=150)
    msg_vec = tfidf.fit_transform(df['message'])

    # Feature matrix
    numeric = csr_matrix(df[['timestamp_num', 'level_enc', 'thread_enc', 'class_enc']].values)
    X = hstack([numeric, msg_vec])

    # Fit IsolationForest
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    df['anomaly'] = model.fit_predict(X)

    # === STEP 3: Keyword-based severity tagging ===
    def tag_severity(msg):
        msg = msg.lower()
        if "exception" in msg:
            return "Exception"
        elif "timeout" in msg:
            return "Timeout"
        elif "error" in msg:
            return "Error"
        elif "fail" in msg:
            return "Failure"
        else:
            return "Normal"

    df['severity'] = df['message'].apply(tag_severity)

    # === STEP 4: Show and group anomalies ===
    anomalies = df[df['anomaly'] == -1]
    print("\n🔍 Anomalies Detected:\n")
    print(anomalies[['@timestamp', 'level', 'thread', 'class_name', 'message', 'severity']])

    print("\n📊 Grouped by class_name:")
    print(anomalies.groupby('class_name').size().sort_values(ascending=False))

    print("\n📊 Grouped by thread:")
    print(anomalies.groupby('thread').size().sort_values(ascending=False))

    # Optionally: save to CSV
    anomalies.to_csv("detected_anomalies.csv", index=False)

# === RUN ===
prepare_jsonl(INPUT_TXT_FILE, OUTPUT_JSONL_FILE)
detect_anomalies(OUTPUT_JSONL_FILE)
