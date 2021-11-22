//identify the top 10 most active companies by number of positions opened

df.groupBy("company_name").count().select("company_name","count").orderBy(desc("count")).show(10)
