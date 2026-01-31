import streamlit as st
import pandas as pd
import random
import re
import time

USERS_FILE = "users.csv"

def load_users():
    try:
        return pd.read_csv(USERS_FILE)
    except:
        return pd.DataFrame(columns=["name", "email", "password"])

def save_user(name, email, password):
    df = load_users()
    df.loc[len(df)] = [name, email, password]
    df.to_csv(USERS_FILE, index=False)

def authenticate(email, password):
    df = load_users()
    user = df[(df["email"] == email) & (df["password"] == password)]
    return not user.empty



# ================= CONFIG =================
st.set_page_config(page_title="Student Placement Predictor", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: black;'>🎓 Student Placement Predictor</h1>",
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .stApp {
        background: 
            linear-gradient(
                rgba(255, 255, 255, 0.75),
                rgba(255, 255, 255, 0.75)
            ),
            url("https://i.iheart.com/v3/re/assets.getty/60623a3aec85858a41dcf005?ops=contain(1480,0)");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Normal text */
    p, span, div, label {
        color: black !important;
    }

    /* Question text */
    h1, h2, h3, h4, h5 {
        color: black !important;
    }

    /* Radio button options */
    div[role="radiogroup"] label {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# ================= SESSION STATE =================
def init_state():
    defaults = {
        "page": "details",
        "q_index": 0,
        "questions": [],
        "answers": {},
        "score": 0,
        "timer_start": 0,

        "name": "",
        "email": "",
        "mobile": "",
        "branch": "",
        "year": "",
        "cgpa": 0.0,
        "skill_levels": {},

        # ✅ needed only for palette colors
        "visited": set()
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ================= AUTH STATE =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = ""


# ================= FILES =================
BRANCH_FILES = {
    "CSE": "datasets/cse_questions.csv",
    "CIVIL": "datasets/civil_questions.csv",
    "EEE": "datasets/eee_questions.csv",
    "ECE": "datasets/ece_questions.csv",
    "MECH": "datasets/mech_questions.csv"
}

# ================= JOB ROLES =================
JOB_ROLES = {
    "CSE": {
        "Python": ["Python Developer"],
        "Machine Learning": ["Data Scientist"],
        "Java": ["Java Developer"]
    },
    "EEE": {"Power Systems": ["Power Engineer"]},
    "ECE": {"Communication": ["Network Engineer"]},
    "MECH": {"Design": ["Design Engineer"]},
    "CIVIL": {"Structures": ["Site Engineer"]}
}

# ================= MATERIALS =================
MATERIALS = {
    "CSE": [
        "https://www.w3schools.com/python/",
        "https://www.freecodecamp.org/",
        "https://www.codechef.com/"
    ],
    "EEE": ["https://nptel.ac.in"],
    "ECE": ["https://nptel.ac.in"],
    "MECH": ["https://nptel.ac.in"],
    "CIVIL": ["https://nptel.ac.in"]
}

# ================= LOGIN / SIGNUP =================
if not st.session_state.logged_in:

    st.title("🔐 Student Login")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # ---------- LOGIN ----------
    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(email, password):
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("✅ Login successful")
                st.session_state.page = "details"
                st.rerun()
            else:
                st.error("❌ Invalid email or password")

    # ---------- SIGN UP ----------
    with tab2:
        name = st.text_input("Name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")

        if st.button("Sign Up"):
            if not name or not email or not password:
                st.error("⚠ Fill all fields")
            else:
                df = load_users()
                if email in df["email"].values:
                    st.error("⚠ Email already exists")
                else:
                    save_user(name, email, password)
                    st.success("🎉 Account created! Please login")

    st.stop()   # ⛔ stop app until login


# ================= PAGE 1 : DETAILS =================
if st.session_state.logged_in:
    if st.button("🚪 Logout",):
        st.session_state.logged_in = False
        st.session_state.page = "details"
        st.rerun()

if st.session_state.page == "details":
    st.subheader("🧾 Student Details")

    st.session_state.name = st.text_input("Name", st.session_state.name)
    st.session_state.email = st.text_input("Email", st.session_state.email)
    st.session_state.mobile = st.text_input("Mobile Number", st.session_state.mobile)
    st.session_state.branch = st.selectbox("Branch", BRANCH_FILES.keys())
    st.session_state.year = st.selectbox("Year", ["1st", "2nd", "3rd", "4th"])
    st.session_state.cgpa = st.slider("CGPA", 0.0, 10.0, st.session_state.cgpa)

    if st.button("Next ➡"):
        if not st.session_state.name or not st.session_state.email:
            st.error("⚠ Fill all details")
        elif not re.fullmatch(r"\d{10}", st.session_state.mobile):
            st.error("⚠ Enter valid 10-digit mobile number")
        else:
            st.session_state.page = "skills"
            st.rerun()

# ================= PAGE 2 : SKILLS =================
elif st.session_state.page == "skills":
    st.subheader("📘 Skill Levels")

    df = pd.read_csv(BRANCH_FILES[st.session_state.branch])
    skills = df["Skill"].unique()

    for s in skills:
        if s not in st.session_state.skill_levels:
            st.session_state.skill_levels[s] = "Beginner"

        st.session_state.skill_levels[s] = st.selectbox(
            f"{s} Level",
            ["Beginner", "Intermediate", "Advanced"],
            index=["Beginner", "Intermediate", "Advanced"].index(
                st.session_state.skill_levels[s]
            ),
            key=f"skill_{s}"
        )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "details"
            st.rerun()

    with col2:
        if st.button("Start Test 🚀"):
            qs = []
            for _, r in df.iterrows():
                opts = [r["Option1"], r["Option2"], r["Option3"], r["Option4"]]
                qs.append(
                    (r["Question"], opts, r["Answer"], r["Skill"], r.get("Reference", ""))
                )

            random.shuffle(qs)
            st.session_state.questions = qs[:20]
            st.session_state.answers = {}
            st.session_state.q_index = 0
            st.session_state.timer_start = time.time()
            st.session_state.visited = set()

            st.session_state.page = "test"
            st.rerun()

# ================= PAGE 3 : TEST =================
elif st.session_state.page == "test":
    TOTAL_TIME = 20 * 10

    elapsed = int(time.time() - st.session_state.timer_start)
    remaining = max(0, TOTAL_TIME - elapsed)

    q, opts, correct, skill, ref = st.session_state.questions[st.session_state.q_index]

    # ✅ only added to track visited questions
    st.session_state.visited.add(st.session_state.q_index)

    st.subheader(f"Question {st.session_state.q_index + 1}/20")
    st.warning(f"⏳ Time left: {remaining} seconds")
    st.write(q)

    prev = st.session_state.answers.get(st.session_state.q_index)
    selected = st.radio(
        "Choose an option",
        opts,
        index=opts.index(prev) if prev in opts else None
    )

    if selected is not None:
        st.session_state.answers[st.session_state.q_index] = selected

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous") and st.session_state.q_index > 0:
            st.session_state.q_index -= 1
            st.rerun()

        if st.button("Next ➡"):
            if st.session_state.q_index < 19:
                st.session_state.q_index += 1
                st.rerun()
            else:
                score = 0
                for i, (_, _, ans, _, _) in enumerate(st.session_state.questions):
                    if st.session_state.answers.get(i) == ans:
                        score += 1

                st.session_state.score = score
                st.session_state.page = "result"
                st.rerun()

    # ---------------- RIGHT SIDE PALETTE ----------------
     #================= QUESTION PALETTE =================
    with col2:
        st.markdown("### 🧭 Question Palette")

        rows, cols = 4, 5

        for r in range(rows):
            row_cols = st.columns(cols)
            for c in range(cols):

                q_no = r * cols + c

                if q_no < 20:
                    
                    # ✅ COLOR LOGIC
                    if q_no in st.session_state.answers:
                        color = "#28a745"   # green answered
                    else:
                        color = "#dc3545"   # red not answered

                    if q_no == st.session_state.q_index:
                        color = "#007bff"   # blue current
                    
                    text_color = "#170202"
                    label = str(q_no + 1)

                

                    row_cols[c].markdown(
                        f"""
                        <button style="
                            background-color:{color};
                            color:black;
                            border:none;
                            border-radius:8px;
                            height:45px;
                            width:45px;
                            font-size:16px;
                            font-weight:bold;
                            cursor:pointer;
                        "
                        onclick="window.location.href='?q={q_no}'">
                        {label}
                        </button>
                        """,
                        unsafe_allow_html=True
                    )


    # AUTO SUBMIT (unchanged)
    if remaining == 0:
        score = 0
        for i, (_, _, ans, _, _) in enumerate(st.session_state.questions):
            if st.session_state.answers.get(i) == ans:
                score += 1

        st.session_state.score = score
        st.session_state.page = "result"
        st.rerun()

# ================= PAGE 4 : RESULT ================
elif st.session_state.page == "result":
    total = len(st.session_state.questions)
    percent = (st.session_state.score / total) * 100

    st.subheader("📊 Final Result")
    st.write(f"Score: *{st.session_state.score}/{total} ({percent:.2f}%)*")

    if percent >= 70:
        st.balloons()
        st.success("🎉 High Placement Chance")
    elif percent >= 40:
        st.warning("🙂 Medium Placement Chance")
    else:
        st.error("⚠ Low Placement Chance")

    st.subheader("💼 Job Roles")
    skill_ok = set(
        skill for i, (_, _, a, skill, _) in enumerate(st.session_state.questions)
        if st.session_state.answers.get(i) == a
    )

    for s in skill_ok:
        for r in JOB_ROLES.get(st.session_state.branch, {}).get(s, []):
            st.write("•", r)

    st.subheader("📚 Learning References")
    for m in MATERIALS[st.session_state.branch]:
        st.write("•", m)

    if st.button("📝 Review Answers"):
        st.session_state.page = "review"
        st.rerun()

# ================= PAGE 5 : REVIEW =================
elif st.session_state.page == "review":
    st.title("📝 Answer Review")

    for i, (q, _, correct, _, ref) in enumerate(st.session_state.questions):
        st.markdown(f"### Q{i+1}. {q}")
        user_ans = st.session_state.answers.get(i)

        if user_ans is None:
            st.warning("⚠ Not Answered")
        elif user_ans == correct:
            st.success(f"✅ Your Answer: {user_ans}")
        else:
            st.error(f"❌ Your Answer: {user_ans}")
            st.info(f"✔ Correct Answer: {correct}")

        if ref:
            st.markdown(f"🔗 Reference: {ref}")

        st.divider()

    if st.button("⬅ Back to Result"):
        st.session_state.page = "result"
        st.rerun()