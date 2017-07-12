class User:
    def __init__(self, first_name, second_name, email, password, confirm_password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.confirm_password = password


class Bucket:
    def __init__(self, bucket_name, bucket_items):
        self.bucket_name = bucket_name
        self.bucket_items = bucket_items


class My_bucket:
    def __init__(self, bucket_name, bucket_items):
        self.bucket_name = bucket_name
        self.bucket_items = bucket_items
