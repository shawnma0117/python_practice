#-*- coding:utf8 -*-
import os
import pyspark
from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.types import *
import pyspark.sql.functions as func
import types
from pyspark import SparkConf
import sys
import pandas as pd

if __name__=="__main__":	
	conf = SparkConf().set('spark.rpc.message.maxSize', '512') \
	.set('spark.core.connection.ack.wait.timeout', '600') \
	.set('spark.akka.frameSize', '150') \
	.set('spark.rdd.compress', 'true') \
	.set('spark.driver.cores', '4') \
	.set('spark.driver.memory', '4g') \
	.set("spark.driver.maxResultSize", "4g")\
	.set('spark.executor.instances', '100') \
	.set('spark.executor.memory', '12g') \
	.set('spark.executor.cores', '8') \
	.set('spark.default.parallelism', '1600') \
	.set('spark.memory.useLegacyMode', 'true') \
	.set('spark.storage.memoryFraction', '0.5')\
	.set('spark.shuffle.memoryFraction', '0.3')\
	.set("spark.sql.shuffle.partitions", '1000')\
	.set('spark.sql.autoBroadcastJoinThreshold', '200000000')  #约为190MB

	sc=SparkContext(appName="ff",conf=conf)	
	sqlContext=HiveContext(sc)

	click = sqlContext.sql("select user_pin,user_id from ad.ad_waidan_click where advertise_pin='toplife_xhl' and dt>='2018-01-09' and dt<='2018-03-23' and (user_id !='' OR user_pin !='') and is_bill != '1' and ad_plan_id in (113840026,113260686,113088062,113025807,112845304,112676443,112646863,112564469,112534433,112529504,112524145,112501679,111715521,111487177,111251358)").cache()
	sqlContext.registerDataFrameAsTable(click,"click_table")

	click_goodpin = sqlContext.sql("select user_pin from click_table where user_pin not in ('','nobody')").cache()
	sqlContext.registerDataFrameAsTable(click_goodpin, "goodpin")

	pin_supp = sqlContext.sql("select a.pin as user_pin from (select uuid,pin from app.app_uuid_pin_mapping where dt='2018-03-22') a LEFT SEMI JOIN (select user_id from click_table where user_pin in ('','nobody')) b on a.uuid=b.user_id").cache()
	# 从mapping表里捞pin
	sqlContext.registerDataFrameAsTable(pin_supp, "pin_sup")

	click_mapped = sqlContext.sql("select * from goodpin UNION select * from pin_sup").cache() 
	sqlContext.registerDataFrameAsTable(click_mapped, "click_mapped_table")

	pf = sqlContext.sql("select a.* from (select user_log_acct,cpp_base_ulevel,cpp_base_age, cpp_base_sex, cpp_base_marriage, cpp_base_education,cpp_base_profession,cpp_seni_haschild,cpp_addr_province, cpp_addr_city,csf_sale_client,csf_sale_paytype,csf_medal_mombaby,csf_medal_beauty,csf_medal_wine,cgp_cust_purchpower,cfv_sens_promotion,cfv_cate_90dcate1,cfv_cate_90dcate2, cfv_cate_90dcate3,cfv_brand_favor from app.app_ba_userprofile_prop_nonpolar_view_ext where dt = 'ACTIVE') a LEFT SEMI JOIN click_mapped_table b on a.user_log_acct = trim(lower(b.user_pin))").coalesce(20)

	pf.write.csv(path='shawnma/toplife/ysl_click_profile0323',sep='|')