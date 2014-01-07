#Imports from facepy api
from facepy.utils import get_extended_access_token

#App key/APP ID and App_secret from https://developers.facebook.com/apps
app_id = ''
app_secret = ''
#1391587941094306
#f26f0ec4dd654de641126a71cf28df7f
#Token got by selecting app_name from the drop-down list.
short_lived_access_token = ""
'''CAATxpFDnE6IBAP24wjRXu298IL4xUoV2UzRPsGed981x2Gf2LRHLwgZBdVWYbZBKyEiW84gRYPbcF8ZAAZBblEa2XZBoKaPiv9aYI8bDrlAN49G3IUsMPpXX8XGZCRVTXn5q6LsP1yklDGIpbZCh1zTLh4u4TUiqfmxHyVg9EFCZB7M6ulMAP39t5niNqA6i6xufmtA2Hs4V8QZDZD'''
long_lived_access_token, expires_at = get_extended_access_token(
    short_lived_access_token,
    app_id, app_secret)

print long_lived_access_token
print expires_at
