# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import numpy as np

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

#价格离散化 高低顺序会产生奇怪结果
#orgData2.User_purchase_amount_LEVEL[orgData2.User_purchase_amount_LEVEL <= 1299] = '低' #SettingWithCopyWarning
orgData2.loc[orgData2.User_purchase_amount >= 4999, 'User_purchase_amount'] = '高'
orgData2.loc[orgData2.User_purchase_amount <= 1299, 'User_purchase_amount'] = '低'
orgData2.loc[(orgData2.User_purchase_amount > 1299) & (orgData2.User_purchase_amount < 4999), 'User_purchase_amount'] = '中'
#输出csv文件
orgData2.to_csv('/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier没有离散化.csv', encoding='utf-8')