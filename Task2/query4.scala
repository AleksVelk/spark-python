//create a UDF function to clean job description from HTML code contained inside

def replace_html(str:String):String = {str.replaceAll("""<.*?>""", "")}

val udf_replace_html = udf(replace_html _)

val df_clean_desc = df.withColumn("job_desc",udf_replace_html($"html_job_description"))
 df_clean_desc.select("job_desc").show()
