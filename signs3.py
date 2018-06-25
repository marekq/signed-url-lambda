#!/usr/bin/python
# marek kuczynski
# @marekq
# www.marek.rocks
# coding: utf-8

import boto3, os

client      = boto3.client('s3', region_name = os.environ['s3_region'])
mail        = boto3.client('ses')

def handler(event, context):
	bucketn = os.environ['s3_bucket']
	days    = os.environ['days_to_expiry']	
    
	s3list	= client.list_objects(Bucket = bucketn)
	html	= ['<html><body><table>']
	
	for x in s3list['Contents']:
		u	= client.generate_presigned_url('get_object', Params = {'Bucket': bucketn, 'Key': x['Key']}, ExpiresIn = int(86400) * int(days))
		html.append('<tr><td><a href='+u+'>'+x['Key']+'</a></td></tr>')
		
	html.append('</td></tr></table></body></html>')
	mail.send_email(
        Source = os.environ['from_email'],
        Destination = {'ToAddresses': [os.environ['to_email']]},
        Message = {
            'Subject': {
                'Data': 's3 signed URLs',
                'Charset': 'utf8'
            },
            'Body': {
                'Html': {
                    'Data': '\n'.join(html),
                    'Charset': 'utf8'
                }
            }
        }
    )
