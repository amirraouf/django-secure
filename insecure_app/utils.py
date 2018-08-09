import datetime


def user_directory_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT/<year>/<name>_<filename>"""
    return '{0}/{1}_{2}'.format(datetime.datetime.now().year, instance.name, filename)


def pkgen():
    """
    Function to generate reference hash
    ref: https://code-examples.net/en/q/395b9e # python 2 version
    :return:
    """
    from base64 import b32encode
    from hashlib import sha1
    from random import random
    rude = (b'lol',)
    bad_pk = True
    while bad_pk:
        sha1_obj = sha1()
        sha1_obj.update(str(random()).encode('utf-8'))
        pk = b32encode(sha1_obj.hexdigest().encode()).lower()
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0:
                bad_pk = True
        return pk.decode()