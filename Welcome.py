import streamlit as st

st.set_page_config(page_title="NER Streamlit App", layout="wide")

st.markdown("# 👋 Welcome to My NER App")
st.markdown("""
Named Entity Recognition (NER) is a key task in **Natural Language Processing (NLP)** that identifies and classifies important information—like names of people, places, organizations, dates, and more—from text.  
            
This website is designed to help you understand what NER is, how it works, and why it matters. Whether you are new to the concept or looking to explore its real-world applications, you'll find interactive tools and resources here to guide you.  

Use the sidebar to explore different sections of the app. Try out hands-on tools, learn about NER in context, and see how machines extract meaning from language.  

**So… what even is NER? Let's find out.**
""")

st.markdown("# What is Named Entity Recognition (NER)?")

# Image outside of st.markdown, and using use_container_width
st.image(
    "https://www.labellerr.com/blog/content/images/2024/01/ner-1.webp",
    use_container_width=True
)

# Follow with markdown block to explain more of how it works
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

# new text 
st.markdown(
    """
   # What Does this Actually Look Like?
    """
)

# Create columns for image + text side-by-side
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn.botpenguin.com/assets/website/few_nerd_1_ae19b90a78.webp", use_container_width=True, caption="Example of NER in Action")

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

# new text 
st.markdown("## Why Does this Matter?")

# Expandable section
with st.expander("# Click to Find Out"):
    
    # Add spacing below image
    st.markdown("")

    st.write("""
    NER helps computers understand the *meaning* behind words, like who is involved,
    where things are happening, or when events occurred. This makes it crucial in
    search engines, recommendation systems, chatbots, and even fact-checking tools!
    """)
    
    st.markdown(
        """
        NER is used in tons of real-world applications!

        Entity Recognition isn’t just an academic concept—it’s a powerful tool that quietly drives innovation in the technologies we use every day. Behind the scenes, it's helping teams and developers extract meaning from language at scale, enabling smarter, faster, and more personalized systems across countless industries.
        
        **For example:**
        
        On a **hiring platform**, entity detection helps scan thousands of resumes, automatically identifying names, job titles, companies, degrees, and salaries—cutting down hours of manual work into seconds. 
        
        In **healthcare**, it’s used to process and sort patient data by recognizing medications, diagnoses, or symptoms within medical records, enabling faster and more accurate analysis.
        Even voice bots and virtual assistants rely on entity detection to understand what users are saying. When you say, “Call Dr. Smith at Stanford,” the system doesn’t just hear words—it understands that “Dr. Smith” is a person and “Stanford” is an organization, then uses that information to take meaningful action.

        Other real-world uese include...
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
