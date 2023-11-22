import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import inflection
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static

st.set_page_config(page_title='Cuisines',
                    page_icon=':knife_fork_plate:', layout='wide')

st.title(':knife_fork_plate: Visão Tipos de Cozinha')
st.header('Melhores Restaurantes dos Principais tipos Culinários')

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
                          options=df1.loc[:,'country_name'].unique().tolist(),
                            default= ['Brazil','England','Qatar','South Africa','Canada','Australia'])

df_filter = st.sidebar.slider('Selecione a quantidade de Restaurantes', 1, 20, 10)

cuisines = st.sidebar.multiselect(
        "Escolha os Tipos de Culinária", df1.loc[:,"Cuisines"].unique().tolist(),
        default=[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ],
    )

cols = ['Restaurant ID','Restaurant Name','country_name','City','Cuisines','Average Cost for two','Aggregate rating','Votes']
lines = (df1["Cuisines"].isin(cuisines)) & (df1["country_name"].isin(country))

top_rest = (df1.loc[lines,cols]
           .sort_values(['Aggregate rating','Restaurant ID'], ascending=[False,True])
           .reset_index(drop=True).head(20))


# LAYOUT DO STREAMLIT 
# ==================================== MÉTRICAS ================================ #

st.container()
col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    linha = df1['Cuisines'] == 'Italian'
    italian = (df1.loc[linha,('Restaurant Name','Aggregate rating','Restaurant ID')]
                .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                .reset_index().iloc[0,2])
             
    col1.metric('Italiana - Darshan', value = f'{italian}/5.0',
                help=' País: Índia \n\n Cidade: Pune \n\n Média Prato para dois: 700 (Indian Rupees(Rs.))')


with col2:
   
    linha = df1['Cuisines'] == 'American'
    american = (df1.loc[linha,('Restaurant Name','Aggregate rating','Restaurant ID')]
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                    .reset_index()
                    .iloc[0,2])
    col2.metric('Americana - Burger & Lobster', value = f'{american}/5.0', help= 'País: England \n\n Cidade: London \n\n Média Prato para dois: 45 (Pounds(£)')

with col3:
    linha = df1['Cuisines'] == 'Arabian'

    arabian = (df1.loc[linha,('Restaurant Name','Aggregate rating','Restaurant ID')]
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                    .reset_index()
                    .iloc[0,2])
    col3.metric('Árabe - Mandi@36', value = f'{arabian}/5.0', help='País: India \n\n Cidade: Hyderabad \n\n Média Prato para dois: 600 (Indian Rupees(Rs.)')

with col4:

    linha = df1['Cuisines'] == 'Japanese'

    japanese = (df1.loc[linha,('Restaurant Name','Aggregate rating','Restaurant ID')]
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                    .reset_index()
                    .iloc[0,2])
    col4.metric(label = f'Japonesa: Sushi Samba', value = f'{japanese}/5.0',help='País: England \n\n Cidade: London \n\n Média Prato para dois: 110 (Pounds(£)')   
   
with col5:
   
   linha = df1['Cuisines'] == 'Brazilian'

   brazil = (df1.loc[linha,('Restaurant Name','Aggregate rating','Restaurant ID')]
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                    .reset_index().iloc[0,2])
   col5.metric('Brasileira - Braseiro da Gávea', value = f'{brazil}/5.0', help='País: Brazil \n\n Cidade: Rio de Janeiro \n\n Média Prato para dois: 100 (Brazilian Real(R$))')

#====================================== DATA FRAME ==========================================================
st.container()

dataframe = top_rest.head(df_filter)

st.dataframe(dataframe, width=1000)

# ===================================== TOP 10 MELHORES E PIORES ============================================
st.container()
col1, col2 = st.columns(2)

with col1:
   
    df_aux= (df1.loc[:,('Cuisines','Aggregate rating','Restaurant ID')].groupby('Cuisines').mean()
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[False,True])
                    .reset_index()
                    .head(20))
    
    total_10_melhor = df_aux.head(df_filter)
   
    fig = px.bar(total_10_melhor, x='Cuisines',y='Aggregate rating', title='Top 10 Melhores Tipos de Culinária', text_auto=True,
        labels={'Cuisines':'Tipo de Culinária', 'Aggregate rating':'Média da Avaliação'}, width=600)

    st.plotly_chart(fig)

# ===============================================================================================================
with col2:
       
    linha = df1['Aggregate rating'] > 0

    df_aux= (df1.loc[linha,('Cuisines','Aggregate rating','Restaurant ID','country_name')].groupby(['Cuisines','country_name']).mean()
                    .sort_values(['Aggregate rating','Restaurant ID'],ascending=[True,False])
                    .reset_index()
                    .head(20))
    
    total_10_pior = df_aux.head(df_filter)
    
    fig = px.bar(total_10_pior, x='Cuisines',y='Aggregate rating', title='Top 10 Piores Tipos de Culinária', text_auto=True,
        labels={'Cuisines':'Tipo de Culinária', 'Aggregate rating':'Média da Avaliação'}, width=600)
    
    st.plotly_chart(fig)


