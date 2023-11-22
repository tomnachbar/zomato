import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static
import io
import zipfile


df = pd.read_csv('zomato.csv')

df1 = df.copy()

st.set_page_config(
    page_title='Main',
    page_icon='📋',
    layout='wide')


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


# METRICAS DA MAIN PAGE #
# =================================================================== #

st.header('**Fome ZERO!**')

st.subheader("O Melhor lugar para encontrar seu mais novo restaurante favorito! :spaghetti: ",  divider='red')

st.subheader("*Temos as seguintes marcas dentro da nossa plataforma:*")

with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")

    with col1:
       total_rest = len(df1[('Restaurant ID')].unique())
       col1.metric ('Restaurantes Cadastrados', total_rest)

    with col2:
       total_paises= len(df1[('Country Code')].unique())
       col2.metric('Países Cadastrados', total_paises)
       
    with col3:
       city_cadastro = len(df1[('City')].unique())
       col3.metric('Cidades Cadastrados', city_cadastro)
    
    with col4:
        avaliacoes = df1['Votes'].sum()
        col4.metric('Avaliações feitas na plataforma','{:,}'.format(avaliacoes).replace(',','.'))
                 
    with col5:
       tipos = len(df1[('Cuisines')].unique())
       col5.metric('Tipos de Culinária Oferecidas',tipos)


# =================== BARRA LATERAL NO STREAMLIT ================= #

with st.sidebar:

   st.sidebar.title('Fome Zero')
   st.sidebar.image('logo.png', width=100)
   st.sidebar.markdown(""" ___ """)
   st.sidebar.subheader('Filtros')

   country = st.sidebar.multiselect( label='Escolha os Paises que Deseja visualizar os Restaurantes',
                          options=['India','Australia','Brazil','Canada','Indonesia','New Zeland','Philippines',
                                   'Qatar','Singapure','South Africa','Sri Lanka','Turkey','United Arab Emirates',
                                   'England','United States of America'],
                            default= ['Brazil','England','Qatar','South Africa','Canada','Australia'])
   
   # EXPORTANDO ARQUIVO CSV TRATADO
# ===================================================================== #
# Salvando o DataFrame como um arquivo CSV em memória

st.sidebar.markdown(" ## Dados Tratados ")

buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w') as zip_file:
    
    # Adicionando o DataFrame como um arquivo CSV dentro do arquivo zip
    zip_file.writestr('data.csv', df1.to_csv(index=False))

new_df = df1
new_df.to_csv('data.zip', index=False, sep=';')

buffer.seek(0)
st.sidebar.download_button('Download', data=buffer, file_name='data.zip', mime='text/csv')

# FILTROS DE PAÍS NO STREAMLIT
# ==================================================================== #

linhas_selecionadas = df1['country_name'].isin(country) 
df1= df1.loc[linhas_selecionadas,:]


# MAPA GEOGRÁFICO #
# ===================================================================== #

with st.container():
   
   columns_groupby = [
    'Restaurant Name', 'Restaurant ID',
    'Average Cost for two', 'Currency',
    'Cuisines',
    'Aggregate rating',
    'Latitude',
    'Longitude',
    'City',
    'country_name',
    'color_name'
]

df_aux = (df1.loc[:, columns_groupby]
                   .groupby('Restaurant ID')
                   .max()
                   .reset_index())
map = folium.Map()

contador = 0

marker_cluster = MarkerCluster().add_to(map)

for index, location_info in df_aux.iterrows():
      folium.Marker(
        [location_info['Latitude'], location_info['Longitude']],
   popup=folium.Popup(
      f"Name:{location_info['Restaurant Name']}"
      f"Type: {location_info['Cuisines']}"
      f"Price: {location_info['Average Cost for two']}"
      f"Rating: {location_info['Aggregate rating']}", max_width=300, parse_html=True),
        icon=folium.Icon(color=location_info['color_name'])  # Usa diretamente a coluna 'color_name'
    ).add_to(marker_cluster)

contador = contador+1                                         

folium_static(map,width=1000,height=600)



