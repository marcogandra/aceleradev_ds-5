import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



@st.cache(allow_output_mutation=True)
def load_file( data ):
    return pd.read_csv( data )




def main():
    st.title("Codenation - Explorador de dados")
    st.subheader("Aplicativo para exploração de dados ")
    st.sidebar.image("logo_codenation.jpeg",  use_column_width=True,)

    df = pd.DataFrame()
  

    
    
    st.text("Faça o upload de um arquivo .csv para iniciar a análise")
    file_bytes = st.file_uploader("Upload a file", type=("csv"))
    
    
    #verifica se o arquivo já foi carregado
    if file_bytes and df.empty :
        df = load_file(file_bytes)
        
        
        
    #coloca os widgets na sidebar
    show_file = st.sidebar.checkbox("Exibir amostra do arquivo")
    show_columns = st.sidebar.checkbox("Exibir colunas do arquivo")
    show_heatmap = st.sidebar.checkbox("Exibir heatmap")
    show_heatmap_campos = st.sidebar.checkbox("Selecionar campos do heatmap")
    
    
    
    if not df.empty :       
        st.subheader("Descrição dos dados do arquivo (Describe)")
        st.write(df.describe())
    
    
    #Se o arquivo está definido, preenche os dados
    if not df.empty :
        corrmat = df.select_dtypes(include=['int64', 'float64']).corr()
        
       
        dtypes = df.dtypes
        cols = df.columns
        
        
    if show_file and  not df.empty :
        st.subheader("Amostra do conteúdo do arquivo")
        
        if  not df.empty  :
            st.write(df.head())
            st.text("shape do arquivo linhas {0} x colunas {1}".format(df.shape[0],df.shape[1]))     
      
    
    
    if show_columns and not df.empty :
        st.subheader("Colunas e tipos de dados dos campos")
        st.write(dtypes)
    
    
    
    if show_heatmap :
        st.subheader("Heatmap de correlacao (somente campos numéricos)")
        
        corrmat = df.select_dtypes(include=['int64', 'float64']).corr()
        
        f, ax = plt.subplots(figsize=(10, 7))
        sns.heatmap(corrmat)
        st.pyplot()

     

    
    
    #plota o histograma do campo selecionado, ou um gráfico de barras de acordo com o tipo de 
    #dados do campo
    if not df.empty:
        st.subheader("Histograma")
        
        selectbox_hist = st.selectbox("Selecione o campo para ver no histograma", df.columns, key="id2") 
        
        
        if( df[selectbox_hist].dtype == 'object'  ):
            df[selectbox_hist].value_counts().plot.bar()
                
            st.pyplot()
       
        
        else:
            bins = st.slider("Bins", min_value=1, max_value=100)        
            df[selectbox_hist].plot.hist(bins = bins)
            st.pyplot()

            
        
    if not df.empty and show_heatmap_campos:
        
        
        st.subheader("Selecione os campos para ver o heatmap de correlação entre eles")
        colunas_selecionadas = st.multiselect("Campos disponíveis", df.columns)
        
        
        if len(cols1) > 0:
           

            sns.heatmap(df[colunas_selecionadas].corr())
            st.pyplot()
            
        
        
    st.sidebar.info("""Escrito por **Charles Alves**. 
    [Meu Linkedin](https://www.linkedin.com/in/charles-alves/)
    [Meu github](http://github.com/macintoxic/)""")
    
    
if __name__ == '__main__':
    main()