from zk import ZK, const

def upload_to_biometrics(ip, port, user_id):
    """
    Uploads the face image to the scanner.
    """
    conn = None
    # create ZK instance
    zk = ZK(ip, port=port, timeout=120, password=0, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()

        conn.set_user(uid=50, user_id='50', privilege=const.USER_DEFAULT)
        
        # Test Voice: Say Thank You
        conn.test_voice()
        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print ("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()