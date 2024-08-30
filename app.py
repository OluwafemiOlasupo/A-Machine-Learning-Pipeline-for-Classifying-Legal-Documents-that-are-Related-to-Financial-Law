# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle


app = FastAPI()
# Load the saved SVM model and TF-IDF vectorizer
with open('svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)



# Initialize FastAPI app
app = FastAPI()


# Define the request body structure
class Document(BaseModel):
    DocumentID: str
    Title: str | None = None  # Optional field
    RegulatorId: str
    SourceLanguage: str
    DocumentTypeId: str
    PublicationDate: str
    IsPdf: bool
    Content: str

# Define a route for health check
@app.get("/")
def read_root():
    return {"message": "SVM model is running"}


# Define a route for making predictions
@app.post("/predict")
def predict(document: Document):
    try:
        # Validate the request body
        document = Document(**document)  # Raises ValidationError for invalid data

        # ... (rest of the prediction logic remains the same)

        return {
            "DocumentID": document.DocumentID,
            "Prediction": label,
            "Confidence": probability,
            "Explanation": "**Add explanation logic here**"  # Placeholder for explanation
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Invalid request body: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))