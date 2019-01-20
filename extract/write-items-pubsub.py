import pdb
from google.cloud import pubsub_v1

# pdb.set_trace()

project_id = 'reliable-realm-222318'
topic_name = 'my-topic'

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_name)

for n in range(1, 10):
    data = u'Message number: {}'.format(n)
    # data must be bytestring
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print('Published {} of message ID {}.'.format(data, future.result()))

print('Published messages')
