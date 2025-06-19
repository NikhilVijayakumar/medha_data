## File Operations

**Main Themes:** Interacting with different file types, including text files, images (using Pillow), and PDFs (using PyPDF2). Understanding file modes and basic file manipulation.

**Important Ideas and Facts:**

* **Text Files:**
    * Files are opened using the built-in `open()` function.
    * The `open()` function returns a file object.
    * It's crucial to close files after you're done with them to release system resources. You can do this using the `.close()` method or, more conveniently, using a `with open(...) as f:` block, which automatically closes the file even if errors occur.
    * **File Modes:**
        * `'r'`: Read only (default). The file pointer is placed at the beginning of the file.
        * `'w'`: Write only. If the file exists, it is overwritten. If the file does not exist, a new file is created.
        * `'a'`: Append. If the file exists, the file pointer is placed at the end of the file. If the file does not exist, a new file is created.
        * `'r+'`: Read and write. The file pointer is placed at the beginning of the file.
        * `'w+'`: Write and read. If the file exists, it is overwritten. If the file does not exist, a new file is created.
        * `'x'`: Exclusive creation. Creates a new file and opens it for writing. Raises a `FileExistsError` if the file already exists.
        * `'t'`: Text mode (default). Handles file content as text (decodes/encodes using the system default encoding or a specified encoding).
        * `'b'`: Binary mode. Handles file content as raw bytes. Used for non-text files like images and PDFs.

    * **Reading from Text Files:**
        ```python
        # Using .read() - reads the entire file content into a single string
        with open("my_text_file.txt", "r") as f:
            content = f.read()
            print(content)

        # Using .readline() - reads one line at a time (including the newline character)
        with open("my_text_file.txt", "r") as f:
            line1 = f.readline()
            line2 = f.readline()
            print(f"Line 1: {line1.strip()}") # .strip() removes leading/trailing whitespace
            print(f"Line 2: {line2.strip()}")

        # Iterating over lines - efficient for large files
        with open("my_text_file.txt", "r") as f:
            for line in f:
                print(line.strip())
        ```

    * **Writing to Text Files:**
        ```python
        # Using .write() - writes a string to the file
        with open("output.txt", "w") as f:
            f.write("Hello, this is the first line.\n")
            f.write("This is the second line.\n")

        # Using .writelines() - writes a list of strings to the file
        lines_to_write = ["Line three.\n", "Line four.\n"]
        with open("output.txt", "a") as f:
            f.writelines(lines_to_write)
        ```

    * **Moving the Cursor (`.seek()`):**
        * The `.seek(offset, whence)` method changes the file pointer position.
        * `offset`: The number of bytes to move.
        * `whence`: The reference point (0: beginning of file, 1: current position, 2: end of file).
        ```python
        with open("my_text_file.txt", "r") as f:
            print(f.readline().strip()) # Read the first line
            f.seek(0)                   # Go back to the beginning
            print(f.readline().strip()) # Read the first line again
        ```

* **Image Objects (using Pillow - PIL):**
    * **Installation:** If not already installed, you need to install the Pillow library: `pip install Pillow` in your Colab notebook or terminal.
    * **Opening an Image:**
        ```python
        from PIL import Image

        try:
            img = Image.open("my_image.jpg")
            print(f"Filename: {img.filename}")
            print(f"Size: {img.size}")      # (width, height)
            print(f"Mode: {img.mode}")      # e.g., 'RGB', 'RGBA', 'L' (grayscale)
            print(f"Format Description: {img.format_description}")
        except FileNotFoundError:
            print("Error: Image file not found.")
        ```
    * **Image Manipulation (Examples):**
        ```python
        from PIL import Image

        try:
            img = Image.open("my_image.jpg")

            # Cropping
            cropped_img = img.crop((100, 100, 300, 300)) # (left, top, right, bottom)
            cropped_img.save("cropped_image.jpg")

            # Resizing
            resized_img = img.resize((128, 128))
            resized_img.save("resized_image.png")

            # Pasting one image onto another
            logo = Image.open("logo.png").resize((50, 50))
            img.paste(logo, (10, 10)) # Paste logo at (10, 10)
            img.save("image_with_logo.jpg")

            # Transparency (for RGBA images)
            if img.mode == 'RGBA':
                alpha = img.getchannel('A')
                # You can manipulate the alpha channel here
                img.putalpha(alpha)
                img.save("transparent_image.png")

            # Converting to grayscale
            grayscale_img = img.convert("L")
            grayscale_img.save("grayscale_image.jpg")

        except FileNotFoundError:
            print("Error: Image file not found.")
        ```
    * **Creating a New Image:**
        ```python
        from PIL import Image

        new_img = Image.new("RGB", (200, 100), color="lightblue")
        new_img.save("new_image.png")
        ```

* **PDF Objects (using PyPDF2):**
    * **Installation:** Install PyPDF2: `pip install PyPDF2`
    * **Opening a PDF:** Open in binary read mode (`'rb'`).
        ```python
        from PyPDF2 import PdfReader

        try:
            with open("my_document.pdf", "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                num_pages = len(reader.pages)
                print(f"Number of pages: {num_pages}")

                # Accessing a specific page
                if num_pages > 0:
                    page = reader.pages[0] # Get the first page (index 0)
                    text = page.extract_text()
                    print(f"Content of page 1:\n{text[:500]}...") # Print first 500 characters
        except FileNotFoundError:
            print("Error: PDF file not found.")
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
        ```
    * **Extracting Text:** The `.extract_text()` method retrieves the text content of a page.

* **CSV Files (using `csv` module and Pandas):**
    * **`csv` Module (Built-in):**
        * **Reading CSV:**
            ```python
            import csv

            with open("data.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
            ```
        * **Writing CSV:**
            ```python
            import csv

            data = [["Name", "Age", "City"],
                    ["Alice", 30, "New York"],
                    ["Bob", 25, "London"]]

            with open("output.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data) # Write multiple rows
            ```
    * **Pandas Library (More Powerful for Data Manipulation):**
        * **Installation:** `pip install pandas`
        * **Reading CSV to DataFrame:**
            ```python
            import pandas as pd

            try:
                df = pd.read_csv("data.csv")
                print(df)
            except FileNotFoundError:
                print("Error: CSV file not found.")
            ```
        * **Writing DataFrame to CSV:**
            ```python
            import pandas as pd

            data = {'Name': ['Alice', 'Bob'], 'Age': [30, 25], 'City': ['New York', 'London']}
            df = pd.DataFrame(data)
            df.to_csv("pandas_output.csv", index=False) # index=False prevents writing the DataFrame index to the file
            ```

* **Lecture Slides on Files:** Emphasize the importance of choosing the correct file mode for the intended operation and the necessity of closing files. Libraries like Pandas and Openpyxl are crucial for more advanced operations with structured data like spreadsheets (Excel files).