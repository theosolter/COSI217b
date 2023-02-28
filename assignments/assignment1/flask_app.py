from flask import Flask, request, jsonify, render_template
import sys, os

# importing
from ner import SpacyDocument

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        response = {"message": "This is a RESTful API for named entity recognition. Please use POST method to send your text."}
        return jsonify(response)

    elif request.method == 'POST':
        text = request.get_data(as_text=True)
        doc = SpacyDocument(text)
        result = doc.get_entities()
        return jsonify(result)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        text = request.form['text']
        doc = SpacyDocument(text)
        result = doc.get_entities_with_markup()
        return render_template('result.html', xml=result)

if __name__ == '__main__':
    app.run(debug=True)