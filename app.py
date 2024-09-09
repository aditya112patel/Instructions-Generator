import streamlit as st
from utils.image import create_temp_file
from utils.llm import analyze_image_file, stream_parser


page_title ="TESTING INSTRUCTION GENERATOR"

# configures page settings
st.set_page_config(
    page_title=page_title,
)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title(page_title)

st.markdown("#### Select an image file.")

uploaded_file = st.file_uploader("Choose image file(necessary)", type=['png', 'jpg', 'jpeg'] )
image_model = 'llava'

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True


chat_input = st.text_input("Context (Optional)",placeholder='Enter context')

st.button('GENERATE TESTING INSTRUCTIONS', on_click=click_button)

if st.session_state.clicked:
    if uploaded_file is None:
        st.error('You must select an image file to analyze!')
        st.stop()

    # Color formatting example https://docs.streamlit.io/library/api-reference/text/st.markdown
    with st.status(":red[Processing image file...]", expanded=True) as status:
        st.write(":orange[Analyzing Image File...]")

        # creates the audio file
        stream = analyze_image_file(uploaded_file, model=image_model, user_prompt=chat_input)
       
        stream_output = st.write_stream(stream_parser(stream))

        st.write(":green[Done]")