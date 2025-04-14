import streamlit as st

st.set_page_config(page_title="NER Streamlit App", layout="wide")

st.markdown("# 👋 Welcome to My Custom NER App")
st.markdown("NER refers to Named Entity Recognition. Read more to understand what exactly this means! ")
st.markdown("Use the sidebar to navigate through the different tools and learn about Named Entity Recognition.")


st.markdown("### What even is Named Entity Recognition (NER)?")

# ✅ Image outside of st.markdown, and using use_container_width
st.image(
    "https://www.labellerr.com/blog/content/images/2024/01/ner-1.webp",
    use_container_width=True
)

# Follow with clean markdown block
st.markdown(
    """
    Named Entity Recognition is a key **Natural Language Processing (NLP)** technique that identifies and labels entities in text, like:

    - 🧑 **People**
    - 🗺️ **Locations**
    - 🏢 **Organizations**
    - 📅 **Dates**
    - 💰 **Monetary Values**
    """
)

# Create columns for image + text side-by-side
col1, col2 = st.columns(2)

with col1:
    st.image("https://f5b623aa.delivery.rocketcdn.me/wp-content/uploads/2022/02/Blog_Common-Examples-of-NER_500x350.jpg", use_column_width=True, caption="Example of NER in Action")

with col2:
    st.markdown(
        """
        When a computer reads this sentence:  
        > `"Barack Obama was born in Hawaii."`  
        
        It understands:
        - "Barack Obama" → **PERSON**
        - "Hawaii" → **GPE** (Geopolitical Entity)

        This allows machines to *understand* context in text — kinda like how we do!
        """
    )

# Expandable section
with st.expander("📚 Why does this even matter?"):
    
    # Add spacing below image
    st.markdown("")

    st.write("""
    NER helps computers understand the *meaning* behind words, like who is involved,
    where things are happening, or when events occurred. This makes it crucial in
    search engines, recommendation systems, chatbots, and even fact-checking tools!
    """)
    
    st.markdown(
        """
        NER is used in tons of real-world applications:
        
        - 📰 News Aggregators  
        - 🔎 Search Engines  
        - 🧠 Knowledge Graphs  
        - 🏥 Medical Research  
        - 🕵️ Intelligence + Cybersecurity

        It's one of the **foundational skills** in applied NLP.
        """
    )

# Footer teaser
st.markdown("---")
st.markdown("👉 Head to the sidebar to try out the **Entity Recognizer** yourself!")
