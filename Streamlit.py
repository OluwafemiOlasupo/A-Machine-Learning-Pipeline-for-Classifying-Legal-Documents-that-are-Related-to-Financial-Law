import streamlit as st
import pandas as pd
import pickle
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load the pre-trained model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open('svm_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

def process_csv(df):
    # Check if required columns are present
    if 'Content' not in df.columns or 'SourceLanguage' not in df.columns:
        raise ValueError("The CSV must contain 'Content' and 'SourceLanguage' columns for classification")

    # Concatenate 'Content' and 'SourceLanguage' columns
    df['TextToClassify'] = df['Content'] + " " + df['SourceLanguage']

    # Vectorize the concatenated text
    X = vectorizer.transform(df['TextToClassify'])

    # Make predictions
    predictions = model.predict(X)

    # Get confidence scores
    confidence_scores = model.decision_function(X)
    confidence_scores = 1 / (1 + np.exp(-confidence_scores))

    # Generate simple explanations
    explanations = [
        f"The document was classified as {'relevant' if pred else 'not relevant'} with a confidence of {conf:.2f}"
        for pred, conf in zip(predictions, confidence_scores)]

    # Add results to the dataframe
    df['Prediction'] = predictions
    df['Confidence'] = confidence_scores
    df['Explanation'] = explanations

    return df[['DocumentID', 'Prediction', 'Confidence', 'Explanation']]

def validate_csv(df):
    required_columns = ['DocumentID', 'Content', 'SourceLanguage']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

st.title('Document Relevance Classification')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Validate the CSV structure
        validate_csv(df)

        # Process the CSV
        result_df = process_csv(df)

        # Convert the result to CSV
        csv = result_df.to_csv(index=False)

        # Provide download link
        st.download_button(
            label="Download processed CSV",
            data=csv,
            file_name="processed_output.csv",
            mime="text/csv"
        )

        # Display the result
        st.write(result_df)

    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty. Please upload a valid CSV file.")
    except pd.errors.ParserError:
        st.error("Unable to parse the CSV file. Please ensure it's a valid CSV.")
    except ValueError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
else:
    st.info("Please upload a CSV file to process.")
