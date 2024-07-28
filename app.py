import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set Streamlit page configuration
st.set_page_config(page_title="Sketch to Image using GAN", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;  /* Black background */
        color: #ffffff;  /* White text */
    }
    .main {
        background-color: #1e1e1e;  /* Black background */
    }
    h1, h2 {
        color: #ff6347; /* Tomato color for titles */
    }
    .stButton>button {
        color: #ffffff;
        background-color: #ff6347; /* Tomato color for buttons */
        border-radius: 10px;
        border: 2px solid #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Title with colors and emojis
st.markdown("<h1 style='text-align: center;'>Sketch to Image using GAN 🖌️</h1>", unsafe_allow_html=True)

# Slide plane with three sections: Home, About, and Upload Pic
section = st.sidebar.radio("Navigate", ["Home", "About", "Upload Pic"])

# Home Section
if section == "Home":
    st.markdown("<h2 style='text-align: center;'>Empowering Multiple Fields with GANs 🌐</h2>", unsafe_allow_html=True)
    st.write("The application of Generative Adversarial Networks (GANs) in the Sketch to Image project extends beyond creative endeavors, finding significant utility in various fields. The ability to transform sketches into vibrant and detailed images has far-reaching implications, especially in sectors such as law enforcement, forensic science, and more.")
    st.image("home.jpeg", caption="Sketch Example", width=300)   
    st.write("In law enforcement and police investigations, where visual evidence plays a crucial role, this technology provides a novel approach to enhancing and understanding sketches. The generated images offer a clearer representation, aiding investigators in identifying suspects and solving cases more efficiently.")
    st.image("home1.jpeg", caption="Sketch Example", width=300)
    st.write("Moreover, the applications of this project are not limited to forensics. In creative fields, such as digital art and design, artists can benefit from the seamless transformation of conceptual sketches into visually striking images. The project acts as a bridge between imagination and reality, providing a valuable tool for artists to bring their ideas to life.")

    st.write("In essence, the Sketch to Image project stands as a testament to the versatility and transformative power of GANs. It is a technological innovation that has the potential to revolutionize the way we perceive and utilize visual data in various professional domains.")

    # Add more details and images to make the page attractive

  
# About Section
elif section == "About":
    st.markdown("<h2 style='text-align: center;'>About the Sketch to Image Project 🌟</h2>", unsafe_allow_html=True)
    st.write("Greetings! Titled 'Sketch to Image using GAN.' This project is a culmination of my passion for artificial intelligence, machine learning, and their real-world applications.")

    st.write("The Sketch to Image project is centered around leveraging the power of Generative Adversarial Networks (GANs) to transform sketches into vibrant and realistic images. GANs, a class of machine learning models, are particularly adept at generating new data that closely resembles existing samples. This capability makes them an ideal choice for creative projects like converting sketches into colorful masterpieces.")
    st.image("o2.jpg", caption="Sketch Example", width=300)
    st.write("The motivation behind this project stems from the desire to bridge the gap between the conceptual and the tangible. Sketches, often the initial step in the creative process, are transformed into visually appealing images with the help of advanced machine learning algorithms. This transformation opens up new possibilities in fields such as digital art, forensic science, and more.")

    st.write("One of the primary applications of this project lies in forensic investigations. The ability to convert rough sketches into detailed images can significantly enhance the accuracy and efficiency of investigations. It provides law enforcement agencies with a valuable tool for visualizing and understanding evidence, ultimately contributing to more effective decision-making.")
   # st.image("about1.jpeg", caption="Sketch Example", width=200) 
    col1, col2 = st.columns(2)
    col1.image("about1.jpeg", caption="Sketch Example", width=170)
    col2.image("about 2.jpeg", caption="Sketch Example", width=150)
    st.write("As the developer of this project, I am thrilled about the potential impact it can have on various fields. Whether used for creative expression, forensic analysis, or other applications, the Sketch to Image project represents the intersection of technology and creativity.")
   # st.image("about 2.jpeg", caption="Sketch Example", width=200)
    st.write("I invite you to explore the project and witness firsthand the transformative capabilities of GANs. Feel free to navigate through the different sections and experience the magic of turning sketches into vibrant images!")

    # Add more details and images to make the page attractive

    

# Upload Pic Section
else:
    st.markdown("<h2 style='text-align: center;'>Upload Your Sketch 📤</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image... 📤", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image in the center
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(uploaded_file, caption="Uploaded Image 🖼️", width=300)

        # Button to generate the image with emoji
        if st.button('Generate 🚀'):
            # Display a message while generating the image
            with st.spinner('Wait for it... Generating your image 🎨'):
                # Prepare the file for sending
                files = {"file": uploaded_file.getvalue()}

                # Send POST request to FastAPI server
                response = requests.post("http://127.0.0.1:8000/generate-image/", files=files)

                if response.status_code == 200:
                    # Convert the response content to an image
                    generated_image = Image.open(BytesIO(response.content))

                    # Display the generated image in the center
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.image(generated_image, caption="Generated Image ✨", width=300)
                else:
                    st.error("Error in image generation 😢")