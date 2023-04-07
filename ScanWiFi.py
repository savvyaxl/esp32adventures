def scan():
    import wifi
    from mysecrets import secrets
    import globals as g
    networks = []
    for network in wifi.radio.start_scanning_networks():
        networks.append(network)
    wifi.radio.stop_scanning_networks()
    networks = sorted(networks, key=lambda net: net.rssi, reverse=True)
    for network in networks:
        print("ssid:",network.ssid, "rssi:",network.rssi)
        for secret in secrets:
            print("ssidbob:",secret['ssid'])
            if network.ssid == secret['ssid']:
                g.myssid = secret['ssid']
                g.mypass = secret['password']
