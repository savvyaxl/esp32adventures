def connect():
    import wifi
    import globals as g
    wifi.radio.connect(ssid=g.myssid,password=g.mypass)
    print("my IP addr:", wifi.radio.ipv4_address)
