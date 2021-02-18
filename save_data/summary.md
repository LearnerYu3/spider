# 数据存储
## 文本存储
### TXT 文本存储
TXT 文本几乎兼容任何平台，但是不利于检索。所以对检索和数据结构要求不高，追求方便的话，可以采用 TXT 文本。
### 文本打开方式
* r: 以只读方式打开文件，文件的指针将放在文件的开头，这是默认模式。
* rb: 以二进制只读方式打开一个文件。文件的指针将会放在文件的开头。
* r+: 以读写方式打开一个文件。文件指针将会放在文件的开头。
* rb+: 以二进制读写方式打开一个文件。文件指针将会放在文件的开头。
* w: 以写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果文件不存在，则创建新文件。
* wb: 以二进制写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
* w+: 以读写方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
* wb+: 以二进制读写格式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
* a: 以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。
* ab: 以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。也就是说，新的内容将会被写入的已有内容之后。如果该文件不存在，则创建新文件来写入。
* a+: 以读写方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，则创建新文件来读写。
* ab+: 以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。如果该文件不存在，则创建新文件用于读写。
### JSON 文件存储
JSON，全称为 JavaScript Object Notation，也就是 JavaScript 对象标记，它通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式。

1. 对象和数组
   
   在 JavaScript 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等，但是对象和数组是比较特殊且常用的两种类型。
   * 对象: 它在 JavaScript 中是使用花括号`{}`包裹起来的内容，数据结构为`{key1: value1, key2: value2, ...}`的键值对结构。在面向对象的语言中，key 为对象的属性，value 为对应的值。键名可以使用整数和字符串来表示，值的类型可以是任意类型。
   * 数组: 数组在 JavaScript 中是方括号`[]`包裹起来的内容。它也可以像对象那样使用键值对，但还是索引用的多。
   
   一个 JSON 对象可以写为如下形式:
   ```python
   [{
       "name": "Bob",
       "gender": "male",
       "birthday": "1992-10-18"
   }, {
       "name": "Selina",
       "gender": "female",
       "birthday": "1995-10-18"
   }]
   ```
   JSON 可以由以上两种形式自由组合而成，可以无限嵌套，是数据交换的极佳形式。
2. 读取 JSON
   
   调用 JSON 库中的 `loads()` 方法将 JSON 文本字符串转为 JSON 对象，可以通过 `dumps()` 方法将 JSON 对象转为文本字符串。如:
   ```python
   import json
   str = '''
   [{
       "name": "Bob",
       "gender": "male",
       "birthday": "10-18"
   }, {
       "name": "Selina",
       "gender": "female",
       "birthday": "10-18"
   }]
   '''
   print(type(str))
   data = json.loads(str)
   print(data)
   print(type(data))
   >>> <class 'str'>
   [{'name': 'Bob','gender': 'male','birthday': '10-18'},{...}]
   <class 'list'>
   ```
   注意 JSON 的数据需要用双引号来包围，不能使用单引号，否则会出现错误。

   这样读取一个 JSON 就可以
   ```python
   import json
   with open('data.json', 'r') as file:
       str = file.read()
       data = json.loads(str)
       print(data)
    ```
3. 输出 JSON
   
   我们可以将 JSON 对象转化为字符串。如
   ```python
   import json
   data = [{
       'name': 'Bob',
       'gender': 'male',
       'birthday': '10-18'
   }]
   with open('data.json', 'w') as file:
       file.write(json.dumps(data))
    ```
    想要保存 JSON 的格式，可以再加一个参数`indent`，代表缩进字符个数。
    ```python
    with open('data.json', 'w') as file:
        file.write(json.dumps(data, indent=2))
    ```
    当输出中包含中文时，还需要指定参数 ensure_ascii 为 False，还要规定输出的编码
    ```python
    with open('data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))
    ```

### CSV 文件存储
CSV，全称为 Comma-Separated Value(逗号分隔值)，其文件以纯文本形式存储表格数据。该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符分隔。每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。不过所有记录都有完全相同的字段序列，相当于一个结构化表的纯文本形式。XLS 文本是电子表格，它包含了文本、数值、公式和格式等内容，而 CSV 中不包含这些内容，就是特定字符分隔的纯文本。
1. 写入
    ```python
    import csv
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name','age'])
        writer.writerow(['1001', 'Bob', 20])
        writer.writerow(['1002', 'Mike', 21])
    ```
    如果想要修改列与列之间的分隔符，可以传入 delimiter 参数
    ```python
    writer = csv.writer(file, delimiter=' ')
    ```
    也可以调用`writerows()`方法同时写入多行，此时参数就需要为二维列表，如
    ```python
    writer.writerows([['1001','Bob',20], ['1002', 'Mike',21]])
    ```
    同样 csv 库中也提供了字典的写入方式
    ```python
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'1001', 'name':'Bob', 'age':20})
    ```
## 关系型数据库存储
### MySQL 的存储

通过 pymysql 中的 `connect()` 方法声明一个 MySQL 连接对象，传入 MySQL 运行的 `host` (IP)。由于在本地运行，所以传入的是 `localhost`。如果MySQL在远程运行，则传入其公网 IP 地址。后续的参数 `user` 即用户名，`password` 即密码，`port` 即端口（默认为3306）。

连接成功后，需要再调用 `cursor()` 方法获得操作光标，利用光标来执行 SQL 语句，用`execute()` 方法执行即可。调用 `fetchone()`方法获得第一条数据。在创建数据库后，在连接时需要额外指定一个参数 `db`
```python
db = pymysql.connect(host='localhost', user='root', password='ycysql', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
```
* 插入数据

    `commit()` 方法可以实现数据的插入，这个方法将语句提交到数据库执行。对于数据插入、更新、删除操作，都需要调用该方法才能生效。

    这里涉及事务的问题，比如插入一条数据，不会存在插入一半的情况，要么全部插入，要么都不插入。
    <table>
    <tr>
        <th>事务的属性</th> <th>解释</th>
    </tr>
    <tr>
        <td>原子性</td> <td>事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做</td>
    </tr>
    <tr>
        <td>一致性</td> <td>事务必须使数据库从一个一致性状态变到另一个一致性状态，一致性与原子性是密切相关的</td>
    </tr>
    <tr>
        <td>隔离性</td> <td>一个事务的执行不能被其它事务干扰，即一个事务内部的操作及使用的数据对并发的其它事务是隔离的，并发执行的各个事务之间不能互相干扰</td>
    </tr>
    <tr>
        <td>持久性</td> <td>持久性也称永久性，指一个事务一旦提交，它对数据库中数据的改变就应该是永久的。接下来的其它操作或故障不应该对其有任何影响</td>
    </tr>
    </table>
    插入、更新和删除操作都是对数据库进行更改的操作，而更改的操作都必须为一个事务，标准的写法是:

    ```python
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    ```
    在`use_mysql.py`中，插入数据的操作是通过构造 SQL 语句实现的，但是当突然增加一个属性字段时，就需要做相应的改动。所以我们可以传入动态变化的字典
    ```python
    data = {
        'id': '1001',
        'name': 'Bob',
        'age': 20
    }
    table = 'spiders'
    keys = ','.join(data.keys())
    values = ','.join(['%s']*len(data)) #len(data)字典键值对的个数
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()
    ```
* 更新数据
  
    可使用如下方式进行简单的数据更新
    ```python
    sql = 'UPDATE students SET age = %s WHERE name = %s'
    ```
    但是在实际的数据抓取过程中，在插入数据时我们关心的是会不会出现重复数据，如果出现了，我们希望更新数据而不是重复保存一次。所以我们需要实现去重，如果数据存在，则更新数据，如果数据不存在，则插入数据。示例如下：
    ```python
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
    update = ','.join(["{key}= %s".format(key=key) for key in data])
    sql += update
    ```
* 删除数据
  
    直接使用`DELETE`语句即可，仍需要使用 `commit()` 方法才能生效。
    ```python
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    ```
* 查询数据
  
    查询会用到 SELECT 语句，如:
    ```python
    sql = 'SELECT * FROM students WHERE age >= 20'
    ```
    **注意:** 在使用`cursor`（光标）查询数据或获取数据时，光标的位置会相应的移动，所以在使用`fetchone()`、`fetchall()`方法时，要特别注意光标的位置。
## 非关系型数据库
### redis
Redis 是一个基于内存的高效的键值型非关系型数据库，存取效率极高，而且支持多种存储数据结构，使用也非常简单。

redis-py 库提供两个类 `Redis` 和 `StrictRedis`，`StrictRedis` 实现了绝大部分官方的命令，参数也与`redis`命令一一对应。而`Redis`是`StrictRedis`的子类，为了做兼容，它将方法进行了改写，这与`redis`命令行的命令参数不一致。

`redis`默认端口为6379，默认没有密码
```python
from redis import StrictRedis
redis = StrictRedis(host='localhost',port=6379,db=0,password=None)
redis.set('name','Bob')
print(redis.get('name'))
>>> b'Bob'
```
还可支持url来构建，支持的方式有三种
```shell
redis://[:password]@host:port/db # Redis Tcp 连接
rediss://[:password]@host:port/db # Redis Tcp+SSL 连接
unix://[:password]@path/to/socket.sock?db=db # Redis UNIX socket 连接
```
`password`有则写，没有则不写，则可
```python
url = 'redis://localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
```
### RedisDump
RedisDump 提供了强大的 Redis 数据的导入和导出功能

