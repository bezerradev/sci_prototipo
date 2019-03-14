# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyAdwqkuhiQMZRRp8axNDO__8cvGjwdA740")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging


def enviar_push(keys, titulo, corpo):
  result = push_service.notify_multiple_devices(registration_ids=keys, message_title=titulo, message_body=corpo)

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
