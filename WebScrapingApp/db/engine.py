from sqlalchemy import create_engine


def connect_mysql():
    return create_engine(
         "mysql+pymysql://orxan:0rx<>n2022@173.212.238.58:3306/cd67003_test"
    )

