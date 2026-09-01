from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Gracie Schmidt | Data Science Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"

GITHUB_URL = "https://github.com/GracieHannah"
GITHUB_REPOS_URL = "https://github.com/GracieHannah?tab=repositories"
LINKEDIN_URL = "https://www.linkedin.com/in/gracehannahschmidt/"
RESUME_URL = "https://docs.google.com/document/d/1mH454hDdVzIUEWgw1q2sBCCZSCvMqSA2yLJxfeHOrKo/edit?tab=t.0#heading=h.5x0d5h95i329"
EMAIL = "graciehannahschmidt@gmail.com"

# -----------------------------
# Theme / styling
# -----------------------------
st.markdown(
    """
    <style>
        .block-container {
            max-width: 1180px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }
        h1, h2, h3 {
            letter-spacing: -0.025em;
        }
        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(255,255,255,0.10);
            padding: 1rem;
            border-radius: 16px;
        }
        .hero {
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 24px;
            padding: 2.1rem 2.2rem;
            margin-bottom: 1.2rem;
            background:
              radial-gradient(circle at 92% 12%, rgba(244,162,97,.20), transparent 26%),
              radial-gradient(circle at 76% 74%, rgba(42,157,143,.15), transparent 24%),
              rgba(255,255,255,.025);
        }
        .eyebrow {
            text-transform: uppercase;
            letter-spacing: .16em;
            font-size: .78rem;
            font-weight: 700;
            color: #F4A261;
            margin-bottom: .75rem;
        }
        .hero-title {
            font-size: clamp(2.2rem, 7vw, 4.8rem);
            line-height: .98;
            font-weight: 800;
            letter-spacing: -.05em;
            margin: 0 0 1rem 0;
        }
        .hero-copy {
            max-width: 780px;
            font-size: 1.15rem;
            line-height: 1.65;
            color: rgba(245,247,250,.84);
        }
        .accent {
            color: #F4A261;
        }
        .soft {
            color: rgba(245,247,250,.68);
        }
        .tiny {
            color: rgba(245,247,250,.58);
            font-size: .85rem;
        }
        .section-kicker {
            color: #F4A261;
            text-transform: uppercase;
            letter-spacing: .12em;
            font-size: .78rem;
            font-weight: 700;
            margin-bottom: .25rem;
        }
        .personality-box {
            border-left: 3px solid #F4A261;
            padding: .25rem 0 .25rem 1rem;
            margin: .5rem 0 1.25rem 0;
        }
        .footer {
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid rgba(255,255,255,.08);
            color: rgba(245,247,250,.55);
            font-size: .85rem;
        }
        div[data-testid="stExpander"] details {
            border-radius: 14px;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: .3rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data used by the portfolio
# -----------------------------
PROJECTS = [
    {
        "name": "Beats by Dre | Product & Market Strategy",
        "year": 2026,
        "category": "Product Analytics",
        "tools": ["Python", "NLP", "Customer Insights", "Product Strategy"],
        "metric": "1,300 cleaned reviews",
        "summary": "Analyzed cleaned Amazon headphone reviews across eight brands to identify what builds or breaks trust in a premium audio product.",
        "impact": "Recommended stabilizing Solo 4 risk, using Studio Pro as the premium anchor, and concept-testing a comfort-first everyday premium headphone before launch approval.",
        "featured": True,
    },
    {
        "name": "Telecom Customer Churn",
        "year": 2026,
        "category": "Machine Learning",
        "tools": ["Python", "CatBoost", "LightGBM", "Classification"],
        "metric": "0.93 ROC-AUC",
        "summary": "Built an end-to-end churn model using customer lifecycle, billing, contract, and service behavior.",
        "impact": "Identified higher-risk segments and translated feature importance into retention actions for month-to-month, early-tenure, and service-friction customers.",
        "featured": True,
    },
    {
        "name": "Spotify Listening Behavior",
        "year": 2026,
        "category": "Behavioral Analytics",
        "tools": ["Python", "Pandas", "EDA", "Time Analysis"],
        "metric": "38,977 cleaned rows",
        "summary": "Combined multi-year Spotify extended-history files and transformed timestamps into local time features for longitudinal listening analysis.",
        "impact": "Explores core taste versus changing life-stage behavior through artist, album, track, year, weekday, and time-of-day patterns.",
        "featured": True,
    },
    {
        "name": "Taxi Demand Forecasting",
        "year": 2025,
        "category": "Forecasting",
        "tools": ["Python", "XGBoost", "Time Series", "Feature Engineering"],
        "metric": "38.95 RMSE",
        "summary": "Forecasted hourly taxi demand using lag features and rolling statistics.",
        "impact": "Connected forecast accuracy to operational capacity planning and demand peaks.",
        "featured": True,
    },
    {
        "name": "Computer Vision Age Estimation",
        "year": 2026,
        "category": "Deep Learning",
        "tools": ["TensorFlow", "Keras", "CNN", "Computer Vision"],
        "metric": "~7.6 year MAE",
        "summary": "Trained a convolutional neural network to estimate customer age from images for a retail verification scenario.",
        "impact": "Evaluated model error and generalization in the context of real-world compliance decisions.",
        "featured": False,
    },
    {
        "name": "Oil Well Profit & Risk",
        "year": 2025,
        "category": "Decision Science",
        "tools": ["Python", "Regression", "Bootstrapping", "Risk Analysis"],
        "metric": "$4.41M mean profit",
        "summary": "Predicted oil reserves across three regions and used bootstrap simulations to compare expected profit and downside risk.",
        "impact": "Recommended the region with the strongest expected return while keeping estimated loss risk within the project threshold.",
        "featured": False,
    },
    {
        "name": "Gold Recovery Modeling",
        "year": 2025,
        "category": "Machine Learning",
        "tools": ["Python", "Regression", "Model Evaluation", "sMAPE"],
        "metric": "5.94 final sMAPE",
        "summary": "Modeled gold recovery performance from multi-stage process data.",
        "impact": "Built and evaluated regression approaches using a custom error metric tied to production recovery outcomes.",
        "featured": False,
    },
    {
        "name": "Megaline Plan Recommendation",
        "year": 2025,
        "category": "Machine Learning",
        "tools": ["Python", "Classification", "Scikit-learn"],
        "metric": "0.733 test accuracy",
        "summary": "Built a classification model to recommend mobile plans from customer usage behavior.",
        "impact": "Compared models and validated the selected approach on held-out data.",
        "featured": False,
    },
]

SPOTIFY_OVERALL = pd.DataFrame(
    {
        "Artist": [
            "ODESZA", "Twenty One Pilots", "BRONSON", "Big Wild", "Bob Moses",
            "Crooked Colours", "MEMBA", "Parry Gripp", "PINES", "Linkin Park",
        ],
        "Plays": [3482, 1657, 901, 760, 609, 570, 513, 510, 481, 412],
    }
)

SPOTIFY_BY_YEAR = {
    "2023": pd.DataFrame({
        "Artist": ["Nine Inch Nails", "TOOL", "A Perfect Circle", "Panic! At The Disco", "Deftones"],
        "Plays": [19, 6, 5, 4, 4],
    }),
    "2024": pd.DataFrame({
        "Artist": ["Twenty One Pilots", "ODESZA", "BRONSON", "Bob Moses", "Big Wild", "MEMBA", "Highly Suspect", "pluko", "Crooked Colours", "Chevelle"],
        "Plays": [1045, 1038, 332, 284, 253, 236, 228, 207, 204, 195],
    }),
    "2025": pd.DataFrame({
        "Artist": ["ODESZA", "Parry Gripp", "BRONSON", "Big Wild", "Twenty One Pilots", "PINES", "Bob Moses", "Crooked Colours", "MEMBA", "BAYNK"],
        "Plays": [2072, 493, 462, 456, 400, 277, 268, 248, 235, 190],
    }),
    "2026": pd.DataFrame({
        "Artist": ["ODESZA", "Twenty One Pilots", "Phantogram", "Linkin Park", "Ian Asher", "RÜFÜS DU SOL", "PLÜM", "Crooked Colours", "LEAP", "BRONSON"],
        "Plays": [372, 212, 207, 200, 155, 139, 131, 118, 116, 107],
    }),
}

BEATS_PRODUCT_DATA = {
    "Studio Pro": {"reviews": 199, "rating": 4.51, "low_rating_rate": 1.0, "role": "Premium anchor"},
    "Solo 4": {"reviews": 300, "rating": 4.34, "low_rating_rate": 11.3, "role": "Concentrated risk"},
}

BEATS_POSITIVE = pd.DataFrame(
    {
        "Theme": ["Sound", "Quality", "Comfort", "Price / Value", "Battery"],
        "Share": [44, 33, 21, 18, 17],
    }
)

BEATS_TRUST_BREAKERS = pd.DataFrame(
    {
        "Theme": ["Durability", "Charging / Battery", "Connectivity", "Sound", "Comfort"],
        "Share": [38.9, 25.0, 25.0, 25.0, 16.7],
    }
)


def plot_bar(df: pd.DataFrame, x: str, y: str, title: str, horizontal: bool = True):
    data = df.copy()
    if horizontal:
        fig = px.bar(data.sort_values(y), x=y, y=x, orientation="h", text=y, title=title)
        fig.update_traces(texttemplate="%{text}", textposition="outside", cliponaxis=False)
    else:
        fig = px.bar(data, x=x, y=y, text=y, title=title)
        fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_traces(marker_color="#F4A261")
    fig.update_layout(
        height=390,
        margin=dict(l=10, r=35, t=55, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F5F7FA"),
        title_font=dict(size=18),
        xaxis=dict(gridcolor="rgba(255,255,255,.08)", zeroline=False),
        yaxis=dict(gridcolor="rgba(255,255,255,.04)", zeroline=False),
    )
    return fig


def tag_line(tags):
    return " · ".join(tags)


def project_card(project):
    with st.container(border=True):
        top, metric = st.columns([4, 1.3], vertical_alignment="top")
        with top:
            st.markdown(f"### {project['name']}")
            st.caption(f"{project['category']} · {project['year']} · {tag_line(project['tools'])}")
        with metric:
            st.metric("Project signal", project["metric"])
        st.write(project["summary"])
        st.markdown(f"**Why it matters:** {project['impact']}")


# -----------------------------
# Header / contact row
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Data Scientist · Applied Analytics · Product & Customer Insights</div>
        <div class="hero-title">Gracie <span class="accent">Schmidt</span></div>
        <div class="hero-copy">
            Business operator turned data scientist. I use machine learning, experimentation,
            behavioral analysis, and visual storytelling to turn messy data into decisions people can actually use.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.link_button("LinkedIn ↗", LINKEDIN_URL, use_container_width=True)
with c2:
    st.link_button("GitHub ↗", GITHUB_URL, use_container_width=True)
with c3:
    st.link_button("Resume ↗", RESUME_URL, use_container_width=True)
with c4:
    st.link_button("Email me ✉", f"mailto:{EMAIL}", use_container_width=True)

# -----------------------------
# Main navigation
# -----------------------------
overview_tab, projects_tab, beats_tab, spotify_tab, background_tab = st.tabs(
    ["Overview", "Project Gallery", "Beats Case Study", "Spotify Explorer", "Background"]
)

with overview_tab:
    st.markdown('<div class="section-kicker">At a glance</div>', unsafe_allow_html=True)
    st.subheader("A technical portfolio grounded in real business decisions")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Business experience", "10+ years", "ownership + operations")
    m2.metric("Churn model", "0.93 ROC-AUC", "classification")
    m3.metric("Beats analysis", "1,300 reviews", "8 brands")
    m4.metric("Spotify project", "38,977 rows", "multi-year behavior")

    left, right = st.columns([1.2, 1])
    with left:
        st.markdown("### What I do")
        st.write(
            "I’m most interested in the space where technical analysis connects with human behavior: "
            "why customers leave, what changes demand, where a product experience breaks trust, "
            "and which signals are strong enough to act on."
        )
        st.write(
            "My background in business ownership means I naturally connect model performance "
            "to revenue, retention, customer experience, operations, and the decision someone has to make next."
        )
    with right:
        st.markdown("### How I work")
        st.markdown(
            """
            1. **Start with the decision.** What needs to become clearer?
            2. **Understand the behavior.** Look for the pattern behind the metric.
            3. **Build only what helps.** Use the right level of modeling complexity.
            4. **Translate the result.** Make the recommendation usable by a real team.
            5. **Visualize Data** Display information for non techs to better comprehend. 
            """
        )

    st.markdown("### Featured work")
    featured = [p for p in PROJECTS if p["featured"]]
    for project in featured:
        project_card(project)

    st.markdown("### A little personality")
    st.markdown(
        """
        <div class="personality-box">
            I like work that has both structure and a little chaos. Outside the notebook, I’m drawn to
            mountains, music, photography, creative projects, and family life — all things that keep me curious,
            adaptable, and comfortable figuring things out as I go.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown("### Currently exploring")
        st.write(
            "Data Scientist · Product Data Scientist · Applied Scientist · Product / Customer Insights · Growth Analytics"
        )
        st.caption("Remote roles are a strong fit; Seattle / Central Washington hybrid opportunities also make sense.")

with projects_tab:
    st.markdown('<div class="section-kicker">Selected work</div>', unsafe_allow_html=True)
    st.subheader("Filter the portfolio by the kind of problem you care about")

    categories = sorted({p["category"] for p in PROJECTS})
    filter_col, search_col = st.columns([1, 1.3])
    with filter_col:
        selected_categories = st.multiselect(
            "Focus area",
            options=categories,
            default=categories,
        )
    with search_col:
        keyword = st.text_input("Search projects", placeholder="Try: retention, forecasting, NLP, risk...")

    filtered_projects = []
    for p in PROJECTS:
        haystack = " ".join([p["name"], p["summary"], p["impact"], *p["tools"]]).lower()
        if p["category"] in selected_categories and keyword.lower().strip() in haystack:
            filtered_projects.append(p)

    st.caption(f"Showing {len(filtered_projects)} of {len(PROJECTS)} projects")
    for p in filtered_projects:
        project_card(p)

    st.link_button("Browse all public GitHub repositories ↗", GITHUB_REPOS_URL)
    st.caption("Project-specific repository links can be mapped here once the exact repo URLs are confirmed.")

with beats_tab:
    st.markdown('<div class="section-kicker">Product strategy case study</div>', unsafe_allow_html=True)
    st.subheader("Beats by Dre: from review data to a launch recommendation")
    st.write(
        "This case study uses 1,300 cleaned Amazon headphone reviews across eight brands. "
        "The goal was not just to summarize sentiment, but to decide what Beats should validate before approving a major new launch."
    )

    a, b, c, d = st.columns(4)
    a.metric("All reviews", "1,300")
    b.metric("Beats reviews", "499")
    c.metric("Positive Beats reviews", "432")
    d.metric("Low-rated Beats reviews", "36")

    st.markdown("### Compare the two Beats product families")
    product = st.selectbox("Product family", list(BEATS_PRODUCT_DATA.keys()), label_visibility="collapsed")
    p = BEATS_PRODUCT_DATA[product]
    p1, p2, p3, p4 = st.columns(4)
    p1.metric("Reviews", f"{p['reviews']}")
    p2.metric("Avg rating", f"{p['rating']:.2f} ★")
    p3.metric("Low-rating rate", f"{p['low_rating_rate']:.1f}%")
    p4.metric("Strategic role", p["role"])

    chart_left, chart_right = st.columns(2)
    with chart_left:
        st.plotly_chart(
            plot_bar(BEATS_POSITIVE, "Theme", "Share", "What positive reviewers reward (%)"),
            use_container_width=True,
        )
    with chart_right:
        st.plotly_chart(
            plot_bar(BEATS_TRUST_BREAKERS, "Theme", "Share", "Trust-breaker signals in low ratings (%)"),
            use_container_width=True,
        )

    with st.container(border=True):
        st.markdown("### Recommendation")
        st.markdown(
            "**Stabilize → Position → Concept-test → Build the business case.**  "
            "Investigate Solo 4 risk, anchor premium positioning with Studio Pro, validate a comfort-first daily-use concept, "
            "and approve launch only after purchase intent, willingness to pay, unit economics, and launch thresholds support it."
        )

    beats_pdf = ASSET_DIR / "beats_analysis.pdf"
    beats_cover = ASSET_DIR / "beats_cover.png"
    if beats_cover.exists():
        with st.expander("Preview the full presentation"):
            st.image(str(beats_cover), caption="Beats by Dre Headphones Analysis & Launch Recommendation")
    if beats_pdf.exists():
        st.download_button(
            "Download the Beats case study PDF",
            data=beats_pdf.read_bytes(),
            file_name="Gracie_Schmidt_Beats_Analysis.pdf",
            mime="application/pdf",
        )

with spotify_tab:
    st.markdown('<div class="section-kicker">Personal behavioral analytics</div>', unsafe_allow_html=True)
    st.subheader("Spotify Explorer: the dataset is personal, the analysis is professional")
    st.write(
        "I combined multiple Spotify extended-history JSON files, cleaned the data, converted timestamps to Pacific time, "
        "and created year / month / weekday / hour features to examine how listening behavior changes over time."
    )

    s1, s2, s3 = st.columns(3)
    s1.metric("Initial rows", "39,252")
    s2.metric("Cleaned rows", "38,977")
    s3.metric("Overall #1 artist", "ODESZA", "3,482 plays")

    view = st.radio("Artist view", ["Overall", "By year"], horizontal=True)
    if view == "Overall":
        artist_df = SPOTIFY_OVERALL
        title = "Top artists across the cleaned history"
    else:
        year = st.select_slider("Year", options=list(SPOTIFY_BY_YEAR.keys()), value="2025")
        artist_df = SPOTIFY_BY_YEAR[year]
        title = f"Top artists in {year}"

    st.plotly_chart(plot_bar(artist_df, "Artist", "Plays", title), use_container_width=True)

    with st.container(border=True):
        st.markdown("### Why this belongs in a professional portfolio")
        st.write(
            "The fun part is the music. The transferable skill is behavioral analysis: combining messy longitudinal data, "
            "engineering time-based features, comparing cohorts or periods, and finding the difference between stable preferences "
            "and context-driven behavior."
        )

    spotify_pdf = ASSET_DIR / "spotify_analysis.pdf"
    if spotify_pdf.exists():
        st.download_button(
            "Download the current Spotify analysis PDF",
            data=spotify_pdf.read_bytes(),
            file_name="Gracie_Schmidt_Spotify_Analysis.pdf",
            mime="application/pdf",
        )

with background_tab:
    st.markdown('<div class="section-kicker">Background</div>', unsafe_allow_html=True)
    st.subheader("The path into data science is part of the value")

    intro, skills = st.columns([1.1, 1])
    with intro:
        st.markdown("### Professional story")
        st.write(
            "Before data science, I spent more than a decade running and managing customer-facing businesses. "
            "That meant working with retention, scheduling, revenue, customer feedback, service quality, capacity, and the tradeoffs "
            "that come with making decisions when the data is imperfect."
        )
        st.write(
            "I now pair that business intuition with Python, SQL, machine learning, experimentation, forecasting, "
            "NLP, computer vision, and visualization."
        )

        st.markdown("### Experience")
        with st.expander("Beats by Dre consumer insights externship · 2026", expanded=True):
            st.write(
                "Conducted qualitative and quantitative review analysis, used Python / NLP techniques to surface customer themes, "
                "and translated findings into product and market recommendations."
            )
        with st.expander("Founder & Owner · 2014–2026"):
            st.write(
                "Used customer behavior, repeat-booking patterns, service utilization, feedback, and seasonal demand to guide "
                "operations, capacity, pricing, and retention decisions."
            )
        with st.expander("Spa Manager · Leavenworth, WA"):
            st.write(
                "Managed scheduling, staff coordination, customer experience, and operations in a high-volume tourism environment."
            )

    with skills:
        st.markdown("### Technical toolkit")
        skill_groups = {
            "Data": "Python · SQL · Pandas · NumPy · EDA · Statistical Analysis",
            "Machine Learning": "Scikit-learn · CatBoost · LightGBM · XGBoost · Regression · Classification",
            "Advanced": "TensorFlow / Keras · Computer Vision · NLP · Time-Series Forecasting",
            "Experimentation": "A/B Testing · Bootstrapping · Model Evaluation · Cohort Analysis",
            "Visualization": "Plotly · Tableau · Matplotlib · Streamlit",
            "Workflow": "Git · GitHub · Jupyter · VS Code",
        }
        for label, values in skill_groups.items():
            with st.container(border=True):
                st.markdown(f"**{label}**")
                st.caption(values)

        st.markdown("### Education")
        st.markdown(
            "**Certified Data Scientist · 2026**  \n"
            "Machine Learning & Applied Analytics program  \n\n"
            "**Associate of Arts**  \n"
            "Wenatchee Valley Community College"
        )

    st.markdown("### Let’s connect")
    st.write(
        "If you’re hiring for a role where customer behavior, product decisions, analytics, and business judgment overlap, I’d love to talk."
    )
    q1, q2, q3 = st.columns(3)
    q1.link_button("LinkedIn ↗", LINKEDIN_URL, use_container_width=True)
    q2.link_button("GitHub ↗", GITHUB_URL, use_container_width=True)
    q3.link_button("Email ✉", f"mailto:{EMAIL}", use_container_width=True)

st.markdown(
    "<div class='footer'>Built with Streamlit · Portfolio content © Gracie Schmidt</div>",
    unsafe_allow_html=True,
)
