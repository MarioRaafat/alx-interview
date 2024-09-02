# UTF-8 Validation

This project provides a function to validate whether a given dataset represents a valid UTF-8 encoding. The dataset is represented by a list of integers where each integer represents a byte (8 bits). The function checks if these bytes conform to the UTF-8 encoding rules.

## UTF-8 Encoding Rules

UTF-8 is a variable-length encoding system that uses 1 to 4 bytes to represent a character. Each byte must follow specific patterns for the encoding to be considered valid.

### 1. One-Byte Character

- A 1-byte character is represented by a byte where the most significant bit (MSB) is `0`.
- Binary format: `0xxxxxxx`
- Valid range for a 1-byte character is `0` to `127` (standard ASCII characters).

### 2. Multi-Byte Characters

Characters that require more than 1 byte are encoded with a leading byte followed by one or more continuation bytes:

- **2-Byte Character:**
  - The first byte starts with `110`.
  - Binary format: `110xxxxx 10xxxxxx`
  - Example: `[0b110xxxxx, 0b10xxxxxx]`

- **3-Byte Character:**
  - The first byte starts with `1110`.
  - Binary format: `1110xxxx 10xxxxxx 10xxxxxx`
  - Example: `[0b1110xxxx, 0b10xxxxxx, 0b10xxxxxx]`

- **4-Byte Character:**
  - The first byte starts with `11110`.
  - Binary format: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
  - Example: `[0b11110xxx, 0b10xxxxxx, 0b10xxxxxx, 0b10xxxxxx]`

### 3. Continuation Bytes

- Continuation bytes must always start with `10`.
- Binary format: `10xxxxxx`
- Any byte that starts with `10` should be part of a multi-byte character sequence, not a leading byte.

## Factors That Determine Validity

To determine if a dataset is a valid UTF-8 encoding, the following factors are considered:

1. **Correct Starting Byte Pattern:**
   - Each multi-byte character must start with a byte that matches the appropriate pattern for its length (e.g., `110xxxxx` for 2-byte, `1110xxxx` for 3-byte, etc.).

2. **Correct Number of Continuation Bytes:**
