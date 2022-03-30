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

        users = conn.get_users()

        for user in users:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'
            print ('+ UID #{}'.format(user.uid))

        
        # Test Voice: Say Thank You
        conn.test_voice()
        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print ("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()