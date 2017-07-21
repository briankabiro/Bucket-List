import unittest
from app.app import Bucketlist, User


class TddinBucketlist(unittest.TestCase):
    def setUp(self):
        # create an object
        self.bucketlist = Bucketlist("bucketlist")

    def test_bucketlist_created(self):
        # test if object is created
        self.assertEqual(self.bucketlist.name, "bucketlist")

    def test_item_added_to_bucket(self):
        # test if an item is added to the object
        self.bucketlist.add_item("the winner by a knockout is")
        self.assertEqual(self.bucketlist.bucket[0]["body"],
                         "the winner by a knockout is")

    def test_item_removed_from_bucket(self):
        # test if an item is removed from the bucket
        self.bucketlist.add_item("One")
        self.bucketlist.remove_item(0)
        self.assertNotIn(0, self.bucketlist.bucket)

    def test_delete_method_deletes(self):
        # test if the object is deleted
        self.assertTrue(self.bucketlist.__del__())

    def test_multiple_items_added(self):
        # test if multiple items are added to object
        self.bucketlist.bucket = []
        self.bucketlist.add_item("One")
        self.bucketlist.add_item("Two")
        self.assertEqual(len(self.bucketlist.bucket), 2)


class TddinUser(unittest.TestCase):
    def setUp(self):
        # create a User object
        self.user = User("user", "1234")

    def test_user_created(self):
        # test if the user has been created
        self.assertEqual(self.user.name, "user")

    def test_user_logged_out(self):
        # test if the user object is deleted
        self.assertTrue(self.user.__del__())

'''
if __name__ == '__main__':
    unittest.main()
'''