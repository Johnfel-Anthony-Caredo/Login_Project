# Security Documentation

## 1. Hashing Algorithm Used
This project utilizes the **SHA-256** (Secure Hash Algorithm 256-bit) cryptographic hash function. It is a widely accepted industry standard that securely transforms incoming data into a fixed-size, completely irreversible 64-character hexadecimal signature. 

## 2. Salt Generation and Usage
A unique salt is generated for every individual user at the exact moment of registration using Python's native `secrets.token_hex(16)` function. This ensures cryptographically secure, unpredictable randomness. 
* **Usage**: Before the password is run through the SHA-256 algorithm, this unique string is appended directly to the user's plaintext password. The salt is then stored openly in the database alongside the user's generated hash.

## 3. Pepper Storage and Application
The pepper is a heavily guarded, unchanging application-wide secret. It is strictly stored in the application's configuration file (`config/settings.py`) and is intentionally never logged or stored inside the database.
* **Application**: During both registration and login, the system extracts the plaintext password, appends the user's unique database salt, and finally appends the secret pepper. Only after all three components are combined (`password + salt + pepper`) does the system apply the SHA-256 hash.

## 4. Why Salt and Pepper Improve Security
Using a standalone password hash leaves user data highly vulnerable to sophisticated cracking techniques, but adding salts and peppers critically neutralizes these vectors:
* **Salt**: Because every single user has a unique salt, identical passwords will generate completely different baseline hashes, protecting the system against pre-computed Rainbow Table attacks.
* **Pepper**: If a malicious attacker successfully steals the entire database, they still cannot brute-force the hashes because they lack the required secret pepper, which is independently locked away in the system's source code configuration.
