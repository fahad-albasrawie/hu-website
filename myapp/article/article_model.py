import mysql.connector
from myapp.configuration import ArticleDbConfiguration
from mysql.connector import Error, IntegrityError
from myapp import app


class ArticleDatabase:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def make_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def my_cursor(self):
        return self.cursor


class UserDatabase:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def make_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def my_cursor(self):
        return self.cursor

class ArticleModel:
    def __init__(self, connection):
        try:
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as err:
            print('Something went wrong! Internet connection or database connection.')
            print(f'Error: {err}')

    def get_articles(self):
        sql = """
                SELECT 
            article_topic.id AS topic_id,
            article_topic.topic,
            article_topic.img AS image,
            article_topic.topic_context,
            topic_category.category AS category_name,
            author.id AS author_id,
            CONCAT(author.f_name, ' ', author.s_name, ' ', author.l_name) AS full_name,
            article.visibility AS article_visibility,
            article.my_date AS article_my_date,
            article_count.total_articles AS article_count,
            article.id AS article_id
        FROM 
            article
            JOIN article_topic ON article.topic_id = article_topic.id
            JOIN author ON article_topic.author_id = author.id
            JOIN topic_category ON article_topic.topic_category_id = topic_category.id
            JOIN (
                -- Subquery to count articles per topic
                SELECT topic_id, COUNT(*) AS total_articles
                FROM article
                GROUP BY topic_id
            ) article_count ON article.topic_id = article_count.topic_id
            WHERE article.visibility = 'open' ORDER BY article_topic.id DESC;
            ;
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                print('Waa la heli karaa maqaallada')
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]

                return True, result
            else:
                print('Maqaallo oo qoran ma jiraan wali.')
                return True, {}
        except Exception as e:
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def get_favorite_articles(self):
        sql = """
                SELECT 
            article_topic.id AS topic_id,
            article_topic.topic,
            article_topic.img AS image,
            article_topic.topic_context,
            topic_category.category AS category_name,
            author.id AS author_id,
            CONCAT(author.f_name, ' ', author.s_name, ' ', author.l_name) AS full_name,
            article.visibility AS article_visibility,
            article.my_date AS article_my_date,
            article_count.total_articles AS article_count,
            article.id AS article_id
        FROM 
            article
            JOIN article_topic ON article.topic_id = article_topic.id
            JOIN author ON article_topic.author_id = author.id
            JOIN topic_category ON article_topic.topic_category_id = topic_category.id
            JOIN (
                -- Subquery to count articles per topic
                SELECT topic_id, COUNT(*) AS total_articles
                FROM article
                GROUP BY topic_id
            ) article_count ON article.topic_id = article_count.topic_id
            WHERE article.visibility = 'favorate' ORDER BY article_topic.id DESC;
            ;
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                print('Waa la heli karaa maqaallada')
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]

                return True, result
            else:
                print('Maqaallo oo qoran ma jiraan wali.')
                return True, []
        except Exception as e:
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def get_article_by_topic_id1(self, topic_id):
        sql = """
        SELECT article FROM article WHERE topic_id = %s;
        """
        try:
            self.cursor.execute(sql, (topic_id,))
            result = self.cursor.fetchone()
            if result:
                print('Waa la heli karaa maqaalkan')
                return True, result[0]
            else:
                print(f'Ma jiro maqaalka aqoonsigiisu yahay: {topic_id}')
                return True, {}
        except Exception as e:
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def get_article_by_topic_name(self, topic_name):
        sql = """
                SELECT 
            article_topic.id AS topic_id,
            article_topic.topic,
            article_topic.img AS image,
            article_topic.topic_context,
            topic_category.category AS category_name,
            CONCAT(author.f_name, ' ', author.s_name, ' ', author.l_name) AS full_name,
            article.my_date AS article_my_date,
            article.id AS article_id,
            article.article AS article_body
        FROM 
            article
            JOIN article_topic ON article.topic_id = article_topic.id
            JOIN author ON article_topic.author_id = author.id
            JOIN topic_category ON article_topic.topic_category_id = topic_category.id
            WHERE article_topic.topic = %s;
            ;
        """
        try:
            self.cursor.execute(sql, (topic_name,))
            result = self.cursor.fetchall()
            if result:
                print('Waa la heli karaa maqaallada')
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]

                return True, result
            else:
                print('Maqaallo oo qoran ma jiraan wali.')
                return True, []
        except Exception as e:
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def get_img_topic_id(self, topic_id):
        sql = """
        SELECT img FROM article_topic WHERE id = %s;
        """
        try:
            self.cursor.execute(sql, (topic_id,))
            result = self.cursor.fetchone()
            if result:
                print('Waa la heli karaa maqaalkan')
                return True, result[0]
            else:
                print(f'Ma jiro maqaalka aqoonsigiisu yahay: {topic_id}')
                return True, {}
        except Exception as e:
            print(f'Error: {e}')
            return False, f'Error: {e}.'


my_configuration = ArticleDbConfiguration()


def check_article_model_connection():
    try:
        mysql_connect = ArticleDatabase(
            host=my_configuration.DB_HOSTNAME,
            port=3306,
            user=my_configuration.DB_USERNAME,
            password=my_configuration.DB_PASSWORD,
            database=my_configuration.DB_NAME
        )
        # Create an instance of the Store class
        mysql_connect.make_connection()
        article_model = ArticleModel(mysql_connect.connection)

        return True, article_model
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'


if __name__ == '__main__':
    # Create an instance of the MySQLConnect class

    # connection to the database
    print('Connecting to the database...')
    connection_status, article_model = check_article_model_connection()
    if connection_status:
        print('You are connected to the database successfully!')
        flag, _ = article_model.get_favorite_articles()
        if flag:
            print(_)
            # send_last_phase_email(_)
            # print(len(_))
        else:
            print('False')
            print(_)
        '''
        while True:
            print('====================')
            word = input('\n\nEnter the word: ')
            if word.strip(' ') == '':
                break
            language = input('Enter the language (1 for Somali, 2 for English): ')
            level = input('Enter the level (1 for Hoose, 2 for Dhexe, 3 for Sare): ')

            if level == '1':
                level = 'hoose'
            elif level == '2':
                level = 'dhexe'
            elif level == '3':
                level = 'sare'

            if language == '1':
                language = 'Soomaali'
            elif language == '2':
                language = 'English'

            print('Fadlan sug...')
            flag, _ = admin.add_word(word, language, level)
            if flag:
                print(_)
                print('====================')
            else:
                print(_)
        '''

    else:
        print(f'Database Connection {article_model}')
