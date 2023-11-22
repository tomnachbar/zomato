import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static

st.set_page_config(page_title='Countries',page_icon='🌎',layout='wide')

st.title('🌏 Visão Países') 


df = pd.read_csv('zomato.csv')
df1 = df.copy()

# ================== RENOMEANDO COLUNA DE PAÍSES ================ #

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

# ================== CRIANDO COLUNA DE PAÍSES ================ #

df1['country_name'] = df1.loc[:,'Country Code'].apply(lambda x: country_name(x))

# ======================== CRIANDO AS CORES PARA O GRAFICO ============= #
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

# =================== CRIANDO COLUNA DE COLORS =====================#

df1['color_name'] = df1.loc[:,'Rating color'].apply(lambda x: color_name(x))

# ======================= CRIANDO RANGE DE PREÇOS ================= #

def create_price_tye(price_range):
 if price_range == 1:
    return "cheap"
    
 elif price_range == 2:
    return "normal"
    
 elif price_range == 3:
    return "expensive"
    
 else:
    return "gourmet"
 
# ============ LIMPEZA DOS DADOS =================== #

df1 = df1.dropna()

df1 = df1.drop_duplicates()

df1['Cuisines'] = df1['Cuisines'].astype(str)

df1["Cuisines"] = df1.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])

df1['Restaurant Name'] = df1['Restaurant Name'].str.strip()
df1['City'] = df1['City'].str.strip()
df1['Address'] = df1['Address'].str.strip()
df1['Cuisines'] = df1['Cuisines'].str.strip()
df1['Rating text'] = df1['Rating text'].str.strip()
df1['country_name'] = df1['country_name'].str.strip()
df1['color_name'] = df1['color_name'].str.strip()

linhas_vazias = df1['Restaurant ID'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['Restaurant Name'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['City'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['Address'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['Cuisines'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['Rating text'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['country_name'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['color_name'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

linhas_vazias = df1['Votes'] != 'NaN'
df1 = df1.loc[linhas_vazias, :]

df1 = df1.drop(columns='Switch to order menu', axis=1)

# ======================= BARRA LATERAL ====================== #

st.sidebar.subheader('Filtros')

country = st.sidebar.multiselect( label='Escolha os Paises que Deseja visualizar os Restaurantes',
                          options=['India','Australia','Brazil','Canada','Indonesia','New Zeland','Philippines',
                                   'Qatar','Singapure','South Africa','Sri Lanka','Turkey','United Arab Emirates',
                                   'England','United States of America'],
                            default= ['Brazil','England','Qatar','South Africa','Canada','Australia'])

# FILTROS DE PAÍS NO STREAMLIT
# ==================================================================== #

linhas_selecionadas = df1['country_name'].isin(country) 
df1= df1.loc[linhas_selecionadas,:]


# ======================= LAYOUT STREAMLIT ==================== #

st.container()

df_aux = (df1.loc[:, ['Restaurant ID', 'country_name']]
            .groupby( 'country_name' )
            .nunique().sort_values('Restaurant ID', ascending=False)
            .reset_index())

fig = px.bar(df_aux,x='country_name',y='Restaurant ID',
             title ='Quantidade de Restaurantes Registrados por País', 
             labels={'country_name':'Países', 'Restaurant ID': 'Quantidade de Restaurantes'},text_auto=True)

st.plotly_chart(fig, use_container_width=True)

st.container()

df_aux = (df1.loc[:, ['country_name', 'City']]
           .groupby( 'country_name' )
           .nunique().sort_values('City', ascending=False)
           .reset_index())

fig = px.bar(df_aux,x='country_name',y='City',text_auto=True,
             title='Quantidade de Cidades Registrados por País', 
             labels={'country_name':'Países','City':' Quantidade de Cidades'})

st.plotly_chart(fig, use_container_width=True)

st.container()
col1, col2 = st.columns(2)

with col1:

    df_aux = (df1.loc[:,('country_name','Votes')]
           .groupby('country_name')
           .mean().sort_values('Votes', ascending=False)
           .reset_index()
           .round(2))



    fig = px.bar(df_aux, x='country_name',y='Votes',
                 title='Média de avaliações feitas por país', 
                 labels={'country_name': 'Países', 'Votes': 'Quantidade de Avaliações'}, text_auto=True)
    
    st.plotly_chart(fig, use_container_width=True)


    with col2:
       df_aux = (df1.loc[:,('country_name','Average Cost for two')]
                  .groupby('country_name')
                  .mean()
                  .sort_values('Average Cost for two', ascending=False)
                  .reset_index().round(2))


       fig = px.bar(df_aux, x='country_name', y='Average Cost for two',
                     title='Média de preços de um prato para duas pessoas',
                     labels={'country_name':'Países','Average Cost for two':'Preço de prato para duas pessoas'}, text_auto=True)
       st.plotly_chart(fig, use_container_width=True)
       
