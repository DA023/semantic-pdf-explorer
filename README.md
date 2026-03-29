# Semantic PDF Explorer 🚀

## 📌 Objective

Build an AI-powered tool to search and retrieve relevant information from PDF documents using **Hugging Face Transformers**.

---

## 🧠 Overview

Semantic PDF Explorer allows users to input a query and find the most relevant sections from a PDF.
Instead of simple keyword matching, it uses **zero-shot classification** to understand the meaning of the query and match it with document content.

---

## ⚙️ Approach

The project follows a structured pipeline:

1. **Text Extraction**
   Extract text from the PDF using `pypdf`.

2. **Text Chunking**
   Split extracted text into smaller chunks (~150 words each) for efficient processing.

3. **Model Loading**
   Use Hugging Face’s pre-trained model (`facebook/bart-large-mnli`) via the `transformers` pipeline.

4. **Semantic Matching**
   Compare each chunk with the user query using zero-shot classification.

5. **Filtering Results**
   Only retain chunks with confidence score ≥ **0.8**.

6. **Ranking & Output**
   Sort results by score and display the top matches.

---

## 🔄 Pipeline Explanation

PDF → Text Extraction → Chunking → Zero-Shot Classification → Score Filtering → Ranked Output

---

## 🧪 Sample Usage

### Input

```
Enter PDF path: sample.pdf
Enter your query: overview
```

### Output

```
Total relevant chunks found: 2

Result 1 | Score: 1.00
ADVAIT | Focus Groups/Tracks Overview...

Result 2 | Score: 0.87
This document outlines the assignments...
```

---

## ⚠️ Difficulties Faced

* Extracting clean and readable text from PDFs
* Choosing optimal chunk size for better model performance
* Initial delay due to model loading
* Deciding an appropriate confidence threshold

---

## 🛠️ Solutions Implemented

* Ignored empty or invalid text during extraction
* Used chunk size of ~150 words for balance between context and performance
* Leveraged pre-trained models to avoid training overhead
* Set threshold to **0.8** to ensure high relevance

---

## 📚 Learnings

* Practical use of **Hugging Face Transformers**
* Understanding of **zero-shot classification**
* Importance of preprocessing in NLP pipelines
* Building a real-world AI-powered search system

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install transformers torch pypdf
```

### 2. Run the script

```
python pdf_explorer.py
```

### 3. Provide input

* Enter PDF path
* Enter your query

---

## 📌 Constraints Satisfied

* ✅ Used Hugging Face Transformers
* ✅ Implemented zero-shot classification
* ✅ CLI-based solution (no UI required)

---

## 🔮 Future Improvements

* Convert into a web-based application
* Use semantic embeddings (FAISS) for faster search
* Support multiple PDFs simultaneously
* Improve ranking with hybrid search techniques

---

## 📝 Note

This tool works with **any PDF file**.
Users can provide their own PDF path at runtime.

---