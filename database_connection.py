from pymongo import MongoClient

# Connect to MongoDB (replace with your details)
client = MongoClient("mongodb://localhost:27017/")  # Change if using a remote DB
db = client["dms_scs"]  # Database name
collection = db["content_search"]  # Collection name


# Example text
# sentence = "SBERT embeddings are useful."
# embedding = model.encode(sentence).tolist()  # Convert NumPy array to list

def save_document(sentence,embedding):
    # Prepare the document
    doc = {
        "text": sentence,
        "embedding": embedding.tolist()
    }
    # Insert into MongoDB
    collection.insert_one(doc)
    print("Embedding saved successfully!")

