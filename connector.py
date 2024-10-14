import boto3
from pyhesity import apiauth, apiconnected, api

def get_s3_client(server, username='admin', password='Syst7mt7st'):
    apiauth(vip=server, username=username, password=password)
    # exit if not authenticated
    if apiconnected() is False:
        print('authentication failed')
        exit(1)
    # end authentication =====================================================

    user = api('get', 'sessionUser')

    s3 = boto3.resource('s3',
                        endpoint_url='https://%s:3000' % server,
                        aws_access_key_id=user['s3AccessKeyId'],
                        aws_secret_access_key=user['s3SecretKey'],
                        verify=False)
    return s3
def get_bucket_obj(server, viewname, username='admin', password='Syst7mt7st'):
    s3 = get_s3_client(server, username, password)
    return s3.Bucket(viewname)


