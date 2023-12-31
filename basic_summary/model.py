from transformers import pipeline

# Open and read the article
f = open("article.txt", "r", encoding="utf8")
to_tokenize = f.read()

# Initialize the HuggingFace summarization pipeline
summarizer = pipeline("summarization")
summarized = summarizer(to_tokenize, min_length=75, max_length=150)

# Print summarized text
print(summarized)