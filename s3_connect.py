import boto3
from botocore.client import Config
from config import ACCESS_KEY_ID, ACCESS_SECRET_KEY, BUCKET_NAME

def s3_connection():
    try:
        s3 = boto3.resource(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=ACCESS_SECRET_KEY,
            config=Config(signature_version='s3v4')
        )
    except Exception as e:
        print(e)
    else:
        return s3


def s3_img_upload(s3,f):
    try:
        data = open('./capture/' +f, 'rb') # '로컬의 해당파일경로'+ 파일명 + 확장자
        s3.Bucket(BUCKET_NAME).put_object(
            Key=f, Body=data, ContentType='image/jpg')
    except Exception as e:
        return False
    return True

    
def s3_get_img_url(filename):
    return f"https://{BUCKET_NAME}.s3.ap-northeast-2.amazonaws.com/{filename}"

default_img = f"https://{BUCKET_NAME}.s3.ap-northeast-2.amazonaws.com/default_image.png"
