class User:
    def __init__(self, first_name, second_name, email, password, confirm_password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.buckets = {}

    def add_bucket(self, bucket):
        if bucket.id in self.buckets.keys():
            return False
        else:
            self.buckets[bucket.id] = bucket
            return True


class Bucket:
    def __init__(self, bucket_id, bucket_name):
        self.bucket_name = bucket_name
        self.id = bucket_id


class BucketActivity:
    def __init__(self, bucket_name, bucket_items):
        self.bucket_name = bucket_name
        self.bucket_items = bucket_items
