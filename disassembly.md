When you run `poetry build`, it generates distribution artifacts (usually a **source distribution** and a **wheel** file) in the `dist/` directory of your project. These artifacts are the packaged version of your Python project and can be used for various purposes such as:

- Distributing your package to PyPI or a private repository.
- Installing your package locally or in other environments.
- Sharing your package with others.

Here’s a detailed explanation of how to work with these artifacts:

---

### 1. **Understanding the Generated Artifacts**

When you run `poetry build`, Poetry will create two types of distribution files in the `dist/` directory by default:

```bash
poetry build
```

#### a) **Source Distribution (sdist)**
This is a `.tar.gz` file, which contains your source code and metadata. It’s a compressed archive of your project that users can download and build on their systems. The name format is typically:

```
<package-name>-<version>.tar.gz
```

Example: `my_project-0.1.0.tar.gz`

#### b) **Wheel Distribution (.whl)**
This is a pre-compiled binary distribution for Python projects, known as a **wheel** file. It’s faster to install because there’s no need to compile the source code at install time. The name format is typically:

```
<package-name>-<version>-<python-version>-<platform>.whl
```

Example: `my_project-0.1.0-py3-none-any.whl`

### 2. **Installing the Artifacts Locally**

After generating the distribution files, you may want to install the package locally on your machine to test or use it. Do this in a virtual environment. 

#### a) **Using `pip` to Install the Wheel or Source Distribution**

To install your package using the wheel (`.whl`) file, run:

```bash
pip install dist/my_project-0.1.0-py3-none-any.whl
```
Note : wheel is platform specific and so python wheels generated on windows will not work in linux

If you want to install the source distribution (`.tar.gz`), you can use:

```bash
pip install dist/my_project-0.1.0.tar.gz
```

#### b) **Installing with Poetry Directly (from the Dist)**
Poetry itself can install the built package, but you’ll need to use `pip` for the `.whl` or `.tar.gz` file installations. Alternatively, you can re-install the project in editable/development mode:

```bash
poetry install
```

This command will install the project in editable mode from your source code.

---


#### a) **Installing the Package Using `pip`**
From PyPI (or a private repository), you can install it in any Python project:

```bash
pip install my_project
```

#### b) **Installing the Package Using `Poetry`**
You can add your package to another project managed by Poetry by adding it as a dependency:

```bash
poetry add my_project
```

If it's hosted on TestPyPI or a private repository, you can specify the custom repository:

```bash
poetry add my_project --source test-pypi
```

Or:

```bash
poetry add my_project --source your-private-repo
```

---

## Unpacking wheel
To disassemble a Python wheel file, you can follow these steps to extract its contents and inspect them. A `.whl` file is essentially a ZIP archive that contains the Python package files.

### Step-by-Step Guide to Disassemble a `.whl` File

1. **Install `wheel` package** (if not already installed):
   You may need to install the `wheel` package for handling `.whl` files.

   ```bash
   pip install wheel
   ```

2. **Extracting the `.whl` file**:
   Since a `.whl` file is essentially a ZIP file, you can use Python's `zipfile` module to extract its contents. Here's a Python script that extracts the contents of a `.whl` file.

   ```python
   import zipfile
   import os

   def disassemble_wheel(wheel_path, extract_dir):
       # Check if the provided file is a valid wheel file
       if not wheel_path.endswith('.whl'):
           raise ValueError("The provided file is not a wheel file")

       # Extract the .whl file as a zip archive
       with zipfile.ZipFile(wheel_path, 'r') as whl_zip:
           whl_zip.extractall(extract_dir)
           print(f"Extracted {wheel_path} to {extract_dir}")

   # Usage example
   wheel_file = 'path/to/your/file.whl'  # Replace with your .whl file path
   extract_dir = 'path/to/extract/folder'  # Replace with your desired output folder
   disassemble_wheel(wheel_file, extract_dir)
   ```

3. **Inspecting the Contents**:
   After extraction, you can inspect the files in the output directory. Inside a wheel file, you will typically find:
   - Python modules and packages (as `.py` or compiled `.pyc` files).
   - A `METADATA` file that includes metadata about the package (such as the version, author, and dependencies).
   - A `RECORD` file that lists all files and their corresponding hashes.
   - Optionally, license files, documentation, etc.

4. **Explore the Extracted Files**:
   After extraction, you can explore and inspect the files manually, or use additional Python code to automate any analysis you need.

### Example of Extracted Contents
After disassembling a `.whl` file, you might see a structure similar to:

```
package_name-1.0.dist-info/
    METADATA
    WHEEL
    RECORD
    LICENSE
package_name/
    __init__.py
    module.py
```

Each folder and file serves a specific role in the package distribution.

This method will allow you to "disassemble" and examine any Python `.whl` file. Let me know if you'd like more specific guidance on inspecting particular parts of the wheel file.
