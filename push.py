# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyAdwqkuhiQMZRRp8axNDO__8cvGjwdA740")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

r_id = "fpwLasNQ4W0:APA91bHEgOp-GJD_KRXoQCEGq8oVbQv1oxEVJQ4azSsCuG4COUYbI54X7f37DGfYqFM8kxlT-B-RU5bAVQWDHR_hd0tIMaRfrNl1Su52CXqdwjyl2pwLoIk5_71HbrFy2bfWRf1Ckwuj"
message_title = "Comunicado Residência TRE-RN"
message_body = "Mateus, você ganhou na mega da virada!"
result = push_service.notify_single_device(registration_id=r_id, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)

