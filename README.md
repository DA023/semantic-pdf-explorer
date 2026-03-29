# Semantic PDF Explorer

## Objective
Build an AI-powered tool to search relevant content inside PDFs using Hugging Face Transformers.

## Pipeline
1. Extract text from PDF using pypdf  
2. Split text into chunks  
3. Use zero-shot classification  
4. Compare query with chunks  
5. Filter results using confidence score  

## Sample Usage

Enter PDF path: sample.pdf  
Enter query: overview  

Output:
Result 1 | Score: 1.00  
ADVAIT | Focus Groups/Tracks Overview...

## Learnings
- Learned how Transformers work  
- Understood zero-shot classification  
- Learned real-world AI pipeline  

## How to Run
pip install transformers torch pypdf  
python pdf_explorer.py  

## Note
Works with any PDF file.