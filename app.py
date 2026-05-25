import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CareerVerse",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "rank" not in st.session_state:
    st.session_state.rank = "Novice Explorer"

if "tech" not in st.session_state:
    st.session_state.tech = 20

if "biz" not in st.session_state:
    st.session_state.biz = 20

if "creative" not in st.session_state:
    st.session_state.creative = 20

# =========================================================
# HEADER
# =========================================================

st.title("🚀 CAREERVERSE : STUDENT MISSION")

st.markdown("### Interactive Career Guidance System")

st.divider()

# =========================================================
# SIDEBAR ANALYTICS
# =========================================================

st.sidebar.title("📊 LIVE PROFILE ANALYTICS")

st.sidebar.metric("XP Points", st.session_state.xp)

st.sidebar.metric("Current Rank", st.session_state.rank)

# =========================================================
# SKILL MATRIX
# =========================================================

data = pd.DataFrame({
    "Skills": ["Technology", "Business", "Creative"],
    "Score": [
        st.session_state.tech,
        st.session_state.biz,
        st.session_state.creative
    ]
})

st.sidebar.bar_chart(data.set_index("Skills"))

# =========================================================
# CAREER TIPS
# =========================================================

tips = [
    "💡 Engineering needs logical thinking skills.",
    "💡 AI & Cybersecurity are future careers.",
    "💡 Commerce students can become entrepreneurs.",
    "💡 Communication skills help in every career.",
    "💡 Creative careers are highly demanded today.",
    "💡 Data Science is one of the highest paying fields.",
]

st.sidebar.info(tips[st.session_state.xp % len(tips)])

# =========================================================
# MAIN SELECTION
# =========================================================

level = st.selectbox(
    "🎓 Select Your Education Level",
    [
        "After 10th Standard",
        "After 2nd PU"
    ]
)

# =========================================================
# AFTER 10TH
# =========================================================

if level == "After 10th Standard":

    st.header("🧭 Career Paths After 10th")

    stream = st.radio(
        "Choose Your Interest Area",
        [
            "Science & Technology",
            "Commerce & Business",
            "Technical / Creative"
        ]
    )

    # =====================================================
    # SCIENCE
    # =====================================================

    if stream == "Science & Technology":

        st.success("""
        🔬 SCIENCE STREAM DETAILS

        Career Options:
        • Engineering
        • Artificial Intelligence
        • Robotics
        • Software Development
        • Biotechnology
        • Medical
        """)

        choice = st.radio(
            "Choose Specialization",
            [
                "Engineering & Computer Science",
                "Medical & Biology"
            ]
        )

        if choice == "Engineering & Computer Science":

            st.session_state.tech += 30
            st.session_state.xp += 100
            st.session_state.rank = "Cyber Architect"

            st.balloons()

            st.subheader("⚡ Recommended Careers")

            st.write("""
            • Software Engineering  
            • Artificial Intelligence  
            • Robotics  
            • Cybersecurity  
            """)

        else:

            st.session_state.tech += 20
            st.session_state.xp += 100
            st.session_state.rank = "Elite Scientist"

            st.subheader("🩺 Recommended Careers")

            st.write("""
            • MBBS  
            • Pharmacy  
            • Nursing  
            • Biotechnology  
            """)

    # =====================================================
    # COMMERCE
    # =====================================================

    elif stream == "Commerce & Business":

        st.info("""
        💼 COMMERCE STREAM DETAILS

        Career Options:
        • Chartered Accountant
        • Banking
        • Finance
        • Entrepreneurship
        • Business Management
        """)

        choice = st.radio(
            "Choose Commerce Goal",
            [
                "Chartered Accountant / CS",
                "Business Leadership / Startup"
            ]
        )

        if choice == "Chartered Accountant / CS":

            st.session_state.biz += 30
            st.session_state.xp += 100
            st.session_state.rank = "Financial Mastermind"

            st.subheader("💎 Recommended Careers")

            st.write("""
            • Chartered Accountant  
            • Banking  
            • Finance  
            • Investment Banking  
            """)

        else:

            st.session_state.biz += 20
            st.session_state.creative += 10
            st.session_state.xp += 100
            st.session_state.rank = "Venture Captain"

            st.subheader("💼 Recommended Careers")

            st.write("""
            • Entrepreneurship  
            • Startup Founder  
            • Marketing  
            • Business Administration  
            """)

    # =====================================================
    # TECHNICAL / CREATIVE
    # =====================================================

    else:

        st.warning("""
        🎨 TECHNICAL / CREATIVE CAREERS

        Recommended Fields:
        • Animation
        • Designing
        • ITI
        • Polytechnic
        • Hardware Networking
        """)

        st.session_state.creative += 40
        st.session_state.xp += 100
        st.session_state.rank = "Creative Master"

# =========================================================
# AFTER 2ND PU
# =========================================================

elif level == "After 2nd PU":

    st.header("🎓 Higher Education Career Paths")

    stream = st.radio(
        "Choose Stream",
        [
            "Science",
            "Commerce",
            "Arts / Design"
        ]
    )

    # =====================================================
    # SCIENCE
    # =====================================================

    if stream == "Science":

        st.success("""
        🔬 SCIENCE STREAM

        Career Paths:
        • Engineering
        • AI & Data Science
        • Medical
        • Cybersecurity
        • Robotics
        """)

        st.session_state.tech += 25
        st.session_state.xp += 120
        st.session_state.rank = "Advanced Navigator"

    # =====================================================
    # COMMERCE
    # =====================================================

    elif stream == "Commerce":

        st.info("""
        💸 COMMERCE STREAM

        Career Paths:
        • B.Com
        • BBA
        • CA
        • Banking
        • Finance
        """)

        st.session_state.biz += 25
        st.session_state.xp += 120
        st.session_state.rank = "Business Strategist"

    # =====================================================
    # ARTS
    # =====================================================

    else:

        st.warning("""
        🎨 ARTS / DESIGN STREAM

        Career Paths:
        • Journalism
        • Fashion Designing
        • Animation
        • UI/UX Designing
        • Law
        """)

        st.session_state.creative += 25
        st.session_state.xp += 120
        st.session_state.rank = "Creative Visionary"

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.success(
    f"✨ XP: {st.session_state.xp} | 🏆 Rank: {st.session_state.rank}"
)

# =========================================================
# RESET BUTTON
# =========================================================

if st.button("🔄 Restart Mission"):

    st.session_state.xp = 0
    st.session_state.rank = "Novice Explorer"

    st.session_state.tech = 20
    st.session_state.biz = 20
    st.session_state.creative = 20

    st.rerun()
