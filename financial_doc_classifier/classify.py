from utils import classify_document

label = classify_document("examples/1040_example.pdf")
print("Detected document type:", label)
