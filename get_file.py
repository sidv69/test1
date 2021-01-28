from minio import Minio

client = Minio("10.2.0.5", access_key="testuser", secret_key="testpass", secure=False)
try:
    response = client.get_object("mybucket", "src.jpg", offset=1000)
    f = open("result.jpg", "w+b")
    f.write(response.read())
finally:
    response.close()
    response.release_conn()
    f.close()
