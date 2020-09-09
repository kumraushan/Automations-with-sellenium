import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
bucket_name = 'uploadingimageandgettingurl'
#for bucket in s3.buckets.all():
 #   print(bucket.name)

# with open('batmanRises.png', 'wb') as img:
#     s3.download_fileobj('uploadingimageandgettingurl', 'batmanRises.png' , img)

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name=file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#with open('putatoe.jpg', 'rb') as img:
#     s3.upload_fileobj(img ,'uploadingimageandgettingurl', "putatoe_image")


s3.upload_file('batmanRises.png',bucket_name, 'batman_img' ,ExtraArgs = {'ACL':'public-read'})

key = "putatoe_image"
location = s3.get_bucket_location(Bucket = bucket_name)['LocationConstraint']
url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
print(url)





