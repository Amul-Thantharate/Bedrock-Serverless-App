## ServerLess Chat Application using AWS Bedrock and Langchain and Python.

# Breakdown of the project
* Amazon Bedrock: It is a serverless application framework that provides a set of tools and best practices for building serverless applications. It is built on top of the AWS Cloud Development Kit (CDK) and AWS Serverless Application Model (SAM).
* Langchain: It is a serverless application framework that provides a set of tools and best practices for building serverless applications. It is built on top of the AWS Cloud Development Kit (CDK) and AWS Serverless Application Model (SAM).
* Streamlit: It is a serverless application framework that provides a set of tools and best practices for building serverless applications. It is built on top of the AWS Cloud Development Kit (CDK) and AWS Serverless Application Model (SAM).

# Pre-requisites
* AWS Account
* AWS CLI installed and configured
* Python 3.6 or later
* Docker

# Installation
* Clone the repository
* Install the required packages using the following command
```bash
    git clone https://github.com/Amul-Thantharate/Serverless-Chat-Application.git
```
* Install the required packages using the following command
```bash
    pip install -r requirements.txt
```
* Run the following command to start the application
```bash
    streamlit run app.py
```
* Open the browser and go to the following URL
```bash
    http://localhost:8501
```
* For Docker installation, run the following command
```bash
    docker build -t chat-app .
```
* Run the following command to start the application
```bash
    docker run -p 8501:8501 chat-app
```

# Acknowledgements
* AWS Bedrock (https://aws.amazon.com/bedrock/)
* Langchain (https://langchain.io/)
* Streamlit (https://streamlit.io/)

## Happy Coding! :smile: :+1:
