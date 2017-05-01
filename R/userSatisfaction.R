library(arules)
library(arulesViz)
#library(xlsx)
orgData = read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier1.csv")
head(orgData)
tail(orgData)
orgData1 = orgData
#删除无用的列
orgData1$X<-NULL
orgData1$id_LEVEL<-NULL
orgData1$Comment_time_LEVEL<-NULL
orgData1$User_region_LEVEL<-NULL
#orgData1$Changing_price_LEVEL<-NULL
#orgData1$Price_gap_LEVEL<-NULL
orgData1$Product_model_LEVEL<-NULL
orgData1$Customer_satisfaction_level_LEVEL<-NULL
#只关心客户满意度为后项的规则
#rules_好评 <- apriori(orgData1, parameter =list(supp=0.1,conf=0.3,minlen = 2,maxlen = 2),appearance = list(rhs = c("Customer_satisfaction_LEVEL=好评"), default="lhs"))
#rules_中评 <- apriori(orgData1, parameter =list(supp=0.1,conf=0.3,minlen = 2,maxlen = 2),appearance = list(rhs = c("Customer_satisfaction_LEVEL=中评"), default="lhs"))
#rules_差评 <- apriori(orgData1, parameter =list(supp=0.1,conf=0.3,minlen = 2,maxlen = 2),appearance = list(rhs = c("Customer_satisfaction_LEVEL=差评"), default="lhs"))
#查看好评的关联规则
#filter_rules<-subset(rules,items %pin% c("satisfaction"))
#rule_filtered_好评_2 <- subset(rules_filtered_by_lift_好评, subset = !(lhs %pin% c("Customer_satisfaction_level_LEVEL"))) #去掉包含原生评价等级的前项
#rule_filtered_好评_3<-subset(rule_filtered_好评_2,lhs %pin% c("好评") | lhs %pin% c("是"))
#rules_filtered_by_lift_好评 <- subset(rules_好评,lift>1.53)#通过提升度筛选
#rule_ordered_by_lift_好评<-sort(rules_filtered_by_lift_好评,by = "lift")#通过提升度排序
#summary(rule_ordered_by_lift_好评)
#length(rule_ordered_by_lift_好评)
#inspect(rule_ordered_by_lift_好评[0:10])

#查看中差评的关联规则
#通过提升度筛选
#rules_filtered_by_lift_中评 <- subset(rules_中评,lift>1.3)
#rules_filtered_by_lift_差评 <- subset(rules_差评,lift>1.1)
#rule_filtered_差评_1<-subset(rules_filtered_by_lift_差评,lhs %pin% c("差评") | lhs %pin% c("否")) #筛选出前项包含“差评”或“否”的规则
#summary(rules_filtered_by_lift_差评)
#inspect(rules_filtered_by_lift_差评)

#找出最后一层的变量
#rules_subset2<-subset(rules_subset,items %pin% c("satisfaction"))

#验证关联规则信度
#Figures <- interestMeasure(rules_filtered_by_lift_差评, method=c("coverage","fishersExactTest","conviction", "chiSquared"), transactions=orgData1) 
#inspect(filter_rules[0:10])

#保存到外部文件
#write(rules_好评, file="/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/rules_好评.txt", sep=",", quote=TRUE, row.names=FALSE)  
#保存到数据框
#rules_好评_df <- as(rules_好评, "data.frame")
#rules_中评_df <- as(rules_中评, "data.frame")
#rules_差评_df <- as(rules_差评, "data.frame")

#毕业设计用到的
rules <- apriori(orgData1, parameter =list(supp=0.1,conf=0.8,minlen = 2,maxlen = 2))
rules_subset<- subset(rules,lift>=1.5|lift<=0.67)
#rules_subsets2
rules_subset2<-subset(rules_subset,items %pin% c("satisfaction"))
rules_第一层次<-c(1,6,7,8,9,12,13,15,18,19,21,22,[24],[25],[27],33,[61])
rules_第二层次<-c(40,45,48,51,54,55,57,58,64,82,[83])
rules_第三层次<-c(46,70,72,75,88,89,[94],[95],105,107)
#rules_subset2_补集
rules_subset2_补集<-subset(rules_subset,subset = !(items %pin% c("satisfaction")))
rules_第一层次_补集<-c()
rules_第二层次_补集<-c()
rules_第三层次_补集<-c()
#test
test<-subset(rules_subset,items %pin% c("Customer_complaints_index_LEVEL"))
rules_第一层次_test<-c()
rules_第二层次_test<-c()
rules_第三层次_test<-c(1,2,10)
#test1
test1<-subset(rules_subset,items %pin% c("Awareness_to_product_LEVEL"))
rules_第一层次_test1<-c()
rules_第二层次_test1<-c()
rules_第三层次_test1<-c(14,15)
#test2
test2<-subset(rules_subset,items %pin% c("Brand_awareness_to_Haier"))
rules_第一层次_test2<-c()
rules_第二层次_test2<-c()
rules_第三层次_test2<-c(5,12)
#至此，真的数据到此结束。可以放宽置信度和支持度再测。



#作图
par(family='STKaiti')
plot(rules_好评, measure="confidence", method="graph", control=list(type="items"), shading = "lift")
plot(rules_中评, measure="confidence", method="graph", control=list(type="items"), shading = "lift")
plot(rules_差评, measure="confidence", method="graph", control=list(type="items"), shading = "lift")
plot(rules_subset2, measure="confidence", method="graph", control=list(type="items"), shading = "lift")
