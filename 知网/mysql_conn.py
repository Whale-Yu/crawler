import pymysql

settings = {
    "MYSQL_HOST":"127.0.0.1",
    "MYSQL_DB":"zhiwang",
    "MY_USER":"root",
    "MY_PWD":"123456"
}
def create_table(table_name,*args):
    # 连接数据库
    conn = pymysql.connect(host=settings["MYSQL_HOST"],
                           database=settings["MYSQL_DB"],
                           user=settings["MY_USER"],
                           password=settings["MY_PWD"])
    # # 建立游标
    cursor = conn.cursor()
    mysql_create = f"""create table {table_name}({''.join([f'{args[i]}' +' char(200),' if i != len(args) - 1 else f'{args[i]}' +' char(200)'for i in range(len(args))])});"""
    # print(mysql_create)
    cursor.execute(mysql_create)
    conn.commit()
    cursor.close()
    conn.close()

def insert_table(table_name,args):
    # 连接数据库
    conn = pymysql.connect(host=settings["MYSQL_HOST"],
                           database=settings["MYSQL_DB"],
                           user=settings["MY_USER"],
                           password=settings["MY_PWD"])
    # 建立游标
    cursor = conn.cursor()
    mysql_insert = f"""insert into {table_name} values({','.join([args[i] for i in range(len(args))])});"""
    cursor.execute(mysql_insert)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_table(123,"saas","asdasd")
