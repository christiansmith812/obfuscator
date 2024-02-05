# Introduction:
The Python Obfuscator App is a tool designed to obfuscate Python code files, thereby making them harder to understand or reverse-engineer. This app is particularly useful for developers who want to protect their intellectual property or sensitive algorithms.

Here are the websites that inspired this project:
- [Python Obfuscator](https://github.com/ThePlasmaRailgun/Obfuscator)
- [Obfuscating "Hello world!"](https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html)

# Features:
**Code Obfuscation:** The app obfuscates Python code files by converting them into a less readable format, making it difficult for others to decipher the original logic.
File Structure Preservation: It preserves the directory structure of the source files while obfuscating them, ensuring that the obfuscated files are organized in the same way as the original ones.
Support for Non-Python Files: The app also supports copying non-Python files directly to the destination directory without modification, maintaining the integrity of the project.
How It Works:

The app recursively scans the specified source directory for Python code files (`.py` extension) and other necessary files.
It creates corresponding directories in the destination directory to replicate the source file structure.
For Python code files, it obfuscates the content using a custom obfuscation algorithm.
The obfuscated code is then written to new files in the destination directory.
Non-Python files are copied directly to the destination directory without modification.

# Usage Example
Suppose you have a directory structure as follows:

```
- resources
  - source
    - script1.py
    - script2.py
    - data.txt
  - destination
```

You can run the Python Obfuscator App with the following command:

```python
python app.py
```

After execution, the destination directory will contain obfuscated Python files and copied non-Python files, preserving the original directory structure:

```- resources
  - destination
    - source
      - script1.py
      - script2.py
      - data.txt
```

**Note:** The obfuscated code may not be directly executable and may require further processing or deobfuscation for use in production environments.

**Disclaimer:** This app is intended for educational and informational purposes only. Users are responsible for ensuring compliance with applicable laws and regulations when using this tool. The developers disclaim any liability for misuse or unintended consequences of the app.
