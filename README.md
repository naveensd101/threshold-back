# Threshold Cryptography Service

Back end for Threshold Cryptrography as a service. Following are the API specifications for the encryption and decryption modules.

```
there are two endpoints:
/encrypt [POST]
input:
{
    "secret_int" : 666,
    "num_of_keys" : 3,
    "min_keys" : 2,
    "mail_list": ["example@gmail.com", "example@gmail.com", "example@gmail.com"]
}
output: OK
send email containing the key pair according to the threshold scheme
```

```
/decrypt [POST]
input:
{
    "3": 2856086346,
    "1": 952029226
}
output:
value after decryption using threshold cryptography scheme
```

# Diagramatic explanation of the scheme

![encrytpion](img/Encrypt.svg)

![decryption](img/Decrypt.svg)

# Setting up development environment

1. Make a new `.env` file with the following content

```
email="<email id of bot>"
password="<password of the account>"
```

2. After that run a `venv`

```
python3 -m venv <name>
```

3. Activate the environment

```
source /path/to/env/bin/activate
```

4. Install all the packages

```
pip install -r requirements.txt
```

5. Run the `main.py` file

```
python3 main.py
```

6. Opening the dev link will give a short description of the API's that we provide
