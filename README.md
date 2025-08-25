# Phishing Project Report: Amazon Credential Theft

## How to run the project

- Open the project in a Dev container.

- Run the following commands:

  - reference to "[trusting_cert_instructions.md](trust_cert_instructions.md)"
  - python3 ./collect.py
  - python3 ./phishing.py

- Open browser with the URL: `https://localhost:4443/amazon-login.html#`

- Now enter email and password (does not have to be correct), then click Sign-in. It intentionally tell you have incorrect credentials, keep enter your input 3 times.

- At the third time, it should automatically navigate back to the unauthenticated Amazon home page.

- Go back to the project folder, there should be a file `stolen.txt` that stores all captured credentials.

