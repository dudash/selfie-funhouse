import boto3
import botocore
import urllib

# Setup AWS access and S3 buckets - never git commit defaults for the KEYS!
ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3OUTBUCKET = os.environ.get('S3OUTBUCKET')
S3INBUCKET = os.environ.get('S3INBUCKET')

# lambda might be able to give the session without manually setting it up,
# but for now we will create it ourselves
session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')

def process_selfie(image_key)
    print "started processing a image - ", image_key
    try:
        s3.Bucket(S3INBUCKET).download_file(image_key, '/tmp/' + image_key)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print "The s3 object does not exist:", S3INBUCKET + "/" + image_key
        else:
            raise
    
    # TODO

    return "done processing"

# This lets us run this as a lambda function triggered off incoming photos
# into arriving to a named S3 bucket
def lambda_handler(event, context):
	bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
	print "processing triggered by key=", key
	process_selfie(key)
	return "done handling"

# main entry point
if __name__ == "__main__":
	lambda_handler(42, 42)