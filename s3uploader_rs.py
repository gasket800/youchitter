import boto3

bucket_name = 'junoyos'
s3 = boto3.resource('s3')

s3.Bucket(bucket_name).upload_file('./booTweetcount_rs.png', 'booTweetcount_rs.png')
s3.Bucket(bucket_name).upload_file('./booTweetcount_rs.data', 'booTweetcount_rs.data')
