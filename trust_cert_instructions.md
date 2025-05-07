
# 🔐 Generating TLS Certificate for `localhost`

The `phishing.py` server needs a TLS certificate to serve over HTTPS on `https://localhost:4443`.

Below are **two ways to generate a local certificate**:
- **Option A (recommended)**: Use [`mkcert`](https://github.com/FiloSottile/mkcert) – fast, trusted, and cross-platform.
- **Option B**: Use `openssl` as a manual fallback if `mkcert` isn't available.

---

## ✅ Option A — Using `mkcert` (Recommended)

### 1️⃣ Install and trust `mkcert` CA (one-time)

- **Windows**
  ```powershell
  choco install mkcert
  mkcert -install
  ```
- **macOS**
  ```bash
  brew install mkcert nss
  mkcert -install
  ```
- **Ubuntu / WSL**
  ```bash
  sudo apt update
  sudo apt install mkcert
  mkcert -install
  ```

> 🔁 **After `mkcert -install`:**
> - Restart your browser (completely quit and reopen).
> - Open a new terminal so `mkcert` is available in your PATH.

### 2️⃣ Generate localhost cert (per project)

```bash
cd path/to/366_final_project
mkcert localhost
```

This creates two files in your directory:

- `localhost.pem`  
- `localhost-key.pem`

Copy the files to the formats we have in our `phishing.py` by running:
```bash
cp localhost.pem cert.pem
cp localhost-key.pem key.pem
```

Your Python server script will automatically use these.

---

## 🛠 Option B — Using `OpenSSL` (Manual Fallback)

If you can’t install `mkcert`, use this instead:

### 1️⃣ OpenSSL one-liner (Linux/macOS)

```bash
openssl req -x509 -nodes -sha256 -days 365 \
  -newkey rsa:2048 \
  -keyout localhost.key \
  -out   localhost.crt \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost" \
  -addext "keyUsage=digitalSignature" \
  -addext "extendedKeyUsage=serverAuth"
```

This creates:

- `localhost.crt` (certificate)
- `localhost.key` (private key)

Copy the files to the formats we have in our `phishing.py` by running:
```bash
cp localhost.crt cert.pem
cp localhost.key key.pem
```

> 🧠 You’ll need to **manually trust the certificate** for browsers to accept it.

---

## ✅ Trusting the Certificate

### macOS

1. Double-click `cert.pem` → opens in **Keychain Access**.
2. Drag into the **System** or **login** keychain.
3. Right-click → **Get Info** → **Trust** → set **“Always Trust.”**
4. Fully quit and reopen your browser.

_Or use CLI:_
```bash
sudo security add-trusted-cert -d \
  -r trustRoot \
  -k /Library/Keychains/System.keychain \
  cert.pem
```

---

### Windows
for Windows users, you may have to retain `localhost.crt` for this step

1. Open **PowerShell or Command Prompt as Administrator**
2. Run:
   ```powershell
   certutil -addstore "Root" "$(Resolve-Path localhost.crt)"
   ```
3. Restart your browser completely.

---

### Linux

```bash
sudo cp localhost.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

---
