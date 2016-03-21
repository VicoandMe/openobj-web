import hashlib
import re
import uuid
from django.utils.html import conditional_escape


def trans_illegal(s):
    """
    转换不合法的字符
    """
    g = lambda src: src if re.search(r'^http', src) else conditional_escape(src)
    if isinstance(s, str):
        return g(s)
    elif isinstance(s, (list, tuple)):
        s = list(s)
        for i in s:
            trans_illegal(i)
    elif isinstance(s, dict):
        for k, v in s.items():
            s[k] = trans_illegal(v)
    else:
        pass
    return s


def hash_password(password):
    """
    生成加密后的密码
    :param password:用户输入的密码
    :return:加密后的密码
    """
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    """
    判断密码是否相同
    :param hashed_password:数据库中保存的密码
    :param user_password:玩家输入的密码
    :return:
    """
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
