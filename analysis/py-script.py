#!/usr/bin/env python
# coding: utf-8

# # Exploratory analysis of Perceptions about Science and Open Science
# 
# This analysis revolves around the undergraduate thesis carried out by Franco Sebastián Benítez, under the supervision of Débora Burin and Lucas Cuenya, from the School of Psychology of the University of Buenos Aires.
# 
# As set in our preregistration, we are checking the following aspects:
# 
# 1) Check for exclusion criteria in the demographic data, and in the completion rate.
# 
# 2) Describe the sample’s demographic characteristics. 
# 
# 3) Analyse the total percentage of “yes” responses to belief in crisis. Analyse as a function of career stage and methodological approach.
# 
# 4) Qualitative analysis of open field response to belief in crisis.
# 
# 5) Percentage of  agreement with each, and combined, statements about replication crisis, p-value, publication bias. Analyse as a function of career stage and methodological approach.
# 
# 6) Percentage of  agreement with each, and combined, statements about perceived barriers. Analyse as a function of career stage and methodological approach.
# 
# 7) Percentage of  agreement with each, and combined, statements about attitudes against adopting open science practices. Analyse as a function of career stage and methodological approach.
# 
# 8) Qualitative analysis of open field response to attitudes about barriers against adopting open science practices.

# ## Loading the necessary libraries

# In[1]:


import pandas as pd                  # data wrangling
import matplotlib.pyplot as plt      # plotting


# ## Loading the dataset

# In[2]:


df = pd.read_csv("../data/Percepciones sobre ciencia y ciencia abierta.csv")


# In[3]:


df


# In[4]:


df.shape


# The data contains 53 columnas and 40 rows.

# Now let's rename the columns to make it easier to manipulate.

# In[5]:


column_names = {"Timestamp": "timestamp",
                "Edad (años)": "age",
                "Nivel educativo alcanzado": "education",
                "Área/s de investigación": "area",
                "¿Ha participado en un proyecto de investigación (v. g., UBACyT, CONICET) en los últimos 5 años?": "project",
                "¿Ha publicado en una revista indexada con referato (v. g., Scopus, Scimago, Scielo) en los últimos 5 años?": "journal",
                "Marque su posición actual en la Facultad de Psicología de la UBA": "position",
                "¿Qué tipo de metodología suele predominar en sus estudios?": "methodology",
                "¿Cree que hay una crisis en la ciencia?": "belief",
                "[Poner los materiales (e.g., cuestionarios, procedimientos) a disposición mediante plataformas o repositorios públicos].1": "materials",
                "[Reportar toda la información necesaria detalladamente para que otras personas puedan replicar mi estudio].1": "report",
                "[Compartir una pre-impresión (pre-print) publicándola en un repositorio de confianza]": "share",
                "[Usar revisión por partes abierta]": "open_review",
                "[Publicar en revistas de acceso abierto].1": "open_journal",
                "[Adaptar un test psicométrico].1": "psychometric_test",
                "[Participar en proyectos abiertos y colaborativos a gran escala].1": "open_project",
                "¿Cuáles le parecen que son las mayores barreras para la aceptación y puesta en práctica de prácticas de ciencia abierta en su campo y/o lugar de trabajo?": "barriers_1",
                "Si aplica, por favor describa brevemente qué barreras ha experimentado para incorporar o mantener prácticas de ciencia abierta": "barriers_2",
                "Por último, si posee alguna idea o comentario respecto a esta encuesta o al tema que aborda, por favor escribalo brevemente a continuación": "comments"
               }

df.rename(columns = column_names, inplace=True)
df.timestamp = pd.to_datetime(df.timestamp)


# ## Analysis 

# ### 1) Check for exclusion criteria in the demographic data, and in the completion rate.

# In[6]:


df["project"].value_counts()


# In[7]:


df["journal"].value_counts()


# In[8]:


exclusion_criteria = df[["project", "journal"]]

i = -1 # to take in account the index 0
for a, b in exclusion_criteria.itertuples(index=False):
    i = i + 1
    if a == "No" and b == "No":
        print(f"Participant n° {i} will be excluded")


# In[9]:


df[["project", 
    "journal"]].iloc[26]


# In[10]:


df[["project", 
    "journal"]].iloc[20]


# In[11]:


df.drop([20, 26], axis=0)


# Now we have two less rows.

# ### 2) Describe the sample’s demographic characteristics.

# #### 2.1) Education

# In[12]:


plt.figure(figsize=(15,10))
ax = df.groupby('education').size().sort_values(ascending=False).plot.bar()
ax.set_title('Education')
ax.set_xlabel("Researchers")
ax.set_ylabel("Frecuency")

def add_value_labels(ax, spacing=5):
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        space = spacing
        va = 'bottom'
        if y_value < 0:
            space *= -1
            va = 'top'
        label = y_value
        ax.annotate(
            label,                      
            (x_value, y_value),         
            xytext=(0, space),          
            textcoords="offset points", 
            ha='center',                
            va=va)                      

add_value_labels(ax)
plt.xticks(rotation=0)


# #### 2.2) Research area

# In[13]:


df["area"].value_counts()


# #### 2. 3) Position 

# In[14]:


plt.figure(figsize=(20,15))
ax = df.groupby("position").size().sort_values(ascending=True).plot.barh(fontsize=20)
ax.set_title('Education', fontsize=20)
ax.set_xlabel("Researchers", fontsize=20)
ax.set_ylabel("Frecuency", fontsize=20)


# #### 2.4) Methodology

# In[15]:


plt.figure(figsize=(20,15))
df["methodology"].value_counts().plot.pie(autopct='%1.0f%%', fontsize=20)


# #### 2.5) Age

# In[16]:


fig = plt.figure(figsize=(20,15))
ax = fig.add_subplot(1,1,1)
ax.hist(df["age"], bins = 7)
plt.title('Ages distribution', fontsize = 20)
plt.xlabel('Age', fontsize = 20)
plt.ylabel('Frecuency', fontsize = 20)


# ### 3) Analyse the total percentage of “yes” responses to belief in crisis. Analyse as a function of career stage and methodological approach.

# #### 3.1) Belief

# In[17]:


df["belief"].value_counts().plot.pie(figsize = (20,15), autopct = "%1.0f%%", fontsize = 20)


# In[ ]:




