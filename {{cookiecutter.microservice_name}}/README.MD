# Development with Aerospike db 

## Install Aerospike

```
docker run -d --name aerospike -p 3000:3000 -p 3001:3001 -p 3002:3002 -p 3003:3003 aerospike
```

#### Optional
```
-v <DIRECTORY>:/opt/aerospike/etc
```

## Install Aerospike client 
```
pip install aerospike
```

### Fixing issue with SSL
```
brew update && brew upgrade
brew uninstall openssl; brew uninstall openssl; brew install https://github.com/tebelorg/Tump/releases/download/v1.0.0/openssl.rb
```

## Load Demo data 
```python
import aerospike

config = {
    'hosts': [
        ( '127.0.0.1', 3000 )
    ],
    'policies': {
        'timeout': 1000 # milliseconds
    }
}

client = aerospike.client(config)

client.connect()
 
NAME_SPACE = 'test'
DB_SET = 'CustomerInfo' ## Aerospike set

key = (NAME_SPACE, DB_SET, "1") ## third tuple value is key 
bins = {
  "id": "1",
  "firstName": "Petar",
  "lastName": "Markovic",
  "sex": "Male",
  "address": "Belgrade, Belgrade",
  "birthDate": "16.02.1995",
  "phoneMobile": "00034234234",
  "phoneHome": "324234324234",
  "phoneBusiness": "24324234",
  "emailHome": "petar@markovic.com",
  "emailBusiness": None,
  "company": None
}

client.put(key, bins) ## You should get 0 as response if ok

```

#### Build index for Query()
```python

import aerospike

config = {
    'hosts': [
        ( '127.0.0.1', 3000 )
    ],
    'policies': {
        'timeout': 1000 # milliseconds
    }
}

client = aerospike.client(config)

client.connect()
 
NAME_SPACE = 'test'
DB_SET = 'CustomerInfo' ## Aerospike set

# Get only the records with 'name' = 'Robert'
# Build an index called 'my_name_idx' on on the 'name' bin in test.demo

index_name = 'id_idx'
client.index_string_create(NAME_SPACE, DB_SET, 'id', index_name)

```


## Documentation
- https://www.aerospike.com/docs/client/python/usage/kvs/record-structure.html
- https://www.aerospike.com/docs/client/python/usage/query/query.html
- https://hub.docker.com/_/aerospike
- https://www.aerospike.com/apidocs/python/predicates.html