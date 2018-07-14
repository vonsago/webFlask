#!/usr/bin/env python
# coding=utf-8
'''
> File Name: mysql_db.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  7/12 11:12:13 2018
'''

import time
from uuid import uuid4

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserStatus(Base):
    __tablename__ = "user_status"
    id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))

    name = Column(String(255), primary_key=True)
    last_login_time = Column(DOUBLE, nullable=False, default=lambda: time.time())  # 上次登陆的时间
    last_fail_times = Column(Integer, nullable=False)  # 上次失败次数
    last_change_password_time = Column(DOUBLE, nullable=False, default=lambda: time.time())  # 上次修改密码时间
    password_level = Column(Integer, default=0)  # 密码强度
    password_period = Column(Integer, default=0)  # 密码时效
    max_try_times = Column(Integer, default=0)  # 最大尝试次数

if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://root:dangerous@localhost/csp-test', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    user_status = session.query(UserStatus).filter(UserStatus.name == 'admin').first()
    
    if not user_status:
        user_status = UserStatus(
                id=str(uuid4()),
                name="admin",
                last_login_time=time.time(),
                last_fail_times=0,
                last_change_password_time=time.time(),
                password_level=0,
                password_period=0,
                max_try_times=4
            )
    print(user_status.name,user_status.last_login_time)
    user_status.last_login_time = time.time()
    user_status.max_try_times =5 
    session.flush()

    #session.commit()
