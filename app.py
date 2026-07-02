from pathlib import Path
import base64
import streamlit as s1

ASSETS = Path(__file__).parent / "assets"


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


s1.set_page_config(
    page_title="Aneeq Altaf | Portfolio",
    page_icon="🤖",
    layout="wide"
)

# HERO
with s1.container():
    s1.title("Hi, I am Aneeq :wave:")
    s1.subheader(
        "A junior majoring in Computer Science at George Mason University Honors College, "
        "focused on Software Engineering, AI/ML, and building reliable end-to-end systems. :desktop_computer:"
    )

s1.divider()

# ABOUT
with s1.container():
    s1.header("About Me")

    left_col, right_col = s1.columns([5, 5])

    with left_col:
        s1.write(
            "🚀 Welcome to my tech corner! I’m a Machine Learning-focused Computer Science student "
            "with hands-on experience building end-to-end AI systems in NLP and computer vision."
        )
        s1.write(
            "I enjoy working with Python, PyTorch, Scikit-Learn, FastAPI, and JavaScript to create "
            "reliable, well-tested software."
        )
        s1.write(
            "Currently, I am a Software Engineering Intern at Amazing Energy Solutions, where I develop "
            "software solutions, analyze operational data, and help improve internal workflows."
        )
        s1.write(
            "Feel free to [connect with me on LinkedIn](https://www.linkedin.com/in/aneeq-altaf-chagani/) "
            "or check out my [GitHub](https://github.com/AneeqAltaf-2121)."
        )

    with right_col:
        b64 = img_to_base64(ASSETS / "profile photo.jpeg")
        s1.markdown(f"""
        <style>
        .portrait img {{
            width: 60%;
            height: clamp(320px, 50vh, 620px);
            object-fit: cover;
            object-position: center 32%;
            border-radius: 18px;
            box-shadow: 0 12px 30px rgba(0,0,0,.35);
            display: block;
            margin-left: -20px;
            margin-top: -40px;
        }}
        </style>

        <div class="portrait">
            <img src="data:image/jpeg;base64,{b64}" alt="Aneeq portrait">
        </div>
        """, unsafe_allow_html=True)

s1.divider()

# EXPERIENCE
with s1.container():
    s1.header("Experience")

    s1.subheader("Software Engineering Intern — Amazing Energy Solutions")
    s1.caption("June 2026 – Present")

    s1.markdown("""
    - Develop software solutions in Python and JavaScript supporting fuel wholesale, retail, logistics, and service operations.
    - Analyze operational data to improve reporting accuracy and support business decision-making.
    - Collaborate with engineers and business stakeholders to enhance internal software and streamline workflows.
    - Write tests, debug, document, and automate processes to improve application reliability.
    """)

s1.divider()

# PROJECTS
with s1.container():
    s1.header("Projects")

    image_coloumn, text_coloumn = s1.columns([1, 2])

    with image_coloumn:
        b65 = img_to_base64(ASSETS / "Project image.jpg")
        s1.markdown(f"""
        <style>
        .project-img img {{
            width: 100%;
            border-radius: 14px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        }}
        </style>

        <div class="project-img">
            <img src="data:image/jpeg;base64,{b65}" alt="AI project image">
        </div>
        """, unsafe_allow_html=True)

    with text_coloumn:
        s1.subheader("Sentiment Analysis AI")
        s1.write(
            "Built an end-to-end NLP pipeline that classifies 50,000 IMDb reviews "
            "as positive or negative using text preprocessing, lemmatization, "
            "TF-IDF vectorization, Logistic Regression, and Multinomial Naive Bayes."
        )
        s1.write(
            "Developed a FastAPI REST API for real-time sentiment prediction with Swagger documentation."
        )
        s1.write("[Source code](https://github.com/AneeqAltaf-2121)")

        s1.subheader("MovieMatch AI")
        s1.write(
            "Created a content-based movie recommendation system using MovieLens data, "
            "genre similarity, user-rating behavior, cosine similarity, and feature engineering "
            "to generate personalized recommendations."
        )
        s1.write(
            "Designed a modular architecture to support future FastAPI integration and cloud deployment."
        )
        s1.write("[Source code](https://github.com/AneeqAltaf-2121)")

        s1.subheader("Plant Disease Detection AI")
        s1.write(
            "Developed a computer vision system using PyTorch, CNNs, transfer learning, "
            "image preprocessing, data augmentation, and a pretrained ResNet18 model "
            "to classify plant leaf diseases from images."
        )
        s1.write(
            "Built a modular training, evaluation, and prediction pipeline with future FastAPI deployment."
        )
        s1.write("[Source code](https://github.com/AneeqAltaf-2121)")

        

s1.divider()

# SKILLS
with s1.container():
    s1.header("Skills")

    col1, col2, col3 = s1.columns(3)

    with col1:
        s1.subheader("AI/ML")
        s1.write("PyTorch, Scikit-Learn, Machine Learning, Deep Learning, NLTK, TF-IDF, Pandas, NumPy")

    with col2:
        s1.subheader("Languages")
        s1.write("Python, Java, JavaScript, SQL")

    with col3:
        s1.subheader("Frameworks & Tools")
        s1.write("FastAPI, Git, GitHub, VS Code")

s1.divider()

# CERTIFICATIONS
with s1.container():
    s1.header("Certifications")

    s1.markdown("""
    - Machine Learning Specialization — Stanford University / DeepLearning.AI
    - Deep Learning Specialization — DeepLearning.AI
    """)

s1.divider()

# LEADERSHIP
with s1.container():
    s1.header("Leadership and Honors 🤝")

    left_col1, right_col1 = s1.columns([1.7, 1.3], gap="large")

    with left_col1:
        s1.markdown("""
        ### Honors College — George Mason University

        **Focus:** Interdisciplinary scholarship, research, and leadership development.

        - Selected for George Mason University’s Honors College.
        - Complete interdisciplinary coursework connecting computing, ethics, research, and social impact.
        - Maintain strong academic standing with a 3.8 GPA.

        [Honors College at Mason](https://honorscollege.gmu.edu/)

        ### Student Council for Leadership and Academic Excellence

        **Areas of focus:** Leadership, mentorship, professional development, and academic excellence.

        - Contribute to student leadership, mentorship, and professional development initiatives.
        - Collaborate with peers to support inclusive academic and community-focused programming.
        - Participate in leadership development through service, reflection, and campus engagement.

        [Society for Collegiate Leadership & Achievement](https://www.thescla.org/)
        """)

    with right_col1:
        b66 = img_to_base64(ASSETS / "s2.jpeg")
        s1.markdown(f"""
        <style>
        .portrait3 img {{
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            margin-left: 50px;
        }}
        </style>

        <div class="portrait3">
            <img src="data:image/jpeg;base64,{b66}" alt="Leadership Image">
        </div>
        """, unsafe_allow_html=True)

s1.divider()

# PASSIONS
with s1.container():
    s1.header("Passions Beyond the Classroom ⚽🏋️‍♂️")

    left_col5, right_col5 = s1.columns([1.7, 1.3], gap="large")

    with left_col5:
        s1.markdown("""
        <style>
        .passions-list {
            list-style: none;
            padding-left: 0;
            margin-top: 0.5rem;
        }

        .passions-list li {
            margin: .45rem 0;
            font-size: 1.08rem;
            display: flex;
            gap: .6rem;
            align-items: center;
        }

        .passions-list .emoji {
            width: 1.25rem;
            text-align: center;
            opacity: .95;
        }
        </style>

        <ul class="passions-list">
          <li><span class="emoji">🦊</span><strong>Naruto</strong></li>
          <li><span class="emoji">☘️</span><strong>Black Clover</strong></li>
          <li><span class="emoji">🎮</span><strong>Dota 2</strong></li>
          <li><span class="emoji">🕷️</span><strong>Hunter x Hunter</strong></li>
        </ul>
        """, unsafe_allow_html=True)

    with right_col5:
        s1.image(ASSETS / "Gon x Killua.png", use_container_width=True)

s1.divider()

# FOOTER
with s1.container():
    s1.markdown("""
    ---
    <div style='text-align: center; padding-top: 10px; font-size: 0.9rem; color: #999999;'>
    © 2026 <b>Aneeq Altaf</b>. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
