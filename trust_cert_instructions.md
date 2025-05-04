# Generate a self-signed cert & key

```bash
openssl req -x509 \
  -out localhost.crt \
  -keyout localhost.key \
  -newkey rsa:2048 \
  -nodes \
  -sha256 \
  -subj '/CN=localhost' \
  -extensions EXT \
  -config <(printf "\
[dn]
CN=localhost
\
[req]
distinguished_name = dn
\
[EXT]
subjectAltName=DNS:localhost
\
keyUsage=digitalSignature
\
extendedKeyUsage=serverAuth")
```

- You only need this one command to get `localhost.crt` and `localhost.key`.
- If you’d rather use a custom dev hostname—e.g., `amz.com` or `amzn.com`—just replace **localhost** everywhere (in the CN and SAN).

---

# Trust the certificate

## macOS

1. Double-click the `localhost.crt` file to open Keychain Access.
2. Drag it into the **System** or **login** keychain.
3. Find the cert, right-click → **Get Info** → **Trust** → set **When using this certificate** to **Always Trust**.
4. Quit & reopen your browser.

_Or via CLI:_  
```bash
sudo security add-trusted-cert -d \
  -r trustRoot \
  -k /Library/Keychains/System.keychain \
  localhost.crt
```

## Windows (CLI)

1. Open **Command Prompt** or **PowerShell** **as Administrator**.
2. Run:
   ```powershell
   certutil -addstore "Root" "$(Resolve-Path localhost.crt)"
   ```
3. Restart your browser.

## Linux (Debian/Ubuntu)

```bash
sudo cp localhost.crt /usr/local/share/ca-certificates/ \
  && sudo update-ca-certificates
```

### Fedora / RHEL / CentOS

```bash
sudo cp localhost.crt /etc/pki/ca-trust/source/anchors/ \
  && sudo update-ca-trust extract
```

---

If the certificate isn’t trusted, browsers will warn or block the `https://` connection.
