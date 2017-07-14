import unittest
from app.modal import User, Bucket


class TestUserBucket(unittest.TestCase):
    def setUp(self):
        self.user = User("tinah", "ashaba", "tinahashaba@gmail.com", "456", "456")

    def test_if_the_user_can_create_a_bucket(self):
        bucket = Bucket("RSTYVWXYZ", "school")
        self.assertTrue(self.user.add_bucket(bucket))

    def test_the_bucket_to_be_updated_does_not_exist(self):
        self.assertFalse(self.user.edit_bucket("BDBHGF", "Playing"))

    def test_to_ensure_bucket_is_deleted(self):
        bucket = Bucket("RSTYVWXYZ", "school")
        self.user.buckets = {"RSTYVWXYZ": bucket}
        self.user.delete("RSTYVWXYZ")
        self.assertEqual(self.user.buckets, {})

    def test_for_when_bucket_exists(self):
        bucket = Bucket("RSTYVWXYZ", "school")
        self.user.buckets = {"RSTYVWXYZ": bucket}
        self.assertFalse(self.user.add_bucket(bucket))

    def test_a_bucket_is_returned_when_an_id_is_specified(self):
        bucket = Bucket("RSTYVWXYZ", "school")
        self.user.buckets = {"RSTYVWXYZ": bucket}
        self.assertEqual(self.user.get_user_bucket("RSTYVWXYZ"), bucket)

    def test_to_ensure_none_is_returned_when_deleting_un_existing_bucket(self):
        self.assertFalse(self.user.delete("RSTYVWXYZ"))


if __name__ == '__main__':
    unittest.main()
