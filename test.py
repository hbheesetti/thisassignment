from urllib import request
import unittest
import http

BASEURL = "http://127.0.0.1:8080"

class TestYourWebserver(unittest.TestCase):
    def setUp(self,baseurl=BASEURL):
        """do nothing"""
        self.baseurl = baseurl
    
    # def test_get_deep(self):
    #     url = self.baseurl + "/deep/"
    #     req = request.urlopen(url, None, 3)
    #     self.assertTrue( req.getcode()  == 200 , "200 OK Not FOUND!")

    # def test_css(self):
    #     url = self.baseurl + "/base.css"
    #     req = request.urlopen(url, None, 3)
    #     self.assertTrue( req.getcode() == 200 , "200 OK Not FOUND!")
    #     self.assertTrue( req.info().get_content_type() == "text/css", ("Bad mimetype for css! %s" % req.info().get_content_type()))

    # def test_get_root(self):
    #     url = self.baseurl + "/"
    #     req = request.urlopen(url, None, 3)
    #     self.assertTrue( req.getcode()  == 200 , "200 OK Not FOUND!")

    # def test_get_indexhtml(self):
    #     url = self.baseurl + "/index.html"
    #     req = request.urlopen(url, None, 3)
    #     self.assertTrue( req.getcode()  == 200 , "200 OK Not FOUND!")


    def test_get_404(self):
        url = self.baseurl + "/do-not-implement-this-page-it-is-not-found"
        try:
            req = request.urlopen(url, None, 3)
            self.assertTrue( False, "Should have thrown an HTTP Error!")
        except request.HTTPError as e:
            self.assertTrue( e.getcode()  == 404 , ("404 Not FOUND! %d" % e.getcode()))
        else:
            self.assertTrue( False, "Another Error was thrown!")


if __name__ == '__main__':
    unittest.main()