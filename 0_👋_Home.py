import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Guilherme Datt Portfolio",
    page_icon="📊",
)

# ----- Left menu -----
with st.sidebar:
    st.header("Contact me!")
    st.write("###")
    st.write("""- 🧑‍💻 Linkedin: - 📫 Email: guilhermedatt@gmail.com, - 🛩️ GitHub: - 🛩️ WhatsApp:) # COMPLETE HERE

# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Welcome to my Portfolio!</h1></div>""", unsafe_allow_html=True)  


# ----- Profile image file -----
profile_image_file_path = "profile_image2.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Business Intelligence Trainee at Neuroeletrics. Big Data & Analytics Master Student at EAE Business School"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space

# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 TALK ABOUT WHAT AM I DOING NOW

- 🛩️ prev: TALK ABOUT EXPERIENCE

- ❤️ TALK ABOUT INTERESTS

- 🏠 Barcelona
""")

# ----- HARD SKILLS SECTION -----
st.subheader("Tools that I use")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""

- 🧑‍💻TALK ABOUT THE TOOLS I HAVE EXPERIENCE: PYTHON, SQL, Visualization: Power BI, Google Datastudio, Tableau, Statistics.

""")
