import streamlit as st
import json

def load_patterns(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Could not load patterns: {e}")
        return []

def highlight_entities(doc):
    if doc and doc.ents:
        st.markdown("### ✨ Recognized Entities")
        for ent in doc.ents:
            st.write(f"`{ent.text}` → **{ent.label_}** (start: {ent.start_char}, end: {ent.end_char})")
    else:
        st.info("No entities were recognized.")
