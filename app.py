import streamlit as st
import base64
import json
from groq import Groq

from streamlit_lottie import st_lottie

st.set_page_config(page_title="Image Captioning", page_icon="⚡")

canvas = st.markdown("""
    <style>
        header{ visibility: hidden; }   
    </style> """, unsafe_allow_html=True)


def generate(uploaded_image, prompt):
    base64_image = base64.b64encode(uploaded_image.read()).decode('utf-8')
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': prompt},
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': f'data:image/jpeg;base64,{base64_image}',
                        },
                    },
                ],
            }
        ],
        model='meta-llama/llama-4-scout-17b-16e-instruct',
    )
    return chat_completion.choices[0].message.content

st.title("⚡Image Captioning")

tab_titles = [
    "Home",
    "Vision Instruct",
    "About",
]

vision = [
    "1. Go to Vision Instruct tab.\n\n2. Click on upload option and upload the image.\n\n3. Give the prompt (Question).\n\n4. Click on Generate option."
    ]      

tabs = st.tabs(tab_titles)
with tabs[0]:
    def lottie(anime="anime.json"):
        with open(anime, "r", encoding='UTF-8') as animation:
            return json.load(animation)
    animes = lottie()
  


    col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
    with col2:
          st_lottie(animes, width=300, height=300)
    with col1:      
        st.markdown("""<h4>Welcome to Image Captioning!</h4>
                    <p style="text-align: justify;">Unlock the power of AI-driven image analysis with our innovative application. It is designed to simplify complex tasks, providing accurate and efficient results.</p>""", unsafe_allow_html=True)
    st.markdown("""<hr>""", unsafe_allow_html=True)
    st.markdown("""<h4>Advantages of Image Captioning</h4>
                        <p style="text-align: justify;">It simplifies daily life tasks by using AI, generates the anlyzed data with in a minute. It saves the time by reading all data in files using AI-driven model.</p>""", unsafe_allow_html=True)
    st.image(image="advantage.png")
    st.markdown("""<hr>
                        <h4>Instructions</h4>
                        """, unsafe_allow_html=True)
    with st.expander("V I S I O N - I N S T R U C T"):
        st.write(vision[0])


with tabs[1]:
    uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
            st.image(uploaded_file, caption='Uploaded Image')
            prompt = st.text_input('Enter the prompt')

            if st.button('Generate'):
                with st.spinner('Generating output...'):
                    if prompt:
                        output = generate(uploaded_file, prompt)
                    else:
                        output = generate(uploaded_file, 'What is in this picture?')
                st.subheader('Result:')
                st.write(output)
with tabs[2]:
    st.markdown("""
        <h4>About</h4>
        <p style="text-indent: 60px; text-align: justify;">The objective of this project is to build a production-ready, highly responsive web application that bridges Computer Vision (CV) and Natural Language Processing (NLP). Users can upload standard image formats (JPEG, PNG) via a web browser, which are immediately processed using a vision model hosted via the Groq API.</p>
        <hr>""", unsafe_allow_html=True)
    col5, col6 = st.columns(2, gap="large", vertical_alignment="center")
    with col5:
        st.markdown("""<ul> 
            <h3>Project Development Details</h3>
            <h4>Developers</h4>
            <li>P.Rahul </li>
            <li>N.Sai ravi teja </li>
            <li>R.Uma sri</li>
            <li>K.Harika</li>
            <h4>Mentor</h4>
            <li>P.Chandrakala</li>
        </ul>
        <br>""", unsafe_allow_html=True)
    with col6:
        def coding(coding = "coding.json"):
            with open(coding, 'r', encoding='UTF-8') as f:
                return json.load(f)
        icon = coding()
        st_lottie(icon, width=350, height=350)
    st.markdown("""        <hr> 
            <h3>Contact</h3>    
            <p>For any queries or feedback, please reach out to us at <a href='mailto:rahulpalivela02@gmail.com'>rahulpalivela02@gmail.com</a>.</p> 
         """, unsafe_allow_html=True) 
   
