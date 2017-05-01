# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import numpy as np
#数据可视化包
import pylab as pl
import matplotlib.pyplot as plt
import seaborn as sns
#线性回归库
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#线性回归库
import statsmodels.formula.api as sm
#随机森林库
from sklearn.ensemble import RandomForestRegressor




#读取文件
orgData = pd.read_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier.xlsx', header= 1, encoding = 'utf-8')
orgData = pd.DataFrame(orgData)
orgData1 = orgData

#列名重命名
#orgData1.columns = ['id','User_region','User_level','User_purchase_amount','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','Intactness performance','If product is faulty','Fault index','Ease of use','Brand awareness to Haier','Awareness to product','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
orgData1.columns = ['id','Order_from','Comment_time','Order_processing_speed','Sending_out_speed','Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product','If intact in transit','If the last Km is difficult','If the last Km is served','Distribution staff service attitude','Installer arrival time','Installer arrival speed','Installation speed','Installation effect','Explaining service','Installer service attitude','If installer has any charges','If the bill is complete','If any gifts','If any after-sales processes','If any revisiting','If any gifts from after-sales','If contacted customer service','Reason contacting customer service','Customer service processing efficiency','If fixing','Number of fixing','Fixing result','If replacement','Replacement result','If return','Return result','After-sales processing efficiency','After-sales attitude','If problems solved','Product model','If price changed in a short time','Changing price','Compared to different channel prices','Price gap','Product functional diversity','Energy saving index','Performance index','Noise situation','Aesthetics performance','Intactness performance','If product is faulty','Fault index','Ease of use','Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction','Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction','Product quality satisfaction','User_region','User_level','User_purchase_amount','Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction','Customer satisfaction','Customer satisfaction level','Customer complaints index','Brand awareness to Haier','Awareness to product','Will of repurchase the same brand and the same kind of product','Will of repurchase the same brand','Recommended to buy index']
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

orgData2.loc[orgData2.Changing_price <= 100, 'Changing_price'] = 1
orgData2.loc[orgData2.Changing_price >= 300, 'Changing_price'] = 3
orgData2.loc[(orgData2.Changing_price > 100) & (orgData2.Changing_price < 300), 'Changing_price'] = 2

orgData2.loc[orgData2.Price_gap <= 100, 'Price_gap'] = 1
orgData2.loc[orgData2.Price_gap >= 300, 'Price_gap'] = 3
orgData2.loc[(orgData2.Price_gap > 100) & (orgData2.Price_gap < 300), 'Price_gap'] = 2

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
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('售前咨询','2')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('物流配送','3')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('咨询赠品','4')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('预约安装','5')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('效果一般','6')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('安装问题','7')
orgData2.Reason_contacting_customer_service = orgData2.Reason_contacting_customer_service.replace('价格波动','8')

#删除不必要的列
orgData2 = orgData2.drop('id',axis = 1)
orgData2 = orgData2.drop('User_region',axis = 1)
orgData2 = orgData2.drop('Comment_time',axis = 1)
orgData2 = orgData2.drop('Product_model',axis = 1)
orgData2 = orgData2.drop('Customer_satisfaction_level',axis = 1)

#改变指标类型
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
#缺失列：处理四行价格有关的列
orgData2.loc[orgData2.If_price_changed_in_a_short_time == 0, 'Changing_price'] = '0'
orgData2.loc[orgData2.Compared_to_different_channel_prices == 0, 'Price_gap'] = '0'
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
orgData4 = orgData2.loc[orgData2['If_any_after-sales_processes']==0,]#无售后过程
orgData4 = orgData4.drop('If_any_after-sales_processes',axis = 1)#去掉是否有售后过程的一列
orgData4 = orgData4.drop('After-sales_service_satisfaction',axis = 1)#去掉售后满意度
#orgData4去掉售后相关指标
orgData4 = orgData4.drop('If_any_revisiting',axis = 1)
orgData4 = orgData4.drop('If_any_gifts_from_after-sales',axis = 1)
orgData4 = orgData4.drop('If_contacted_customer_service',axis = 1)
orgData4 = orgData4.drop('Reason_contacting_customer_service',axis = 1)
orgData4 = orgData4.drop('Customer_service_processing_efficiency',axis = 1)
orgData4 = orgData4.drop('If_fixing',axis = 1)
orgData4 = orgData4.drop('Number_of_fixing',axis = 1)
orgData4 = orgData4.drop('Fixing_result',axis = 1)
orgData4 = orgData4.drop('If_replacement',axis = 1)
orgData4 = orgData4.drop('Replacement_result',axis = 1)
orgData4 = orgData4.drop('If_return',axis = 1)
orgData4 = orgData4.drop('Return_result',axis = 1)
orgData4 = orgData4.drop('After-sales_processing_efficiency',axis = 1)
orgData4 = orgData4.drop('After-sales_attitude',axis = 1)
orgData4 = orgData4.drop('If_problems_solved',axis = 1)
#原数据单纯比较"有没有售后过程"对满意度的区别
orgData5 = orgData2
orgData5 = orgData5.drop('If_any_revisiting',axis = 1)
orgData5 = orgData5.drop('If_any_gifts_from_after-sales',axis = 1)
orgData5 = orgData5.drop('If_contacted_customer_service',axis = 1)
orgData5 = orgData5.drop('Reason_contacting_customer_service',axis = 1)
orgData5 = orgData5.drop('Customer_service_processing_efficiency',axis = 1)
orgData5 = orgData5.drop('If_fixing',axis = 1)
orgData5 = orgData5.drop('Number_of_fixing',axis = 1)
orgData5 = orgData5.drop('Fixing_result',axis = 1)
orgData5 = orgData5.drop('If_replacement',axis = 1)
orgData5 = orgData5.drop('Replacement_result',axis = 1)
orgData5 = orgData5.drop('If_return',axis = 1)
orgData5 = orgData5.drop('Return_result',axis = 1)
orgData5 = orgData5.drop('After-sales_processing_efficiency',axis = 1)
orgData5 = orgData5.drop('After-sales_attitude',axis = 1)
orgData5 = orgData5.drop('If_problems_solved',axis = 1)
#处理售后满意度缺失值
orgData5['After-sales_service_satisfaction'] = orgData5['After-sales_service_satisfaction'].fillna(3)
#orgData5 = orgData5.drop('After-sales_service_satisfaction',axis = 1)#去掉售后满意度

#X包含缺失值，需要处理
"""
X = orgData2[['User_level','User_purchase_amount','Order_from','Order_processing_speed','Sending_out_speed',
              'Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product',
              'If_intact_in_transit','If_the_last_Km_is_difficult', 'If_the_last_Km_is_served',
              'Distribution_staff_service_attitude', 'Installer_arrival_time','Installer_arrival_speed',
              'Installation_speed','Installation_effect', 'Explaining_service','Installer_service_attitude',
              'If_installer_has_any_charges','If_the_bill_is_complete', 'If_any_gifts','If_any_after-sales_processes',
              'If_any_revisiting','If_any_gifts_from_after-sales', 'If_contacted_customer_service',
              'Reason_contacting_customer_service','Customer_service_processing_efficiency',
              'If_fixing','Number_of_fixing', 'Fixing_result', 'If_replacement','Replacement_result',
              'If_return', 'Return_result','After-sales_processing_efficiency', 'After-sales_attitude',
              'If_problems_solved','Product_functional_diversity','Energy_saving_index','Performance_index',
              'Noise_situation', 'Aesthetics_performance','Intactness_performance',
              'If_product_is_faulty', 'Fault_index','Ease_of_use']]
"""
#X1包含四行价格列
X1 = orgData5[['User_level','User_purchase_amount','Order_from','Order_processing_speed','Sending_out_speed',
              'Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product',
              'If_intact_in_transit','If_the_last_Km_is_difficult', 'If_the_last_Km_is_served',
              'Distribution_staff_service_attitude', 'Installer_arrival_time','Installer_arrival_speed',
              'Installation_speed','Installation_effect', 'Explaining_service','Installer_service_attitude',
              'If_installer_has_any_charges','If_the_bill_is_complete', 'If_any_gifts',
              'If_any_after-sales_processes',
              'If_price_changed_in_a_short_time','Changing_price',
              'Compared_to_different_channel_prices','Price_gap',
              'Product_functional_diversity','Energy_saving_index','Performance_index',
              'Noise_situation', 'Aesthetics_performance','Intactness_performance',
              'If_product_is_faulty', 'Fault_index','Ease_of_use']]

xx1 = orgData5[['Order_from','Order_processing_speed','Sending_out_speed']]
xx2 = orgData5[['Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product',
              'If_intact_in_transit','If_the_last_Km_is_difficult', 'If_the_last_Km_is_served',
              'Distribution_staff_service_attitude']]
xx3 = orgData5[['Installer_arrival_time','Installer_arrival_speed',
              'Installation_speed','Installation_effect', 'Explaining_service','Installer_service_attitude',
              'If_installer_has_any_charges','If_the_bill_is_complete', 'If_any_gifts']]
xx4 = orgData5[['If_any_after-sales_processes']]
xx5 = orgData5[['If_price_changed_in_a_short_time','Changing_price',
              'Compared_to_different_channel_prices','Price_gap']]
xx6 = orgData5[['Product_functional_diversity','Energy_saving_index','Performance_index',
              'Noise_situation', 'Aesthetics_performance','Intactness_performance',
              'If_product_is_faulty', 'Fault_index','Ease_of_use']]

#X2不含售后服务满意度
X2 = orgData5[['Cost-effective_satisfaction','Reputation_and_price_satisfaction',
               'Order_processing_satisfaction','Logistics_distribution_satisfaction',
               'Installation_satisfaction','Product_quality_satisfaction']]

X3 = orgData5[['Cost-effective_satisfaction','Reputation_and_price_satisfaction',
               'Order_processing_satisfaction','Logistics_distribution_satisfaction',
               'Installation_satisfaction','Product_quality_satisfaction',
               'After-sales_service_satisfaction']]

X4 = orgData5[['Customer_satisfaction','Customer_complaints_index','Brand_awareness_to_Haier',
               'Awareness_to_product']]

y1 = orgData5[['Customer_satisfaction']]
y2 = orgData5[['Consistent_with_the_description_satisfaction']]
y3 = orgData5[['Compared_with_pre-purchase_expectations_satisfaction']]
y4 = orgData5[['Customer_complaints_index']]
y5 = orgData5[['Will_of_repurchase_the_same_brand_and_the_same_kind_of_product']]
y6 = orgData5[['Will_of_repurchase_the_same_brand']]
y7 = orgData5[['Recommended_to_buy_index']]
y8 = orgData5[['Brand_awareness_to_Haier']]
y9 = orgData5[['Awareness_to_product']]

#各模块子目标变量
yy1 = orgData5[['Cost-effective_satisfaction']]
yy2 = orgData5[['Reputation_and_price_satisfaction']]
yy3 = orgData5[['Order_processing_satisfaction']]
yy4 = orgData5[['Logistics_distribution_satisfaction']]
yy5 = orgData5[['Installation_satisfaction']]
yy6 = orgData5[['Product_quality_satisfaction']]
yy7 = orgData3[['After-sales_service_satisfaction']]


"""
#利用随机森林评估指标重要性
forest = RandomForestRegressor()
forest.fit(X1,y1)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
feat_lables = X1.columns[0:]
for f in range(X1.shape[1]):
    print('%2d) %-*s %f' % (f+1,30,feat_lables[f],importances[indices[f]]))


#建立线性回归模型
#使用scikit-learn进行线性回归
orgData5.corr()
plt.matshow(orgData5.corr())
lr = LinearRegression()
lr.fit(X1,y1)
lr.intercept_,lr.coef_
#预测
y_predict = lr.predict(X1)
mean_squared_error(y1,y_predict)#MSE
#作图
#plt.scatter(X,y) #Error:x and y must be the same size
plt.plot(X1,y_predict)
#save image
#plt.savefig('./image/orgData5.png')

#使用statmodels库进行线性回归
#linear_model = sm.OLS(y,X)
#results = linear_model.fit()
linear_model = sm.OLS(y1, X1.astype(float)).fit()
linear_model.summary()
"""

#sns.pairplot(orgData5)

#for R
orgData5.to_csv('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据.csv', encoding='utf-8')
#for SPSS
orgData5.to_excel('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据.xlsx',encoding='utf-8')
