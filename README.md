# Gracie Schmidt — Interactive Data Science Portfolio

I designed this portfolio to bring my projects together in one place and make the thinking behind the work easy to explore. The common thread across the projects is translating technical analysis into a decision that matters for a customer, product, or business.

## What you can explore

- **Project Map** — compare projects by technical depth and business relevance, then filter by year or focus area.
- **Beats Lab** — explore the product comparison, loyalty drivers, trust breakers, and staged launch recommendation from my consumer-insights analysis.
- **Spotify Lab** — interact with multi-year listening patterns and compare overall behavior with individual years.
- **About** — see the technical and business experience I bring to data science.

## Design choices

I wanted this to feel professional without looking like a generic corporate dashboard. I chose a black background with neon/pastel accents to reflect my creative side, reduced the amount of text, and used interactive visuals to let people explore the work for themselves.

The dashboard intentionally shows both technical performance and business relevance. A strong model matters, but so does understanding the customer behavior behind it and communicating what should happen next.

## Technical structure

The application is written in Python with:

- **Streamlit** for the interface, navigation, filters, and interactive controls
- **Pandas** for structuring the project and analysis data
- **Plotly** for interactive charts
- **Custom CSS** for the visual design and responsive layout

The app is organized around:

1. project metadata stored as structured Python dictionaries and DataFrames;
2. reusable chart functions that apply a consistent visual theme;
3. Streamlit widgets that filter data and change the displayed visual;
4. separate tabs for the overall portfolio and deeper case-study exploration.

## Run locally

Clone this repository, install the dependencies, and start Streamlit:

```bash
git clone https://github.com/GracieHannah/Portfolio.git
cd Portfolio
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

## Featured analyses

### Beats by Dre

Consumer-review analysis across 1,300 cleaned headphone reviews and eight brands. The project moves from review themes and product risk to a staged launch recommendation.

### Spotify listening behavior

Longitudinal analysis of 38,977 cleaned streaming-history records, including overall and year-level artist patterns.

### Additional work

The portfolio also highlights telecom churn modeling, taxi-demand forecasting, computer-vision age estimation, oil-well profit and risk analysis, gold-recovery modeling, and mobile-plan recommendation.

---

Designed and maintained by **Gracie Schmidt**. Built with Python, Streamlit, Pandas, and Plotly 🤙
