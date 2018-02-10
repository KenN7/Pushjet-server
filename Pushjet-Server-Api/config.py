from settings import *

# Must be a mysql database!
database_uri = 'mysql://%s:%s@mysql/%s' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)

# Are we debugging the server?
# Do not turn this on when in production!
debug = False

# Google Cloud Messaging configuration (required for android!)
google_api_key = GOOGLE_API_KEY
google_gcm_sender_id = int(GOOGLE_GCM_SENDER_ID)  # Change this to your gcm sender id

# Message Queueing, this should be the relay. A "sane" value
# for this would be something like ipc:///tmp/pushjet-relay.ipc
zeromq_relay_uri = 'ipc:///tmp/pushjet-relay.ipc'
