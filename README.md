# TOPHAWKS-AI-INTERNSHIP-PRACTICAL-SCREENING-ASSIGNMENT

## Candidate: Priyanshu Saini

---

##  Introduction

This repository presents my end-to-end solution to the **Tophawks AI Internship Screening Assignment**.
The goal of this submission is to demonstrate the ability to design **practical AI systems** that solve the real-world business problems.

The approach focuses on:

* Building a scalable and reliable AI pipelines
* Combining the machine learning with business understanding
* Handling of messy, real-world data
* Delivering the simple yet impactful solutions

---

# SECTION 1: ARCHITECTING SOLUTIONS

## Q1. Intelligent Lead Scoring System

### Logic

The system predicts the probability of a lead converting using both **demographic data** and **behavioral intent signals**.

### Data Handling

* **Categorical Features** (Industry, Company Size)
  → Encoded using One-Hot Encoding or Target Encoding (for high-cardinality features)

* **Numerical Features** (Website Traffic, Engagement Metrics)
  → Scaled using StandardScaler / MinMaxScaler

* **Missing Values**
  → Handled using median/mode imputation to ensure robustness

---

### Intent Signal Engineering

Not all features contribute equally. High-intent signals are prioritized:

* Time spent on pricing/product pages
* Number of return visits
* Demo requests or form submissions
* Email click-through rate

These signals either:

* Receive higher weights during feature engineering, OR
* Are automatically prioritized by tree-based models

---

### Modeling Approach

* Supervised learning using historical data (Converted / Not Converted)
* Model: **XGBoost / LightGBM** (handles tabular + non-linear patterns well)

The model outputs a probability score, which is scaled to **0–100** for business interpretation.

Additionally, **feature importance** is analyzed to help sales teams understand key conversion drivers.

---

### Sample Output

```json
{
  "generated_at": "2026-04-04T10:30:00Z",
  "leads": [
    {
      "lead_id": "L001",
      "company_name": "ABC Technologies",
      "conversion_score": 94,
      "priority": "High"
    },
    {
      "lead_id": "L002",
      "company_name": "XYZ Manufacturing",
      "conversion_score": 72,
      "priority": "Medium"
    }
  ]
}
```

---

### Tech Stack

* Python (Pandas, NumPy)
* Scikit-learn
* XGBoost / LightGBM
* Optional: OpenAI Embeddings (for text signals)

---

## Q2. Data Wrangling: Handling Messy Data

### 🏗 Pipeline Overview

A modular pipeline is designed to transform unstructured inputs into structured data:

**Data Sources → OCR → Cleaning → LLM Extraction → Validation → Storage → Dashboard**

---

### Step-by-Step Pipeline

1. **Data Ingestion**

   * Inputs: WhatsApp chats, PDFs, Excel sheets

2. **OCR & Text Extraction**

   * Tools: Tesseract OCR / AWS Textract

3. **Preprocessing**

   * Remove noise, normalize formats (dates, currency)
   * Standardize text and encoding

4. **LLM-Based Extraction**

   * Extract structured fields (Name, Date, Amount, etc.)
   * Use prompt templates for consistent output

5. **Schema Mapping**

   * Convert extracted data into structured schema
   * Enforce correct data types

6. **Validation Layer**

   * Regex checks (dates, numbers)
   * Range validation
   * Cross-field consistency

7. **Storage**

   * SQL database (PostgreSQL / MySQL)

8. **Dashboard**

   * Streamlit / Power BI / Tableau

---

### Validation Strategy (Avoiding Hallucination)

* Source grounding (verify against original text)
* Confidence scoring for extracted fields
* Rule-based validation (format checks)
* Cross-field validation
* Human-in-the-loop for low-confidence cases
* Logging and retry mechanisms for failed extractions

---

##  Q3. Workflow Automation (Resume Screening)

### Workflow

**Resume Input → Text Extraction → Skill Extraction → Similarity Matching → Scoring → Ranked Candidates → Dashboard**

---

### How It Works

* Extract text from resumes (PDF/DOCX)
* Use NLP (TF-IDF or embeddings) to match skills with job description
* Compute similarity score
* Rank candidates based on relevance

---

### Estimated Impact

* Manual effort: ~20 hours/week per recruiter
* Automated system: ~5 hours/week

For a team of 10 → **~150 hours saved per week**

---

# SECTION 2: HANDS-ON AI & DEVELOPMENT

## Q4. Engineering the Perfect Prompt

### System Prompt

You are an AI Customer Support Assistant.

Your task is to analyze a raw customer complaint and return a structured JSON output with the following fields:

* Sentiment (1 to 5, where 1 = very negative, 5 = very positive)
* Root_Issue (concise summary of the problem)
* Draft_Response (polite, professional, and helpful response)

Rules:

* Always return valid JSON only (no extra text)
* Do not hallucinate missing information
* If the issue is unclear, set Root_Issue as "Unknown"
* Keep the response empathetic and concise

---

### Example

**Input:**
"My order arrived late and the product is damaged."

**Output:**

```json
{
  "Sentiment": 1,
  "Root_Issue": "Late delivery and damaged product",
  "Draft_Response": "We sincerely apologize for the inconvenience caused. We will arrange a replacement or refund immediately."
}
```

---

## Q5. Mini AI Tool – Lead Scoring App

### Overview

A simple AI-powered web app that predicts lead conversion probability.

---

### Workflow

**User Input → Preprocessing → Model Prediction → Score Output → UI Display**

---

### Features

* Input form for lead attributes
* Real-time prediction
* Conversion score (0–100)
* Priority classification (High / Medium / Low)

---

### Model Logic

* Preprocessing: encoding + scaling
* Model: trained classification model (XGBoost / Logistic Regression)
* Output: probability → converted to score

---

### Tech Stack

* Python
* Scikit-learn
* Streamlit (UI)

---

# SECTION 3: DATA & ANALYTICS INTELLIGENCE

## Q6. Feature Engineering

### Key Features

* Time spent on pricing page
* Number of demo requests
* Email engagement rate
* Company size
* Industry type
* Website visit frequency
* Past purchase history
* Lead source

---

### Why Pricing Page Matters

“Time spent on pricing page” is a **high-intent signal**, indicating strong buying interest.
In contrast, total website visits may include casual browsing with no conversion intent.

---

## Q7. Beyond Accuracy

### Why Accuracy is Misleading

Lead datasets are often imbalanced (many non-converting leads).
A model predicting “no conversion” can still achieve high accuracy but provide no business value.

---

### Metrics to Prioritize

* **Recall (High Priority)**
  → Ensures high-value leads are not missed

* **Precision**
  → Avoids wasting time on low-quality leads

* **F1-Score**
  → Balances precision and recall

---

# ⚙️ SECTION 4: TECHNICAL PROFICIENCY

| Skill                  | Level        |
| ---------------------- | ------------ |
| Python (Pandas/NumPy)  | Intermediate |
| Scikit-learn / ML      | Intermediate |
| OpenAI APIs            | Intermediate |
| LangChain / LlamaIndex | Beginner     |
| Streamlit / Gradio     | Intermediate |
| Git / GitHub           | Intermediate |

---

# SECTION 5: STRATEGIC THINKING

## Q9. 20% Growth Proposal

### AI Intervention

Deploy an **AI-powered Lead Prioritization System** integrated with the CRM.

---

### Execution Plan (4 Weeks)

**Week 1:** Data collection & preprocessing
**Week 2:** Model development
**Week 3:** Integration with CRM
**Week 4:** Dashboard + alerts

---

### Impact vs Effort

* **Impact:** High
  → Sales teams focus only on high-probability leads

* **Effort:** Moderate
  → Uses existing data and tools

Expected Result: **15–25% increase in conversions**

---

# Conclusion

This project demonstrates the ability to:

* Design end-to-end AI systems
* Solve real-world business problems
* Build practical and scalable solutions

The focus has been on **simplicity, clarity, and impact**, ensuring that every component directly contributes to business value.

---
