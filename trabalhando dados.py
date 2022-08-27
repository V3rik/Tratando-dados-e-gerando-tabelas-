#!/usr/bin/env python
# coding: utf-8

# In[1]:


# trabalhando dados


# In[ ]:


#comando de instalação da biblioteca pandas
#pip install pandas


# In[42]:


# display(tb_gerente)
# display(tb_loja)
# display(tb_produto)


# In[ ]:





# In[143]:


#importando biblioteca

import pandas as pd


#importando bae de dados:
tb_gerente = pd.read_csv("identifica_gerente.csv", sep=";")
tb_loja = pd.read_csv("identifica_loja.csv", sep=";")
tb_produto = pd.read_excel("identifica_produto.xlsx")
                
    
    
                # alterando nome da coluna quantidade para quantidade_vendida
tb_produto = tb_produto.rename(columns={'quantidade':'quantidade_vendida'})


                # criando nova coluna dentro da tabela tb_produts
                #tabela['coluna_nova'] = ? 
tb_produto['total em vendas'] = 0



#multiplicando coluna valor x quantidade vendida
tb_produto['total em vendas'] = tb_produto['valor'] * tb_produto['quantidade_vendida']



print('nome da coluna alterado')
print('Coluna total vendas adicionada')
print('calculo de multiplicação feito')

#exibir dados
#display(tb_gerente)
#display(tb_loja)
#display(tb_produto)






                                                    #mesclar tabelas


tb_gerente = tb_gerente.merge(tb_loja, on='id')
tb_gerente = tb_gerente.merge(tb_produto, on='id')





print(tb_gerente)





# In[142]:


#contagem de vendas por id:
#conta quantas vezes apareceram o mesmo id 
print('vendas por loja')
contar_vendas = tb_gerente['id'].value_counts()
print(contar_vendas)


# In[133]:


#somar todas as vendas
    
somar_vendas_por_id = tb_gerente['total em vendas'].sum()
print('total em vendas foi de: ', somar_vendas_por_id)


# In[137]:


#somando quantidade de vendas
print('total vendido por loja(id)')
tb_gerente = tb_gerente.groupby("id").sum()
print(tb_gerente)


# # Exportando dataframe em csv
# 

# In[146]:


tb_gerente.to_csv("tabela-gerada-pelo-python1.csv", sep=";")


# In[ ]:




