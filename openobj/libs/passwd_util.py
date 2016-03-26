import hashlib
import uuid


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
