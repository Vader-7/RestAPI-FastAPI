import oracledb

conection = oracledb.connect(user='API_ARC', password='Kkkk123_123*', dsn='db202201030958_high', config_dir='/Users/ty/opc/wallet_db',
                             wallet_location='/Users/ty/opc/wallet_db', wallet_password='Kkkk123_123*')
cursor = conection.cursor();
