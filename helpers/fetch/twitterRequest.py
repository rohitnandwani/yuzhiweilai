# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 14:14:58 2015

@author: Nandwani
"""


import oauth2 as oauth
import urllib2 as urllib
import json


access_token_key = "306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd"
access_token_secret = "eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE"

consumer_key = "BeJvMbvBdYoptsvMiTxCg"
consumer_secret = "Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

 