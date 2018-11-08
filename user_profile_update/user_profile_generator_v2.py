#-*- coding:utf8 -*-
import pandas as pd
import numpy as np
import types
import os
import sys

'''
Modified on 2018/04/20
What's new:
1. Delete 'cpp_seni_haschild', which will be not updated in the future
2. More structured coding style
3. Transfer cpp_base_education, cgp_cust_purchpower to int when reading text file, to avoid type error. 

update: 
1.replacing -1 to chinese at first is too time consuming.
2. how to read in two piece of data, and make a shoulder-to-shoulder comparison

'''
# 枚举值处理
education_dict = dict()
education_dict['1'] = u'初中及以下'
education_dict['2'] = u'高中(中专)'
education_dict['3'] = u'大学(专科及本科)'
education_dict['4'] = u'研究生(硕士及以上)'

profession_dict = dict()
profession_dict['a'] = u'金融从业者'
profession_dict['b'] = u'医务人员'
profession_dict['c'] = u'公务员 / 事业单位'
profession_dict['d'] = u'白领 / 一般职员'
profession_dict['e'] = u'工人 / 服务业人员'
profession_dict['f'] = u'教师'
profession_dict['g'] = u'农民'
profession_dict['h'] = u'学生'

purchpower_dict = dict()
purchpower_dict['1'] = u'土豪'
purchpower_dict['2'] = u'高级白领'
purchpower_dict['3'] = u'小白领'
purchpower_dict['4'] = u'蓝领'
purchpower_dict['5'] = u'收入很少'

senspromo_dict = dict()
senspromo_dict['1'] = u'不敏感'
senspromo_dict['2'] = u'轻度敏感'
senspromo_dict['3'] = u'中度敏感'
senspromo_dict['4'] = u'高度敏感'
senspromo_dict['5'] = u'极度敏感'

paytype_dict = dict()
paytype_dict['00000a'] = u'在线微信支付'
paytype_dict['00000b'] = u'白条支付'
paytype_dict['00000c'] = u'其他在线支付'
paytype_dict['1'] = u'货到付款'
paytype_dict['2'] = u'邮局汇款'
paytype_dict['3'] = u'上门自提'
paytype_dict['5'] = u'公司转帐'
paytype_dict['6'] = u'银行卡转帐'
paytype_dict['7'] = u'分期-招行'
paytype_dict['8'] = u'分期付款'
paytype_dict['10'] = u'高校代理-自己支付'
paytype_dict['11'] = u'高校代理-代理垫付'
paytype_dict['12'] = u'月结'
paytype_dict['13'] = u'高校代理－货到付款'
paytype_dict['15'] = u'地铁自提'
paytype_dict['165'] = u'银联手机支付'
paytype_dict['50'] = u'支票'
paytype_dict['51'] = u'现金'
paytype_dict['52'] = u'定金/余额'
paytype_dict['53'] = u'电汇'
paytype_dict['54'] = u'POS'

'''
expand_col_trim:
1. keep the numbers of column after expanding constant.
2. when expanded columns has values like '', replace it with None.
3. for senspromo,take the second column after spliting
'''

def expand_col_trim(exp_df,profile):
    if len(exp_df.columns)>=3:
        exp_df = exp_df.iloc[:,0:3]
        exp_df.rename(columns={0:'c1',1:'c2',2:'c3'},inplace=True)
        exp_df = exp_df.replace(to_replace=[u'',u'-1',-1],value=[None,u'未识别',u'未识别'])
    elif len(exp_df.columns)==2:
        exp_df = exp_df.iloc[:,1]
        exp_df.rename(columns={0:'c1'},inplace=True)
        exp_df.fillna(u'未识别',inplace=True)
    exp_df = pd.concat([profile['user_log_acct'],exp_df],axis=1)
    return exp_df

'''
basic_col_agg:
1. aggregate columns that don't need splitting 
2. sort province, city because they are too long 
'''
def basic_col_agg(df):
    basic = []  # create an empty list
    for i in range(1,len(df.columns)):
        g=df.groupby(df.columns[i]).agg({df.columns[0]:'count'}).rename(columns={df.columns[0]:'count'}).reset_index()
        if df.columns[i] in ['cpp_addr_province','cpp_addr_city']:
          g.sort_values(['count'],ascending=False,inplace=True)        
        all = {g.columns[0]: u'总体' ,'count':g['count'].sum(axis=0)} 
        g= g.append(all, ignore_index=True)
        g['pct'] = g['count']/g.iloc[len(g)-1,1]
        basic.append(g)
    return basic
  
'''
split_col_agg:
1. aggregate columns that need splitting. they have multiple columns, c1,c2,c3.
2. map paytype, promotion code to Chinese because they haven't been. 
'''
def split_col_agg(col_name,df):
    agg=[]
    for i,value in enumerate(df.columns): 
        if i > 0:
            agg.append(df.groupby([value],as_index=False)[df.columns[0]].count().rename(columns={value:'c',df.columns[0]:'count'+str(i)}))
    agg = [df.set_index('c') for df in agg]
    a = agg[0].join(agg[1:],how='outer')
    a['count'] = a.sum(axis=1)
    b = a.filter(['count'],axis=1) # the opposite of df.drop
    b.sort_values(['count'],ascending=False,inplace=True)
    b = b.reset_index()
    b.rename(columns={b.columns[0]: col_name},inplace=True)
    if col_name == 'csf_sale_paytype':
      b[col_name] = b[col_name].apply(lambda x: paytype_dict[str(x)] if x!=u'未识别' else u'未识别')
    elif col_name == 'cfv_sens_promotion':
      b[col_name] = b[col_name].apply(lambda x: senspromo_dict[str(x)] if x!=u'未识别' else u'未识别')
    all = {b.columns[0]:u'总体','count':b['count'].sum(axis=0)}
    b = b.append(all,ignore_index=True)
    b['pct'] = b['count']/b.iloc[len(b)-1,1]
    return b

if __name__== '__main__':
  filename = sys.argv[1]
  cwd = os.getcwd()
  dp = cwd + '/' + filename

  # what variables are selected from HIVE tables, and the order of the variables MATTERS!
  PROFILE_VARS=['user_log_acct','cpp_base_ulevel','cpp_base_age','cpp_base_sex','cpp_base_marriage','cpp_base_education','cpp_base_profession','cpp_addr_province','cpp_addr_city','csf_sale_client','csf_sale_paytype','csf_medal_mombaby','csf_medal_beauty','csf_medal_wine','cgp_cust_purchpower','cfv_sens_promotion','cfv_cate_90dcate1','cfv_cate_90dcate2', 'cfv_cate_90dcate3','cfv_brand_favor']
  # PROFILE_VARS=['user_log_acct','cpp_base_ulevel','cpp_base_age','cpp_base_sex','cpp_base_marriage','cpp_base_education','cpp_base_profession','cpp_addr_province','cpp_addr_city','csf_sale_client','csf_sale_paytype','csf_medal_mombaby','csf_medal_beauty','csf_medal_wine','cgp_cust_purchpower','cfv_sens_promotion']
  profile = pd.read_csv(dp, sep='|', encoding='utf-8', header=None, names=PROFILE_VARS, index_col=False, dtype={'cpp_base_education':np.int32,'cgp_cust_purchpower':np.int32})


  profile = profile.replace(to_replace=[u'',u'-1',-1],value=[None,u'未识别',u'未识别'])
  profile['cpp_base_education'] = profile['cpp_base_education'].apply(lambda x: education_dict[str(x)] if x!=u'未识别' else u'未识别')
  profile['cpp_base_profession'] = profile['cpp_base_profession'].apply(lambda x:profession_dict[str(x)] if x!=u'未识别' else u'未识别')
  profile['cgp_cust_purchpower'] = profile['cgp_cust_purchpower'].apply(lambda x:purchpower_dict[str(x)] if x!=u'未识别' else u'未识别')

  # 新思路，需要分列的字段，与pin一起，单独做一个dataframe
  # 所有需要处理的字段单独处理
  csf_sale_client = profile['csf_sale_client'].str.split('#',expand=True)
  csf_sale_paytype = profile['csf_sale_paytype'].str.split('#',expand=True)
  cfv_sens_promotion = profile['cfv_sens_promotion'].str.split('-',expand=True)
  cfv_cate_90dcate1 = profile['cfv_cate_90dcate1'].str.split('#',expand=True)
  cfv_cate_90dcate2 = profile['cfv_cate_90dcate2'].str.split('#',expand=True)
  cfv_cate_90dcate3 = profile['cfv_cate_90dcate3'].str.split('#',expand=True)
  cfv_brand_favor = profile['cfv_brand_favor'].str.split(',',expand=True)

  basic = profile.drop(['csf_sale_client','csf_sale_paytype','cfv_sens_promotion','cfv_cate_90dcate1','cfv_cate_90dcate2','cfv_cate_90dcate3','cfv_brand_favor'],axis=1)


  split_col_list = [csf_sale_client,csf_sale_paytype,cfv_sens_promotion,cfv_cate_90dcate1,cfv_cate_90dcate2,cfv_cate_90dcate3,cfv_brand_favor]
  # split_col_list = [csf_sale_client,csf_sale_paytype,cfv_sens_promotion]
  after_coltrim_list = []
  after_coltrim_list = map(lambda x: expand_col_trim(x,profile),split_col_list)

  after_coltrim_dict = dict(zip(['csf_sale_client','csf_sale_paytype','cfv_sens_promotion','cfv_cate_90dcate1','cfv_cate_90dcate2','cfv_cate_90dcate3','cfv_brand_favor'],after_coltrim_list))
  # zip的作用是将两个等长的list两两配对构成一个新的tuple list
  # 然后再用dict（）构造函数生成：表名 － 表 结构的字典


  ''' 
  basic: store aggregated result that don't need column splitting 
  advance: store aggregated result that needs column splitting
  '''
  basic_metrics = basic_col_agg(basic)
  advance_metrics = list()


  for key in after_coltrim_dict:
      df = split_col_agg(key,after_coltrim_dict[key])   
      advance_metrics.append(df)


  output_filename=filename.split('.')[0] +'.xlsx'
  writer = pd.ExcelWriter(output_filename, engine='xlsxwriter')
  for df in basic_metrics:
    df.to_excel(writer,df.columns[0],index=False, encoding='utf-8')
  for df in advance_metrics:
    df.to_excel(writer,df.columns[0],index=False, encoding='utf-8')
  writer.save()
