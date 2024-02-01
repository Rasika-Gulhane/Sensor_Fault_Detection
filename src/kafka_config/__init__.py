
import os



#Cloud APIs
API_KEY = "HRII4SKKHB7S7UTH" #os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL = "https://psrc-wrp99.us-central1.gcp.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = "79EmmPBcyLXK2H+hEt/8PlHlYwlOLHcUDrGqd2Qv8nh73gqFm23AzDZ+dEIEB2l0" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# Authenti cation related variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

# schema related variables
SCHEMA_REGISTRY_API_KEY = "PFANYTEZOVD4V35S" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "DM5VBhGlLnEaUkxYBcbG42bbeUk7LeJZvLifVbB1AfR50BsZ7vZkkIjAJP318uir"  #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

