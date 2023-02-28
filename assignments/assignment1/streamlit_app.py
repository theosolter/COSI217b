import streamlit as st
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

st.title("SpaCy Demo")
st.markdown("---")

text = st.text_input("Enter text to analyze:")
if st.button("Analyze"):

    # Sentiment Analysis
    st.header("Sentiment Analysis")
    doc = nlp(text)
    sentiment = doc.sentiment
    if sentiment > 0:
        st.write("Sentiment: Positive")
    elif sentiment == 0:
        st.write("Sentiment: Neutral")
    else:
        st.write("Sentiment: Negative")
    st.markdown("---")

    # Named Entity Recognition
    st.header("Named Entity Recognition")
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    st.write("Named Entities:", entities)
    st.markdown("---")

    # Sentence Similarity
    st.header("Sentence Similarity")
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    similarity_scores = []
    for i in range(len(sentences)):
        for j in range(i+1, len(sentences)):
            similarity_scores.append((sentences[i], sentences[j], nlp(sentences[i]).similarity(nlp(sentences[j]))))
    st.write("Sentence Similarity Scores:", similarity_scores)
    st.markdown("---")

    # Dependency Parsing
    st.header("Dependency Parsing")
    doc = nlp(text)
    
    # Display dependency tree for each sentence
    for sent in doc.sents:
        st.write(f"Sentence: {sent.text}")
        dep_tree_data = []
        for token in sent:
            dep_tree_data.append((
                token.i, 
                token.text, 
                token.dep_, 
                token.head.text, 
                token.head.pos_, 
                [child.text for child in token.children]
            ))
        table_data = pd.DataFrame(dep_tree_data, columns=["Token ID", "Token Text", "Dependency", "Head Text", "Head POS", "Children"])
        table_data = table_data.astype(str)  # Convert all columns to string
        st.table(table_data)