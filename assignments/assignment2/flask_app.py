from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import os

# importing
from ner import SpacyDocument

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

# Models
class NERResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    entities = db.relationship('Entity', backref='result', lazy=True)

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(20))
    text = db.Column(db.String(100))
    result_id = db.Column(db.Integer, db.ForeignKey('ner_result.id'))
    count = db.Column(db.Integer, default=1)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        text = request.form['text']
        doc = SpacyDocument(text)
        result = doc.get_entities_with_markup()

        # Save result to database
        ner_result = NERResult(text=text)
        db.session.add(ner_result)

        soup = BeautifulSoup(result, 'html.parser')
        for tag in soup.find_all():
            if tag.name == 'entity':
                label = tag.attrs['class'][0]
                text = tag.string
                entity = Entity.query.filter_by(label=label, text=text).first()
                if entity:
                    entity.count += 1
                else:
                    entity = Entity(label=label, text=text, result=ner_result)
                    db.session.add(entity)
                
        db.session.commit()

        return render_template('result.html', xml=result)

@app.route('/results', methods=['GET'])
def results():
    # Query the database for all entities and their counts
    entities = db.session.query(Entity.text, db.func.sum(Entity.count)).group_by(Entity.text).all()
    # Render the results template with the query results
    return render_template('all_results.html', entities=entities)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0')