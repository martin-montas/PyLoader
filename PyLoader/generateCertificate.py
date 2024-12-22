from OpenSSL import crypto
import os
import secrets

# Paths to CA key and certificate
CA_KEY_PATH = "ca.key"
CA_CERT_PATH = "ca.crt"
CERTS_DIR = "./certs"

def generate_certificate(domain):
    """Generate a certificate for a specific domain."""
    if not os.path.exists(CERTS_DIR):
        os.makedirs(CERTS_DIR)

    cert_path = os.path.join(CERTS_DIR, f"{domain}.crt")
    key_path = os.path.join(CERTS_DIR, f"{domain}.key")

    if os.path.exists(cert_path) and os.path.exists(key_path):
        return key_path, cert_path

    # Load CA
    with open(CA_KEY_PATH, "rb") as ca_key_file:
        ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, ca_key_file.read())

    with open(CA_CERT_PATH, "rb") as ca_cert_file:
        ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, ca_cert_file.read())

    # Generate a private key
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Generate a CSR
    req = crypto.X509Req()
    req.get_subject().CN = domain
    req.set_pubkey(key)
    req.sign(key, "sha256")

    # Generate certificate
    cert = crypto.X509()
    cert.set_subject(req.get_subject())
    cert.set_serial_number(secrets.randbits(64))  # Generates a 64-bit random number
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)
    cert.set_issuer(ca_cert.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(ca_key, "sha256")

    # Save certificate and key
    with open(cert_path, "wb") as cert_file:
        cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open(key_path, "wb") as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    return key_path, cert_path
