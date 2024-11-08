
# PersoDocs: Personalized Document Generator

PersoDocs is a Django-based web application that generates personalized Word documents from user-provided templates and Excel/CSV data. Users can create document templates with placeholders, upload a file containing customer data, and generate individual Word documents tailored for each customer. The app supports S3 for file storage, allowing seamless document management.

## Features

- **Document Template Management**: Users can upload Word templates (.docx) with placeholders, which are used to generate personalized documents.
- **Data Upload via Excel/CSV**: Supports Excel file uploads to populate placeholders with customer data.
- **Dynamic Document Generation**: Generates separate Word documents for each entry in the uploaded data, with customized information.
- **Document Storage with S3**: All documents are uploaded to and stored in an S3 bucket, allowing efficient cloud storage.
- **Batch Download**: Users can download generated documents as a single .zip file.
- **Document Update & Delete**: Update or delete documents with seamless S3 integration for managing files.
  
## Tech Stack

- **Backend**: Django, Python
- **Storage**: Amazon S3 for file storage
- **Frontend**: HTML, CSS, JavaScript (with Django templates)
- **Database**: Django ORM, PostgreSQL
- **Libraries**: `python-docx` for document handling, `pandas` for Excel data processing, `boto3` for S3 integration

## Setup and Installation

### Prerequisites

- Python 3.7+
- AWS account with S3 bucket
- Django environment setup
- Required Python packages (`requirements.txt`)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/persodocs.git
   cd persodocs
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up AWS credentials**:
   Configure your AWS credentials to allow Django to interact with S3. Add them in a `.env` file or configure them in `settings.py` as shown below:

   ```plaintext
   AWS_ACCESS_KEY_ID = 'your-access-key'
   AWS_SECRET_ACCESS_KEY = 'your-secret-key'
   AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
   ```

5. **Configure Django settings**:
   Update `settings.py` with the following S3 storage settings:

   ```python
   DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   AWS_S3_REGION_NAME = 'your-region'  # e.g., 'us-east-1'
   AWS_QUERYSTRING_AUTH = False  # Optional: disable query string for public URLs
   ```

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser to access the app.

## Usage

### Uploading a Document Template

1. Navigate to the "Upload Document" section.
2. Choose a `.docx` Word template and upload it. The document should contain placeholders in the `{{ placeholder_name }}` format.

### Uploading Data (Excel/CSV)

1. Select an uploaded document template.
2. Upload an Excel file (.xlsx) with columns matching the placeholder names in the template (e.g., `{{ name }}`, `{{ address }}`).
3. Submit the form to generate personalized documents.

### Downloading Generated Documents

1. After generating documents, you can download all files as a .zip archive.

### Updating and Deleting Documents

1. **Update**: Select a document and choose "Edit" to re-upload or change document details.
2. **Delete**: Choose "Delete" to remove the document from both the database and S3 storage.

## Code Overview

### `views.py`

- **`doc_detail`**: Displays document details and the upload form for Excel files.
- **`generate_doc`**: Handles document generation by reading Excel data, replacing placeholders, and creating personalized Word files.
- **`update_doc`**: Allows users to update the document details and file on S3.
- **`delete_doc`**: Deletes the document from the database and S3.

### `models.py`

Defines the `Doc` model, which stores metadata and file references for each document template.

### `forms.py`

Contains the `DocForm` for handling document uploads and updates, and `UploadExcelForm` for Excel file uploads.

## Important Considerations

- **S3 Integration**: Ensure the AWS S3 bucket has the correct permissions to allow file uploads, updates, and deletions.
- **Error Handling**: The app includes error handling for file operations. In case of file-related errors, a message will be logged.
- **Security**: Ensure AWS credentials are stored securely (e.g., in environment variables) and not hardcoded in the source code.

## Dependencies

Key dependencies are listed in `requirements.txt`, including:

- `Django`: Web framework
- `boto3`: AWS SDK for Python, required for S3 integration
- `python-docx`: For handling .docx document manipulation
- `pandas`: For reading Excel files and handling data

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For any questions or feedback, please contact:

**Ashfaqur Riaz**  
Email: [ashfakurriaz@gmail.com](mailto:ashfakurriaz@gmail.com)  

---

Enjoy generating personalized documents with **PersoDocs**!
