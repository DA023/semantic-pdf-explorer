# Semantic PDF Explorer

## Objective
Build an AI-powered tool to search relevant content inside PDFs using Hugging Face Transformers.

---

## Approach
1. Extract text from the PDF using pypdf  
2. Split the text into smaller chunks  
3. Use Hugging Face zero-shot classification  
4. Compare user query with each chunk  
5. Get confidence scores for each chunk  
6. Filter chunks with score ≥ 0.8  
7. Display most relevant chunks  

---

## Difficulties Faced
- Extracting clean text from PDFs  
- Choosing optimal chunk size  
- Initial model loading time was slow  
- Deciding threshold for filtering  

---

## Resolutions
- Ignored empty text while extracting  
- Used chunk size of ~150 words  
- Used pre-trained model to avoid training  
- Set threshold = 0.8 for better relevance  

---

## Results

Sample Input:
Enter PDF path: sample.pdf  
Enter query: overview  

Sample Output:
Total relevant chunks found: 2  

Result 1 | Score: 1.00  
ADVAIT | Focus Groups/Tracks Overview...

---

## Learnings
- Learned how Transformers work  
- Understood zero-shot classification  
- Learned how to process real-world text data  
- Built an AI-based search pipeline  

---

## How to Run

Install dependencies:
pip install transformers torch pypdf  

Run the script:
python pdf_explorer.py  

---

## Note
This project works with any PDF file. Users can input any PDF path at runtime.