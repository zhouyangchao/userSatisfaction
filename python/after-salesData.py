#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import numpy as np
#数据可视化包
import pylab as pl
import matplotlib.pyplot as plt
#线性回归库
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#线性回归库
import statsmodels.formula.api as sm
#随机森林库
from sklearn.ensemble import RandomForestRegressor

#对接R中绘图文件中的售后部分和用于售后部分的线性回归




#读取文件
orgData = pd.read_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier.xlsx', header= 1, encoding = 'utf-8')
orgData = pd.DataFrame(orgData)
orgData1 = orgData

#列名重命名
#orgData1.columns = ['id','User_region','User_level','User_purchase_amount','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','If_product_is_intact','If product is faulty','Fault index','Ease of use','Brand awareness to Haier','Awareness to product','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
orgData1.columns = ['id','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','If_product_is_intact','If product is faulty','Fault index','Ease of use','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','User_region','User_level','User_purchase_amount','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Brand awareness to Haier','Awareness to product','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
orgData1.columns = orgData1.columns.str.replace(' ','_')
orgData1.columns

#将'/'和'／'替换为缺失值
orgData2 = orgData1
orgData2 = orgData2.replace('／',np.nan)
orgData2 = orgData2.replace('/',np.nan)

#连续化处理
orgData2.User_level = orgData2.User_level.replace('钻石会员','1')
orgData2.User_level = orgData2.User_level.replace('金牌会员','2')
orgData2.User_level = orgData2.User_level.replace('银牌会员','3')
orgData2.User_level = orgData2.User_level.replace('铜牌会员','4')
orgData2.User_level = orgData2.User_level.replace('PLUS会员','5')
orgData2.User_level = orgData2.User_level.replace('PLUS会员[试用]','6')
#考虑一下价格如何离散化，统一量纲
orgData2.loc[orgData2.User_purchase_amount <= 1299, 'User_purchase_amount'] = 1
orgData2.loc[orgData2.User_purchase_amount >= 4999, 'User_purchase_amount'] = 3
orgData2.loc[(orgData2.User_purchase_amount > 1299) & (orgData2.User_purchase_amount < 4999), 'User_purchase_amount'] = 2

"""
orgData2.loc[orgData2.Changing_price <= 100, 'Changing_price'] = 1
orgData2.loc[orgData2.Changing_price >= 300, 'Changing_price'] = 3
orgData2.loc[(orgData2.Changing_price > 100) & (orgData2.Changing_price < 300), 'Changing_price'] = 2

orgData2.loc[orgData2.Price_gap <= 100, 'Price_gap'] = 1
orgData2.loc[orgData2.Price_gap >= 300, 'Price_gap'] = 3
orgData2.loc[(orgData2.Price_gap > 100) & (orgData2.Price_gap < 300), 'Price_gap'] = 2
"""

orgData2.Order_from = orgData2.Order_from.replace('iphone客户端','1')
orgData2.Order_from = orgData2.Order_from.replace('ipad客户端','2')
orgData2.Order_from = orgData2.Order_from.replace('android客户端','3')
orgData2.Order_from = orgData2.Order_from.replace('微信购物','4')
orgData2.Order_from = orgData2.Order_from.replace('网页购物','5')

orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('配送员安装','8')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('半天内','7')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('当天下午','6')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('次日','5')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('第三日','4')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('三到七日','3')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('大于一周','2')
orgData2.Installer_arrival_time = orgData2.Installer_arrival_time.replace('无安装服务','1')

orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('质量问题','1')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('安装问题','2')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('物流配送','3')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('预约安装','4')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('价格波动','5')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('效果一般','6')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('咨询赠品','7')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('售前咨询','8')

#删除不必要的列
orgData2 = orgData2.drop('id',axis = 1)
orgData2 = orgData2.drop('User_region',axis = 1)
orgData2 = orgData2.drop('Comment_time',axis = 1)
orgData2 = orgData2.drop('Product_model',axis = 1)
orgData2 = orgData2.drop('Customer_satisfaction_level',axis = 1)

orgData2.info()

#统一指标类型
orgData2['If_delivered_on_original/promised_date'] = orgData2['If_delivered_on_original/promised_date'].astype('object')
orgData2['If_delivered_right_product'] = orgData2['If_delivered_right_product'].astype('object')
orgData2['If_intact_in_transit'] = orgData2['If_intact_in_transit'].astype('object')
orgData2['If_the_last_Km_is_difficult'] = orgData2['If_the_last_Km_is_difficult'].astype('object')
orgData2['If_the_last_Km_is_served'] = orgData2['If_the_last_Km_is_served'].astype('object')
orgData2['If_any_after-sales_processes'] = orgData2['If_any_after-sales_processes'].astype('object')
orgData2['If_product_is_faulty'] = orgData2['If_product_is_faulty'].astype('object')
orgData2['If_price_changed_in_a_short_time'] = orgData2['If_price_changed_in_a_short_time'].astype('object')
orgData2['Compared_to_different_channel_prices'] = orgData2['Compared_to_different_channel_prices'].astype('object')


#处理缺失值
#缺失列：服务兵到达时间 Installer_arrival_time为factor类型
orgData2.loc[(orgData2.Installer_arrival_time.isnull()) & (orgData2.Installer_arrival_speed == 1), 'Installer_arrival_time'] = '2'
orgData2.loc[(orgData2.Installer_arrival_time.isnull()) & (orgData2.Installer_arrival_speed == 2), 'Installer_arrival_time'] = '3'
orgData2.loc[(orgData2.Installer_arrival_time.isnull()) & (orgData2.Installer_arrival_speed == 3), 'Installer_arrival_time'] = '5'
orgData2.loc[(orgData2.Installer_arrival_time.isnull()) & (orgData2.Installer_arrival_speed == 4), 'Installer_arrival_time'] = '7'
orgData2.loc[(orgData2.Installer_arrival_time.isnull()) & (orgData2.Installer_arrival_speed == 5), 'Installer_arrival_time'] = '8'
#缺失列：针对【服务兵到达时间】为【无安装服务】
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'Installer_arrival_speed'] = 1
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'Installation_speed'] = 1
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'Installation_effect'] = 1
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'Explaining_service'] = 1
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'Installer_service_attitude'] = 1
orgData2.loc[(orgData2.Installer_arrival_time == 1) , 'If_installer_has_any_charges'] = '0'
orgData2.loc[(orgData2.Installer_arrival_time == 1) & (orgData2.If_any_gifts.isnull()) , 'If_any_gifts'] = '0'
orgData2.loc[(orgData2.Installer_arrival_time == 1) & (orgData2.If_the_bill_is_complete.isnull()), 'If_the_bill_is_complete'] = '1'

"""
#缺失列：处理四行价格有关的列
orgData2.loc[orgData2.If_price_changed_in_a_short_time == 0, 'Changing_price'] = '0'
orgData2.loc[orgData2.Compared_to_different_channel_prices == 0, 'Price_gap'] = '0'
"""

#缺失列：设备故障指数
orgData2.loc[orgData2.If_product_is_faulty == 0, 'Fault_index'] = 0

#再次统一指标类型
orgData2['If_installer_has_any_charges'] = orgData2['If_installer_has_any_charges'].astype('object')
orgData2['If_the_bill_is_complete'] = orgData2['If_the_bill_is_complete'].astype('object')
orgData2['If_any_gifts'] = orgData2['If_any_gifts'].astype('object')
orgData2['User_purchase_amount'] = orgData2['User_purchase_amount'].astype('object')
orgData2['Changing_price'] = orgData2['Changing_price'].astype('object')
orgData2['Price_gap'] = orgData2['Price_gap'].astype('object')

#区分有售后过程和没有售后过程
orgData3 = orgData2.loc[orgData2['If_any_after-sales_processes']==1,]#有售后过程
orgData3 = orgData3.drop('If_any_after-sales_processes',axis = 1)#去掉是否有售后过程的一列

#缺失列：维修次数，缺失值填充为0，没有维修的维修次数为0
orgData3['Number_of_fixing'] = orgData3['Number_of_fixing'].fillna(0)

#缺失列：客服处理效率，用均值取整填充
orgData3.Customer_service_processing_efficiency = orgData3.Customer_service_processing_efficiency.fillna(999) #填充缺失值为了转格式
orgData3.Customer_service_processing_efficiency = orgData3.Customer_service_processing_efficiency.astype('int') #转格式为了求均值
orgData3.Customer_service_processing_efficiency = orgData3.Customer_service_processing_efficiency.replace(999,np.nan) #还原缺失值为了求均值
orgData3['Customer_service_processing_efficiency'] = orgData3['Customer_service_processing_efficiency']\
    .fillna(round(orgData3['Customer_service_processing_efficiency'].mean())) #求均值填充上缺失值

#缺失列：联系客服原因
orgData3['Reason_contacting_customer_service'] = orgData3['Reason_contacting_customer_service'].fillna('9')
#缺失列：维修结果
orgData3['Fixing_result'] = orgData3['Fixing_result'].fillna('2')
#缺失列：换货结果
orgData3['Replacement_result'] = orgData3['Replacement_result'].fillna('2')
#缺失列：退货结果
orgData3['Return_result'] = orgData3['Return_result'].fillna('2')
orgData3.info()

#定位缺失值行
orgData3.loc[orgData3['After-sales_service_satisfaction'].isnull(),:].index
orgData3.loc[orgData3['If_problems_solved'].isnull(),:].index
orgData3.loc[orgData3['After-sales_attitude'].isnull(),:].index
orgData3.loc[orgData3['After-sales_processing_efficiency'].isnull(),:].index
#发现只有五行，删除好了
orgData3.drop(orgData3.index[[6,23,21,36,69]],axis = 0,inplace = True)

#再次转换数据类型
orgData3['After-sales_service_satisfaction'] = orgData3['After-sales_service_satisfaction'].astype('int')

#做线性回归
xx7 = orgData3[['If_any_revisiting','If_any_gifts_from_after-sales','If_contacted_customer_service',
                'Reason_contacting_customer_service','Customer_service_processing_efficiency',
                'If_fixing','Number_of_fixing','Fixing_result','If_replacement','Replacement_result',
                'If_return','Return_result','After-sales_processing_efficiency','After-sales_attitude',
                'If_problems_solved']]
xx7_test = orgData3[['Reason_contacting_customer_service',
                'If_fixing','Number_of_fixing','Fixing_result','If_replacement','Replacement_result',
                'If_return','Return_result','After-sales_processing_efficiency','After-sales_attitude',
                'If_problems_solved']]

yy7 = orgData3[['After-sales_service_satisfaction']]

#X2包含售后服务满意度
X2 = orgData3[['Cost-effective_satisfaction','Reputation_and_price_satisfaction',
               'Order_processing_satisfaction','Logistics_distribution_satisfaction',
               'Installation_satisfaction','Product_quality_satisfaction',
               'After-sales_service_satisfaction']]


y1 = orgData3[['Customer_satisfaction']]
y2 = orgData3[['Consistent_with_the_description_satisfaction']]
y3 = orgData3[['Compared_with_pre-purchase_expectations_satisfaction']]
y4 = orgData3[['Customer_complaints_index']]
y5 = orgData3[['Will_of_repurchase_the_same_brand_and_the_same_kind_of_product']]
y6 = orgData3[['Will_of_repurchase_the_same_brand']]
y7 = orgData3[['Recommended_to_buy_index']]
y8 = orgData3[['Brand_awareness_to_Haier']]
y9 = orgData3[['Awareness_to_product']]

#linear_model = sm.OLS(yy7, xx7.astype(float)).fit()
#linear_model.summary()

#随机森林重要性排序
forest = RandomForestRegressor()
#forest.fit(X2,y1)
#importances = forest.feature_importances_
#importance_df = pd.DataFrame(index=len(importances),columns=['viarible','importance'])
#for i in range(0,len(importances)):
#    importances_df.importance = importances[i]

#输出excel文件 for SPSS
orgData3.to_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据-有售后.xlsx', encoding='utf-8')
#输出csv文件  for R
orgData3.to_csv('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据-有售后.csv', encoding='utf-8')
