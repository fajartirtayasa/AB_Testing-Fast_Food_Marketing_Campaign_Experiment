#!/usr/bin/env python
# coding: utf-8

# # [AB Testing] - Fast Food Marketing Campaign Experiment
# ### by Fajar Tirtayasa

# ![gambar.png](attachment:gambar.png)

# ## [Context & Content]
# Suatu perusahaan makanan cepat saji berencana untuk menambahkan item baru ke menunya. Namun mereka masih belum memutuskan mana di antara **tiga kemungkinan marketing campaign** yang akan digunakan untuk promosi produk tersebut. Untuk menentukan promosi mana yang memiliki pengaruh terbesar pada penjualan, item baru diperkenalkan di lokasi di beberapa pasar yang dipilih secara acak. Promosi yang berbeda digunakan di setiap lokasi, dan penjualan mingguan item baru **dicatat selama empat minggu pertama**. Tujuannya adalah untuk **mengevaluasi hasil pengujian A/B dan memutuskan strategi pemasaran mana yang paling berhasil**.
# 
# Dataset: https://drive.google.com/drive/folders/1uzQ0UI1VUogXMss1wMYur3avnyVFPpcE

# ## [Load Data]

# In[69]:


import pandas as pd

df = pd.read_csv('/Data Science/PROA - Data Visualization/Fast Food Dataset/WA_Marketing-Campaign.csv')
df


# ## [Exploratory Data Analysis]
# ### Checking Data

# In[70]:


df.sample(10)


# In[71]:


df.info()


# In[72]:


df['LocationID'] = df['LocationID'].astype('object')
df['Promotion'] = df['Promotion'].astype('category')
df['week'] = df['week'].astype('category')


# In[73]:


df.info()


# In[74]:


df.describe()


# In[75]:


df.describe(include='object')


# In[76]:


df.describe(include='category')


# ### The Amount of Data for Each Promotion

# In[77]:


cek = pd.DataFrame(df.groupby('Promotion')['Promotion'].count())
cek = cek.rename(columns={'Promotion':'Count of Promotion'})
cek = cek.reset_index()
cek


# In[78]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,6))
plt.pie(cek['Count of Promotion'], labels = cek['Promotion'], autopct='%1.2f%%')
plt.title('Percentage of Data for Each Promotion', loc='center', pad=10, fontsize=15)
plt.show()


# ### The Amount of Data for Each Market Size

# In[79]:


cek2 = pd.DataFrame(df.groupby('MarketSize')['MarketSize'].count())
cek2 = cek2.rename(columns={'MarketSize':'Count of MarketSize'})
cek2 = cek2.reset_index()
cek2


# In[80]:


plt.figure(figsize=(6,6))
plt.pie(cek2['Count of MarketSize'], labels = cek2['MarketSize'], autopct='%1.2f%%')
plt.title('Percentage of Data for Each Market Size', loc='center', pad=10, fontsize=15)
plt.show()


# ### Total Sales, Breakdown by Market Size

# In[81]:


df.groupby(['Promotion', 'MarketSize'])['SalesInThousands'].sum().sort_values(ascending=False).unstack().plot(kind='bar', stacked=True)
plt.title('Total Sales, Breakdown by Market Size\nin Last 4 Weeks', loc='center', pad=30, fontsize=15)
plt.xlabel('Promotion', fontsize=12)
plt.ylabel('Total Sales (in Thousands)', fontsize=12)
plt.legend(bbox_to_anchor=(1,1), shadow=True, ncol=1, title='Market Size')
plt.ylim(ymin=0)
plt.xticks(rotation=0)
plt.gcf().set_size_inches(15,8)
plt.tight_layout()
plt.show()


# ### Average Sales per Week for Each Promotion in All Market Size

# In[82]:


df_avg_sales_per_week = df.groupby(['week', 'Promotion'])['SalesInThousands'].mean().unstack()
df_avg_sales_per_week


# In[83]:


df_avg_sales_per_week.plot()
plt.title('Average Sales per Week for Each Promotion\nin All Market Size', fontsize=18, pad=20)
plt.xlabel('Week', fontsize=15)
plt.ylabel('Average Sales (in Thousands)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=40)
plt.gcf().set_size_inches(15,8)
plt.legend(loc='lower left', shadow=True, ncol=1, title='Promotion')


# ### Splitting DataFrame into 3 Market Size: Small, Medium, and Large

# In[84]:


df_small = df.loc[df['MarketSize']=='Small']
df_medium = df.loc[df['MarketSize']=='Medium']
df_large = df.loc[df['MarketSize']=='Large']


# ### Average Sales per Week for Each Promotion in Small Market Size

# In[85]:


box_plot = sns.catplot(x='Promotion',
                      y='SalesInThousands',
                      data=df_small,
                      kind='box')
plt.title('Sales Distribution for Each Promotion\nin Small Market Size', pad=20)
plt.show()


# In[86]:


df_small_avg_sales_per_week = df_small.groupby(['week', 'Promotion'])['SalesInThousands'].mean().unstack()
df_small_avg_sales_per_week


# In[87]:


df_small_avg_sales_per_week.plot()
plt.title('Average Sales per Week for Each Promotion\nin Small Market Size', fontsize=18, pad=20)
plt.xlabel('Week', fontsize=15)
plt.ylabel('Average Sales (in Thousands)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=40)
plt.gcf().set_size_inches(15,8)
plt.legend(loc='lower left', shadow=True, ncol=1, title='Promotion')


# ### Average Sales per Week for Each Promotion in Medium Market Size

# In[88]:


box_plot = sns.catplot(x='Promotion',
                      y='SalesInThousands',
                      data=df_medium,
                      kind='box')
plt.title('Sales Distribution for Each Promotion\nin Medium Market Size', pad=20)
plt.show()


# In[89]:


df_medium_avg_sales_per_week = df_medium.groupby(['week', 'Promotion'])['SalesInThousands'].mean().unstack()
df_medium_avg_sales_per_week


# In[90]:


df_medium_avg_sales_per_week.plot()
plt.title('Average Sales per Week for Each Promotion\nin Medium Market Size', fontsize=18, pad=20)
plt.xlabel('Week', fontsize=15)
plt.ylabel('Average Sales (in Thousands)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=30)
plt.gcf().set_size_inches(15,8)
plt.legend(loc='lower left', shadow=True, ncol=1, title='Promotion')


# ### Average Sales per Week for Each Promotion in Large Market Size

# In[91]:


box_plot = sns.catplot(x='Promotion',
                      y='SalesInThousands',
                      data=df_large,
                      kind='box')
plt.title('Sales Distribution for Each Promotion\nin Large Market Size', pad=20)
plt.show()


# In[92]:


df_large_avg_sales_per_week = df_large.groupby(['week', 'Promotion'])['SalesInThousands'].mean().unstack()
df_large_avg_sales_per_week


# In[93]:


df_large_avg_sales_per_week.plot()
plt.title('Average Sales per Week for Each Promotion\nin Large Market Size', fontsize=18, pad=20)
plt.xlabel('Week', fontsize=15)
plt.ylabel('Average Sales (in Thousands)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=50)
plt.gcf().set_size_inches(15,8)
plt.legend(loc='lower left', shadow=True, ncol=1, title='Promotion')


# ### Some Insight Gained from The Exploratory Data Analysis Process
# 1. Segmentasi pasar untuk perusahaan _fast food_ yang sedang diamati ini didominasi oleh market berukuran menengah. Hal ini ditunjukkan dengan besarnya persentase market berukuran menengah, yakni di atas 50%.
# 2. Secara keseluruhan, _Market Size_ yang menggunakan _marketing campaign_ no.3 menyumbang total penjualan _fast food_ tertinggi.
# 3. Performa rata-rata penjualan mingguan untuk _Market Size_ 'Kecil', 'Menengah', maupun 'Besar' menunjukkan hasil yang relatif lebih baik ketika menggunakan _marketing campaign_ no.1 atau no.3, dibandingkan dengan no.2.
# 
# Selanjutnya, akan dilakukan tes signifikansi dengan t-test untuk menguji apakah terdapat perbedaan yang signifikan antara rata-rata penjualan dari setiap _marketing campaign_.

# ## [Hypothesis]
# H0: Rata-rata penjualan antara dua buah _marketing campaign_ adalah sama.
# 
# H1: Rata-rata penjualan antara dua buah _marketing campaign_ adalah berbeda.

# In[94]:


from scipy.stats import ttest_ind

def test_2_groups(arr_1, arr_2, alpha):
    stat, p = ttest_ind(arr_1, arr_2)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Sebaran distribusinya SAMA (tidak cukup bukti menolak H0)')
    else:
        print('Sebaran distribusi BERBEDA (menolak H0)')

mc_1 = df.loc[df['Promotion']==1, 'SalesInThousands']
mc_2 = df.loc[df['Promotion']==2, 'SalesInThousands']
mc_3 = df.loc[df['Promotion']==3, 'SalesInThousands']


# ## [Hypothesis Test 1 : Marketing Campaign 1 and 2]

# In[95]:


test_2_groups(mc_1, mc_2, 0.05)


# ## [Hypothesis Test 2 : Marketing Campaign 1 and 3]

# In[96]:


test_2_groups(mc_1, mc_3, 0.05)


# ## [Hypothesis Test 3 : Marketing Campaign 2 and 3]

# In[97]:


test_2_groups(mc_2, mc_3, 0.05)


# ## [Conclusion]
# Berdasarkan hipotesis yang telah ditetapkan, H0 akan ditolak apabila nilai p-value < alpha=0.05.
# 
# Sehingga dapat diketahui:
# 1. Terdapat perbedaan yang signifikan antara _marketing campaign_ no.1 dan no.2.
# 2. Tidak terdapat perbedaan yang signifikan antara _marketing campaign_ no.1 dan no.3.
# 3. Terdapat perbedaan yang signifikan antara _marketing campaign_ no.2 dan no.3.
# 
# Berdasarkan hasil ketiga pengujian hipotesis di atas, serta _insight_ yang diperoleh pada tahap _exploratory data analysis_, dapat disimpulkan bahwa perusahaan _fast food_ tersebut lebih baik menggunakan **_marketing campaign_ no.1 atau no.3** sebagai strategi pemasaran produk baru yang akan di-_launching_.
