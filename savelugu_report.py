import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import base64
import plotly.graph_objects as go
import networkx as nx

st.set_page_config(
    page_title="Savelugu Municipal Report",
    page_icon="./Images/cropped2.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Report on Savelugu Municipal Demographics and Development Overview")

def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
# Define your logo and animation paths
logo_path = "./Images/combo.gif"
cropped = "./Images/coat.png"
animation_home_path = "./Animations/home.json"
animation_employee_path = "./Animations/employee.json"
image_path = "./Images/login.png"
logo_base64 = load_image(logo_path)
cropped_logo =load_image(cropped)
logo_base64 = load_image(logo_path)
# Define a function to create a capacity-building training plan

# Sidebar with custom logo and navigation menu
with st.sidebar:
    # Adding the logo with custom styling
    st.markdown(
    f"""
    <style>
    @keyframes glow {{
        0% {{ box-shadow: 0 0 5px #15ffff; }}
        100% {{ box-shadow: 0 0 15px #15ffff; }}
    }}
    .custom-box {{
        background: linear-gradient(135deg, #2f2f2f, #1c1c1c);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        #animation: glow 2s ease-in-out infinite alternate;
        color: #ffffff;
        box-shadow: 0 0 10px rgba(21,255,255,0.3);
    }}
    .custom-box h2 {{
        margin: 10px 0;
        font-size: 20px;
        color: #15ffff;
    }}
    .custom-box p {{
        font-size: 14px;
        margin: 0;
    }}
    </style>

    <div class="custom-box">
        <img src="data:image/png;base64,{cropped_logo}" alt="Logo" style="width: 100px; margin-top: 10px;" />
    </div>
    """,
    unsafe_allow_html=True
)



def create_card(title, value, image_path=None):
    image_base64 = load_image(image_path) if image_path else ""
    style = """
    <style>
        .card-container {
            display: flex;
            justify-content: center;
        }
        .glow {
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px #00ff00
            background: #001f3f;
            animation: glow 1.5s infinite alternate;
            width: 300px;
            height: 150px;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            text-align: center;
        }
        @keyframes glow {
            from {
                box-shadow: 0 0 10px #28a745;
            }
            to {
                box-shadow: 0 0 20px #28a745;
            }
        }
        .card-image {
            width: 50px;
            height: 50px;
            margin-left: 10px;
        }
        .card-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
    </style>
    """
    card_html = f"""
    <div class="card-container">
        <div class="glow">
            <div class="card-content">
                <h2 class="card-title" style="font-size: 16px;">{title}</h2>
                <p style="font-size: 16px;">{value}</p>
            </div>
            {"<img src='data:image/png;base64," + image_base64 + "' class='card-image'/>" if image_base64 else ""}
        </div>
    </div>
    """
    st.markdown(style, unsafe_allow_html=True)
    st.markdown(card_html, unsafe_allow_html=True)



# 1. Introduction
st.markdown("### 1. Introduction")

st.markdown("""
<div style='text-align: justify;'>
Savelugu Municipal is located in the Northern Region of Ghana. 
The municipality covers a total land area of 1,550 square kilometers and had a population 
of 122,888 according to the 2021 Census. This report presents the demographic characteristics, 
population structure, and development indicators of Savelugu Municipal.
</div>
""", unsafe_allow_html=True)


# 2. Geographic & Administrative Context
st.markdown("### 2. Geographic & Administrative Context")
st.write("""
Savelugu Municipal lies just north‑west of Tamale, sharing boundaries with Nanton (south‑east), Tolon (west), Karaga (east) and West Mamprusi (north). Created as a separate municipality in 2018, it forms part of Ghana’s Guinea Savannah ecological zone. The terrain is largely flat to gently undulating with vast stretches suited to rain‑fed agriculture as well as seasonal grazing.
""")

st.subheader("📍 Map of Savelugu in Ghana")

# Coordinates of Savelugu
savelugu_coords = {
    "lat": 9.6241,
    "lon": -0.8306
}

# Create map view
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=savelugu_coords["lat"],
        longitude=savelugu_coords["lon"],
        zoom=7,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=[savelugu_coords],
            get_position='[lon, lat]',
            get_color='[255, 0, 0, 160]',
            get_radius=10000,
        )
    ],
))

st.markdown("### 3. Key Development Metrics")

st.markdown("""
<style>
.card-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: nowrap;
    gap: 20px;
    margin-top: 10px;
}
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    flex: 1;
    min-width: 200px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    text-align: center;
    color: white;
    font-family: "Segoe UI", sans-serif;
}
.card-title {
    font-size: 14px;
    color: #bbbbbb;
}
.card-value {
    font-size: 28px;
    font-weight: bold;
    color: #f1f1f1;
}
</style>

<div class="card-container">
  <div class="card">
    <div class="card-title">Total Population</div>
    <div class="card-value">122,888</div>
  </div>
  <div class="card">
    <div class="card-title">Land Area</div>
    <div class="card-value">1,550 km²</div>
  </div>
  <div class="card">
    <div class="card-title">Population Density</div>
    <div class="card-value">79.27/km²</div>
  </div>
  <div class="card">
    <div class="card-title">Annual Growth Rate</div>
    <div class="card-value">2.6%</div>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown("### 📊 Demographic & Socioeconomic Snapshot")

st.markdown("""
<style>
.card-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
}
.card {
    background-color: #1e1e1e;
    color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    font-family: "Segoe UI", sans-serif;
}
.card-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #1E90FF;
}
.card-body {
    font-size: 15px;
    line-height: 1.6;
    text-align: justify;
}
</style>

<div class="card-grid">

  <div class="card">
    <div class="card-title">4. Demographic Profile</div>
    <div class="card-body">
      • <b>Rapid population growth</b>: From 92,717 in 2010 to 122,888 in 2021 (≈ 2.6% p.a.)<br>
      • <b>Youthful population</b>: 54% are under 20 years<br>
      • <b>Slightly more females</b> (50.9%) — sex ratio 96.6<br>
      • <b>Urbanisation</b>: 63%, driven by Savelugu township expansion
    </div>
  </div>

  <div class="card">
    <div class="card-title">5. Households & Housing</div>
    <div class="card-body">
      • <b>Avg. household size</b>: 5.2 vs 3.6 national<br>
      • <b>Housing deprivation</b>: 62.6% in poor housing<br>
      • <b>Toilets</b>: 94.3% lack improved toilets<br>
      • <b>Urban infrastructure</b>: Slightly better electricity & water access
    </div>
  </div>

  <div class="card">
    <div class="card-title">6. Education & Literacy</div>
    <div class="card-body">
      • <b>60,689 persons aged 6+</b> cannot read or write<br>
      • <b>57% of the illiterate are female</b><br>
      • 5th highest illiteracy count in Northern Region
    </div>
  </div>

  <div class="card">
    <div class="card-title">7. Economic Activity</div>
    <div class="card-body">
      • <b>Agriculture</b> employs ≈70% (maize, rice, soy, livestock)<br>
      • <b>Trade & transport</b> growing along the N10 corridor<br>
      • <b>Youth unemployment</b> is high (16–18%)
    </div>
  </div>

</div>
""", unsafe_allow_html=True)


st.title("📄 Multidimensional Poverty Fact Sheet - Savelugu Municipal")

st.markdown("""
This fact sheet summarizes the **multidimensional poverty statistics** for **Savelugu Municipal**,  
based on the **2021 Population and Housing Census (PHC)**.  

It highlights:
- **Incidence** (*Who is poor?*)
- **Intensity** (*How poor are the poor?*)
- **Deprivation in 13 indicators** (*What are people in the district lacking?*)
- **Contribution to poverty** (*How is poverty experienced?*)

🔗 For more on multidimensional poverty and the methodology, visit:  
[https://statsghana.gov.gh/MPI-Primer.pdf](https://statsghana.gov.gh/MPI-Primer.pdf)
""")

st.markdown("---")

st.subheader("📊 Key Statistics for Savelugu Municipal")

st.markdown("""
- **41.1%** of the population live in **multidimensional poverty**.
- The **average intensity** of poverty is **45.5%**.
- Therefore, the **Multidimensional Poverty Index (MPI)** is estimated at **0.187**.
- **Ranking:**  
  - **221st out of 261** districts nationally  
  - **5th out of 16** districts in the **Northern Region**  
  *(A lower rank means less poverty)*

""")

st.subheader("🚫 Areas of Highest Deprivation")

st.markdown("""
- **Improved toilet facilities:** **94.3%** of the population lack access  
- **Housing (material quality):** **62.6%** deprived  
- **Health insurance coverage:** **59.3%** of people are uninsured

📌 In **9 out of 13 indicators**, Savelugu Municipal had **higher deprivation** than the national averages.
""")



# 8. Multidimensional Poverty Index (MPI)
st.markdown("### 8. Multidimensional Poverty Index (MPI)")

# Add card-style formatting via HTML & CSS
st.markdown("""
    <style>
        .metric-card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }
        .metric-label {
            font-size: 14px;
            color: #87CEFA; /* Light Blue */
            margin-bottom: 8px;
        }
        .metric-value {
            font-size: 28px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">MPI Value</div>
            <div class="metric-value">0.187</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Incidence</div>
            <div class="metric-value">41.1%</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Intensity</div>
            <div class="metric-value">45.5%</div>
        </div>
    """, unsafe_allow_html=True)


st.subheader("🌡️ Heatmap of MPI by Sub-District (Demo)")

# Sample poverty data by zone
poverty_data = pd.DataFrame({
    "Zone": ["Savelugu Central", "Tunaayili", "Kadia", "Yong", "Gushie", "Diare"],
    "Latitude": [9.6241, 9.7001, 9.5202, 9.6500, 9.4800, 9.7400],
    "Longitude": [-0.8306, -0.8500, -0.8000, -0.8100, -0.7800, -0.8700],
    "MPI": [0.19, 0.22, 0.17, 0.15, 0.25, 0.18]
})

# Show as map with color intensity
layer = pdk.Layer(
    "HeatmapLayer",
    data=poverty_data,
    get_position='[Longitude, Latitude]',
    get_weight="MPI",
    radius=30000,
    aggregation=pdk.types.String("MEAN")
)

view_state = pdk.ViewState(
    latitude=9.6,
    longitude=-0.82,
    zoom=9,
    pitch=30,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))


st.markdown("### Key Deprivation Indicators")

# CSS Styling for Cards
st.markdown("""
    <style>
        .info-card {
            background-color: #1e1e1e;
            padding: 18px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            font-size: 14px;
        }
        .info-card-title {
            font-weight: bold;
            color: #87CEFA;  /* Light Blue */
            margin-bottom: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# Create 2 rows of 2 cards each
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

with row1_col1:
    st.markdown("""
        <div class="info-card">
            <div class="info-card-title">Living Standards</div>
            62.6% deprived (housing material)
        </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
        <div class="info-card">
            <div class="info-card-title">Sanitation</div>
            94.3% lack improved toilets
        </div>
    """, unsafe_allow_html=True)

with row2_col1:
    st.markdown("""
        <div class="info-card">
            <div class="info-card-title">Health Insurance</div>
            59.3% not insured
        </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
        <div class="info-card">
            <div class="info-card-title">Education</div>
            Over 40% adults have no formal schooling
        </div>
    """, unsafe_allow_html=True)



# 9. Population Structure
st.markdown("### 9. Population Structure")

st.subheader("9.1 Gender Distribution")
gender_df = pd.DataFrame({
    "Gender": ["Males", "Females"],
    "Number of Persons": [60390, 62498]
})
st.dataframe(gender_df, use_container_width=True)

st.subheader("9.2 Age Group Distribution")
age_group_df = pd.DataFrame({
    "Age Group": ["0-14 years", "15-64 years", "65+ years"],
    "Number of Persons": [53963, 64484, 4441]
})
st.dataframe(age_group_df, use_container_width=True)

st.subheader("9.3 Age Distribution by Gender")
age_gender_df = pd.DataFrame({
    "Age Group": ["80+ years", "70-79", "60-69", "50-59", "40-49", 
                  "30-39", "20-29", "10-19", "0-9"],
    "Males": [503, 917, 1453, 2333, 4661, 6747, 9767, 13756, 20253],
    "Females": [788, 1179, 1513, 2361, 5164, 8434, 11197, 12076, 19786]
})
st.dataframe(age_gender_df, use_container_width=True)

# 10. Urbanization
st.markdown("### 10. Urbanization")
urban_df = pd.DataFrame({
    "Category": ["Rural", "Urban"],
    "Number of Persons": [45567, 77321]
})
st.dataframe(urban_df, use_container_width=True)

# Urbanization Pie Chart
st.subheader("🧭 Urban vs Rural Population Share")
urban_pie = px.pie(
    urban_df,
    names="Category",
    values="Number of Persons",
    title="Urbanization Distribution",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0.4
)
st.plotly_chart(urban_pie, use_container_width=True)


# 11. Literacy Levels
st.markdown("### 11. Literacy (Aged 11+)")
literacy_df = pd.DataFrame({
    "Literacy Status": ["Literate", "Illiterate"],
    "Number of Persons": [31961, 47451]
})
st.dataframe(literacy_df, use_container_width=True)

# 12. Ethnic Composition
st.markdown("### 12. Ethnic Composition")
ethnic_df = pd.DataFrame({
    "Ethnic Group": [
        "Akan", "Ga-Dangme", "Ewe", "Guan", "Gurma", 
        "Mole-Dagbani", "Grusi", "Mandé", "Other Ethnic Groups"
    ],
    "Number of Persons": [1365, 65, 799, 207, 565, 114076, 1102, 3330, 621]
})
st.dataframe(ethnic_df, use_container_width=True)

# Ethnic Group Pie Chart
st.subheader("🌍 Ethnic Composition of Savelugu Municipal")
ethnic_pie = px.pie(
    ethnic_df,
    names="Ethnic Group",
    values="Number of Persons",
    title="Ethnic Group Share",
    color_discrete_sequence=px.colors.qualitative.Set3,
    hole =0.4
)
st.plotly_chart(ethnic_pie, use_container_width=True)


# 13. Population Projections
st.markdown("### 13. Population Projections (2021–2032)")
years = list(range(2021, 2033))
total_pop = [122888, 127613, 132413, 137243, 142091, 146290, 150984, 155697, 160422, 165152, 169902, 174667]
male_pop =  [60390,  63051,  65422,  67804,  70192,  72256,  74561,  76874,  79189,  81505,  83828,  86157]
female_pop = [62498, 64562, 66991, 69439, 71899, 74034, 76423, 78823, 81233, 83647, 86074, 88510]

proj_df = pd.DataFrame({
    "Year": [str(y) for y in years],
    "Total Population": total_pop,
    "Male Population": male_pop,
    "Female Population": female_pop
})
# Create frames for each year
frames = []
for i in range(len(proj_df)):
    year = proj_df.loc[i, "Year"]
    frame_data = [
        go.Scatter(x=proj_df["Year"][:i+1], y=proj_df["Total Population"][:i+1], mode='lines+markers', name="Total Population"),
        go.Scatter(x=proj_df["Year"][:i+1], y=proj_df["Male Population"][:i+1], mode='lines+markers', name="Male Population"),
        go.Scatter(x=proj_df["Year"][:i+1], y=proj_df["Female Population"][:i+1], mode='lines+markers', name="Female Population"),
    ]
    frames.append(go.Frame(data=frame_data, name=year))

# Initial figure
fig_proj = go.Figure(
    data=[
        go.Scatter(x=[proj_df["Year"][0]], y=[proj_df["Total Population"][0]], mode='lines+markers', name="Total Population"),
        go.Scatter(x=[proj_df["Year"][0]], y=[proj_df["Male Population"][0]], mode='lines+markers', name="Male Population"),
        go.Scatter(x=[proj_df["Year"][0]], y=[proj_df["Female Population"][0]], mode='lines+markers', name="Female Population"),
    ],
    layout=go.Layout(
        title="Population Projections (2021–2032)",
        xaxis=dict(tickmode='linear'),
        yaxis=dict(title="Population"),
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }],
        sliders=[{
            "active": 0,
            "steps": [
                {
                    "method": "animate",
                    "label": str(year),
                    "args": [[str(year)], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate"}]
                }
                for year in proj_df["Year"]
            ]
        }]
    ),
    frames=frames
)

# Display in Streamlit
st.plotly_chart(fig_proj, use_container_width=True)

with st.expander("📋 View Raw Projection Table"):
    st.dataframe(proj_df, use_container_width=True)

st.markdown("""
<style>
.dark-card {
    background-color: #1e1e1e;
    padding: 1.2rem;
    margin-bottom: 1rem;
    border-left: 6px solid;
    border-radius: 10px;
    font-size: 1.05rem;
    color: #f1f1f1;
    box-shadow: 0 0 10px rgba(0, 150, 255, 0.2);
}

.dark-info { border-color: #00bfff; }
.dark-success { border-color: #28a745; }
.dark-warning { border-color: #ffc107; }
.dark-error { border-color: #dc3545; }

.dark-card span.emoji {
    font-size: 1.3rem;
    margin-right: 0.4rem;
}
</style>
""", unsafe_allow_html=True)



st.markdown("### 14. Planning Implications")

st.markdown("""
<div class="dark-card dark-info">
    <span class="emoji">📘</span> <strong>Expand education, health, and job opportunities</strong> for the growing youth population
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dark-card dark-success">
    <span class="emoji">🚽</span> <strong>Address water, sanitation, and housing material</strong> deficits
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dark-card dark-warning">
    <span class="emoji">👧</span> <strong>Promote adult literacy and girl-child school retention</strong> programs
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dark-card dark-error">
    <span class="emoji">🎯</span> <strong>Target MPI indicators</strong> for focused and measurable poverty reduction
</div>
""", unsafe_allow_html=True)




st.subheader("📊 Poverty vs Key Infrastructure Indicators")

# Sample zone-level data
infra_data = pd.DataFrame({
    "Zone": ["Savelugu Central", "Tunaayili", "Kadia", "Yong", "Gushie", "Diare"],
    "MPI": [0.19, 0.22, 0.17, 0.15, 0.25, 0.18],
    "Improved Toilets (%)": [15, 10, 20, 18, 8, 22],
    "Electricity Access (%)": [65, 45, 55, 60, 40, 70],
    "Literacy Rate (%)": [58, 42, 50, 55, 37, 62],
    "Health Insurance (%)": [45, 30, 35, 40, 25, 50]
})

# Melt dataframe for grouped bar chart
melted = infra_data.melt(id_vars=["Zone", "MPI"], var_name="Indicator", value_name="Percentage")

import altair as alt

chart = alt.Chart(melted).mark_bar().encode(
    x=alt.X("Zone:N", title="Zone"),
    y=alt.Y("Percentage:Q", title="Percentage"),
    color="Indicator:N",
    tooltip=["Zone", "Indicator", "Percentage"]
).properties(
    width=800,
    height=400,
    title="Infrastructure Access vs MPI by Zone"
)

st.altair_chart(chart, use_container_width=True)


st.subheader("🫧 Bubble Chart: MPI vs Improved Toilets")

bubble = alt.Chart(infra_data).mark_circle().encode(
    x="MPI:Q",
    y="Improved Toilets (%):Q",
    size="Electricity Access (%):Q",
    color="Zone:N",
    tooltip=["Zone", "MPI", "Improved Toilets (%)", "Electricity Access (%)"]
).properties(
    width=700,
    height=400
)

st.altair_chart(bubble, use_container_width=True)




# Load your data
df = pd.read_csv("communities.csv")  # Replace with actual path

# Bar Chart: Top 15 Communities by Total Population
top_communities = df.sort_values("Total_Population", ascending=False).head(15)
fig_pop = px.bar(top_communities, 
                 x="Community_Name", 
                 y="Total_Population", 
                 title="Top 15 Most Populous Communities in Savelugu",
                 labels={"Total_Population": "Population"},
                 color="Total_Population")

st.plotly_chart(fig_pop)



# --- CSS Animation for the Header ---
css_animation = """
    <style>
    @keyframes bump {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .bumping-text {
        display: inline-block;
        animation: bump 1s infinite;
        font-size: 42px;
        color: #15FFFF;
        text-align: center;
        width: 100%;
    }
    
    /* Glow effect for metric cards */
.metric-glow {
    padding: 1rem;
    margin: 0.5rem;
    border-radius: 12px;
    background: #111;
    box-shadow: 0 0 15px rgba(0, 153, 255, 0.6);
    transition: 0.3s ease-in-out;
}

.metric-glow:hover {
    box-shadow: 0 0 25px rgba(0, 153, 255, 1);
    transform: scale(1.02);
}

/* Center and style headings */
.bumping-text {
    color: #00ccff;
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 2rem;
}
    </style>
"""
st.markdown(css_animation, unsafe_allow_html=True)
st.markdown("<h1 class='bumping-text'>Savelugu Community Dashboard</h1>", unsafe_allow_html=True)

# --- Metrics ---
total_communities = df['Community_Name'].nunique()
total_population = df['Total_Population'].sum()
total_males = df['Male_Population'].sum()
total_females = df['Female_Population'].sum()
total_households = df['HouseHold'].sum()
head_male = df['Head_Male'].sum()
head_female = df['Head_Female'].sum()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Total Communities", total_communities)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Total Population", total_population)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Male Population", total_males)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Female Population", total_females)
    st.markdown('</div>', unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)
with col5:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Total Households", total_households)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Male Household Heads", head_male)
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    st.markdown('<div class="metric-glow">', unsafe_allow_html=True)
    st.metric("Female Household Heads", head_female)
    st.markdown('</div>', unsafe_allow_html=True)
# --- Optional: Show full dataset ---
with st.expander("📊 Show Raw Data"):
    st.dataframe(df)


# Compute totals across all communities
total_male = df['Male_Population'].sum()
total_female = df['Female_Population'].sum()

# Gender distribution pie chart
gender_df = pd.DataFrame({
    'Gender': ['Male', 'Female'],
    'Count': [total_male, total_female]
})

# Head of household by gender
head_male = df['Head_Male'].sum()
head_female = df['Head_Female'].sum()

household_head_df = pd.DataFrame({
    'Gender': ['Male Head', 'Female Head'],
    'Count': [head_male, head_female]
})

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color: #15FFFF;'>Gender Distribution</h3>", unsafe_allow_html=True)
    
    fig_gender_dist = px.pie(
        gender_df,
        values='Count',
        names='Gender',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    fig_gender_dist.update_traces(textposition='inside', textinfo='percent+label')
    fig_gender_dist.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=dict(showgrid=False))
    st.plotly_chart(fig_gender_dist)

with col2:
    st.markdown("<h3 style='color: #15FFFF;'>Household Head by Gender</h3>", unsafe_allow_html=True)
    
    fig_head_dist = px.pie(
        household_head_df,
        values='Count',
        names='Gender',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig_head_dist.update_traces(textposition='inside', textinfo='percent+label')
    fig_head_dist.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=dict(showgrid=False))
    st.plotly_chart(fig_head_dist)

st.divider()

# Sidebar Filter for Poverty Breakdown Charts
st.sidebar.markdown("### 📂 Filter Poverty Data")
selected_chart = st.sidebar.selectbox(
    "Select Poverty Breakdown:",
    (
        "By Sex of Head of Household",
        "By Household Size",
        "By Educational Level",
        "By Sector of Employment",
        "By Economic Sector"
    )
)

# Chart: Multidimensional Poverty Breakdown
if selected_chart == "By Sex of Head of Household":
    data = {
        "Sex of Head": ["Savelugu Municipal", "Female", "Male"],
        "Poverty Rate (%)": [41.1, 56.6, 37.7]
    }
    df = pd.DataFrame(data)
    title = "Multidimensional Poverty by Sex of Head of Household - Savelugu Municipal"
    y_col = "Sex of Head"

elif selected_chart == "By Household Size":
    data = {
        "Household Size": [
            "Savelugu Municipal",
            "One to four members",
            "Five to nine members",
            "Ten or more members"
        ],
        "Poverty Rate (%)": [41.1, 38.4, 40.7, 44.3]
    }
    df = pd.DataFrame(data)
    title = "Multidimensional Poverty by Household Size - Savelugu Municipal"
    y_col = "Household Size"

elif selected_chart == "By Educational Level":
    data = {
        "Education Level": [
            "Savelugu Municipal",
            "No education",
            "Basic",
            "Secondary",
            "Post secondary",
            "Tertiary",
            "Other"
        ],
        "Poverty Rate (%)": [41.1, 45.7, 30.9, 29.3, 22.7, 15.3, 16.7]
    }
    df = pd.DataFrame(data)
    title = "Multidimensional Poverty by Educational Level of Head of Household - Savelugu Municipal"
    y_col = "Education Level"

elif selected_chart == "By Sector of Employment":
    data = {
        "Sector of Employment": [
            "Savelugu Municipal",
            "Private Informal",
            "Private Formal",
            "Public",
            "Other",
            "Not Working"
        ],
        "Poverty Rate (%)": [41.1, 34.2, 18.8, 7.6, 3.6, 71.1]
    }
    df = pd.DataFrame(data)
    title = "Multidimensional Poverty by Sector of Employment of Head of Household - Savelugu Municipal"
    y_col = "Sector of Employment"

elif selected_chart == "By Economic Sector":
    data = {
        "Economic Sector": [
            "Savelugu Municipal",
            "Agriculture",
            "Industry",
            "Service"
        ],
        "Poverty Rate (%)": [41.1, 37.0, 17.9, 14.3]
    }
    df = pd.DataFrame(data)
    title = "Multidimensional Poverty by Economic Sector of Employment of Head of Household - Savelugu Municipal"
    y_col = "Economic Sector"

# Plotting the selected chart
fig = px.bar(
    df,
    y=y_col,
    x="Poverty Rate (%)",
    color=y_col,
    text="Poverty Rate (%)",
    orientation="h",
    title=title,
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(
    yaxis_title=None,
    xaxis_title="Poverty Rate (%)",
    showlegend=False,
    height=500
)

st.plotly_chart(fig, use_container_width=True)





# Data
funnel_data = pd.DataFrame({
    "Stage": ["Total Population", "Covered", "Not Covered"],
    "Count": [122756, 78728, 44028]
})

# Sort for funnel shape
funnel_data = funnel_data.sort_values(by="Count", ascending=False)

# Funnel Chart
fig_funnel = px.funnel(
    funnel_data,
    x="Count",
    y="Stage",
    title="📉 Health Insurance Coverage - Savelugu Municipal",
    color="Stage",
    color_discrete_sequence=px.colors.qualitative.Set3
)

st.plotly_chart(fig_funnel, use_container_width=True)



# --- DATA ---
data = [
    ["Total", "Rural", "Male", 22593],
    ["Total", "Rural", "Female", 22970],
    ["Total", "Urban", "Male", 37749],
    ["Total", "Urban", "Female", 39444],
    ["Not Covered", "Rural", "Male", 11701],
    ["Not Covered", "Rural", "Female", 10688],
    ["Not Covered", "Urban", "Male", 11511],
    ["Not Covered", "Urban", "Female", 10128],
    ["Covered", "Rural", "Male", 10892],
    ["Covered", "Rural", "Female", 12282],
    ["Covered", "Urban", "Male", 26238],
    ["Covered", "Urban", "Female", 29316],
]

df = pd.DataFrame(data, columns=["Coverage", "Area", "Gender", "Count"])

# --- SIDEBAR FILTERS ---
# Custom CSS for blue multiselects
st.markdown("""
    <style>
    section[data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] {
        background-color: #003366;
        color: white;
        border-radius: 5px;
        border: 1px solid #3399ff;
    }

    section[data-testid="stSidebar"] .stMultiSelect span[data-baseweb="tag"] {
        background-color: #3399ff;
        color: white;
        border-radius: 5px;
    }

    section[data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"]:hover {
        border-color: #66ccff;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR FILTERS ---
st.sidebar.title("🧭 Filter Data")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
area_filter = st.sidebar.multiselect("Select Area", options=df["Area"].unique(), default=df["Area"].unique())

# --- FILTERED DATA ---
filtered_df = df[df["Gender"].isin(gender_filter) & df["Area"].isin(area_filter)]

# --- MAIN TITLE ---
st.title("🏥 Health Insurance Coverage - Savelugu Municipal")

# --- FUNNEL CHART ---
st.subheader("🔻 Funnel Chart: Overall Health Insurance Coverage")
funnel_df = filtered_df[filtered_df["Coverage"] != "Total"].groupby("Coverage")["Count"].sum().reset_index()
funnel_df = funnel_df.sort_values(by="Count", ascending=False)

fig_funnel = px.funnel(
    funnel_df,
    y="Coverage",
    x="Count",
    title="Health Insurance Funnel (Filtered)",
    color="Coverage",
    color_discrete_sequence=px.colors.sequential.Burg
)
st.plotly_chart(fig_funnel, use_container_width=True)

# --- GROUPED BAR CHART ---
st.subheader("📊 Grouped Bar Chart: Area & Coverage by Gender")

fig_grouped = px.bar(
    filtered_df[filtered_df["Coverage"] != "Total"],
    x="Area",
    y="Count",
    color="Coverage",
    barmode="group",
    facet_col="Gender",
    title="Coverage Breakdown (Filtered)",
    text="Count"
)
st.plotly_chart(fig_grouped, use_container_width=True)

# --- STACKED BAR CHART ---
st.subheader("📉 Stacked Bar Chart: Health Insurance by Area and Gender")

fig_stacked = px.bar(
    filtered_df[filtered_df["Coverage"] != "Total"],
    x="Area",
    y="Count",
    color="Coverage",
    barmode="stack",
    facet_col="Gender",
    title="Stacked Coverage View (Filtered)"
)
st.plotly_chart(fig_stacked, use_container_width=True)

# --- RAW DATA VIEW ---
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
    


# Sample community MPI + coordinates (fill in real coordinates if available)
data = pd.DataFrame({
    "Community": [
        "Yilpani", "Moglaa", "Langa", "Dipali", "Dinga", "Nelkpanzoo", "Diare",
        "Tamkpaa", "Nyola", "Kadia", "Savelugu", "Zoosali", "Kpalmung", "Bunglung",
        "Pong-Tamale", "Kanshegu", "Nabogu", "Kpangi", "Gushie", "Pigu"
    ],
    "MPI": [
        74.8, 71.2, 68.4, 56.6, 54.2, 47.7, 43.6, 41.9, 39.8, 38.4,
        37.0, 35.3, 35.3, 31.7, 31.3, 30.5, 30.1, 30.0, 26.3, 22.8
    ],
    "lat": [
        9.61, 9.63, 9.60, 9.65, 9.68, 9.59, 9.57,
        9.64, 9.62, 9.66, 9.6241, 9.58, 9.67, 9.70,
        9.72, 9.69, 9.71, 9.55, 9.54, 9.53
    ],
    "lon": [
        -0.84, -0.85, -0.83, -0.86, -0.82, -0.81, -0.80,
        -0.87, -0.89, -0.88, -0.8306, -0.78, -0.82, -0.79,
        -0.83, -0.77, -0.76, -0.75, -0.79, -0.78
    ]
})

# Dark-themed MPI heatmap
st.title("🌍 MPI Heatmap of Savelugu Municipal (Dark Theme)")

view_state = pdk.ViewState(
    latitude=9.62,
    longitude=-0.83,
    zoom=9,
    pitch=30
)

# Heatmap layer
heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data=data,
    get_position='[lon, lat]',
    get_weight="MPI",
    radius=20000,
    aggregation=pdk.types.String("MEAN"),
    pickable=True,
)

# Scatterplot layer for points
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position='[lon, lat]',
    get_color='[255, 140, 0, 160]',  # orange glow
    get_radius=2000,
    pickable=True
)

# Tooltip
tooltip = {
    "html": "<b>Community:</b> {Community} <br/><b>MPI:</b> {MPI}%",
    "style": {"backgroundColor": "rgba(0, 0, 0, 0.8)", "color": "white"}
}

# Dark theme map style
dark_map = "mapbox://styles/mapbox/dark-v9"

# Render chart
st.pydeck_chart(pdk.Deck(
    map_style=dark_map,
    initial_view_state=view_state,
    layers=[heatmap_layer, scatter_layer],
    tooltip=tooltip
))

# --- Sidebar Toggle ---
dark_mode = st.sidebar.toggle("🌙 Use Dark Mode?")
st.sidebar.write("🔍 Compare MPI values across Northern Region districts")

# --- Sample Data ---
mpi_data = pd.DataFrame({
    "District": [
        "Savelugu Municipal", "Tamale Metro", "Tolon", "Kumbungu", "Karaga", 
        "Mion", "Sagnarigu", "Nanton", "Gushegu", "Saboba", 
        "Tatale-Sanguli", "Zabzugu", "Yendi Municipal", "Nanumba North", 
        "Nanumba South", "Bimbilla", "Saboba-Chereponi"
    ],
    "MPI": [
        0.187, 0.101, 0.210, 0.195, 0.250, 
        0.232, 0.140, 0.221, 0.265, 0.273, 
        0.249, 0.244, 0.198, 0.215, 
        0.218, 0.207, 0.260
    ],
    "Incidence (%)": [
        41.1, 20.3, 44.5, 43.0, 52.2,
        49.8, 30.0, 47.1, 56.0, 57.8,
        50.6, 48.9, 42.2, 45.7,
        45.9, 44.0, 55.3
    ],
    "Intensity (%)": [
        45.5, 49.8, 47.2, 45.3, 47.9,
        46.6, 46.7, 46.9, 47.3, 47.3,
        49.2, 49.9, 46.9, 47.0,
        47.5, 47.1, 47.0
    ]
})

# Highlight Savelugu
mpi_data["Highlight"] = mpi_data["District"].apply(lambda x: "Savelugu" if x == "Savelugu Municipal" else "Other")

# --- Dark or Light Color ---
if dark_mode:
    bar_color_map = {"Savelugu": "#FF4136", "Other": "#AAAAAA"}
    background = "#0e1117"
    font_color = "white"
else:
    bar_color_map = {"Savelugu": "#FF4136", "Other": "#A9A9A9"}
    background = "#0e1117"
    font_color = "white"

# --- Plotly Horizontal Bar Chart ---
fig = px.bar(
    mpi_data.sort_values("MPI", ascending=False),
    x="MPI",
    y="District",
    orientation="h",
    color="Highlight",
    text="MPI",
    color_discrete_map=bar_color_map,
    hover_data={
        "MPI": True,
        "District": True,
        "Incidence (%)": True,
        "Intensity (%)": True,
        "Highlight": False
    },
    title="📊 MPI of Savelugu Municipal Compared to Other Districts in Northern Region"
)

fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')

fig.update_layout(
    plot_bgcolor=background,
    paper_bgcolor=background,
    font=dict(color=font_color),
    xaxis_title="Multidimensional Poverty Index (MPI)",
    yaxis_title=None,
    showlegend=False,
    height=700
)

# Annotate Savelugu
fig.add_annotation(
    x=0.187,
    y=mpi_data[mpi_data["District"] == "Savelugu Municipal"].index[0],
    text="⬅ Savelugu",
    showarrow=True,
    arrowhead=2,
    ax=-100,
    ay=0,
    font=dict(size=12, color="#FF4136"),
    bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("<h1 style='text-align: center; color: white;'>TARGET FOR THE 4 DIMENSIONS</h1>", unsafe_allow_html=True)

# Sample scores (replace with actual data)
metrics = {
    "Living Condition": 64,
    "Health": 78,
    "Education": 55,
    "Employment": 82
}

# Function to generate a dark-themed gauge
def create_gauge(title, value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'size': 20, 'color': 'white'}},
        number={'font': {'color': 'white'}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': 'white'},
            'bgcolor': "rgba(0,0,0,0)",
            'bar': {'color': "#006CFF"},  # Professional blue
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': "#2c2f33"},        # dark gray
                {'range': [50, 75], 'color': "#3b3f44"},       # medium gray
                {'range': [75, 100], 'color': "#4c8eda"}       # soft blue-gray
            ],
            'threshold': {
                'line': {'color': "#FFD700", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor="#1e1e1e",
        font={'color': 'white'}
    )
    return fig

# Layout with 2 charts per row
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(create_gauge("Living Condition", metrics["Living Condition"]), use_container_width=True)
with col2:
    st.plotly_chart(create_gauge("Health", metrics["Health"]), use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(create_gauge("Education", metrics["Education"]), use_container_width=True)
with col4:
    st.plotly_chart(create_gauge("Employment", metrics["Employment"]), use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px



st.title("Multidimensional Poverty & Intensity Analysis – Ghana, Northern Region, and Savelugu")

# Define data
categories = [
    "Total", "Urban", "Rural", "Male", "Female", "Not working",
    "Agriculture", "Industry", "Service", "No education", "Basic",
    "Secondary", "Post-secondary", "Tertiary", "Other"
]

# Multidimensional Poverty (%)
mp_data = {
    "Category": categories,
    "Savelugu Municipal": [41.1, 38.0, 46.1, 37.7, 56.6, 71.1, 37.0, 17.9, 14.3, 45.7, 30.9, 29.3, 22.7, 15.3, 16.7],
    "Northern": [38.4, 23.4, 50.8, 37.5, 43.5, 60.0, 44.1, 14.2, 9.9, 45.5, 28.1, 21.9, 15.5, 10.0, 22.5],
    "Ghana": [24.3, 14.6, 36.7, 23.0, 27.0, 47.7, 34.3, 8.9, 6.2, 40.9, 20.0, 13.3, 10.7, 7.1, 16.1],
    "Type": ["Multidimensional Poverty"] * 15
}

# Intensity of Poverty (%)
ip_data = {
    "Category": categories,
    "Savelugu Municipal": [45.5, 45.0, 46.3, 45.0, 47.2, 47.7, 44.4, 42.2, 42.0, 45.8, 45.3, 45.1, 44.7, 44.0, 44.2],
    "Northern": [44.3, 44.4, 44.3, 43.9, 46.1, 47.7, 43.2, 42.1, 42.0, 44.6, 43.3, 43.0, 42.7, 42.4, 43.3],
    "Ghana": [43.8, 43.4, 44.0, 43.0, 44.7, 46.1, 42.6, 41.8, 41.9, 44.7, 43.0, 42.8, 42.4, 42.0, 43.0],
    "Type": ["Intensity of Poverty"] * 15
}

# Combine and melt
df_mp = pd.DataFrame(mp_data)
df_ip = pd.DataFrame(ip_data)
df = pd.concat([df_mp, df_ip])
df_melted = df.melt(id_vars=["Category", "Type"], var_name="Region", value_name="Percentage")

# Chart
fig = px.bar(
    df_melted,
    x="Category",
    y="Percentage",
    color="Region",
    facet_row="Type",
    barmode="group",
    height=800,
    title="Comparison of Poverty Indicators by Region and Category"
)
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)


st.title("MPI  Of  Savelugu Municipal  Compared To Other Districts In Northern  Region")
# Sample grouped data (Region > District > MPI%)
data = {
    "Northern Region": [
        {"district": "Savelugu Municipal", "mpi": 41.1, "color": "purple"},
        {"district": "District A", "mpi": 35.0, "color": "gray"},
        {"district": "District B", "mpi": 36.5, "color": "gray"},
        {"district": "District C", "mpi": 39.0, "color": "royalblue"},  # Highest
        {"district": "District D", "mpi": 38.0, "color": "gray"},
    ],
    "Region Two": [
        {"district": "District E", "mpi": 22.0, "color": "deepskyblue"},  # Lowest
        {"district": "District F", "mpi": 30.0, "color": "gray"},
    ],
    "Region Three": [
        {"district": "District G", "mpi": 25.0, "color": "gray"},
    ],
}

fig = go.Figure()
y_pos = []  # Vertical labels
y_index = 0

# Plot each region group
for region, districts in data.items():
    y_index += 1
    y_pos.append(region)

    for dist in districts:
        y_index += 1
        y_pos.append(dist["district"])

        show_text = dist["district"] == "Savelugu Municipal"
        fig.add_trace(go.Scatter(
            x=[dist["mpi"]],
            y=[y_index],
            mode="markers+text" if show_text else "markers",
            marker=dict(size=16, color=dist["color"]),
            text=[f"{dist['district']}: {dist['mpi']}%"] if show_text else None,
            textposition="middle right",
            hovertemplate=f"{dist['district']}: {dist['mpi']}%<extra></extra>",
            name=dist["district"],
            showlegend=False  # <--- Don't add these to the legend
        ))

# Draw curved highlight for Savelugu
fig.add_shape(
    type="path",
    path="M 41.1,5 Q 55,2 68,5",
    line=dict(color="purple", width=2),
    layer="below"
)

# Annotation for Savelugu
fig.add_annotation(
    x=68,
    y=5,
    text="Savelugu Municipal: 41.1%",
    showarrow=False,
    font=dict(color="purple", size=16)
)

# Remove y-axis
fig.update_yaxes(visible=False)

# Format x-axis
fig.update_xaxes(
    title="MPI (%)",
    showgrid=True,
    range=[0, 70],
    tickformat=".0f",
    tickvals=[0, 10, 20, 30, 40, 50, 60, 70],
    ticktext=["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%"],
    color="white"
)

# --- Manual legend items ---
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(size=16, color='purple'),
    name='Savelugu Municipal'
))

fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(size=16, color='gray'),
    name='All other districts in Northern Region'
))

fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(size=16, color='royalblue'),
    name='District with highest MPI'
))

fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(size=16, color='deepskyblue'),
    name='District with lowest MPI'
))

# Layout
fig.update_layout(
    title="Multidimensional Poverty Index (MPI) by District",
    height=600,
    plot_bgcolor="#111111",
    paper_bgcolor="#111111",
    font=dict(color="white"),
    showlegend=True,
    margin=dict(l=80, r=60, t=80, b=40)
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.title("MPI  Of  Savelugu Municipal  Compared To Other Districts In Ghana")

# Sample data — Savelugu + placeholder districts
df = pd.DataFrame({
    "District": ["District " + str(i) for i in range(1, 30)] + ["Savelugu Municipal"],
    "Poverty (%)": [round(p, 1) for p in list(abs(30 + 10 * pd.Series(range(29)).sample(frac=1).values / 28))] + [41.1]
})

df["Highlight"] = df["District"].apply(lambda x: "Savelugu" if x == "Savelugu Municipal" else "Other")

# Build vertical dot plot
fig = px.scatter(
    df,
    x="District",
    y="Poverty (%)",
    color="Highlight",
    color_discrete_map={"Savelugu": "#AB63FA", "Other": "#555"},
    size=[16 if x == "Savelugu" else 9 for x in df["Highlight"]],
    hover_name="District"
)

# Style markers and layout
fig.update_traces(marker=dict(line=dict(width=1.2, color="white")))

fig.update_layout(
    showlegend=False,
    height=600,
    margin=dict(l=40, r=40, t=40, b=120),
    paper_bgcolor="black",
    plot_bgcolor="black",
    xaxis=dict(
    visible=False  # Hides all x-axis elements
    ),

    yaxis=dict(
        title="Multidimensional Poverty Rate (%)",
        color="white",
        gridcolor="gray",
        zeroline=False,
    ),
    font=dict(color="white")
)

# Add annotation for Savelugu
fig.add_annotation(
    x="Savelugu Municipal",
    y=41.1,
    text="Savelugu Municipal: 41.1%",
    showarrow=True,
    arrowhead=1,
    ax=0,
    ay=-60,
    font=dict(color="#AB63FA", size=15),
    arrowcolor="#AB63FA",
    bgcolor="black"
)

# Display chart
st.plotly_chart(fig, use_container_width=True)


st.markdown("""
<style>
.dark-card {
    background-color: #1e1e1e;
    padding: 1.2rem;
    margin-bottom: 1rem;
    border-left: 6px solid;
    border-radius: 10px;
    font-size: 1.05rem;
    color: #f1f1f1;
    box-shadow: 0 0 10px rgba(0, 150, 255, 0.2);
}

.dark-info { border-color: #00bfff; }
.dark-success { border-color: #28a745; }
.dark-warning { border-color: #ffc107; }
.dark-error { border-color: #dc3545; }

.dark-card span.emoji {
    font-size: 1.3rem;
    margin-right: 0.4rem;
}
</style>
""", unsafe_allow_html=True)



st.title("Incidence of multidimensional poverty of 1km by 1km grid")

col1, col2 = st.columns(2)

# --- Left: Community Network Map ---
with col1:
    st.subheader("Community Network with Poverty Intensity")

    # Coordinates
    nodes = {
        "Disiga": (9.67, -0.88),
        "Pigu": (9.72, -0.89),
        "Kadia": (9.70, -0.84),
        "Gbanaga": (9.73, -0.80),
        "Diari": (9.68, -0.79),
        "Sugutampia": (9.64, -0.76),
        "Dipale": (9.71, -0.82),
        "Nabogu": (9.68, -0.78),
        "Adayili": (9.66, -0.81),
        "Zosale": (9.64, -0.84),
        "Gushegu": (9.75, -0.86),
        "Gunayili": (9.69, -0.85),
        "Nakpanzoo": (9.65, -0.79),
        "Kpong": (9.62, -0.77),
        "Yapalsi": (9.63, -0.82),
        "Kpaling": (9.66, -0.86),
        "Ting": (9.61, -0.80)
    }

    # Example poverty intensity per community
    poverty = {
        "Disiga": 78, "Pigu": 64, "Kadia": 55, "Gbanaga": 42,
        "Diari": 83, "Sugutampia": 70, "Dipale": 88, "Nabogu": 61,
        "Adayili": 48, "Zosale": 50, "Gushegu": 33, "Gunayili": 39,
        "Nakpanzoo": 67, "Kpong": 53, "Yapalsi": 60, "Kpaling": 58, "Ting": 72
    }

    edges = [
        ("Disiga", "Pigu"), ("Pigu", "Kadia"), ("Kadia", "Dipale"),
        ("Dipale", "Nakpanzoo"), ("Nakpanzoo", "Ting"), ("Ting", "Disiga")
    ]

    G = nx.Graph()
    for name, coord in nodes.items():
        G.add_node(name, pos=coord, poverty=poverty.get(name, None))
    G.add_edges_from(edges)

    edge_lons, edge_lats = [], []
    for e0, e1 in G.edges():
        x0, y0 = G.nodes[e0]['pos'][1], G.nodes[e0]['pos'][0]
        x1, y1 = G.nodes[e1]['pos'][1], G.nodes[e1]['pos'][0]
        edge_lons += [x0, x1, None]
        edge_lats += [y0, y1, None]

    # Node attributes
    node_lats = [G.nodes[n]['pos'][0] for n in G.nodes()]
    node_lons = [G.nodes[n]['pos'][1] for n in G.nodes()]
    node_colors = [G.nodes[n]['poverty'] for n in G.nodes()]
    hover_text = [f"{n}: {G.nodes[n]['poverty']}%" for n in G.nodes()]

    fig_map = go.Figure()

    fig_map.add_trace(go.Scattermapbox(
        lon=edge_lons,
        lat=edge_lats,
        mode='lines',
        line=dict(width=2, color='white'),
        hoverinfo='none'
    ))

    fig_map.add_trace(go.Scattermapbox(
        lon=node_lons,
        lat=node_lats,
        mode='markers+text',
        marker=dict(
            size=12,
            color=node_colors,
            colorscale='Inferno',
            cmin=0,
            cmax=100,
            colorbar=dict(
                title="Poverty (%)",
                thickness=15,
                tickcolor="white"
            )
        ),
        text=list(G.nodes),
        textposition='top center',
        hovertext=hover_text,
        hoverinfo='text'
    ))

    fig_map.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox_zoom=9,
        mapbox_center={"lat": 9.66, "lon": -0.83},
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=600
    )

    st.plotly_chart(fig_map, use_container_width=True)

# --- Right: Poverty Heatmap Chart ---
with col2:
    st.subheader("Poverty Concentration Grid")

    df = pd.DataFrame({
        "x": ["6–34", "34–56", "56–76", "78–100"] * 4,
        "y": ["50–384"]*4 + ["384–1,778"]*4 + ["1,778–4,158"]*4 + ["4,158–4,909"]*4,
        "value": [10, 30, 60, 80, 15, 42, 70, 90, 12, 39, 66, 88, 17, 45, 72, 95]
    })

    fig_heat = px.scatter(
        df,
        x="x",
        y="y",
        size="value",
        color="value",
        color_continuous_scale="Inferno",
        labels={"value": "Poverty Intensity"},
        opacity=0.85
    )

    fig_heat.update_layout(
        xaxis_title="Deprivation Score (%)",
        yaxis_title="Number of Poor People",
        paper_bgcolor='black',
        plot_bgcolor='black',
        font_color='white',
        height=600,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_heat, use_container_width=True)
    
    


# Title
st.title("Ranked Poverty Levels by Community")

# Data
data = {
    "Community": [
        "Yikpani", "Maglaa", "Langa", "Dipali", "Dinga", "Nakpanzoo", "Diane", "Tinkpaa", "Nyola", "Kadia",
        "Savelugu", "Zoosali", "Kpalung", "Bunglung", "Pong-Tamale", "Kamshagu", "Nabogu", "Kpani", "Gusheff", "Piigu"
    ],
    "Poverty (%)": [74.8, 71.2, 68.4, 56.6, 54.2, 47.7, 43.6, 41.9, 39.8, 38.4,
                    37.0, 35.3, 35.3, 31.7, 31.3, 30.5, 30.1, 30.0, 26.3, 22.8]
}

df = pd.DataFrame(data)

# Horizontal bar chart
fig = px.bar(
    df.sort_values("Poverty (%)", ascending=True),
    x="Poverty (%)",
    y="Community",
    orientation='h',
    color="Poverty (%)",
    color_continuous_scale="Inferno",
    labels={"Poverty (%)": "Poverty Intensity"}
)

# Show values on bars
fig.update_traces(
    text=df.sort_values("Poverty (%)", ascending=True)["Poverty (%)"],
    textposition='outside',
    marker_line_color="black",
    marker_line_width=0.5
)

# Layout & style
fig.update_layout(
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white"),
    xaxis=dict(
        title="Poverty Intensity (%)",
        color="white",
        title_font=dict(size=14, family="Arial"),
        gridcolor="gray"
    ),
    yaxis=dict(
        title="",
        color="white"
    ),
    height=700,
    margin=dict(l=70, r=50, t=40, b=40),
    coloraxis=dict(
        colorbar=dict(
            title=dict(text="Poverty (%)", font=dict(color="white")),
            tickcolor="white",
            tickfont=dict(color="white")
        )
    )
)

# Show chart
st.plotly_chart(fig, use_container_width=True)


st.title("📍 Community Network Map – Savelugu Municipal")

# --- Data ---
communities = pd.DataFrame({
    "Number": list(range(1, 21)),
    "Community": [
        "Yikpani", "Maglaa", "Langa", "Dipali", "Dinga", "Nakpanzoo", "Diane", "Tinkpaa", "Nyola", "Kadia",
        "Savelugu", "Zoosali", "Kpalung", "Bunglung", "Pong-Tamale", "Kamshagu", "Nabogu", "Kpani", "Gushei", "Pigu"
    ],
    "Latitude": [
        9.68, 9.73, 9.71, 9.69, 9.66, 9.65, 9.72, 9.62, 9.64, 9.68,
        9.63, 9.62, 9.69, 9.63, 9.67, 9.61, 9.67, 9.66, 9.69, 9.70
    ],
    "Longitude": [
        -0.84, -0.85, -0.80, -0.82, -0.79, -0.78, -0.89, -0.77, -0.83, -0.81,
        -0.84, -0.82, -0.87, -0.83, -0.85, -0.80, -0.78, -0.86, -0.79, -0.88
    ],
    "Poverty (%)": [74.8, 71.2, 68.4, 56.6, 54.2, 47.7, 43.6, 41.9, 39.8, 38.4,
                    37.0, 35.3, 35.3, 31.7, 31.3, 30.5, 30.1, 30.0, 26.3, 22.8]
})

# --- Categorize Poverty Levels ---
def classify(p):
    if p >= 60:
        return "🔴 High Poverty"
    elif p >= 40:
        return "🟠 Medium Poverty"
    else:
        return "🟢 Low Poverty"

communities["Category"] = communities["Poverty (%)"].apply(classify)

# --- Sidebar Filter: Select categories to highlight ---
st.sidebar.markdown("### 📊 Highlight by Poverty Level")
selected_categories = st.sidebar.multiselect(
    "Select Category:",
    options=communities["Category"].unique(),
    default=communities["Category"].unique()
)

# --- Build Graph ---
G = nx.Graph()
for _, row in communities.iterrows():
    G.add_node(row["Number"], pos=(row["Latitude"], row["Longitude"]), label=row["Community"])

edges = [(i, i + 1) for i in range(1, 20)] + [(20, 1)]
G.add_edges_from(edges)

# --- Nodes with Colors ---
node_lats, node_lons, node_labels, node_names, node_colors = [], [], [], [], []

for _, row in communities.iterrows():
    node = row["Number"]
    lat, lon = row["Latitude"], row["Longitude"]
    label = row["Community"]
    category = row["Category"]

    node_lats.append(lat)
    node_lons.append(lon)
    node_labels.append(str(node))
    node_names.append(label)
    node_colors.append(
        "red" if category == "🔴 High Poverty" else
        "orange" if category == "🟠 Medium Poverty" else
        "green"
    )

# --- Edges ---
edge_lats, edge_lons = [], []
for e0, e1 in G.edges():
    lat0, lon0 = G.nodes[e0]["pos"]
    lat1, lon1 = G.nodes[e1]["pos"]
    edge_lats += [lat0, lat1, None]
    edge_lons += [lon0, lon1, None]

# --- Filter for Selected Categories ---
mask = communities["Category"].isin(selected_categories)
filtered_lats = [lat for lat, keep in zip(node_lats, mask) if keep]
filtered_lons = [lon for lon, keep in zip(node_lons, mask) if keep]
filtered_labels = [label for label, keep in zip(node_labels, mask) if keep]
filtered_names = [name for name, keep in zip(node_names, mask) if keep]
filtered_colors = [color for color, keep in zip(node_colors, mask) if keep]

# --- Plot ---
fig = go.Figure()

# Edges
fig.add_trace(go.Scattermapbox(
    lat=edge_lats,
    lon=edge_lons,
    mode='lines',
    line=dict(width=2, color='white'),
    hoverinfo='none'
))

# Nodes
fig.add_trace(go.Scattermapbox(
    lat=filtered_lats,
    lon=filtered_lons,
    mode="markers+text",
    marker=dict(size=16, color=filtered_colors, symbol="circle"),
    text=filtered_labels,
    textfont=dict(color="white", size=12, family="Arial Black"),
    textposition="middle center",
    hovertext=filtered_names,
    hoverinfo="text"
))

fig.update_layout(
    mapbox_style="carto-darkmatter",
    mapbox_zoom=9,
    mapbox_center={"lat": 9.67, "lon": -0.82},
    height=700,
    margin=dict(l=0, r=0, t=30, b=0)
)

# Show
st.plotly_chart(fig, use_container_width=True)


st.title("Educational Attainment Breakdown (Age 5-14) – Savelugu Municipal")

# ------------------------------
# Raw Data
data = [
    # Not economically active
    {"Econ": "Not economically active", "Area": "Rural", "Gender": "Male", "Age": "5-9", "Never attended": 1072, "Nursery": 133, "Kindergarten": 564, "Primary": 2006, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Rural", "Gender": "Male", "Age": "10-14", "Never attended": 564, "Nursery": 1, "Kindergarten": 2, "Primary": 1799, "JSS/JHS": 322, "SSS/SHS": 4, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Rural", "Gender": "Female", "Age": "5-9", "Never attended": 1224, "Nursery": 115, "Kindergarten": 500, "Primary": 1681, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Rural", "Gender": "Female", "Age": "10-14", "Never attended": 769, "Nursery": 1, "Kindergarten": 1, "Primary": 1394, "JSS/JHS": 229, "SSS/SHS": 3, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Urban", "Gender": "Male", "Age": "5-9", "Never attended": 751, "Nursery": 261, "Kindergarten": 1174, "Primary": 3794, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Urban", "Gender": "Male", "Age": "10-14", "Never attended": 321, "Nursery": 1, "Kindergarten": 1, "Primary": 3220, "JSS/JHS": 727, "SSS/SHS": 9, "Secondary": 3, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Urban", "Gender": "Female", "Age": "5-9", "Never attended": 962, "Nursery": 248, "Kindergarten": 1061, "Primary": 3506, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Not economically active", "Area": "Urban", "Gender": "Female", "Age": "10-14", "Never attended": 488, "Nursery": 1, "Kindergarten": 0, "Primary": 2829, "JSS/JHS": 668, "SSS/SHS": 5, "Secondary": 0, "Voc/technical/commercial": 0},
    # Economically active
    {"Econ": "Economically active", "Area": "Rural", "Gender": "Male", "Age": "5-9", "Never attended": 56, "Nursery": 1, "Kindergarten": 4, "Primary": 28, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Rural", "Gender": "Male", "Age": "10-14", "Never attended": 126, "Nursery": 0, "Kindergarten": 0, "Primary": 76, "JSS/JHS": 16, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Rural", "Gender": "Female", "Age": "5-9", "Never attended": 21, "Nursery": 0, "Kindergarten": 2, "Primary": 8, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Rural", "Gender": "Female", "Age": "10-14", "Never attended": 58, "Nursery": 0, "Kindergarten": 0, "Primary": 36, "JSS/JHS": 7, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Urban", "Gender": "Male", "Age": "5-9", "Never attended": 29, "Nursery": 1, "Kindergarten": 9, "Primary": 14, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Urban", "Gender": "Male", "Age": "10-14", "Never attended": 55, "Nursery": 0, "Kindergarten": 0, "Primary": 82, "JSS/JHS": 15, "SSS/SHS": 1, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Urban", "Gender": "Female", "Age": "5-9", "Never attended": 18, "Nursery": 0, "Kindergarten": 3, "Primary": 9, "JSS/JHS": 0, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
    {"Econ": "Economically active", "Area": "Urban", "Gender": "Female", "Age": "10-14", "Never attended": 40, "Nursery": 0, "Kindergarten": 0, "Primary": 37, "JSS/JHS": 9, "SSS/SHS": 0, "Secondary": 0, "Voc/technical/commercial": 0},
]

# ------------------------------
# Raw Data
df = pd.DataFrame(data)  # Assuming `data` is defined as you've posted

# ------------------------------
# Sidebar Filters
st.sidebar.header("📊 Filter Options")
econ_filter = st.sidebar.multiselect("Economic Status", df["Econ"].unique(), default=df["Econ"].unique())
area_filter = st.sidebar.multiselect("Area", df["Area"].unique(), default=df["Area"].unique())
gender_filter = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
age_filter = st.sidebar.multiselect("Age Group", df["Age"].unique(), default=df["Age"].unique())

# ------------------------------
# Filtered Data
filtered_df = df[
    (df["Econ"].isin(econ_filter)) &
    (df["Area"].isin(area_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["Age"].isin(age_filter))
]

# ------------------------------
# Melt the data for animation (retain Age)
edu_cols = ["Never attended", "Nursery", "Kindergarten", "Primary", "JSS/JHS", "SSS/SHS", "Secondary", "Voc/technical/commercial"]
df_melted = filtered_df.melt(
    id_vars=["Age", "Gender", "Area"], 
    value_vars=edu_cols,
    var_name="Education Level",
    value_name="Population"
)

# ------------------------------
# Animated Horizontal Bar Chart by Age
fig = px.bar(
    df_melted,
    x="Population",
    y="Education Level",
    orientation='h',
    title="Animated Educational Levels by Age Group",
    color="Population",
    color_continuous_scale="Viridis",
    animation_frame="Age",
    animation_group="Education Level"
)

fig.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="white",
    xaxis=dict(title="Number of People", color="white", gridcolor="gray"),
    yaxis=dict(color="white"),
    height=550,
    margin=dict(l=80, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)

st.title("Educational Attainment by Industry (Age 5-14) – Savelugu Municipal")

# Sample cleaned dataset
data = [
    {"Industry": "Agriculture", "Education": "Never attended", "Area": "Rural", "Gender": "Male", "Age": "5-9", "Count": 54},
    {"Industry": "Agriculture", "Education": "Never attended", "Area": "Rural", "Gender": "Male", "Age": "10-14", "Count": 123},
    {"Industry": "Agriculture", "Education": "Never attended", "Area": "Rural", "Gender": "Female", "Age": "5-9", "Count": 17},
    {"Industry": "Agriculture", "Education": "Never attended", "Area": "Rural", "Gender": "Female", "Age": "10-14", "Count": 50},
    {"Industry": "Manufacturing", "Education": "Primary", "Area": "Urban", "Gender": "Male", "Age": "10-14", "Count": 6},
    {"Industry": "Wholesale", "Education": "Primary", "Area": "Urban", "Gender": "Female", "Age": "10-14", "Count": 3},
    {"Industry": "Construction", "Education": "Primary", "Area": "Urban", "Gender": "Male", "Age": "10-14", "Count": 7},
    {"Industry": "Accommodation", "Education": "JSS/JHS", "Area": "Urban", "Gender": "Female", "Age": "10-14", "Count": 2},
    {"Industry": "Other services", "Education": "Primary", "Area": "Urban", "Gender": "Male", "Age": "10-14", "Count": 8},
]

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("🔎 Filter Options")
industry = st.sidebar.multiselect("Select Industry", df["Industry"].unique(), default=df["Industry"].unique(), key="industry_filter")
education = st.sidebar.multiselect("Select Education Level", df["Education"].unique(), default=df["Education"].unique(), key="education_filter")
area = st.sidebar.multiselect("Select Area", df["Area"].unique(), default=df["Area"].unique(), key="area_filter")
gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique(), key="gender_filter")
age = st.sidebar.multiselect("Select Age Group", df["Age"].unique(), default=df["Age"].unique(), key="age_filter")


# Filter data
filtered_df = df[
    (df["Industry"].isin(industry)) &
    (df["Education"].isin(education)) &
    (df["Area"].isin(area)) &
    (df["Gender"].isin(gender)) &
    (df["Age"].isin(age))
]

# Summarize for chart
summary = filtered_df.groupby("Education")["Count"].sum().reset_index().sort_values("Count")

# Plot
fig = px.bar(
    summary,
    x="Count",
    y="Education",
    orientation="h",
    title="Filtered Educational Distribution by Industry",
    color="Count",
    color_continuous_scale="Inferno"
)

fig.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="white",
    xaxis=dict(title="Number of People", color="white", gridcolor="gray"),
    yaxis=dict(title="Education Level", color="white"),
    height=550
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("### 15. Conclusion")
st.markdown("""
<div class="dark-card dark-info">
    <span class="emoji">👧</span> <strong>Savelugu Municipal is experiencing rapid demographic change with strong urban growth, high youth population, 
and persistent poverty challenges. With over 122,000 people and a density of 79.27/km², 
targeted investments in education, sanitation, employment, and infrastructure are essential 
to meet the needs of this growing population and reduce multidimensional poverty.</strong>
</div>
""", unsafe_allow_html=True)

