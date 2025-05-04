# Phishing Project Report: Amazon Credential and Credit Card Theft

## How to run the project

- Run the following commands:

  - pip install -r package.txt
  - openssl req -x509 -out localhost.crt -keyout localhost.key \
    -newkey rsa:2048 -nodes -sha256 \
    -subj '/CN=localhost' -extensions EXT -config <( \
     printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

  - openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
  - mv localhost.crt cert.pem
  - mv localhost.key key.pem
  - python3 ./collect.py
  - python3 ./phishing.py

- Open browser with the URL: `https://localhost:4443/amazon-login.html#`

- Now enter email and password (does not have to be correct), then click Sign-in.

- Go back to the project folder, there should be a file `stolen.txt` that stores all captured credentials.
