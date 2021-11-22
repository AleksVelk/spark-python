//load data to df and calculate number of jobs posted on daily basis, per each city

val df = spark.read.json("marketing_sample.ldjson")

val jobs_per_city_day = df.groupBy("post_date","city").count().orderBy(desc("post_date"))
jobs_per_city_day.show()