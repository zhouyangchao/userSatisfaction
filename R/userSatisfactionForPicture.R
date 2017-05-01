library(VIM)
library(randomForest)
library(stringr)
library(effects)
orgDataNA = read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier.csv",encoding = 'UTF-8',fileEncoding="UTF-8",header =  T)
orgDataScale = read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据.csv",encoding = 'UTF-8',fileEncoding="UTF-8",header =  T)
orgDataAftersales<-read.csv("/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier连续化数据-有售后.csv",,encoding = 'UTF-8',fileEncoding="UTF-8",header =  T)
names(orgDataNA)
orgDataNA$X<-NULL
orgDataNA$序号<-NULL
orgDataNA$用户所在区块<-NULL
orgDataNA$评论时间<-NULL
orgDataNA$设备型号<-NULL
orgDataScale$X<-NULL
orgDataAftersales$X<-NULL

# #显示汉字
# par(family='STKaiti')
# 
# #为了让长坐标名换行
# Xlabels = c("下单方式","订单\n处理速度","发货速度","配送速度",
#            "是否\n按原定或\n承诺日期\n配送")
# aggr(orgDataNA[,1:35],prop=TRUE,numbers=TRUE)
# aggr(orgDataNA[,36:67],prop=TRUE,numbers=TRUE)
# 
# #标准化数据框
# scale_data <- scale(orgDataScale)
# 
# #为了检验汉字用不用变数字,其实是不用的
# model<-lm(orgDataForPicture$客户满意度总分~orgDataForPicture$下单方式)


#变量重要性可视化
#为了大论文，将变量名换回汉字
c_连续化数据<-c("下单方式","订单处理速度","发货速度","配送速度","是否按原定或承诺日期配送","配送产品是否正确无误","配送过程中设备是否完好","最后一公里是否有难度(上楼、天气、偏远等)","最后一公里是否送达","配送人员服务态度","安装人员到达时间","安装人员到达感知速度","安装人员安装速度","安装人员安装效果","安装人员讲解服务","安装人员服务态度","安装人员有否乱收费","票据是否齐全","有否小礼品赠送","是否有售后过程","短时间内是否变动价格","变动价格","与不同渠道价格相比水平","与不同渠道价格差距","设备功能多样性","设备节能指数","设备性能指数","设备噪声情况","设备外观美观性","设备外观完备性","设备是否故障",	"设备故障指数",	"设备易用性",	"产品性价比感知价值",	"信誉保价感知价值",	"订单处理水平感知价值",	"物流配送感知价值",	"安装质量感知价值",	"售后服务感知价值",	"产品质量感知价值","用户平台等级","用户购买金额",	"产品与描述相符满意度",	"与购买前期望相比满意度",	"客户满意度总分","客户抱怨指数","对该家电品牌感知","对该品牌该款产品感知",	"回购该品牌同类产品意愿",	"回购该品牌产品意愿","推荐选购指数")
names(orgDataScale)<-c_连续化数据
c_aftersales<-c("是否回访","售后有否小礼品/券赠送","是否联系客服","联系客服原因",	"客服处理效率",	"是否维修",	"维修次数","维修结果","是否换货",	"换货结果",	"是否退货",	"退货结果","售后处理效率","售后态度","需求是否解决")
names(orgDataAftersales)[20:34]<-c_aftersales
names(orgDataAftersales)[53]<-c("售后服务感知价值")

#大论文的图
产品性价比感知价值<-randomForest(产品性价比感知价值~与不同渠道价格相比水平
                                 +设备功能多样性+设备噪声情况+设备外观完备性+设备性能指数+设备是否故障+设备易用性,
                                 data = orgDataScale,importance = TRUE)
names(orgDataScale)[8]<-c("最后一公里是否有难度")
物流配送感知价值<-randomForest(物流配送感知价值~配送速度+是否按原定或承诺日期配送+配送产品是否正确无误
                               +配送过程中设备是否完好
                               +最后一公里是否有难度+最后一公里是否送达+配送人员服务态度,
                               data = orgDataScale,importance = TRUE)
#把安装人员安装效果与态度换一下
a<-names(orgDataScale)[16]
names(orgDataScale)[16]<-names(orgDataScale)[14]
names(orgDataScale)[14]<-a
安装质量感知价值<-randomForest(安装质量感知价值~安装人员安装效果+安装人员服务态度+安装人员有否乱收费,
                               data = orgDataScale,importance = TRUE)
售后服务感知价值<-randomForest(售后服务感知价值~售后处理效率+售后态度+需求是否解决,data = orgDataAftersales,importance = TRUE)

#这是换了个啥不知道了，看论文里的顺序
# a<-names(orgDataScale)[27]
# names(orgDataScale)[27]<-names(orgDataScale)[30]
# names(orgDataScale)[30]<-a

产品质量感知价值<-randomForest(产品质量感知价值~设备功能多样性+设备噪声情况+设备外观美观性
                               +设备外观完备性+设备性能指数+设备故障指数,data = orgDataScale,importance = TRUE)
产品与描述相符满意度<-randomForest(产品与描述相符满意度~产品性价比感知价值+产品质量感知价值,data = orgDataScale,importance = TRUE)
与购买前期望相比满意度<-randomForest(与购买前期望相比满意度~产品性价比感知价值
                                     +物流配送感知价值+安装质量感知价值+售后服务感知价值
                                     +产品质量感知价值,data = orgDataScale,importance = TRUE)
客户满意度总分<-randomForest(客户满意度总分~产品性价比感知价值
                             +物流配送感知价值+安装质量感知价值+售后服务感知价值
                             +产品质量感知价值+用户购买金额,data = orgDataScale,importance = TRUE)
客户抱怨指数<-randomForest(客户抱怨指数~产品性价比感知价值
                           +物流配送感知价值+安装质量感知价值+售后服务感知价值
                           +产品质量感知价值,data = orgDataScale,importance = TRUE)
对该家电品牌感知<-randomForest(对该家电品牌感知~
                                 +物流配送感知价值+安装质量感知价值+售后服务感知价值
                               +产品质量感知价值,data = orgDataScale,importance = TRUE)
对该品牌该款产品感知<-randomForest(对该品牌该款产品感知~产品性价比感知价值
                                   +产品质量感知价值,data = orgDataScale,importance = TRUE)


par(family='STKaiti')
varImpPlot(产品性价比感知价值,type = 1)
varImpPlot(物流配送感知价值,type = 1)
varImpPlot(安装质量感知价值,type = 1)
varImpPlot(售后服务感知价值,type = 1)
varImpPlot(产品质量感知价值,type = 1)
varImpPlot(产品与描述相符满意度,type = 2)
varImpPlot(与购买前期望相比满意度,type = 1)
varImpPlot(客户满意度总分,type = 1)
varImpPlot(客户抱怨指数,type = 2)
varImpPlot(对该家电品牌感知,type = 2)
varImpPlot(对该品牌该款产品感知,type = 2)

回购该品牌产品意愿<-randomForest(回购该品牌产品意愿~与购买前期望相比满意度
                                 +客户满意度总分
                                 +客户抱怨指数+对该家电品牌感知,data = orgDataScale,importance = TRUE)
回购该品牌同类产品意愿<-randomForest(回购该品牌同类产品意愿~产品与描述相符满意度
                                     +与购买前期望相比满意度
                                     +客户满意度总分
                                     +客户抱怨指数+对该品牌该款产品感知,data = orgDataScale,importance = TRUE)
推荐选购指数<-randomForest(推荐选购指数~产品与描述相符满意度+与购买前期望相比满意度
                           +客户满意度总分
                           +客户抱怨指数+对该家电品牌感知+对该品牌该款产品感知,data = orgDataScale,importance = TRUE)
varImpPlot(回购该品牌产品意愿,type = 1)
varImpPlot(回购该品牌同类产品意愿,type = 1)
varImpPlot(推荐选购指数,type = 1)

#变量名换成ICSS论文中的英文名
c_连续化数据<-c("Channel order from","Order processing speed","Sending out speed","Delivery speed","If delivered on original/promised date","If delivered the right product","If intact in transit","If the last Km is difficult(bad weather,remote areas etc.)","If the last Km is served","Distribution staff service attitude","Installer arrival time","Installer arrival speed","Installation speed","Installation effect","Explaining service","Installer service attitude","If the installer has any charges","If the bill is complete",	"If any gifts","If any after sales processes","If price changed in a short time","Changing price","Prices compared to different channel","Price gap","Product functional diversity","Energy saving index","Performance index","Noise situation","Aesthetics performance","Intactness performance","If product is faulty",	"Fault index","Ease of use",
           "Cost-effective perceived value",	"Reputation and price perceived value",	"Order processing perceived value",	"Logistics distribution perceived value",	"Installation perceived value",	"After sales service perceived value",	"Product quality perceived value","用户平台等级","用户购买金额","Consistent with the description satisfaction",	"Compared with pre-purchase expectations satisfaction",	"Customer satisfaction score","Customer complaints index","Brand perception","Perception to the product in the brand","Will of repurchase the same brand and the same kind of product",	"Will of repurchase the same brand","Recommended to buy index")
c_ICSS变量名<-str_replace_all(c_连续化数据," ",".")
c_ICSS变量名<-str_replace(c_ICSS变量名,"-",".")
c_ICSS变量名<-str_replace(c_ICSS变量名,"/",".")
names(orgDataScale)<-c_ICSS变量名
c_aftersales<-c("If any revisiting","If any gifts from after sales","If contacted customer service","Reason contacting customer service",	"Customer service processing efficiency",	"If fixing",	"Number of fixing","Fixing result","If replacement","Replacement result",	"If return","Return result","After sales processing efficiency","After sales attitude","If problems solved")
c_ICSS售后变量名<-str_replace_all(c_aftersales," ",".")
names(orgDataAftersales)[20:34]<-c_ICSS售后变量名
names(orgDataAftersales)[53]<-c("After.sales.service.perceived.value")

#ICSS论文的图
Cost.effective.perceived.value<-randomForest(Cost.effective.perceived.value~Prices.compared.to.different.channel
                                 +Product.functional.diversity+Noise.situation+Intactness.performance
                                 +Performance.index+If.product.is.faulty+Ease.of.use,
                                 data = orgDataScale,importance = TRUE)
names(orgDataScale)[8]<-c("If.the.last.Km.is.difficult")
Logistics.distribution.perceived.value<-randomForest(Logistics.distribution.perceived.value~Delivery.speed+If.delivered.on.original.promised.date+If.delivered.the.right.product
                               +If.intact.in.transit
                               +If.the.last.Km.is.difficult+If.the.last.Km.is.served+Distribution.staff.service.attitude,
                               data = orgDataScale,importance = TRUE)
a<-names(orgDataScale)[16]
names(orgDataScale)[16]<-names(orgDataScale)[14]
names(orgDataScale)[14]<-a
Installation.perceived.value<-randomForest(Installation.perceived.value~Installation.effect+Installer.service.attitude+If.the.installer.has.any.charges,
                               data = orgDataScale,importance = TRUE)
After.sales.service.perceived.value<-randomForest(After.sales.service.perceived.value~After.sales.processing.efficiency+After.sales.attitude+If.problems.solved,data = orgDataAftersales,importance = TRUE)

#这是换了个啥不知道了，看论文里的顺序
# a<-names(orgDataScale)[27]
# names(orgDataScale)[27]<-names(orgDataScale)[30]
# names(orgDataScale)[30]<-a

Product.quality.perceived.value<-randomForest(Product.quality.perceived.value~Product.functional.diversity+Noise.situation+Aesthetics.performance
                               +Intactness.performance+Performance.index+Fault.index,data = orgDataScale,importance = TRUE)
Consistent.with.the.description.satisfaction<-randomForest(Consistent.with.the.description.satisfaction~Cost.effective.perceived.value+Product.quality.perceived.value,data = orgDataScale,importance = TRUE)
Compared.with.pre.purchase.expectations.satisfaction<-randomForest(Compared.with.pre.purchase.expectations.satisfaction~Cost.effective.perceived.value
                                     +Logistics.distribution.perceived.value+Installation.perceived.value+After.sales.service.perceived.value
                                     +Product.quality.perceived.value,data = orgDataScale,importance = TRUE)
Customer.satisfaction.score<-randomForest(Customer.satisfaction.score~Cost.effective.perceived.value
                             +Logistics.distribution.perceived.value+Installation.perceived.value+After.sales.service.perceived.value
                             +Product.quality.perceived.value,data = orgDataScale,importance = TRUE)
Customer.complaints.index<-randomForest(Customer.complaints.index~Cost.effective.perceived.value
                           +Logistics.distribution.perceived.value+Installation.perceived.value+After.sales.service.perceived.value
                           +Product.quality.perceived.value,data = orgDataScale,importance = TRUE)
Brand.perception<-randomForest(Brand.perception~
                                 +Logistics.distribution.perceived.value+Installation.perceived.value+After.sales.service.perceived.value
                               +Product.quality.perceived.value,data = orgDataScale,importance = TRUE)
Perception.to.the.product.in.the.brand<-randomForest(Perception.to.the.product.in.the.brand~Cost.effective.perceived.value
                                   +Product.quality.perceived.value,data = orgDataScale,importance = TRUE)


par(family='STKaiti')
varImpPlot(Cost.effective.perceived.value,type = 1)
varImpPlot(Logistics.distribution.perceived.value,type = 1)
varImpPlot(Installation.perceived.value,type = 1)
varImpPlot(After.sales.service.perceived.value,type = 1)
varImpPlot(Product.quality.perceived.value,type = 1)
varImpPlot(Consistent.with.the.description.satisfaction,type = 2)
varImpPlot(Compared.with.pre.purchase.expectations.satisfaction,type = 1)
varImpPlot(Customer.satisfaction.score,type = 1)
varImpPlot(Customer.complaints.index,type = 2)
varImpPlot(Brand.perception,type = 2)
varImpPlot(Perception.to.the.product.in.the.brand,type = 2)

Will.of.repurchase.the.same.brand<-randomForest(Will.of.repurchase.the.same.brand~Compared.with.pre.purchase.expectations.satisfaction
                                 +Customer.complaints.index+Brand.perception,data = orgDataScale,importance = TRUE)
Will.of.repurchase.the.same.brand.and.the.same.kind.of.product<-randomForest(Will.of.repurchase.the.same.brand.and.the.same.kind.of.product~Consistent.with.the.description.satisfaction
                                     +Compared.with.pre.purchase.expectations.satisfaction
                                     +Customer.complaints.index+Perception.to.the.product.in.the.brand,data = orgDataScale,importance = TRUE)
Recommended.to.buy.index<-randomForest(Recommended.to.buy.index~Compared.with.pre.purchase.expectations.satisfaction
                           +Customer.complaints.index+Perception.to.the.product.in.the.brand,
                           data = orgDataScale,importance = TRUE)
varImpPlot(Will.of.repurchase.the.same.brand,type = 1)
varImpPlot(Will.of.repurchase.the.same.brand.and.the.same.kind.of.product,type = 1)
varImpPlot(Recommended.to.buy.index,type = 1)

#调节效应的图
model_LR<-lm(客户抱怨指数~产品性价比感知价值+物流配送感知价值+安装质量感知价值+售后服务感知价值
                   +产品质量感知价值+用户购买金额+物流配送感知价值:用户购买金额,
                   data = orgDataScale)
par(family='SimHei')
plot(effect("物流配送感知价值:用户购买金额",model_LR,xlevels = list(用户购买金额=c(1,2,3))),multiline = TRUE,family='SimHei')

#深入分析调节效应
x<-c(1,2,3)
y<-0.184*x-0.5420796
plot(x,y)
abline(lm(y~x))
abline(v=0)
abline(h=0)
curve(0.184*x-0.5420796,1,3,3)



#写出文件供spss导入
write.csv(orgDataScale,"/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier汉字名_预处理过.csv",fileEncoding="UTF-8")
write.csv(orgDataAftersales,"/Users/wangtaiqi/Desktop/海尔数据收集/user_data_for_haier/user_data_for_haier_售后_汉字名_预处理过.csv",fileEncoding="UTF-8")
