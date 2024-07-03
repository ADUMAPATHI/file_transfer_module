File Transfer Module:

The File Transfer Module is a Python package designed to facilitate the transfer of files from a specified directory to AWS S3 and Google Cloud Storage 
(GCS), based on configurable file types.

Features:

Uploads images (jpg, png, svg, webp) and media files (mp3, mp4, mpeg4, wmv, 3gp, webm) to AWS S3.
Uploads documents (doc, docx, csv, pdf) to Google Cloud Storage (GCS).
Configurable file type mappings for S3 and GCS uploads.
Supports handling of files in subdirectories of the specified directory.

Installation:

1. Clone the repository or download the source code:
	git clone https://github.com/your_username/file-transfer-module.git
	cd file-transfer-module

2.Install the required dependencies using pip:
	pip install .

This will install boto3 for AWS S3 interactions and google-cloud-storage for GCS interactions.

Configuration:
	Before using the module, make sure to configure AWS credentials and Google Cloud credentials on the environment where the module will run. 
	Refer to AWS and Google Cloud documentation for more details on obtaining and configuring credentials.

Run the script using Python to initiate the file transfer process:
	python file_transfer_module/transfer.py
