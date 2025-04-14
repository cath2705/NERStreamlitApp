from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ner = load_lottie_url("https://lottie.host/2210cc4b-6b14-4a54-ad8a-7107b0da4c34/TMLSc5Jv1t.json")

st_lottie(lottie_ner, height=300, key="ner")

import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
import re

# Load the spaCy model once
@st.cache_resource
def load_model():
    # Using the small English model for demonstration
    nlp = spacy.load("en_core_web_sm")
    return nlp

def add_custom_pattern(nlp, label: str, pattern: str):
    # Ensure the custom EntityRuler is added only once
    ruler = nlp.get_pipe("entity_ruler") if "entity_ruler" in nlp.pipe_names else nlp.add_pipe("entity_ruler", before="ner")
    
    # Build the pattern in spaCy format
    # Here we take the simple approach: pattern as a regex that matches text
    # In a more advanced setup, patterns should be built in spaCy's token-matching format.
    # For demonstration, we use a simple rule that matches literal text.
    new_pattern = {"label": label.upper(), "pattern": pattern}
    ruler.add_patterns([new_pattern])
    return nlp

def highlight_entities(text, doc):
    # This function wraps identified entities in HTML to highlight them.
    # Split the text into parts and reconstruct it with markup.
    highlighted_text = text
    # Iterate through entities in reverse order to avoid indexing issues when inserting HTML tags
    for ent in sorted(doc.ents, key=lambda x: x.start_char, reverse=True):
        # Wrap the entity with a span tag and style it
        highlight = f'<mark style="background-color: #fce883; padding: 0.2em; border-radius: 3px;" title="{ent.label_}">{ent.text}</mark>'
        # Replace the exact slice in the text with the HTML-highlighted version
        highlighted_text = highlighted_text[:ent.start_char] + highlight + highlighted_text[ent.end_char:]
    return highlighted_text

def main():
    st.title("Custom NER Application")
    st.markdown(
        """
        This app allows you to upload or paste text and define custom named entity patterns.
        The spaCy EntityRuler is used to identify your custom entities in the text.
        """
    )

    # Section 1: Text Input
    st.header("Input Your Text")
    input_option = st.radio("Choose text input method:", ("Paste Text", "Upload File"))
    
    text = ""
    if input_option == "Paste Text":
        text = st.text_area("Enter text here:", height=200, value="Type or paste your text here...")
    elif input_option == "Upload File":
        uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
        if uploaded_file is not None:
            text = uploaded_file.read().decode("utf-8")
    
    st.markdown("---")
    
    # Section 2: Define Custom Entity Rules
    st.header("Define Custom Entity")
    st.markdown("Provide a custom entity label and the text pattern to match.")
    custom_label = st.text_input("Entity Label", value="CUSTOM")
    custom_pattern = st.text_input("Entity Pattern", value="sample")

    if st.button("Add Custom Entity Rule"):
        # Load the model and add the custom pattern
        nlp = load_model()
        nlp = add_custom_pattern(nlp, custom_label, custom_pattern)
        st.success(f"Custom entity '{custom_label.upper()}' with pattern '{custom_pattern}' added!")

    st.markdown("---")
    
    # Section 3: Process and Display the Results
    st.header("Detected Entities")
    if st.button("Process Text") and text:
        nlp = load_model()
        # If you added a custom rule, in a more robust app you might store that state; for now, assume the rule is there.
        doc = nlp(text)
        highlighted = highlight_entities(text, doc)
        st.markdown("### Highlighted Text with Detected Entities")
        # Using unsafe_allow_html to render HTML in Streamlit (ensure to trust the content or sanitize input)
        st.markdown(highlighted, unsafe_allow_html=True)

        # Additionally, list each detected entity with its label and position
        st.markdown("### Entity Details")
        for ent in doc.ents:
            st.write(f"**Entity:** {ent.text} | **Label:** {ent.label_} | **Position:** {ent.start_char}-{ent.end_char}")

if __name__ == "__main__":
    main()