#!/usr/bin/env python
# coding: utf-8

# <h1 style="color: red; text-align=center;"> Summer Olympic Medallists 1896-2008 </h1>
# <center>
#   <img align="center" width="600" height="100" src="Summer_Olympic.jpg">
# </center>
# 

# In[2]:


#import the libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#read the csv file
df=pd.read_csv("Summer_Olympic_medallists_1896-2008.csv")

df.head()
#df.shape


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# <h1 style="color: darkBlue;"> 1- Pie Plot</h1>
# <h6 style="color: darkred;"> Fatimah </h6>

# In[14]:


plt.figure(figsize=(15,8), dpi=90)
df["Gender"].value_counts(normalize=True).plot(
kind="pie",
legend=True,
autopct='%.f%%',
colors = ['#6478DD', '#EF81E2'] )
plt.title( "Total Number of Men and Female in Summer Olympic 1896-2008",c="black")


# <h1 style="color: darkBlue;"> 2-Cities Total of Participating in the Summer Olympic 1896-2008</h1>
# <center>
#   <img align="center" width="600" height="100" src="cities.jpg">
# </center>
# <h6 style="color: darkred;"> Fatimah </h6>

# In[13]:


plt.figure(figsize=(20,13), dpi=300)

city=sns.histplot(data=df,
x="Edition",
hue="City",
binwidth=3.5,
palette=sns.color_palette(['#FF0000', '#FF6500','#009AFF','#FFE500',
                                     '#16C540','#9816C5','#E53CA4','#749BE7',
                                     '#00A36C', '#CD7F32','#FFC000','#FF4433',
                                      '#FA8072','#9F2B68','#FF00FF','#F4511E',
                                      '#0000FF','#9DC223','#B4F43A','#B84811',
                                      '#87EFB8','#336600']),
multiple="stack",
).set_title(' Cities Total of Participating in the Summer Olympic 1896-2008')



# <h1 style="color: darkBlue;"> 3-Medal for Men and Women</h1>
# <h6 style="color: darkred;"> Lubna </h6>

# In[15]:


plt.figure(figsize=(15,8), dpi=90)
sns.set(style="darkgrid")

my_color={"Men":"#6478DD","Women":"#EF81E2"}

sns.boxplot(x="Medal", 
y="Edition",
hue="Gender",
data=df , 
width=0.5,
palette=my_color
)

plt.title('Medal for men and women')
plt.show()


# <h1 style="color: darkBlue;"> 4-Number  of Male and Female in Olympic 1896-2008</h1>
# <h6 style="color: darkred;"> Lubna </h6>

# In[16]:


plt.figure(figsize=(15,8), dpi=90)
sns.kdeplot(
    data=df, 
    x="Edition",
    hue="Gender",
    palette=my_color
)
plt.title( "Number  of Male and Female in Olympic 1896-2008",c="black")
plt.show()


# <h1 style="color: darkBlue;"> 5- Total Number of Medals for each City</h1>
# <center>
#   <img align="center" width="600" height="100" src="metals.png">
# </center>
# <h6 style="color: darkred;"> Monyah </h6>

# In[17]:


plt.figure(figsize=(14,9))
med_color={"Gold":"#E3CC07","Silver":"#AEA6A6","Bronze":"#EBAC29"} 
sns.histplot(
    df.sort_values('City').reset_index(),
    y="City",
    hue="Medal",
    multiple="stack",
    alpha=0.8,
    palette=med_color
)
plt.title("Total Number of Medals for each City",c='black');
plt.show()


# <h1 style="color: darkBlue;">subplot</h1>
# <h6 style="color: darkred;"> Fatimah </h6>

# In[21]:


f, sub = plt.subplots(2,2, figsize=(17,20),dpi=200)

# fig.tight_layout()
f.suptitle("Summer Olympic 1896-2008", fontsize="larger")

#1. pie
df["Gender"].value_counts(normalize=True).plot(
                                          kind="pie",
                                          legend=True,
                                          autopct='%.f%%',
                                          colors = ['#6478DD', '#EF81E2'],
                                          title="Total Number of Men and Female in Summer Olympic 1896-2008",
                                          ax=sub[0,0])

#--------------------------------------------------------------------------------------------------
#2. Histogram
sns.kdeplot(
    data=df, 
    x="Edition",
    hue="Gender",
    palette=my_color,
    ax=sub[1,1]
).set_title("Number of Male and Female in Olympic 1896-2008",c="black")

                  
#-------------------------------------------------------------------------------------------------
#3. BoxPlot
my_color={"Men":"#6478DD","Women":"#EF81E2"}

sns.boxplot(x="Medal", 
            y="Edition",
            hue="Gender",
            data=df , 
            width=0.5,
           palette=my_color,
            ax=sub[0,1]
           ).set_title("Medal for men and women",c="black")

#-------------------------------------------------------------------------------------------------
#4 Histogram 
med_color={"Gold":"#E3CC07","Silver":"#AEA6A6","Bronze":"#EBAC29"} 
sns.histplot(
    df.sort_values('City').reset_index(),
    y="City",
    hue="Medal",
    multiple="stack",
    alpha=0.8,
    palette=med_color,
    ax=sub[1,0]
).set_title("Total Number of Medals for each City",c="black")


