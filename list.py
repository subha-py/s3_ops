from connector import get_bucket_obj

def list_objects(server, bucket_name, username='admin', password='Syst7mt7st'):
    bucket_obj = get_bucket_obj(server, bucket_name, username, password)
    count = 0
    for _ in bucket_obj.objects.all():
        count +=1
    return count

if __name__ == '__main__':
    server = '10.14.7.173'
    view = 'vst_s3_1_0_view_ssdnvbe_1'
    bucket = get_bucket_obj(server, view)
    count = list_objects(bucket)
    print(count)