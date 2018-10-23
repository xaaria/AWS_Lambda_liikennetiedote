import requests
import json
import boto3

"""
    $$$
        
        Puhtaasti AWS:n palveluiden testaukseen 
        sekä AWS:n opetteluun käytetty koodi.
        
    $$$

Credientals are in ~/.aws/credientals
Other settings in ~/.aws/config
User name: "***"
"""

# # #

aws_hosted = False # Runs in AWS (True) or local?

# Liikennevirasto API
# Mittausaseman URL-osoite [GET], tukee toistaiseksi vain yhtä asemaa, vaikka onkin taulukko...
api_url = ['http://tie.digitraffic.fi/api/v1/data/tms-data/23451' ]
# Näitä arvoja tutkaillaan... (kaistat molempiin suuntiin)
lookup_value_names = ['KESKINOPEUS_5MIN_LIUKUVA_SUUNTA1', 'KESKINOPEUS_5MIN_LIUKUVA_SUUNTA2']

# SES
ses_sender_email = '<REPLACE ME>' # go to SES settings to verify email address
ses_receivers = ['<REPLACE ME>'] # list of receivers

speed_alert_limit = 50 # km/h



# Aseta tämä AWS:ssä pääfunktioksi. Älä muuta parametreja.
def lambda_handler(event, context):

    # Connect to AWS
    if aws_hosted == True:
        aws_session = boto3.Session() # Automatic
    else:
        aws_session = boto3.Session(profile_name='app')
        
       




    try:
        res = requests.get(api_url[0])
    except Exception:
        raise RuntimeError

    if res.status_code == 200:
        print('Request status 200')

        data = json.loads( res.text ) # .loads(): json to python format
         
        #print(data)

        try:
            sensors = data.get('tmsStations')[0].get('sensorValues')
        except Exception:
            raise ValueError

        # print( sensors )
        print("---\n")

        for sensor in sensors:
            if sensor.get('name', None) in lookup_value_names:

                speed = sensor.get('sensorValue', 0)
            
                content_line = sensor.get('name', '') + ' :: ' + str(speed) + ' ' + sensor.get('sensorUnit', '')
                print( content_line )

                # Send to email (SES)

                ses_client = aws_session.client('ses')
                
                if speed <= speed_alert_limit:
                
                    try:
                        ses_res = ses_client.send_email(
                            Source=ses_sender_email,
                            Destination={
                                'ToAddresses': ses_receivers
                            },
                            Message={
                                'Subject': {
                                    'Data': 'Liikennetiedote',
                                    'Charset': 'UTF-8'
                                },
                                'Body': {
                                    'Text': {
                                        'Data': content_line,
                                        'Charset': 'UTF-8'
                                    }
                                }
                            }
                        )
                        print( ses_res.get('MessageId', '-1') )
                    except Exception:
                        print('Sending message failed!')
                else:
                    print('    Speed OK (limit %i). No alert sent...' % speed_alert_limit)
                # endif
    else:
        print('GET request failed! Code :: ' + str(res.status_code))
