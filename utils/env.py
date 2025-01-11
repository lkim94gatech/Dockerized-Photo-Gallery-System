import os

MINIO_USERNAME = "" # <-----INSERT MINIO USERNAME
MINIO_PASSWORD = "" # <-----INSERT MINIO PASSWORD

# Bucket configuration
BUCKET_NAME = os.getenv("BUCKET_NAME") or "photogallery"
ACCESS_KEY_USERNAME = os.getenv("ACCESS_KEY") or MINIO_USERNAME
SECRET_KEY_PASSWORD = os.getenv("SECRET_KEY") or MINIO_PASSWORD
STORAGE_HOST = os.getenv("STORAGE_HOST") or "localhost"
STORAGE_HOST_PORT = os.getenv("STORAGE_HOST_PORT") or "9000"
STORAGE_HOST_EXT = os.getenv("STORAGE_HOST_EXT") or "localhost"
STORAGE_PORT_EXT = os.getenv("STORAGE_PORT_EXT") or "9000"

# MySQL Configuration
DB_HOSTNAME = os.getenv("DB_HOSTNAME") or "localhost"
DB_USERNAME = os.getenv("DB_USERNAME") or "root"
DB_PASSWORD = os.getenv("DB_PASSWORD") or "photo123"
DB_NAME = os.getenv("DB_NAME") or "photodbs"
DB_PORT = int(os.getenv("DB_PORT") or 6603)
DB_TABLE = os.getenv("DB_TABLE") or "photogallery"
