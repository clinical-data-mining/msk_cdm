# Minio

Minio is an object store very similar to AWS S3. It allows your data to be remotely accessible via the S3 protocol.

## Python API

Steps to access data using Python Minio client API

1. Log into Minio. If you get an error "Expecting a policy to be set for user `X` or one of their groups", contact Pasha, Arfath or Kohli, Armaan with the 'X' String and the names of the buckets you need access to so we can give you access to these buckets. 
2. Create a "Service Account" with a simple access key and the recommended secret key. Copy the secret key to clipboard on creation.

![](images/minio-account.png)

3. Store your access key and secret key in a python-dotenv file.
#### Create .env
```
# create and populate .env file
$ echo "SECRET_KEY=YOUR_SECRET_KEY" >> .env
$ echo "ACCESS_KEY=YOUR_ACCESS_KEY" >> .env


# verify .env file
$ cat .env
SECRET_KEY=YOUR_SECRET_KEY
ACCESS_KEY=YOUR_ACCESS_KEY

$ ls -la
drwxr-xr-x    4 xxx  xxx   128 Jun  1 11:20 .
drwxr-xr-x  121 xxx  xxx  3872 May 26 13:50 ..
-rw-r--r--    1 xxx  xxx    42 Jun  1 11:20 .env
```

4. Change permissions to the dotenv file so only you can read and write to it. 
#### Permissions
```
$ chmod 600 .env
$ ls -la-rw------- 1 xxx xxx 42 Jun 1 11:20 .env
```
5. `pip install python-dotenv minio`
6. Get the full SSL certifcate chain for the Minio instance
#### SSL Cert
```
openssl s_client -showcerts -verify 5 -connect HOST:PORT > certificate.crt

example:
openssl s_client -showcerts -verify 5 -connect tllihpcmind6:9000 > certificate.crt
```



| URL                                | HOST           | PORT |
|------------------------------------|----------------|------|
| https://tllihpcmind6/minio         | tllihpcmind6   | 9000 |
| https://pllimsksparky3/minio/large | pllimsksparky3 | 9006 |
| https://pllimsksparky3/minio/lake  | pllimsksparky3 | 9007 |
| https://pllimsksparky3/minio/small | pllimsksparky3 | 9008 |
| https://pllimsksparky3/minio/user  | pllimsksparky3 | 9009 |

7. Set up python boiler-plate code for creating a minio client object. 
```
from minio import Minio
import urllib3
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# required for self-signed certs
httpClient = urllib3.PoolManager(
cert_reqs='CERT_REQUIRED',
ca_certs='certificate.crt'
)

# Create secure client with access key and secret key
client = Minio(
"tllihpcmind6:9000",
access_key=ACCESS_KEY,
secret_key=SECRET_KEY,
secure=True,
http_client=httpClient
)


# list objects in a bucket
for ii in client.list_objects("test"):
print(ii.__dict__)
```

8. Try other commands like get_object and put_object from the Minio API.
```
import pandas as pd

obj = client.get_object(<BUCKET>,<CSV_FILE_PATH>)

df = pd.read_csv(obj)
df

# for parquet files
from io import BytesIO
obj = client.get_object(<BUCKET>,<PARQUET_FILE_PATH>)

df = pd.read_parquet(BytesIO(obj.data))

pq_obj = df.to_parquet()
client.put_object(<BUCKET>, <PARQUET_FILE_PATH>, data=BytesIO(pq_obj), length=len(pq_obj))
```






## Access via R

Data stored in minio can be accessed in R in the following fashion:
```
# sample r/minio interface via aws.s3

# load external libs
library(aws.s3)
library(httr)
library(dplyr)

# disable ssl verification (required for the time being)
httr::set_config(config( ssl_verifypeer = 0L ))

# params need to be written to environment
Sys.setenv(AWS_SECRET_ACCESS_KEY="***",
AWS_ACCESS_KEY_ID="***",
AWS_S3_ENDPOINT="tllihpcmind6:9000",  # server name
AWS_DEFAULT_REGION="") # region env variable doesn't work must be specified with each call

# list all buckets
bucketlist(region="")

# get bucket
b <- aws.s3::get_bucket(bucket='sample-bucket', region="")
print(b)

# read csv from minio bucket
obj <- aws.s3::get_object(object="test.csv",
bucket='sample-bucket', region="")
csvcharobj <- rawToChar(obj)  
con <- textConnection(csvcharobj)  
data <- read.csv(file = con)
close(con)
# head(data, n=2)


# write csv file back to minio
con <- rawConnection(raw(0), "r+")
write.csv(data, con)
aws.s3::put_object(file = rawConnectionValue(con),
bucket = "sample-bucket", object = "test_write.csv", region="")
close(con)
```



## Troubleshooting
1. If while making a minio client call (mc) you get a certificate error, use '–insecure' in your call to disable certificate verification. The connection will still be encrypted, ony that the certificate verification process with a certificate authority will be skipped in the SSL protocol. This is sometimes necessary for self-signed certificates. Our certificate is a self-signed certificate issued by MSK Open Systems .

2. **mc: <ERROR> Unable to initialize new alias from the provided credentials. Get "https://pllimsksparky3:9006": dial tcp: lookup pllimsksparky3 on 140.163.135.19:53: server misbehaving.**
   * Solution: Ping the server to get its IP address and add it to you '/etc/hosts' file as '10.254.130.16 pllimsksparky3'.

---
[Documentation adapted from MSK-MIND](https://mskconfluence.mskcc.org/display/MM/Minio)


