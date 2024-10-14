from connector import get_s3_client
from list import  list_objects

def delete_all_objects(server, viewname, username='admin',
                   password='Syst7mt7st'):
    s3 = get_s3_client(server, username, password)
    s3_bucket = s3.Bucket(viewname)
    bucket_versioning = s3.BucketVersioning(viewname)
    if bucket_versioning.status == 'Enabled':
        s3_bucket.object_versions.delete()
    else:
        s3_bucket.objects.all().delete()

if __name__ == '__main__':
    server = '10.14.7.173'
    view = 'vst_s3_1_0_view_ssdnvbe_1'
    print(list_objects(server, view))
    delete_all_objects(server, view)
    print(list_objects(server, view))