//calculate average salary per job title and state

def remove_characters(str:String):String = {str.replaceAll(",",".").replaceAll("hour","").replaceAll("\\$","").replaceAll("\\/","")}

val udf_remove_characters = udf(remove_characters _)

val df_clean = df.filter($"salary_offered".isNotNull && $"salary_offered"  =!= "" && $"salary_offered" =!= '0' && $"salary_offered" =!= "N/A" && $"salary_offered" =!= "Competitive" && $"salary_offered" =!= "DOE").withColumn("salary",udf_remove_characters($"salary_offered")).select("salary","job_title","state")

val df_salary_split = df_clean.withColumn("salary",substring_index(col("salary"), "-", 1).cast("int"))

val df_avg_salary = df_salary_split.groupBy("job_title","state").avg("salary")
df_avg_salary.show()