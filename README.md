# Cryptography Coursework — Vernam/One‑Time Pad (Mod 26) in Python

This repository contains my university **Cryptography coursework** implemented in **Python**.  
The coursework demonstrates how to encrypt and decrypt messages using **modular arithmetic (mod 26)** with an **A–Z letter mapping**.

It includes two tasks:

- **Task 1 — Encryption:** converts plaintext + key into ciphertext using modular **addition**  
  `C = (P + K) mod 26`
- **Task 2 — Decryption:** converts ciphertext + key back into plaintext using modular **subtraction**  
  `P = (C − K) mod 26`

> Note: This is a *teaching/learning implementation* using simple A–Z mapping. It is not intended as production security software.

---

## Tech Stack

- Python 3.x (works with standard Python installations)
- No external libraries required

---

## Repository Contents

```
Cryptography/
├─ Cryptography.docx     # coursework brief / instructions
├─ task1.py              # encryption (mod 26)
└─ task2.py              # decryption (mod 26)
```

---

## How It Works

### A–Z Mapping
Letters are mapped to numbers:

- `A → 0, B → 1, …, Z → 25`

The program:
1. Converts letters to numbers
2. Applies modular addition/subtraction
3. Converts numbers back to letters

---

## Input Rules

- Inputs should contain **letters only** (A–Z)
- Recommended: use **UPPERCASE**
- Key length should be **at least** the message length (typical for Vernam/OTP style)

---

## Running the Programs

From the project folder:

### Task 1 — Encrypt
```bash
python task1.py
```

You will be prompted for:
- Plaintext
- Key

The script prints:
- Numeric conversion steps (plaintext/key/cipher numbers)
- Final ciphertext

### Task 2 — Decrypt
```bash
python task2.py
```

You will be prompted for:
- Ciphertext
- Key

The script prints:
- Inputs and adjusted key (if applicable)
- Final decrypted plaintext

---

## Example (Concept)

Plaintext: `HELLO`  
Key: `XMCKL`

Encryption:
- Convert to numbers
- `C = (P + K) mod 26`
- Convert back to letters → Ciphertext

Decryption:
- `P = (C − K) mod 26`
