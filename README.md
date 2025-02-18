# Pdf-Summarizer Using OpenAI 

This project is a web application that summarizes multiple PDF documents using OpenAI's language models and the LangChain framework. The app is built using Streamlit for an interactive web interface.
xdddndjcn
### Installation
Clone the repository and navigate to the project directory.

### Install the required packages:

bash
Copy code
pip install langchain streamlit python-dotenv
Set up environment variables:

### Create a .env file in the project directory.
 
### Add your OpenAI API key:
makefile
OPENAI_API_KEY="your-openai-api-key"
Usage
Run the Streamlit app:

### bash

streamlit run app.py 

Upload PDF files: Use the file uploader in the Streamlit interface to select one or more PDF files.

### Generate Summaries: Click the "Generate Summary" button to get concise summaries of the uploaded PDFs.

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss the proposed modifications.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
 Streamlit: For providing an easy-to-use web app framework.
 LangChain: For simplifying interactions with large language models.
OpenAI: For offering powerful language model APIs.
