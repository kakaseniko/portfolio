import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('./data/trendy_eindhoven_data_Eniko.csv')
st.set_page_config(page_title="Eindhoven Data Stories", page_icon="🏙️", layout="centered")

st.header("Explore trends in Eindhoven 🏙️")

st.write("""This small data visualization project was part of my 'Advanced AI' semester at Fontys. The goal was to create interactive graphs that allow people to 
         see trends in Eindhoven's neighborhoods over the years and demonstrate how data can tell stories. </br></br>
         When you select different variables from the drop down menu you can discover how these different aspects changed during the past years. 
         It is possible to find out, for example, how COVID effected the electricity usage per neighborhood.
         From the graph it is visible that the electricity usage escalated in each neighborhood around 2019, except for the city center where shops had to be closed,
         resulting in less energy use in this area than before. </br></br>
         What I liked about this project is how it allowed me to discover that data and graphs can be super interesting and that they can tell much more than facts,
         they can contain whole stories. And most of the time some extra research has to be done to understand the "whys" behind the numbers which feels like a detective work for me.
         On top of that, I could learn how to make interactive graphs with Plotly which was a fun experience.</br></br>""", unsafe_allow_html=True)

variable = st.selectbox("Select a variable:", ['Gemiddeld elektriciteitsverbruik totaal', 'Aantal woningen', 'Inwoners',  'Verplaatst zich meestal per fiets %',
                                              'Personenauto\'s totaal', 'Doet aan vrijwilligerswerk', 'Sport wekelijks (18-84 jaar)', 
                                              'Bezoekt culturele voorstellingen %', 'Registraties overlast per 1.000 inwoners',
                                              'Voelt zich wel eens onveilig in de eigen buurt %', 'Gemiddeld persoonlijk inkomen per inkomensontvanger (x1000 euro)',
                                              'Totaal aantal winkelpanden'])
size_ref = 1
if variable == 'Aantal woningen' or variable == 'Inwoners' or variable == 'Personenauto\'s totaal':
    size_ref = 500
elif  variable == 'Gemiddeld elektriciteitsverbruik totaal':
    size_ref = 100
    df = df[df['Gemiddeld elektriciteitsverbruik totaal'] != 0]
elif variable == 'Bezoekt culturele voorstellingen %':
    size_ref = 2
elif variable == 'Totaal aantal winkelpanden':
    size_ref = 5

figLine = px.line(df, x='year', y=variable, title=variable + '  per year per neighborhood:', color='neighborhood')
figLine.update_xaxes(type='category')

st.plotly_chart(figLine)

fig = px.scatter_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    color='neighborhood',
    size=variable,
    hover_name='neighborhood',
    animation_frame='year',
    animation_group='neighborhood',
    mapbox_style='carto-positron',
    zoom=10,
).update_traces(marker=dict(sizemode='diameter', sizeref=size_ref))
frames = []
for year in df['year'].unique():
    frame_data = df[df['year'] == year]
    frame = px.scatter_mapbox(
        frame_data,
        lat='latitude',
        lon='longitude',
        color='neighborhood',
        size=variable,
        hover_name='neighborhood',
        mapbox_style='carto-positron',
        zoom=10,
    ).update_traces(marker=dict(sizemode='diameter', sizeref=size_ref))

    frames.append(go.Frame(data=frame.data, name=str(year)))

fig.frames = frames
st.write("Click play to see changes throughout the years:")
st.plotly_chart(fig)


