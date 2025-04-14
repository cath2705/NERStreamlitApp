import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from utils import load_patterns, highlight_entities
import os 

# Set up the page
st.set_page_config(page_title="Custom NER App", layout="wide")
st.title("🧠 Custom Named Entity Recognition")

# New text describing tool
st.write("""
    Curious to see how Named Entity Recognition works in practice? Use this tool to input your own sentences and watch as the system identifies entities in real time.
    
    Type anything you like—maybe a news headline, a made-up story, or a sentence from your favorite book—and see which words the model picks out as names, places, organizations, dates, and more. As you experiment, pay attention to the context. Which words does the system correctly recognize? Which ones does it miss or misinterpret?
    
    This is your chance to think like an algorithm: what clues is it using to make decisions, and where might it be getting confused?
    
    Try to trick it. Surprise it. See what happens!

    """)

# Load a base spaCy model
nlp = spacy.load("en_core_web_sm")

# Load custom patterns
patterns = load_patterns("patterns/example_patterns.json")

# Add EntityRuler with custom patterns
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns) 

# Sidebar for user input
st.sidebar.header("Text Input Options")
upload = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])
default_text = "Barack Obama was born in Hawaii. He was elected president in 2008."

# Get the text
if upload is not None:
    text = upload.read().decode("utf-8")
else:
    text = st.text_area("Paste your text below:", default_text)

# Run entity recognition
if st.button("Analyze Text"):
    doc = nlp(text)
    highlight_entities(doc)

# New Section to help user identify patterns
st.markdown("---")
st.markdown("### What Happens if you Misspell a Word?")

# Load a base spaCy model
nlp = spacy.load("en_core_web_sm")

# Load custom patterns
patterns = load_patterns("patterns/example_patterns.json")

# Add EntityRuler with custom patterns
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns) 

# Sidebar for user input
st.sidebar.header("Text Input Options")
upload = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])
default_text = "Let's turn left, right?"

# Get the text
if upload is not None:
    text = upload.read().decode("utf-8")
else:
    text = st.text_area("Paste your text below:", default_text)

# Run entity recognition
if st.button("Analyze Text"):
    doc = nlp(text)
    highlight_entities(doc)