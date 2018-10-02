# TODO: Add correct copyright header

from django.test import Client, TestCase
from django.urls import reverse


class ViewTest_1st_level(TestCase):
    """
    This is a test case for testing all the first level views originated
    from home pages.

    """

    def setUp(self):
        """
        setUp is called before the execution of each test below
        :return:
        """
        self.client = Client()

    def test_contact_us_get(self):

        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_contact_us_get_pre_populate(self):
        test_http_referrer = "http://foo/bar"

        response = self.client.get(reverse("contact"), HTTP_REFERER=test_http_referrer)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
        # Assert Link has been populated
        self.assertTrue(test_http_referrer, response.content)

    def test_contact_us_post(self):
        post_data = {
            "email": "nobody@example.com",
            "subject": "Problem found",
            "category": "Something is not working",
            "link": "www.loc.gov/nowhere",
            "story": "Houston, we got a problem",
        }

        response = self.client.post(reverse("contact"), post_data)

        # redirected to contact us page.
        self.assertEqual(response.status_code, 302)
