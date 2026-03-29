from pypdf import PdfReader
from transformers import pipeline

# Extract text
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return text

# Chunk text
def chunk_text(text, chunk_size=150):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

# Load model
def load_model():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

# Search chunks
def search_chunks(chunks, query, classifier, threshold=0.8):
    results = []

    for chunk in chunks:
        result = classifier(chunk, candidate_labels=[query])
        score = result["scores"][0]

        if score >= threshold:
            results.append((chunk, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Main function
def main():
    pdf_path = input("Enter PDF path: ")
    query = input("Enter your query: ")

    text = extract_text(pdf_path)
    chunks = chunk_text(text)

    classifier = load_model()

    results = search_chunks(chunks, query, classifier)

    if not results:
        print("No results found.")
    else:
        print(f"\nTotal relevant chunks found: {len(results)}")

        for i, (chunk, score) in enumerate(results[:3], 1):
            print(f"\nResult {i} | Score: {score:.2f}")
            print(chunk)
            print("-" * 50)

if __name__ == "__main__":
    main()