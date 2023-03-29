# Assignment 2 - Adding a Database and Dockerize

## Running the Code

### Python Version
The code was developed and tested using Python 3.10

### Required modules
To run the code, the following modules need to be installed:

spacy
flask
flask_sqlalchemy
beautifulsoup4

You can install them by running the following command:

```bash
pip install spacy flask flask_sqlalchemy beautifulsoup4
```
### Starting the API and Webserver
To start the API and webserver, navigate to the root directory of the project in your terminal and run the following command:

```bash
python flask_app.py
```

This will start the Flask webserver at http://localhost:5000/ and the RESTful API at http://localhost:5000/api/.

### Using the API
To use the API, send a POST request to http://localhost:5000/api/ with  text to analyze. For example, using curl:

```bash
$ curl http://127.0.0.1:5000/api
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```

### Using the Flask webserver
To use the Flask webserver, access http://localhost:5000/, input the text you wish to analyze and click the submit button. Then another page will load with the text entities highlighted. To access the table with all entities seen so far there are 2 options:
 - access http://localhost:5000/results
 - click on the "View all results" link either in the input page or in the result page

### Building and Running the Docker Image
To build the Docker image, navigate to the root directory (/assignment2) of the project in your terminal and run the following command:

```bash
$ docker build -t myflaskapp .
```

To run the Docker container, run the following command:

```bash
$ docker run -dp 5000:5000 `
    -w /app --mount type=bind,src="$(pwd)",target=/app `
    myflaskapp
```

This will start the Docker container at http://localhost:5000/.

