# Assignment 1 - Web Services

## Running the Code

### Python Version
The code was developed and tested using Python 3.10

### Required modules
To run the code, the following modules need to be installed:

spacy
flask
pandas
streamlit

You can install them by running the following command:

```bash
pip install spacy flask pandas streamlit
```
### Starting the API and Webserver
To start the API and webserver, navigate to the root directory of the project in your terminal and run the following command:

```bash
python flask_app.py
```

This will start the Flask webserver at http://localhost:5000/ and the RESTful API at http://localhost:5000/api/.

### Starting the Streamlit application
To start the Streamlit application, navigate to the root directory of the project in your terminal and run the following command:

```bash
streamlit run streamlit_app.py
```

This will open the Streamlit application in a new browser tab.

### Using the API
To use the API, send a POST request to http://localhost:5000/api/ with  text to analyze. For example, using curl:

```bash
$ curl http://127.0.0.1:5000/api
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```

### Using the Flask webserver
To use the Flask webserver, access http://localhost:5000/, input the text you wish to analyze and click the submit button. Then another page will load with the text entities highlighted.

### Using the Streamlit application

Once the Streamlit application is running, you can simply type in the text you want to analyze in the input box and click the "Analyze" button. The entity recognition, sentiment analysis and dependency parsing results will be displayed in the output.