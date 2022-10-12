mysql> use test_one;


mysql> CREATE TABLE base_nft (nft_id INTEGER UNIQUE, acsess TEXT, type TEXT);

mysql> CREATE TABLE base_user (telegramm_id BIGINT UNIQUE, ton_number TEXT);

mysql> CREATE TABLE shop_user (data TEXT,time TEXT,ton_number TEXT, nft_id INTEGER);

phpmyadmin
pass: morog_7567

phpsetuser
brev_prov

Take_82A06
SHOW DATABASES;

databasenft

--------------------------Рабочий шлюз---------------------------
host = "localhost"
port = 3307
user = "root"
password = "Take_82A06"
db_name = "databasenft"
-----------------------------------------------------------------

--------------------------Тестовый шлюз--------------------------
host = "localhost"
port = 3306
user = "root"
password = "take_8206"
db_name = "test_one"
-----------------------------------------------------------------

+-----------------------+
| Tables_in_databasenft |
+-----------------------+
| base_nft              |
| base_user             |
| nft_base              |
| shop_user             |
+-----------------------+

pip install pandas
pip install PyMySQL
pip install pysqlite3
pip install webdriver-manager
pip install pyTelegramBotAPI
pip install selenium
pip install progress
pip install openpyxl