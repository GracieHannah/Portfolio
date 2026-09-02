from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


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
RESUME_URL = "https://docs.google.com/document/d/1mH454hDdVzIUEWgw1q2sBCCZSCvMqSA2yLJxfeHOrKo/edit"
EMAIL = "graciehannahschmidt@gmail.com"

COLORS = ["#FF6EC7", "#7DF9FF", "#B8FF6A", "#C9A7FF", "#FFD166", "#FF8E72"]
PINK, CYAN, LIME, LAVENDER, YELLOW, CORAL = COLORS


st.markdown(
    f"""
    <style>
        :root {{
            --pink: {PINK};
            --cyan: {CYAN};
            --lime: {LIME};
            --lavender: {LAVENDER};
            --yellow: {YELLOW};
        }}
        .stApp {{
            background:
                radial-gradient(circle at 8% 0%, rgba(255,110,199,.11), transparent 24rem),
                radial-gradient(circle at 92% 6%, rgba(125,249,255,.10), transparent 28rem),
                #050507;
        }}
        .block-container {{
            max-width: 1220px;
            padding-top: 1.25rem;
            padding-bottom: 4rem;
        }}
        h1, h2, h3 {{ letter-spacing: -.035em; }}
        .rainbow-line {{
            height: 4px;
            border-radius: 99px;
            margin: .7rem 0 1.4rem;
            background: linear-gradient(90deg, {PINK}, {LAVENDER}, {CYAN}, {LIME}, {YELLOW});
            box-shadow: 0 0 24px rgba(125,249,255,.36);
        }}
        .hero {{
            padding: 2.4rem 2.45rem;
            border: 1px solid rgba(255,255,255,.12);
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(255,255,255,.065), rgba(255,255,255,.018));
            box-shadow: 0 18px 80px rgba(0,0,0,.35);
            overflow: hidden;
        }}
        .eyebrow {{
            color: {CYAN};
            font-size: .76rem;
            font-weight: 800;
            letter-spacing: .17em;
            text-transform: uppercase;
        }}
        .hero-title {{
            font-size: clamp(3rem, 8vw, 6.4rem);
            font-weight: 850;
            line-height: .9;
            margin: .65rem 0 .85rem;
            letter-spacing: -.065em;
        }}
        .gradient-text {{
            background: linear-gradient(90deg, {PINK}, {LAVENDER}, {CYAN}, {LIME});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero-copy {{
            color: rgba(255,255,255,.73);
            font-size: 1.08rem;
            max-width: 720px;
        }}
        .section-label {{
            color: {CYAN};
            font-size: .74rem;
            font-weight: 800;
            letter-spacing: .15em;
            text-transform: uppercase;
            margin-top: .4rem;
        }}
        [data-testid="stMetric"] {{
            border: 1px solid rgba(255,255,255,.12);
            background: rgba(255,255,255,.035);
            border-radius: 18px;
            padding: 1rem;
        }}
        [data-testid="stMetricValue"] {{
            background: linear-gradient(90deg, {PINK}, {CYAN});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            border-color: rgba(255,255,255,.12) !important;
            background: rgba(255,255,255,.025);
            border-radius: 18px;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            gap: .35rem;
            background: rgba(255,255,255,.025);
            border-radius: 16px;
            padding: .3rem;
        }}
        .stTabs [aria-selected="true"] {{
            color: {CYAN} !important;
        }}
        .stButton button, .stLinkButton a {{
            border-radius: 999px !important;
            border-color: rgba(125,249,255,.42) !important;
        }}
        .tag {{
            display: inline-block;
            padding: .25rem .62rem;
            margin: .18rem .16rem .18rem 0;
            border: 1px solid rgba(201,167,255,.38);
            border-radius: 999px;
            color: rgba(255,255,255,.75);
            font-size: .74rem;
        }}
        .mini-card {{
            min-height: 118px;
            padding: 1rem 1.1rem;
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,.11);
            background: linear-gradient(140deg, rgba(255,255,255,.05), rgba(255,255,255,.015));
        }}
        .mini-card strong {{ color: {CYAN}; }}
        .soft {{ color: rgba(255,255,255,.62); }}
        .footer {{
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid rgba(255,255,255,.08);
            color: rgba(255,255,255,.42);
            font-size: .82rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


PROJECTS = [
    {
        "name": "Beats by Dre",
        "subtitle": "Product & Market Strategy",
        "year": 2026,
        "category": "Product Analytics",
        "tools": ["Python", "NLP", "Customer Insights"],
        "signal": "1,300 reviews",
        "score": 94,
        "business": 96,
        "technical": 82,
        "visual": 91,
        "summary": "Review intelligence turned into a staged launch recommendation.",
    },
    {
        "name": "Telecom Churn",
        "subtitle": "Retention Modeling",
        "year": 2026,
        "category": "Machine Learning",
        "tools": ["CatBoost", "LightGBM", "Classification"],
        "signal": "0.93 ROC-AUC",
        "score": 97,
        "business": 92,
        "technical": 94,
        "visual": 78,
        "summary": "High-risk customer segments translated into retention actions.",
    },
    {
        "name": "Spotify",
        "subtitle": "Listening Behavior",
        "year": 2026,
        "category": "Behavioral Analytics",
        "tools": ["Python", "Pandas", "Time Analysis"],
        "signal": "38,977 rows",
        "score": 91,
        "business": 76,
        "technical": 85,
        "visual": 96,
        "summary": "Core taste versus life-stage behavior across multiple years.",
    },
    {
        "name": "Taxi Demand",
        "subtitle": "Time-Series Forecasting",
        "year": 2025,
        "category": "Forecasting",
        "tools": ["XGBoost", "Feature Engineering", "Time Series"],
        "signal": "38.95 RMSE",
        "score": 87,
        "business": 88,
        "technical": 89,
        "visual": 75,
        "summary": "Hourly demand forecasts for operational capacity planning.",
    },
    {
        "name": "Age Estimation",
        "subtitle": "Computer Vision",
        "year": 2026,
        "category": "Deep Learning",
        "tools": ["TensorFlow", "Keras", "CNN"],
        "signal": "~7.6 MAE",
        "score": 84,
        "business": 72,
        "technical": 96,
        "visual": 83,
        "summary": "Image-based age estimation evaluated for retail use.",
    },
    {
        "name": "Oil Well Risk",
        "subtitle": "Profit Simulation",
        "year": 2025,
        "category": "Decision Science",
        "tools": ["Regression", "Bootstrapping", "Risk"],
        "signal": "$4.41M mean",
        "score": 89,
        "business": 95,
        "technical": 88,
        "visual": 79,
        "summary": "Expected profit balanced against downside risk.",
    },
    {
        "name": "Gold Recovery",
        "subtitle": "Process Modeling",
        "year": 2025,
        "category": "Machine Learning",
        "tools": ["Regression", "sMAPE", "Model Evaluation"],
        "signal": "5.94 sMAPE",
        "score": 82,
        "business": 80,
        "technical": 90,
        "visual": 68,
        "summary": "Multi-stage recovery performance modeled with a custom metric.",
    },
    {
        "name": "Megaline",
        "subtitle": "Plan Recommendation",
        "year": 2025,
        "category": "Machine Learning",
        "tools": ["Scikit-learn", "Classification"],
        "signal": "0.733 accuracy",
        "score": 76,
        "business": 78,
        "technical": 77,
        "visual": 65,
        "summary": "Customer behavior used to recommend the right mobile plan.",
    },
]

PROJECT_DF = pd.DataFrame(PROJECTS)

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

BEATS_PRODUCTS = pd.DataFrame(
    {
        "Product": ["Studio Pro", "Solo 4"],
        "Reviews": [199, 300],
        "Rating": [4.51, 4.34],
        "Low-rating rate": [1.0, 11.3],
    }
)

BEATS_POSITIVE = pd.DataFrame(
    {"Theme": ["Sound", "Quality", "Comfort", "Value", "Battery"], "Share": [44, 33, 21, 18, 17]}
)

BEATS_RISKS = pd.DataFrame(
    {"Theme": ["Durability", "Battery", "Connectivity", "Sound", "Comfort"], "Share": [38.9, 25.0, 25.0, 25.0, 16.7]}
)


def polish(fig, height=390):
    fig.update_layout(
        height=height,
        margin=dict(l=12, r=18, t=50, b=16),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="rgba(255,255,255,.78)"),
        title_font=dict(size=17, color="white"),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(gridcolor="rgba(255,255,255,.07)", zeroline=False),
        yaxis=dict(gridcolor="rgba(255,255,255,.07)", zeroline=False),
    )
    return fig


def horizontal_bar(df, label, value, title):
    data = df.sort_values(value)
    bar_colors = [COLORS[index % len(COLORS)] for index in range(len(data))]
    fig = px.bar(data, x=value, y=label, orientation="h", text=value, title=title)
    fig.update_traces(marker=dict(color=bar_colors), textposition="outside", cliponaxis=False)
    return polish(fig)


def project_radar(project):
    labels = ["Business", "Technical", "Visual", "Overall"]
    values = [project["business"], project["technical"], project["visual"], project["score"]]
    fig = go.Figure(
        go.Scatterpolar(
            r=values + [values[0]],
            theta=labels + [labels[0]],
            fill="toself",
            line=dict(color=CYAN, width=3),
            fillcolor="rgba(125,249,255,.16)",
            hovertemplate="%{theta}: %{r}<extra></extra>",
        )
    )
    fig.update_layout(
        title=dict(text="Project strengths", x=0.02, xanchor="left"),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(range=[0, 100], showticklabels=False, gridcolor="rgba(255,255,255,.12)"),
            angularaxis=dict(gridcolor="rgba(255,255,255,.12)"),
        ),
        showlegend=False,
    )
    return polish(fig, 330)


def asset_path(*names):
    for name in names:
        for folder in (ASSET_DIR, BASE_DIR):
            candidate = folder / name
            if candidate.exists():
                return candidate
    return None


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Data science · product thinking · human behavior</div>
        <div class="hero-title">Gracie<br><span class="gradient-text">Schmidt</span></div>
        <div class="hero-copy">I find the signal, connect it to the customer, and turn it into a decision.</div>
        <div class="rainbow-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

link_cols = st.columns(4)
link_cols[0].link_button("LinkedIn ↗", LINKEDIN_URL, width="stretch")
link_cols[1].link_button("GitHub ↗", GITHUB_URL, width="stretch")
link_cols[2].link_button("Resume ↗", RESUME_URL, width="stretch")
link_cols[3].link_button("Email ✉", f"mailto:{EMAIL}", width="stretch")

home_tab, work_tab, beats_tab, spotify_tab, about_tab = st.tabs(
    ["✦ Home", "◌ Project Map", "◉ Beats Lab", "♫ Spotify Lab", "＋ About"]
)


with home_tab:
    st.markdown('<div class="section-label">Portfolio signals</div>', unsafe_allow_html=True)
    metrics = st.columns(4)
    metrics[0].metric("Projects", "8", "across 6 problem types")
    metrics[1].metric("Churn model", "0.93", "ROC-AUC")
    metrics[2].metric("Business", "10+ years", "operations + customers")
    metrics[3].metric("Data explored", "40K+", "behavioral records")

    left, right = st.columns([1, 1.05])
    with left:
        category_counts = PROJECT_DF.groupby("category").size().reset_index(name="Projects")
        fig = px.pie(
            category_counts,
            names="category",
            values="Projects",
            hole=.66,
            color_discrete_sequence=COLORS,
            title="Portfolio mix",
        )
        fig.update_traces(textinfo="label", hovertemplate="%{label}: %{value}<extra></extra>")
        st.plotly_chart(polish(fig, 390), width="stretch", key="home_portfolio_mix")
    with right:
        selected_name = st.selectbox("Explore a project", PROJECT_DF["name"].tolist(), index=0)
        selected = next(p for p in PROJECTS if p["name"] == selected_name)
        st.plotly_chart(project_radar(selected), width="stretch", key="home_project_radar")
        st.caption(f"{selected['subtitle']} · {selected['signal']}")

    st.markdown('<div class="section-label">Featured</div>', unsafe_allow_html=True)
    cards = st.columns(3)
    featured_names = ["Beats by Dre", "Telecom Churn", "Spotify"]
    for column, name, color in zip(cards, featured_names, [PINK, CYAN, LIME]):
        project = next(p for p in PROJECTS if p["name"] == name)
        with column:
            st.markdown(
                f"""
                <div class="mini-card" style="border-top:3px solid {color}">
                    <strong>{project['name']}</strong><br>
                    <span class="soft">{project['summary']}</span><br><br>
                    <span class="tag">{project['signal']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


with work_tab:
    st.markdown('<div class="section-label">Interactive project map</div>', unsafe_allow_html=True)
    st.subheader("Choose what matters to you")

    filters = st.columns([1.4, 1, 1])
    with filters[0]:
        chosen_categories = st.multiselect(
            "Focus area",
            sorted(PROJECT_DF["category"].unique()),
            default=sorted(PROJECT_DF["category"].unique()),
        )
    with filters[1]:
        chosen_year = st.radio("Year", ["All", 2026, 2025], horizontal=True)
    with filters[2]:
        search = st.text_input("Search", placeholder="NLP, risk, customer...")

    filtered = PROJECT_DF[PROJECT_DF["category"].isin(chosen_categories)].copy()
    if chosen_year != "All":
        filtered = filtered[filtered["year"] == chosen_year]
    if search.strip():
        mask = filtered.apply(lambda row: search.lower() in " ".join(map(str, row.values)).lower(), axis=1)
        filtered = filtered[mask]

    fig = px.scatter(
        filtered,
        x="technical",
        y="business",
        size="score",
        color="category",
        text="name",
        hover_data={"subtitle": True, "signal": True, "visual": True, "score": False},
        range_x=[60, 100],
        range_y=[60, 100],
        color_discrete_sequence=COLORS,
        title=f"{len(filtered)} projects · technical depth vs. business relevance",
    )
    fig.update_traces(textposition="top center", marker=dict(line=dict(width=1, color="rgba(255,255,255,.5)")))
    st.plotly_chart(polish(fig, 500), width="stretch", key="project_map_scatter")

    if not filtered.empty:
        detail_name = st.selectbox("Open a project", filtered["name"].tolist())
        detail = next(p for p in PROJECTS if p["name"] == detail_name)
        with st.container(border=True):
            info, chart = st.columns([1.15, 1])
            with info:
                st.subheader(f"{detail['name']} · {detail['subtitle']}")
                st.metric("Key signal", detail["signal"])
                st.write(detail["summary"])
                st.markdown("".join(f'<span class="tag">{tool}</span>' for tool in detail["tools"]), unsafe_allow_html=True)
            with chart:
                st.plotly_chart(project_radar(detail), width="stretch", key="project_map_radar")
    else:
        st.info("No projects match those filters yet.")

    st.link_button("Browse the GitHub repositories ↗", GITHUB_REPOS_URL)


with beats_tab:
    st.markdown('<div class="section-label">Product strategy case study</div>', unsafe_allow_html=True)
    st.subheader("What earns trust—and what breaks it?")

    beats_metrics = st.columns(4)
    beats_metrics[0].metric("Reviews", "1,300")
    beats_metrics[1].metric("Brands", "8")
    beats_metrics[2].metric("Beats reviews", "499")
    beats_metrics[3].metric("Positive", "432")

    view = st.radio("Explore", ["Loyalty drivers", "Trust breakers", "Launch path", "Product comparison"], horizontal=True)

    if view == "Product comparison":
        product = st.selectbox("Product", BEATS_PRODUCTS["Product"].tolist())
        row = BEATS_PRODUCTS[BEATS_PRODUCTS["Product"] == product].iloc[0]
        product_metrics = st.columns(3)
        product_metrics[0].metric("Reviews", int(row["Reviews"]))
        product_metrics[1].metric("Rating", f"{row['Rating']:.2f} ★")
        product_metrics[2].metric("Low ratings", f"{row['Low-rating rate']:.1f}%")

        compare = BEATS_PRODUCTS.melt(
            id_vars="Product",
            value_vars=["Rating", "Low-rating rate"],
            var_name="Measure",
            value_name="Value",
        )
        fig = px.bar(
            compare,
            x="Product",
            y="Value",
            color="Measure",
            barmode="group",
            text_auto=".2f",
            color_discrete_sequence=[CYAN, PINK],
            title="Studio Pro is the anchor; Solo 4 holds the risk",
        )
        st.plotly_chart(polish(fig), width="stretch", key="beats_product_comparison")
    elif view == "Loyalty drivers":
        st.plotly_chart(
            horizontal_bar(BEATS_POSITIVE, "Theme", "Share", "What positive reviewers reward (%)"),
            width="stretch",
            key="beats_loyalty_drivers",
        )
    elif view == "Trust breakers":
        st.plotly_chart(
            horizontal_bar(BEATS_RISKS, "Theme", "Share", "Signals inside low-rated reviews (%)"),
            width="stretch",
            key="beats_trust_breakers",
        )
    else:
        stage_data = pd.DataFrame(
            {
                "Stage": ["1 Stabilize", "2 Position", "3 Concept-test", "4 Business case"],
                "Gate": ["Solo 4 risk", "Studio Pro anchor", "Comfort-first concept", "Intent + economics"],
                "Progress": [100, 78, 55, 32],
            }
        )
        fig = px.bar(
            stage_data,
            x="Progress",
            y="Stage",
            orientation="h",
            text="Gate",
            color="Stage",
            color_discrete_sequence=COLORS,
            title="Recommended launch decision path",
        )
        fig.update_traces(textposition="inside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(polish(fig), width="stretch", key="beats_launch_path")

    beats_pdf = asset_path("beats_analysis.pdf", "Beats by Dre Headphones Analysis & Launch Recommendation.pdf")
    if beats_pdf:
        st.download_button(
            "Download the complete Beats case study",
            beats_pdf.read_bytes(),
            file_name="Gracie_Schmidt_Beats_Analysis.pdf",
            mime="application/pdf",
        )


with spotify_tab:
    st.markdown('<div class="section-label">Personal data · professional analysis</div>', unsafe_allow_html=True)
    st.subheader("How does music shift with life?")

    spotify_metrics = st.columns(3)
    spotify_metrics[0].metric("Initial rows", "39,252")
    spotify_metrics[1].metric("Cleaned rows", "38,977")
    spotify_metrics[2].metric("Top artist", "ODESZA", "3,482 plays")

    controls = st.columns([1, 1, 1])
    with controls[0]:
        scope = st.radio("Scope", ["Overall", "By year"], horizontal=True)
    with controls[1]:
        chart_type = st.radio("View", ["Bars", "Share"], horizontal=True)
    with controls[2]:
        top_n = st.slider("Top artists", 5, 10, 8)

    if scope == "Overall":
        spotify_df = SPOTIFY_OVERALL.head(top_n)
        spotify_title = "Top artists across the cleaned history"
    else:
        year = st.select_slider("Year", options=list(SPOTIFY_BY_YEAR), value="2025")
        spotify_df = SPOTIFY_BY_YEAR[year].head(top_n)
        spotify_title = f"Top artists in {year}"

    if chart_type == "Bars":
        st.plotly_chart(
            horizontal_bar(spotify_df, "Artist", "Plays", spotify_title),
            width="stretch",
            key="spotify_artist_bars",
        )
    else:
        fig = px.pie(
            spotify_df,
            names="Artist",
            values="Plays",
            hole=.58,
            color_discrete_sequence=COLORS,
            title=spotify_title,
        )
        fig.update_traces(textinfo="label+percent", hovertemplate="%{label}: %{value} plays<extra></extra>")
        st.plotly_chart(polish(fig, 470), width="stretch", key="spotify_artist_share")

    spotify_pdf = asset_path("spotify_analysis.pdf", "Spotify.pdf")
    if spotify_pdf:
        st.download_button(
            "Download the current Spotify analysis",
            spotify_pdf.read_bytes(),
            file_name="Gracie_Schmidt_Spotify_Analysis.pdf",
            mime="application/pdf",
        )


with about_tab:
    st.markdown('<div class="section-label">Background</div>', unsafe_allow_html=True)
    st.subheader("Business instinct, backed by data")

    left, right = st.columns([1.05, 1])
    with left:
        skills = pd.DataFrame(
            {
                "Skill": ["Python + SQL", "ML", "Customer insight", "Experimentation", "Visualization", "Business strategy"],
                "Depth": [90, 88, 96, 83, 92, 97],
            }
        )
        st.plotly_chart(
            horizontal_bar(skills, "Skill", "Depth", "How I bring a problem together"),
            width="stretch",
            key="about_skill_depth",
        )
    with right:
        st.markdown("### About Moi")
        st.markdown(
            '<span class="tag">Python</span><span class="tag">SQL</span><span class="tag">Machine Learning</span>'
            '<span class="tag">NLP</span><span class="tag">Forecasting</span><span class="tag">Computer Vision</span>'
            '<span class="tag">Tableau</span><span class="tag">Streamlit</span>',
            unsafe_allow_html=True,
        )

        with st.expander("My path"):
            st.write("""My path into data science has not been traditional, but that is also one of the things I value most about it. It has given me a strong foundation in tenacity, resilience, empathy, logic, and adaptability. I’m naturally curious, resourceful, and someone who tends to ask a lot of “why?” questions. I take feedback well, pivot quickly, and stay calm when things get complicated.

Before moving into data science, I built experience in environments that required focus, responsibility, and clear thinking. From studying human anatomy in the Washington State University cadaver lab to running my own business, those experiences taught me how to observe carefully, solve problems, communicate clearly, and perform under pressure.""")
            st.caption("Certified Data Scientist · Machine Learning & Applied Analytics · Associate of Arts with coursework in graphic design, psychology, and sociology · Human anatomy study in the Washington State University cadaver lab")

        with st.expander("Business + technical experience"):
            st.write("""Today, I combine technical data science skills with more than 10 years of experience in business operations, customer behavior, marketing, retention, and revenue optimization. My work includes machine learning, exploratory data analysis, predictive modeling, experimentation, and business strategy, with projects spanning classification, regression, time-series forecasting, computer vision, NLP, and business analytics.

I work with Python, SQL, scikit-learn, TensorFlow/Keras, CatBoost, LightGBM, XGBoost, Tableau, Matplotlib, and other analytical tools. Just as importantly, I know how to take technical findings and turn them into clear, useful recommendations for the people making decisions.""")
            st.caption("Beats by Dre consumer insights externship · Founder and business owner · Spa management, operations, and customer experience · Always learning and building 😊")

        with st.expander("How I think about data"):
            st.write("""I see data as more than numbers. It is a way to understand people, uncover patterns, identify opportunities, solve problems, and make better decisions. I’m especially interested in work where data can improve products, customer experiences, business performance, and real-world outcomes.

I bring a combination of business ownership, technical training, customer insight, creativity, and strong communication and presentation skills that does not fit neatly into a single job title. When I encounter something I do not know yet, I am resourceful enough to learn quickly, ask the right questions, and figure it out.""")

        st.markdown("### Outside the notebook")
        st.markdown(
            """
            - ❤️ Mom of four with a pretty rad family
            - 🏂 Most at home in the mountains: snowboarding, hiking, camping, and backpacking
            - 🏄 Surfing, waves, and any excuse to be near the water 🌊
            - 📷 Photography, music, and creative projects
            - 😊 Curious, adaptable, and comfortable balancing structure with a little bit of chaos
            """
        )

    st.markdown("### Let’s build something useful")
    contact_cols = st.columns(3)
    contact_cols[0].link_button("LinkedIn ↗", LINKEDIN_URL, width="stretch")
    contact_cols[1].link_button("GitHub ↗", GITHUB_URL, width="stretch")
    contact_cols[2].link_button("Email ✉", f"mailto:{EMAIL}", width="stretch")


st.markdown("<div class='footer'>Built with Streamlit · Portfolio content © Gracie Schmidt</div>", unsafe_allow_html=True)
