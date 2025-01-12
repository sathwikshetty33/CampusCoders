import streamlit as st
import requests
import datetime

# Configure the page
st.set_page_config(
    page_title="Campus Coders",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# [Previous CSS styles remain exactly the same until the last closing style tag]
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    .stApp {
        background-color: #030712;
        color: #f3f4f6;
        font-family: 'Poppins', sans-serif;
    }
    .main-header {
        background: linear-gradient(45deg, #1a1a2e, #16213e, #1a1a2e);
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin-bottom: 2rem;
        animation: gradientBG 15s ease infinite;
        background-size: 200% 200%;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .gradient-text {
        background: linear-gradient(90deg, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s infinite;
        background-size: 200% 100%;
    }
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    .service-card {
        background-color: rgba(31, 41, 55, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 41, 55, 0.2);
        transition: all 0.3s ease;
        border: 1px solid rgba(167, 139, 250, 0.1);
    }
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 40px rgba(167, 139, 250, 0.2);
        border: 1px solid rgba(167, 139, 250, 0.3);
    }
    .project-card {
        background-color: rgba(31, 41, 55, 0.7);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 41, 55, 0.2);
        transition: all 0.3s ease;
        border: 1px solid rgba(167, 139, 250, 0.1);
        overflow: hidden;
    }
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 40px rgba(167, 139, 250, 0.2);
        border: 1px solid rgba(167, 139, 250, 0.3);
    }
    .project-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    .project-card:hover .project-image {
        transform: scale(1.05);
    }
    .tech-tag {
        background: linear-gradient(45deg, #4b5563, #6b7280);
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        margin-right: 0.5rem;
        display: inline-block;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    .tech-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(167, 139, 250, 0.2);
    }
    .contact-section {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.7), rgba(31, 41, 55, 0.4));
        backdrop-filter: blur(10px);
        border-radius: 1rem;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(31, 41, 55, 0.2);
        border: 1px solid rgba(167, 139, 250, 0.1);
        margin-top: 3rem;
    }
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 4rem;
        background: linear-gradient(0deg, rgba(31, 41, 55, 0.7), transparent);
    }
    .button-primary {
        background: linear-gradient(45deg, #a78bfa, #f472b6);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 2rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
    }
    .button-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(167, 139, 250, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Main Header and Services sections remain the same [...]
st.markdown("""
    <div class='main-header'>
        <h1 style='font-size: 4rem; font-weight: bold; margin-bottom: 1rem;'>
            <span class='gradient-text'>Campus Coders</span>
        </h1>
        <h2 style='font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; color: #f3f4f6;'>
            Building Tomorrow's Tech Leaders
        </h2>
        <p style='font-size: 1.2rem; color: #d1d5db; max-width: 800px; margin: 0 auto;'>
            Empowering students to transform their academic journey into professional excellence through innovative coding solutions.
        </p>
    </div>
""", unsafe_allow_html=True)

# Updated Custom Projects
custom_projects = [
    {
        "name": "CodeLintPR",
        "description": "An innovative code review automation tool that enhances pull request workflows with AI-powered analysis, code quality checks, and intelligent suggestions for improvements.",
        "html_url": "https://github.com/sathwikshetty33/CodeLintPR",
        "stargazers_count": "15",
        "forks_count": "5",
        "topics": ["Python", "AI", "Code-Analysis"]
    },
    {
        "name": "SafeHaven",
        "description": "A comprehensive disaster management platform that provides real-time alerts, resource coordination, and emergency response tools for communities during natural disasters.",
        "html_url": "https://github.com/sathwikshetty33/SafeHaven",
        "stargazers_count": "12",
        "forks_count": "4",
        "topics": ["React", "Node.js", "MongoDB"]
    },
    {
        "name": "HealthDash",
        "description": "An intelligent healthcare analytics dashboard that visualizes patient data, tracks medical trends, and provides predictive insights for healthcare professionals. Also alerts the nearby hospital incase of accidents.",
        "html_url": "https://github.com/sathwikshetty33/HealthDash",
        "stargazers_count": "10",
        "forks_count": "3",
        "topics": ["Vue.js", "Python", "Machine Learning"]
    }
]

# Updated project images that better match each project
project_images = [
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&q=80",
    # CodeLintPR - coding/automation
    "https://images.unsplash.com/photo-1498354178607-a79df2916198?auto=format&fit=crop&q=80",
    # SafeHaven - emergency response
    "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80"  # HealthDash - healthcare
]

# Projects Section with updated content
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0; color: #a78bfa;'>Featured Projects</h2>",
            unsafe_allow_html=True)

cols = st.columns(3)
for i, (col, project) in enumerate(zip(cols, custom_projects)):
    with col:
        st.markdown(f"""
            <div class='project-card'>
                <img src="{project_images[i]}" class="project-image">
                <h3 style='font-size: 1.5rem; font-weight: bold; color: #a78bfa;'>{project['name']}</h3>
                <p style='color: #d1d5db; margin: 1rem 0; line-height: 1.6;'>{project['description']}</p>
                <div style='margin: 1.5rem 0;'>
                    {' '.join([f"<span class='tech-tag'>{topic}</span>" for topic in project['topics']])}
                </div>
                <a href="{project['html_url']}" target="_blank" class="button-primary">View Project</a>
            </div>
        """, unsafe_allow_html=True)

# Contact Section
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0; color: #a78bfa;'>Connect With Us</h2>",
            unsafe_allow_html=True)

contact_col1, contact_col2, contact_col3 = st.columns([1, 2, 1])
with contact_col2:
    st.markdown("""
        <div class='contact-section'>
            <div style='text-align: center;'>
                <h3 style='font-size: 1.5rem; color: #a78bfa; margin-bottom: 1.5rem;'>Get In Touch</h3>
                <p style='font-size: 1.1rem; margin-bottom: 1rem;'>
                    <span style='color: #a78bfa;'>📧</span> 
                    <a href='mailto:projectrpa976@gmail.com' style='color: #f3f4f6; text-decoration: none; hover:color: #a78bfa;'>
                        projectrpa976@gmail.com
                    </a>
                </p>
                <p style='font-size: 1.1rem; margin-bottom: 1rem;'>
                    <span style='color: #a78bfa;'>📱</span> 
                    <a href='tel:+919876543210' style='color: #f3f4f6; text-decoration: none; hover:color: #a78bfa;'>
                        +91 98765 43210
                    </a>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        <p style='color: #9ca3af;'>© 2025 Campus Coders. Built with 💜 by CampusCoders</p>
    </div>
""", unsafe_allow_html=True)