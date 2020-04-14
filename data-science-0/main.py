#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[11]:


len(black_friday[ (black_friday.Gender == 'F' )  & ( black_friday.Age == '26-35' ) ])


# In[12]:


black_friday.isnull().sum(axis=0).max()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[93]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return (len(black_friday), len(black_friday.columns) )
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[95]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return len(black_friday[ (black_friday.Gender == 'F' )  & ( black_friday.Age == '26-35' ) ])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[15]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return len(black_friday.User_ID.unique())
    
    


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return len(black_friday.dtypes.unique())
    


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[113]:


def q5():
    # Retorne aqui o resultado da questão 5.    
    return len(black_friday[(black_friday.isnull().sum(axis=1)  > 0)] )/ len(black_friday)
    
    


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[170]:


def q6():      
    return int(black_friday.isnull().sum(axis = 0).max())



# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday.Product_Category_3.dropna().value_counts().idxmax()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[61]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return ((black_friday.Purchase - black_friday.Purchase.min()) / (black_friday.Purchase.max() - black_friday.Purchase.min())).mean()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[9]:


def q9():
    # Retorne aqui o resultado da questão 9.     
    black_friday.Purchase = (black_friday.Purchase-black_friday.Purchase.mean())/black_friday.Purchase.std()
    return len( black_friday[(black_friday.Purchase >- 1) & (black_friday.Purchase < 1)])

    


# In[ ]:





# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[22]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True

