# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Streamlit
RUN pip install streamlit

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run Streamlit app when the container launches
CMD ["streamlit", "run", "Streamlit.py"]
