from pathlib import Path
import base64
import streamlit as s1
ASSETS = Path(__file__).parent / "assets"
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


s1.set_page_config(page_title="My Streamlit App", page_icon=":tada:", layout="wide")

with s1.container():
    s1.title("Hi, I am Aneeq :wave:")
    s1.subheader("A sophomore majoring in CS, passionate about Software Engineering with interest in AI/ML :desktop_computer:")

s1.divider()  # horizontal line


with s1.container():
    s1.header("About me")

    left_col, right_col = s1.columns([5, 5])

    with left_col:
        s1.write("🚀 Welcome to my Tech corner! As an aspiring Software Engineer, I am:")
        s1.write(
            "If this sounds interesting to you, feel free to [connect](https://www.linkedin.com/in/aneeq-altaf-chagani/) with me!"
        )

    
    with right_col:
        # convert image to base64
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
with s1.container():
    s1.header("Projects")
    image_coloumn, text_coloumn = s1.columns([1, 2])
    with image_coloumn:
        
        
        b65 = img_to_base64(ASSETS / "Project image.jpg")
        s1.markdown(f"""
        <style>
        .portrait1 img {{
            width: 120%;
            
        }}
        </style>

        <div class="portrait1">
            <img src="data:image/jpeg;base64,{b65}" alt="Aneeq portrait">
        </div>
        """, unsafe_allow_html=True)
    with text_coloumn:
        s1.subheader("Tic-Tac-Toe with Recursive AI")
        s1.write("Developed a multi-player agentic AI game using recursive minimax algorithms with alpha-beta pruning, reducing computations by 60% for optimal move selection.")  
        s1.write(
            " [Source code](https://github.com/Aneeeq21/TictacToe) !"
        )  
        s1.subheader("Media Library Management System")
        s1.write("Built a console-based application managing 1000+ media items using Java Generics and exception handling. Optimized search with HashSets & HashMaps for 75% faster queries.")  
        s1.write(
            " [Source code](https://github.com/Aneeeq21/Media-library-management-system) !"
        )  

        s1.subheader("Course Gradebook Manager")
        s1.write("Automated GPA and grading calculations for 500+ student records using Java Collections, reducing manual processing by 80%.")  
        s1.write(
            " [Source code](https://github.com/Aneeeq21/StudentGradeChecker) !"
        )  

        s1.subheader("GradGPT")
        s1.write("An AI assistant that helps GMU students discuss internship readiness and next steps based on their academic profile.")  
        s1.write(
            " [HackFax2025](https://devpost.com/software/grad-gpt-53a1so?ref_content=my-projects-tab&ref_feature=my_projects) !"
        )  

s1.divider()
with s1.container():
        s1.header("Leadership and Volunteer 🤝")
        

        left_col1, right_col1 = s1.columns([1.7, 1.3], gap="large")

    
        with left_col1:
            s1.markdown("""
            ### Leadership Council Member — Society for Collegiate Leadership & Achievement (SCLA)

            **Areas of focus:** Networking, Professional Development, Mentoring, and Guidance.  
        
            - Serve as an active council member fostering student leadership through service-learning and mentorship initiatives.  .  
              
            - Collaborate with GMU peers to organize campus-wide events promoting civic engagement, inclusivity, and academic excellence.   
            - Collaborate with GMU peers to organize campus-wide events promoting civic engagement, inclusivity, and academic excellence.  
            - Contribute to ongoing community impact projects aligned with SCLA’s mission of empowering student leaders.

            [Society for Collegiate Leadership & Achievement](https://www.thescla.org/)
                        
            ### Honors College — George Mason University    
            **Focus:** Interdisciplinary scholarship, research, and leadership development. 
            - Selected for GMU’s Honors College; complete interdisciplinary seminars and research integrating computing, ethics, and social impact.  
            - Contribute reflective writing/creative work and collaborate on discussion-based projects; maintain strong academic standing (Dean’s List).  

            [Honors College at Mason](https://honorscollege.gmu.edu/)         
        """)

    #
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
with s1.container():
    s1.header("Passions Beyond the Classroom ⚽🏋️‍♂️")  

    left_col5, right_col5 = s1.columns([1.7, 1.3], gap="large")

    # LEFT: emoji list
    with left_col5:
        s1.markdown("""
<style>

.passions-list { list-style: none; padding-left: 0; margin-top: 0.5rem; }
.passions-list li { margin: .45rem 0; font-size: 1.08rem; display: flex; gap: .6rem; align-items: center; }
.passions-list .emoji { width: 1.25rem; text-align: center; opacity: .95; }
</style>

<ul class="passions-list">
  <li><span class="emoji">🦊🌀</span><strong>Naruto</strong></li>
  <li><span class="emoji">☘︎🖤</span><strong>BlackClover </strong></li>
  <li><span class="emoji">🎮</span><strong>Dota 2</strong></li>
  
  <li><span class="emoji">🕷️</span><strong>Hunter x Hunter</strong></li>
</ul>
""", unsafe_allow_html=True)

    

    with right_col5:
        
        s1.image(ASSETS / "s3.PNG", use_container_width=True)  

s1.divider()
with s1.container():
    s1.markdown("""
---
<div style='text-align: center; padding-top: 10px; font-size: 0.9rem; color: #999999;'>
© 2025 <b>Aneeq Altaf</b>. All rights reserved.
</div>

""", unsafe_allow_html=True)





