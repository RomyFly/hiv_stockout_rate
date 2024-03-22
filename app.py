#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                   STOCKOUT RATE
#___________________________________________________________________________________________________________________________________________________________________________________

#                                                   This app allow to calculate the stockout rate of PEPFAR health facilities

#                                                   import libraries
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

ad=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Adamawa.xls')
ce=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Centre.xls')
es=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Est.xls')
en=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Extrême-Nord.xls')
lt=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Littoral.xls')
no=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Nord.xls')
nw=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Nord-Ouest.xls')
ou=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Ouest.xls')
su=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Sud.xls')
sw=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Sud-Ouest.xls')
def cle_an(df):
    def  col_nm(df1):
        df1=df
        nw_nom = df1[df1.index==0].values.flatten().tolist()
        old_nom = df1.columns.tolist()
        pref='CNLs_FS09_Quantité physique utilisable restante à la fin du mois '
        #remove the prefix 
        for n in range(len(old_nom)):
            for i in range(len(old_nom)):
                if pref in nw_nom[i]:
                    nw_nom[i]=nw_nom[i].replace(pref,'')
                    i=i+1
            df1=df1.rename(columns={old_nom[n]:nw_nom[n]})
            #df=df.drop(['orgunitlevel1 '],axis=1)
        return df1
    df=col_nm(df)
    df=df.drop(['orgunitlevel1'],axis=1)
    df=df.drop(index=0,axis=1)
    df= df.rename(columns={'name':'productname'})
    return df
        

ad = cle_an(ad)
ce = cle_an(ce)
es = cle_an(es)
en = cle_an(en)
lt = cle_an(lt)
no = cle_an(no)
nw = cle_an(nw)
ou = cle_an(ou)
su = cle_an(su)
sw = cle_an(sw)

df0=pd.concat([ad,ce,es,en,lt,no,nw,ou,su,sw])

pdt_lst=df0.productname.unique()

def split (pdt):
    df =df0[df0.productname==pdt]
    return df
df_abcped=split(pdt_lst[0])
df_abcped['commodity_lbl']='ABC/3TC  120/60mg tabs'
df_tld30=split(pdt_lst[1])
df_tld30['commodity_lbl']='TDF/3TC/DTG  300/300/50mg 30tabs'
df_tld90=split(pdt_lst[2])
df_tld90['commodity_lbl']='TDF/3TC/DTG  300/300/50mg 90tabs'
df_tle30=split(pdt_lst[3])
df_tle30['commodity_lbl']='TDF/3TC/EFV  300/300/400mg 30tabs'
df_tle90=split(pdt_lst[4])
df_tle90['commodity_lbl']='TDF/3TC/EFV  300/300/400mg 90tabs'
df_det=split(pdt_lst[5])
df_det['commodity_lbl']='Determine test'
df=pd.concat([df_abcped,df_tld30,df_tld90,df_tle30,df_tle90,df_det])

#df['Period']=df['Period'].str.replace('Janvier ', '01/01/').str.replace('Février ', '01/02/').str.replace('Mars ', '01/03/').str.replace('Avril ', '01/04/').str.replace('Mai ', '01/05/').str.replace('Juin ', '01/06/').str.replace('Juillet ', '01/07/').str.replace('Août ', '01/08/').str.replace('Septembre ', '01/09/').str.replace('Octobre ', '01/10/').str.replace('Novembre ', '01/11/').str.replace('Décembre ', '01/12/')


prd_lst=df.drop(['orgunitlevel2', 'orgunitlevel3', 'orgunitlevel4', 'orgunitlevel5', 'organisationunitname', 'productname','commodity_lbl'],axis =1)
col=prd_lst.columns.tolist()
df=pd.melt(df,id_vars=['orgunitlevel2', 'orgunitlevel3', 'orgunitlevel4', 'orgunitlevel5', 'organisationunitname', 'productname','commodity_lbl'],value_vars=col,var_name='periodname',value_name='stock on hand')

def prd_chg(row):
    if 'Janvier ' in row['periodname']:
        annees = row['periodname'].replace('Janvier ','')
        return str(annees)+('-01-01')
    elif 'Février ' in row['periodname']:
        annees = row['periodname'].replace('Février ','')
        return str(annees)+('-02-01')
    elif 'Mars ' in row['periodname']:
        annees = row['periodname'].replace('Mars ','')
        return str(annees)+('-03-01')
    elif 'Avril ' in row['periodname']:
        annees = row['periodname'].replace('Avril ','')
        return str(annees)+('-04-01')
    elif 'Mai ' in row['periodname']:
        annees = row['periodname'].replace('Mai ','')
        return str(annees)+('-05-01')
    elif 'Juin ' in row['periodname']:
        annees = row['periodname'].replace('Juin ','')
        return str(annees)+('-06-01')
    elif 'Juillet ' in row['periodname']:
        annees = row['periodname'].replace('Juillet ','')
        return str(annees)+('-07-01')
    elif 'Août ' in row['periodname']:
        annees = row['periodname'].replace('Août ','')
        return str(annees)+('-08-01')
    elif 'Septembre ' in row['periodname']:
        annees = row['periodname'].replace('Septembre ','')
        return str(annees)+('-09-01')
    elif 'Octobre ' in row['periodname']:
        annees = row['periodname'].replace('Octobre ','')
        return str(annees)+('-10-01')
    elif 'Novembre ' in row['periodname']:
        annees = row['periodname'].replace('Novembre ','')
        return str(annees)+('-11-01')
    elif 'Décembre ' in row['periodname']:
        annees = row['periodname'].replace('Décembre ','')
        return str(annees)+('-12-01')
    
        
df['periodname']=df['periodname'].str.replace('Janvier ', '01-01-').str.replace('Février ', '01-02-').str.replace('Mars ', '01-03-').str.replace('Avril ', '01-04-').str.replace('Mai ', '01-05-').str.replace('Juin ', '01-06-').str.replace('Juillet ', '01-07-').str.replace('Août ', '01-08-').str.replace('Septembre ', '01-09-').str.replace('Octobre ', '01-10-').str.replace('Novembre ', '01-11-').str.replace('Décembre ', '01-12-')

#df['period']=df.apply(lambda row: prd_chg(row),axis=1 )
df['period']=pd.to_datetime(df['periodname'], format='%d-%m-%Y', errors='coerce')
df=df.drop(['periodname'],axis=1)


#Display Stock out rate

def stk_sttus(row):
    if pd.isna(row['stock on hand'])==True:
        return 'No data'
    elif row['stock on hand']==0:
        return 'Stock Out'
    elif row['stock on hand']>0:
        return 'Stock Available'
    
df['stockstatus']=df.apply(lambda row: stk_sttus(row),axis=1)



abc=pd.pivot_table(df,index=['orgunitlevel2', 'orgunitlevel3', 'orgunitlevel4', 'orgunitlevel5', 'organisationunitname','commodity_lbl','period'],columns='stockstatus',aggfunc='sum')

print(abc)
    
    