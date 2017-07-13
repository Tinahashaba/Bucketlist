class User:
    def __init__(self, first_name, second_name, email, password, confirm_password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.buckets = {}

    def add_bucket(self, bucket):
        """
        Adding a user to the dictionary
        :param bucket:
        :return:
        """
        if bucket.id in self.buckets.keys():
            return False
        else:
            self.buckets[bucket.id] = bucket
            return True

    def edit_bucket(self, bucket):
        """
        Edit an item if it exists.
        :param bucket:
        :return:
        """
        if bucket.id in self.buckets.keys():
            buck = self.buckets[bucket.id]
            buck.bucket_name = bucket.bucket_name
            return True
        return False



class Bucket:
    def __init__(self, bucket_id, bucket_name):
        self.bucket_name = bucket_name
        self.id = bucket_id


class BucketActivity:
    def __init__(self, bucket_name, bucket_items):
        self.bucket_name = bucket_name
        self.bucket_items = bucket_items
