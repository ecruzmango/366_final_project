# Phishing Project Report: Amazon Credential and Credit Card Theft

## How to run the project

Run the following commands:

1. openssl req -x509 -out localhost.crt -keyout localhost.key \
   -newkey rsa:2048 -nodes -sha256 \
   -subj '/CN=localhost' -extensions EXT -config <( \
    printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

1. openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
1. mv localhost.crt cert.pem
1. mv localhost.key key.pem
1. python3 ./sample_HTTPS.py   
