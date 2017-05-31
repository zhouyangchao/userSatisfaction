# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import numpy as np
#用于R中关联规则挖掘，主要进行了变量重命名和


#读取数据
orgData = pd.read_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier.xlsx', header= 1, encoding = 'utf-8',na_rep='/')
orgData = pd.DataFrame(orgData)
#print orgData1.isnull().sum()
#将列名变为英文
orgData1 = orgData
#orgData1.columns = ['id','User_region','User_level','User_purchase_amount','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','If_product_is_intact','If product is faulty','Fault index','Ease of use','Brand awareness to Haier','Awareness to product','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
orgData1.columns = ['id','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','If_product_is_intact','If product is faulty','Fault index','Ease of use','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','User_region','User_level','User_purchase_amount','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Brand awareness to Haier','Awareness to product','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
orgData1.columns = orgData1.columns.str.replace(' ','_')
orgData1.columns
#在英文列名后加上'_LEVEL',表示已离散化
orgData2 = orgData1
orgData2.columns = orgData2.columns + '_LEVEL'
orgData2.columns
#将'/'和'／'替换为缺失值
orgData2 = orgData2.replace('／','/')
orgData2 = orgData2.replace('/',np.nan)


#数据离散化处理
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(0,'没有抱怨')
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(1,'没有抱怨')
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(2,'轻微抱怨')
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(3,'中等抱怨')
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(4,'严重抱怨')
orgData2.Customer_complaints_index_LEVEL = orgData2.Customer_complaints_index_LEVEL.replace(5,'严重抱怨')

orgData2.Compared_to_different_channel_prices_LEVEL = orgData2.Compared_to_different_channel_prices_LEVEL.replace(5,'本产品低')
orgData2.Compared_to_different_channel_prices_LEVEL = orgData2.Compared_to_different_channel_prices_LEVEL.replace(4,'本产品低')
orgData2.Compared_to_different_channel_prices_LEVEL = orgData2.Compared_to_different_channel_prices_LEVEL.replace(3,'持平')
orgData2.Compared_to_different_channel_prices_LEVEL = orgData2.Compared_to_different_channel_prices_LEVEL.replace(2,'本产品高')
orgData2.Compared_to_different_channel_prices_LEVEL = orgData2.Compared_to_different_channel_prices_LEVEL.replace(1,'本产品高')

orgData2.If_price_changed_in_a_short_time_LEVEL = orgData2.If_price_changed_in_a_short_time_LEVEL.replace(5,'购买价格便宜')
orgData2.If_price_changed_in_a_short_time_LEVEL = orgData2.If_price_changed_in_a_short_time_LEVEL.replace(4,'购买价格便宜')
orgData2.If_price_changed_in_a_short_time_LEVEL = orgData2.If_price_changed_in_a_short_time_LEVEL.replace(3,'未明显变动')
orgData2.If_price_changed_in_a_short_time_LEVEL = orgData2.If_price_changed_in_a_short_time_LEVEL.replace(2,'购买价格贵')
orgData2.If_price_changed_in_a_short_time_LEVEL = orgData2.If_price_changed_in_a_short_time_LEVEL.replace(1,'购买价格贵')


orgData2.ix[:,orgData2.columns.str.startswith('If')] = orgData2.ix[:,orgData2.columns.str.startswith('If')].replace(1,'是')
orgData2 = orgData2.replace(5,'好评')
orgData2 = orgData2.replace(4,'好评')
orgData2 = orgData2.replace(3,'中评')
orgData2 = orgData2.replace(2,'差评')
orgData2 = orgData2.replace(1,'差评')
orgData2 = orgData2.replace(0,'否')
orgData2 = orgData2.replace('5','好评')
orgData2 = orgData2.replace('4','好评')
orgData2 = orgData2.replace('3','中评')
orgData2 = orgData2.replace('2','差评')
orgData2 = orgData2.replace('1','差评')
orgData2 = orgData2.replace('0','否')

#价格离散化 高低顺序会产生奇怪结果
#orgData2.User_purchase_amount_LEVEL[orgData2.User_purchase_amount_LEVEL <= 1299] = '低' #SettingWithCopyWarning
orgData2.loc[orgData2.User_purchase_amount_LEVEL >= 4999, 'User_purchase_amount_LEVEL'] = '高'
orgData2.loc[orgData2.User_purchase_amount_LEVEL <= 1299, 'User_purchase_amount_LEVEL'] = '低'
orgData2.loc[(orgData2.User_purchase_amount_LEVEL > 1299) & (orgData2.User_purchase_amount_LEVEL < 4999), 'User_purchase_amount_LEVEL'] = '中'
#print orgData2.User_purchase_amount_LEVEL

"""
orgData2.loc[orgData2.Changing_price_LEVEL >= 300, 'Changing_price_LEVEL'] = '高'
orgData2.loc[orgData2.Changing_price_LEVEL <= 100, 'Changing_price_LEVEL'] = '低'
orgData2.loc[(orgData2.Changing_price_LEVEL > 100) & (orgData2.Changing_price_LEVEL < 300), 'Changing_price_LEVEL'] = '中'

orgData2.loc[orgData2.Price_gap_LEVEL >= 300, 'Price_gap_LEVEL'] = '高'
orgData2.loc[orgData2.Price_gap_LEVEL <= 100, 'Price_gap_LEVEL'] = '低'
orgData2.loc[(orgData2.Price_gap_LEVEL > 100) & (orgData2.Price_gap_LEVEL < 300), 'Price_gap_LEVEL'] = '中'
"""

"""
#在每个数值前添加列名
for i in range(1,3):
    orgData2.ix[:,i] = orgData2.columns[i]+ orgData2.ix[:,i]
for i in range(4,42):
    orgData2.ix[:,i] = orgData2.columns[i]+ orgData2.ix[:,i]
orgData2.ix[:,43] = orgData2.columns[43]+ orgData2.ix[:,43]
for i in range(45,len(orgData2.columns)):
    orgData2.ix[:,i] = orgData2.columns[i]+ orgData2.ix[:,i]
"""

#在每个数值前删除列名
#orgData2.ix[:,1].str.replace(orgData2.columns[1],"")


#orgData2.Will_of_repurchase_the_same_brand_and_the_same_kind_of_product_LEVEL = orgData2.Will_of_repurchase_the_same_brand_and_the_same_kind_of_product_LEVEL.replace(1,'差评')
#orgData2.Order_processing_speed_LEVEL = orgData2.Order_processing_speed_LEVEL.replace(1,'差评')
#orgData2.Sending_out_speed_LEVEL = orgData2.Sending_out_speed_LEVEL.replace(1,'差评')
#orgData2.Delivery_speed_LEVEL = orgData2.Delivery_speed_LEVEL.replace(1,'差评')


#orgData1.notnull()
#orgData1.ix[:,1].notnull()
#返回为true的数据集
#orgData1[orgData1.ix[:,1].str.startswith('/')]
#返回true false值
#orgData1.ix[:,1].str.startswith('/')
#返回该列为空值的列号
#orgData1[orgData1.ix[:,1].str.startswith('/')].ix[:,0]



"""
orgData1.columns
orgData1.columns.summary()
orgData.index
orgData.values
orgData1.shape
orgData1.dtypes#每列数据类型

#行索引
orgData1.loc[0]#对字符型
orgData1.iloc[0]#仅对数字型行标签
orgData.ix[0]#都可，不稳定，但快

#列索引
#orgData.Dept
#orgData['Dept']
orgData.ix[:,0]

#元素索引
#orgData.Dept.ix[0]
#orgData.Dept.loc[0]
#orgData.loc[0].Dept
#orgData.ix[0].Dept
#orgData.ix[0,0]

#切块索引
df.loc[:,['A','B']]

#添加列,删除列
orgData['Dept'] = 1
orgData = orgData.drop('Dept',axis = 1)

#frame2['eastern'] = frame2.state == 'Ohio'

orgData['Dept1','Dept2'] = 1
orgData = orgData.drop(('Dept1', 'Dept2'), axis=1)

orgData['Dept1'] = 1
orgData['Dept2'] = 1
orgData = orgData.drop(['Dept1', 'Dept2'], axis=1)

#删除列
del,pop,drop(inplace)

#添加元素
#sdebt = Series([2.2, 3.3], index=["a","c"])    #注意索引
#f3['debt'] = sdebt
#f3["price"]["c"]= 300

#Business&Society
#Management Communication Quarterly
#Information(Management?) technology Management(Information?)

#统计行数
len(orgData)
#描述性统计
orgData.describe()
#删除对象
#del(orgData2)
#判断对象信息
type(orgData)

#过滤
#df.rain_octsep < 1000
#df[df.rain_octsep < 1000]
#df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)]
#df[df.water_year.str.startswith('199')]
#orgData < 5
#orgData[orgData < 5] = 0
#orgData[101:]
#orgData[:10]
#obj[val]布尔数组，切片，布尔DataFrame

#修改列名
#orgData.columns = ['a', 'b']
#df.columns.values[2] = 'c'
#df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
#df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
#df.columns = df.columns.str.replace('$','')

#old_names = ['$a', '$b', '$c', '$d', '$e']
#new_names = ['a', 'b', 'c', 'd', 'e']
#df.rename(columns=dict(zip(old_names, new_names)), inplace=True)

#按照索引排序
df.sort_index(axis=1, ascending=False)#axis = 1, 按列排序
#按值排序
df.sort_values(by='B')

#要先import才可以看帮助文档
#help(pd.DataFrame.drop)
#print help(pd.read_excel)
print help(pd.DataFrame.to_excel)
"""

#orgData2.to_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier2.xlsx',encoding='utf-8')
orgData2.to_csv('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier1.csv', encoding='utf-8')
