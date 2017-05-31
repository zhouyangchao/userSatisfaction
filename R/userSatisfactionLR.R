library(stats)
library(psych)
library(car)#vif检验多重共线性
orgDataLR = read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据.csv",encoding = 'UTF-8')

orgDataLR_aftersales = read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据-有售后.csv",encoding = 'UTF-8')
orgDataLR_aftersales$Reason_contacting_customer_service = as.factor(orgDataLR_aftersales$Reason_contacting_customer_service)
orgDataLR_aftersales$Fixing_result = as.factor(orgDataLR_aftersales$Fixing_result)
orgDataLR_aftersales$Replacement_result = as.factor(orgDataLR_aftersales$Replacement_result)
#orgDataLR_aftersales$Return_result = as.factor(orgDataLR_aftersales$Return_result)

model_aftersales = lm(yy7~If_any_revisiting+If_any_gifts_from_after.sales+If_contacted_customer_service
                      +Reason_contacting_customer_service+Customer_service_processing_efficiency
                      +If_fixing+Number_of_fixing+Fixing_result+If_replacement+Replacement_result
                      +If_return+Return_result+After.sales_processing_efficiency+After.sales_attitude
                      +If_problems_solved,data = orgDataLR_aftersales)
#去掉是否回访、售后是否有小礼物、是否联系客服、客服处理效率后
model_aftersales = lm(yy7~
                      Reason_contacting_customer_service
                      +If_fixing+Number_of_fixing+Fixing_result+If_replacement+Replacement_result
                      +If_return+Return_result+After.sales_processing_efficiency+After.sales_attitude
                      +If_problems_solved,data = orgDataLR_aftersales)
#去掉是否修理、修理次数、是否换货、是否退货后
model_aftersales = lm(yy7~
                        Reason_contacting_customer_service
                      +Fixing_result+Replacement_result+Return_result
                      +After.sales_processing_efficiency+After.sales_attitude
                      +If_problems_solved,data = orgDataLR_aftersales)
#去掉维修结果、换货结果、退货结果后
model_aftersales = lm(yy7~Reason_contacting_customer_service
                      +After.sales_processing_efficiency+After.sales_attitude
                      +If_problems_solved,data = orgDataLR_aftersales)
#去掉问题是否解决后
model_aftersales = lm(yy7~Reason_contacting_customer_service
                      +After.sales_processing_efficiency+After.sales_attitude,
                      data = orgDataLR_aftersales)
summary(model_aftersales)


names(orgDataLR)
y1 = orgDataLR$Customer_satisfaction
y2 = orgDataLR$Customer_complaints_index
y3 = orgDataLR$Will_of_repurchase_the_same_brand_and_the_same_kind_of_product
y4 = orgDataLR$Will_of_repurchase_the_same_brand
y5 = orgDataLR$Recommended_to_buy_index
y6 = orgDataLR$Brand_awareness_to_Haier
y7 = orgDataLR$Awareness_to_product
#四个争议变量
y8 = orgDataLR$Consistent_with_the_description_satisfaction
y9 = orgDataLR$Compared_with_pre-purchase_expectations_satisfaction
#y10 = orgDataLR$Cost.effective_satisfaction
#y11 = orgDataLR$Reputation_and_price_satisfaction


yy1 = orgDataLR$Cost.effective_satisfaction
yy2 = orgDataLR$Reputation_and_price_satisfaction
yy3 = orgDataLR$Order_processing_satisfaction
yy4 = orgDataLR$Logistics_distribution_satisfaction
yy5 = orgDataLR$Installation_satisfaction
yy6 = orgDataLR$Product_quality_satisfaction
yy7 = orgDataLR_aftersales$After.sales_service_satisfaction

#感知价值——>客户满意
#model_toSatisfaction <- lm(y1~)

#客户满意度变量对所有二级变量
model1 = lm(y1~User_level+User_purchase_amount+Order_from+Order_processing_speed+Sending_out_speed
            +Delivery_speed+If_delivered_on_original.promised_date+If_delivered_right_product
            +If_intact_in_transit+If_the_last_Km_is_difficult+Distribution_staff_service_attitude
            +Installer_arrival_time+Installer_arrival_speed+Installation_speed+Installation_effect
            +Explaining_service+Installer_service_attitude+If_installer_has_any_charges+If_the_bill_is_complete
            +If_any_gifts+If_any_after.sales_processes+If_price_changed_in_a_short_time
            +Changing_price+Compared_to_different_channel_prices+Price_gap+Product_functional_diversity
            +Energy_saving_index+Performance_index+Noise_situation+Aesthetics_performance
            +If_product_is_intact+If_product_is_faulty+Fault_index+Ease_of_use,data = orgDataLR)
#客户满意度变量对所有一级变量
model2 = lm(y1~Cost.effective_satisfaction+Reputation_and_price_satisfaction
            +Order_processing_satisfaction+Logistics_distribution_satisfaction
            +Installation_satisfaction+Product_quality_satisfaction
            +Consistent_with_the_description_satisfaction+Compared_with_pre.purchase_expectations_satisfaction,data = orgDataLR)
model2_step<-step(model2)
#二级变量对相应的一级变量
model3 = lm(yy1~User_level+User_purchase_amount+Order_from+Order_processing_speed+Sending_out_speed
            +Delivery_speed+If_delivered_on_original.promised_date+If_delivered_right_product
            +If_intact_in_transit+If_the_last_Km_is_difficult+Distribution_staff_service_attitude
            +Installer_arrival_time+Installer_arrival_speed+Installation_speed+Installation_effect
            +Explaining_service+Installer_service_attitude+If_installer_has_any_charges+If_the_bill_is_complete
            +If_any_gifts+If_any_after.sales_processes+If_price_changed_in_a_short_time
            +Changing_price+Compared_to_different_channel_prices+Price_gap+Product_functional_diversity
            +Energy_saving_index+Performance_index+Noise_situation+Aesthetics_performance
            +If_product_is_intact+If_product_is_faulty+Fault_index+Ease_of_use,data = orgDataLR)

model4 = lm(yy2~User_level+User_purchase_amount+Order_from+Order_processing_speed+Sending_out_speed
            +Delivery_speed+If_delivered_on_original.promised_date+If_delivered_right_product
            +If_intact_in_transit+If_the_last_Km_is_difficult+Distribution_staff_service_attitude
            +Installer_arrival_time+Installer_arrival_speed+Installation_speed+Installation_effect
            +Explaining_service+Installer_service_attitude+If_installer_has_any_charges+If_the_bill_is_complete
            +If_any_gifts+If_any_after.sales_processes+If_price_changed_in_a_short_time
            +Changing_price+Compared_to_different_channel_prices+Price_gap+Product_functional_diversity
            +Energy_saving_index+Performance_index+Noise_situation+Aesthetics_performance
            +If_product_is_intact+If_product_is_faulty+Fault_index+Ease_of_use,data = orgDataLR)
