from google.cloud import storage
import time
from google.cloud import bigquery

SERVICE_ACCOUNT_JSON = r'D:\GoogleCloud\Dataflow\iam_key\admiral-1409-b37ef309cbe2.json'
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

table_id = "admiral-1409.HR.locations"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("location_id", "INTEGER", mode="REQUIRED"),
        bigquery.SchemaField("location_name", "STRING", mode="REQUIRED"),
    ],
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows =1, autodetect=True
)

sql_qry = """
        TRUNCATE TABLE admiral-1409.HR.locations
"""
qry_job = client.query(sql_qry)

file_path = r'D:\GoogleCloud\Dataflow\dataset\locations.csv'
source_file = open(file_path, "rb")
job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()