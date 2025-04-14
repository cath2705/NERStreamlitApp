from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ner = load_lottie_url("https://lottie.host/2210cc4b-6b14-4a54-ad8a-7107b0da4c34/TMLSc5Jv1t.json")

st_lottie(lottie_ner, height=300, key="ner")