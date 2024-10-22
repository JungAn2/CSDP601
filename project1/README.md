#  Key generator
<img src="https://raw.githubusercontent.com/devicons/devicon/refs/heads/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>

## Description

This Python program generates an RSA key pair (public and private keys) and uses them to encrypt and decrypt messages. It includes functions to:

- Generate an RSA key pair.
- Encrypt a message using the public key.
- Decrypt a message using the private key.

This ensures that messages can be securely encrypted and decrypted using the generated key pair.

## To run
To run the program
- Simple cli
```bash
python key_genCli.py
```
```bash
python3 key_genCli.py
```
- With GUI
```bash
python key_gen.py
```
```bash
python3 key_gen.py
```

## How does it work?
To understand how RSA encryption works, let's break down the key generation and encryption/decryption process:

1. **Select two prime numbers**: Choose two distinct prime numbers, `p` and `q`.

2. **Compute `n`**: Calculate `n` by multiplying `p` and `q`:
    ```
    n = p * q
    ```

3. **Compute `phi(n)`**: Calculate the totient function `phi(n)`, which is:
    ```
    phi(n) = (p-1) * (q-1)
    ```

4. **Choose `e`**: Select an integer `e` such that `1 < e < phi(n)` and `e` is coprime with `phi(n)`. This `e` will be the public exponent.

5. **Compute `d`**: Determine `d` as the modular multiplicative inverse of `e` modulo `phi(n)`:
    ```
    d * e ≡ 1 (mod phi(n))
    ```
    This `d` will be the private exponent.

6. **Public and Private Keys**: The public key is `(e, n)` and the private key is `(d, n)`.

### Encryption
To encrypt a message `m`:
```
c = m^e (mod n)
```
where `c` is the ciphertext.

### Decryption
To decrypt the ciphertext `c`:
```
m = c^d (mod n)
```
where `m` is the original message.

This process ensures that only the holder of the private key `d` can decrypt the message encrypted with the public key `e`.