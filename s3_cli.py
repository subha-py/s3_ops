import argparse
from delete import delete_all_objects
from list import  list_objects
parser = argparse.ArgumentParser(
    description='A program to do s3 ops',
    usage='python3 s3_cli.py')

parser.add_argument('--server', help='ip/hostname of the cohesity cluster',
                      type=str, required=True)
parser.add_argument('--username',
                      help='username of cohesity cluster', default='admin',
                      type=str)
parser.add_argument('--password',
                      help='password of cohesity cluster',
                      default='Syst7mt7st', type=str)
parser.add_argument('--viewname',
                      help='name of s3 enabled view',
                      default='s3_view', type=str)
parser.add_argument('--op', help='list/delete-all', default='list')



if __name__ == '__main__':
    arguments = parser.parse_args()
    op = arguments.op
    server = arguments.server
    username = arguments.username
    password = arguments.password
    viewname = arguments.viewname
    if op == 'list':
        count = list_objects(server, viewname,  username, password)
        print(count)
    elif op == 'delete-all':
        count = list_objects(server, viewname, username, password)
        print(f'Number of items before delete all viewname - {viewname} -'
              f' {count}')
        delete_all_objects(server, viewname, username, password)
        count = list_objects(server, viewname, username, password)
        print(f'Number of items after delete all viewname - {viewname}-'
              f' {count}')