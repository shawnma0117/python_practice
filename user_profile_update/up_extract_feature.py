#-*- coding:utf8 -*-
#!/usr/bin/env python

import os
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession,Row
# from pyspark.sql import HiveContext
from pyspark.sql.functions import *
import types
import sys
# import utility
def get_num_repartition_by_size(data_size, one_partition_data_size = 100000):
    """ compute num partitions for given size, and each partition has the size of one_partition_data_size except
    for the last partition. Once the data_size is 0 return 1 partition as default
    Args:
        one_partition_data_size: 100,000 by default
        data_size: the data_size needs to split
    Returns: num of the partitions
    """
    return max(int(math.ceil(float(data_size) / one_partition_data_size)), 1)

def encodify(a):#a is a list
   out=[]
   for e in a:
	   if isinstance(e,unicode):
		   out.append(e)
	   else:
		   out.append(str(e))
   return '|'.join(out)
'''
20180910 updates:
1. 从运营dmp存储的hdfs路径读取数据
2. 利用pyspark api, 让代码变得简短。
3. 支持多个人群提取画像特征。只要把人群路径加入path_dict即可。

'''
if __name__=="__main__":	
	conf = SparkConf().set('spark.rpc.message.maxSize', '512') \
	.set('spark.core.connection.ack.wait.timeout', '600') \
	.set('spark.rdd.compress', 'true') \
	.set('spark.driver.memory', '20g') \
	.set("spark.driver.maxResultSize", "20g")\
	.set('spark.executor.instances', "100") \
	.set('spark.executor.memory', '20g') \
	.set('spark.executor.cores', '4') \
	.set('spark.default.parallelism', '1600') \
	.set('spark.memory.useLegacyMode', 'true') \
	.set('spark.storage.memoryFraction','0.6') \
	.set('spark.shuffle.memoryFraction', '0.2')\
	.set("spark.sql.shuffle.partitions", '1000')\
	.set('spark.sql.autoBroadcastJoinThreshold', '200000000')\
	.set('spark.sql.broadcastTimeout','1000')\
	.set("spark.scheduler.listenerbus.eventqueue.size", "1000000")

	# sc = SparkContext(conf=conf, appName = "intel")
	spark = SparkSession.builder.appName("hp").config(conf=conf)\
	     .enableHiveSupport() \
	     .getOrCreate()

	sc = spark.sparkContext
	path_dict = {'buy':'/user/jd_ad/dmp/user_tag_data/package_black_dragon_679/latest/part*',\
				'view_nobuy':'/user/jd_ad/dmp/user_tag_data/package_black_dragon_678/latest/part*'
				}
	HDFS_BASE_PATH = '/user/jd_ad/ads_inno/shawnma/hp_workstation'
	crowd = dict()
	for key,path in path_dict.items():
		rdd = sc.textFile(path).map(lambda p: Row(pin=p))
		df_schema = spark.createDataFrame(rdd)
		crowd[key] = df_schema


	# PROFILE_VARS='user_log_acct,cpp_base_ulevel,cpp_base_age, cpp_base_sex, cpp_base_marriage, cpp_base_education,cpp_base_profession,cpp_addr_province, cpp_addr_city,csf_sale_client,csf_sale_paytype,csf_medal_mombaby,csf_medal_beauty,csf_medal_wine,cgp_cust_purchpower,cfv_sens_promotion,cfv_cate_90dcate1,cfv_cate_90dcate2, cfv_cate_90dcate3,cfv_brand_favor'
	PROFILE_VARS='user_log_acct,cpp_base_ulevel,cpp_base_age, cpp_base_sex, cpp_base_marriage, cpp_base_education,cpp_base_profession,csf_sale_client,csf_sale_paytype,cgp_cust_purchpower,cfv_sens_promotion'

	pf = spark.sql("select {0} from app.app_ba_userprofile_prop_nonpolar_view_ext where dt='ACTIVE'".format(PROFILE_VARS)).cache()
	pf.createOrReplaceTempView("pf_table")

	# out_pf_dict = dict()
	# cond = [pf.user_log_acct== trim(lower(df.pin))] # 画像表的pin是小写
	for name,df in crowd.items():
		out_name = name + '_pf'
		out_pf = pf.join(df, pf.user_log_acct == trim(lower(df.pin)),how='left_semi')
		out_pf.write.csv(path=os.path.join(HDFS_BASE_PATH,out_name),sep='|',mode='overwrite')
	
	# distribution of extended attributes of working station
	# crowd['buy'].createOrReplaceTempView('buy')

	spark.stop()

