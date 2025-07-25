
from flask import render_template, request, session, redirect, url_for, flash, make_response, jsonify
from myapp.configuration import ArticleDbConfiguration
from myapp.article.article_model import ArticleDatabase, ArticleModel
from myapp import app
from datetime import datetime
# from myapp.configuration import HuDbConfiguration
# from myapp.public.public_model import UserDatabase, UserModel
# Somali translation of month names
somali_months = {
    'January': 'Janaayo',
    'February': 'Febraayo',
    'March': 'Maarso',
    'April': 'Abriil',
    'May': 'May',
    'June': 'Juun',
    'July': 'Luuliyo',
    'August': 'Agoosto',
    'September': 'Sebteembar',
    'October': 'Oktoobar',
    'November': 'Nofeembar',
    'December': 'Diseembar'
}
somali_months_short = {
    'January': 'Jan',
    'February': 'Feb',
    'March': 'Maar',
    'April': 'Abr',
    'May': 'May',
    'June': 'Juun',
    'July': 'Luul',
    'August': 'Agst',
    'September': 'Seb',
    'October': 'Okt',
    'November': 'Nof',
    'December': 'Dis'
}


def format_date_somali(date_str):
    # Remove any trailing spaces
    date_str = date_str.strip()

    # Convert the string into a datetime object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # Get the English month and translate it to Somali
    month_name = date_obj.strftime('%B')  # Get the full month name in English
    somali_month = somali_months[month_name]  # Translate to Somali

    # Return the formatted date with Somali month name
    return date_obj.strftime(f'{somali_month} %d, %Y')  # Example: "Oktoobar 13, 2024"


def format_date_somali_short(date_str):
    # Remove any trailing spaces
    date_str = date_str.strip()

    # Convert the string into a datetime object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # Get the English month and translate it to Somali
    month_name = date_obj.strftime('%B')  # Get the full month name in English
    somali_month = somali_months_short[month_name]  # Translate to Somali

    # Return the formatted date with Somali month name
    return date_obj.strftime(f'{somali_month} %d, %Y')  # Example: "Oktoobar 13, 2024"

# Register the custom filter in Jinja
@app.template_filter('format_date_somali')
def format_date_somali_filter(date_str):
    return format_date_somali(date_str)

@app.template_filter('format_date_somali_short')
def format_date_somali_filter2(date_str):
    return format_date_somali_short(date_str)

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
        article = ArticleModel(mysql_connect.connection)

        return True, article
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'
#
# user_configuration = HuDbConfiguration()
#
#
# def check_users_model_connection():
#     try:
#         mysql_connect = UserDatabase(
#             host=user_configuration.DB_HOSTNAME,
#             port=3306,
#             user=user_configuration.DB_USERNAME,
#             password=user_configuration.DB_PASSWORD,
#             database=user_configuration.DB_NAME
#         )
#         # Create an instance of the Store class
#         mysql_connect.make_connection()
#         user_model = UserModel(mysql_connect.connection)
#
#         return True, user_model
#     except Exception as e:
#         print(f'')
#         return False, f'Error: {e}.'

# Custom 404 error handler
# @app.errorhandler(404)
# def page_not_found(e):
#     # Render a custom template for 404 errors
#     print('Page not found.1')
#     return render_template('public/page_not_found.html'), 404

@app.route('/news')
def news():

    # connection to the database
    print('Connecting to the database...')
    print("Getting article data...")
    connection_status, article = check_article_model_connection()
    if connection_status:
        print('You are connected to the database successfully!')
        # Get the articles from the database
        article_flag, article_data = article.get_articles()
        favorite_article_flag, favorite_article_data = article.get_favorite_articles()
        if article_flag and favorite_article_flag:
            article_data = {
                'article_info': article_data,
                'favorite_article_info': favorite_article_data
            }
            return render_template('article/news.html', article_data=article_data)
    else:
        print('Connection to the database failed at getting dashboard data!')
        article_data = {

        }
    return render_template('article/news.html', article_data=article_data)





@app.route('/read_article/<string:article_info>')
def read_article(article_info):  # Ensure this name matches the one in url_for

    # Split the string by the hyphen to extract the ID and topic

    # article_info = article_info.split('^^^^^')
    print(article_info)

    print('Waxaanu soo helaynaa qamaalka aqoonsigiisi yahay1...')
    # connect to the database
    print('Connecting to the database...')
    connection_status, article = check_article_model_connection()
    # connection_status = False
    if connection_status:

        my_article_data = {
            'topic': article_info
        }

        # print('The image url: ', article.get_img_topic_id(article_info[0])[-1])
        # print(my_article_data)
        session['my_article_data'] = my_article_data

        return redirect(url_for("reading_article", article=my_article_data.get('topic').replace(' ', '_')))

    else:
        return "Waanu ka xunnahay, ma furi karno maqaalka aad dooratay."


@app.route('/maqaal/akhriso/<string:article>')
def reading_article(article):
    print("*********", article, "*********")
    article = article.replace('_', ' ')
    print(article)
    try:
        # if session['my_article_data']:
        print('Waxaanu soo helaynaa qamaalka aqoonsigiisi yahay2...')
        # connect to the database
        print('Connecting to the database...')
        print(f"This is is the article name '", session['my_article_data']['topic'], "' we are looking for")

        connection_status, article = check_article_model_connection()
        # Check if the article is open or not
        my_flag, res = article.check_status_article_by_topic_name(session['my_article_data']['topic'])
        if not my_flag:
            print('This article is not open for reading.')
            return render_template('article/article_page_not_found.html'), 404

        flag, result = article.get_article_by_topic_name(
            topic_name=session['my_article_data']['topic']
        )
        result = result[0]
        # print(result)
        my_article_data = {
            'article_id': result.get('topic_id'),
            'topic': result.get('topic'),
            'topic_context': result.get('topic_context'),
            'author': result.get('full_name'),
            'article_category': result.get('category_name'),
            'article_date': result.get('article_my_date')[:-5].strip(),
            'img': result.get('image')
        }

        data = {
            'article_info': my_article_data,
            'article_content': result.get('article_body')
        }

        # remove my_article_data from session
        session.pop('my_article_data', None)

        return render_template('article/reading_article.html', data=data)

        # return render_template('public/article_not_found.html'), 404

    except Exception as e:
        print('Trying to open a specific topic...')
        print(f'Error: {e}')

        return read_article(article)
        # return render_template('public/article_page_not_found.html'), 404

# @app.route('/register_subscriber', methods=['POST'])
# def register_subscriber():
#     if request.method == 'POST':
#         if request.is_json:
#             req = request.get_json()
#             print(req)
#             # check if the all fields are filled
#
#             if not req.get('full_name') or not req.get('email') or not req.get('number'):
#                 my_respond = {
#                     'message': f"Fadlan hubi inaad buuxisay dhammaan godadka.",
#                     'status': 'error'
#                 }
#                 res = make_response(jsonify(my_respond), 200)
#                 return res
#
#             if len(req.get('full_name')) > 30 or len(req.get('email')) > 30 or len(req.get('number')) > 15:
#                 my_respond = {
#                     'message': f"Fadlan xarfo badan ha soo galin godadka. "
#                                f"Magaca iyo iimaylka haka badin (30) xaraf, lambarkana haka badin (15) xaraf.",
#                     'status': 'error'
#                 }
#                 res = make_response(jsonify(my_respond), 200)
#                 return res
#
#             # Check email contains @
#             if '@' not in req.get('email'):
#                 my_respond = {
#                     'message': f"Fadlan gali iimaylka saxda ah.",
#                     'status': 'error'
#                 }
#                 res = make_response(jsonify(my_respond), 200)
#                 return res
#
#             # Check phone number. Check the last 7 digits are numbers
#             if not req.get('number')[-7:].isdigit() or len(req.get('number')) < 7:
#                 my_respond = {
#                     'message': f"Fadlan gali nambarkaaga telefoonka oo sax ah.",
#                     'status': 'error'
#                 }
#                 res = make_response(jsonify(my_respond), 200)
#                 return res
#
#             # connection to the database
#             print('Connecting to the database...')
#             print("Getting subscriber data...")
#             connection_status, user_model = check_users_model_connection()
#             if connection_status:
#                 print('You are connected to the database successfully!')
#                 # Get the articles from the database
#                 flag, _ = user_model.get_subscriber(req.get('number'), req.get('email'))
#                 if flag and _:
#                     # Provide information to the user
#                     print(_[0].get('full_name'), ", mar hore aydd inoo diiwaangashanayd, mahadsanid")
#                     my_respond = {
#                         'message': f"{_[0].get('full_name')}, mar hore ayaad inoo diiwaangashanayd, mahadsanid.",
#                         'status': 'info'
#                     }
#                     res = make_response(jsonify(my_respond), 200)
#                     return res
#                 # Now register
#                 else:
#                     flag, _ = user_model.register_subscriber(req.get('full_name'),
#                                                              req.get('email'), req.get('number'),
#                                                              req.get('my_date'))
#                     if flag and _:
#                         # Provide information to the user
#                         print(_)
#                         # print(_[0].get('full_name'), ", mar hore aydd inoo diiwaangashanayd, mahadsanid")
#                         my_respond = {
#                             'message': f"{req.get('full_name')}, si saxan baa laguu diiwaangeliyey, mahadsanid",
#                             'status': 'success'
#                         }
#                         res = make_response(jsonify(my_respond), 200)
#                         return res
#
#                     my_respond = {
#                         'message': f"Waanu ka xunnahaya, qalad baa dhacay (AFGDB).",
#                         'status': 'error'
#                     }
#                     res = make_response(jsonify(my_respond), 200)
#                     return res
#
#             else:
#                 print('Connection to the database failed at getting dashboard data!')
#                 my_respond = {
#                     'message': f"Waanu ka xunnahaya, qalad baa dhacay (DB).",
#                     'status': 'error'
#                 }
#                 res = make_response(jsonify(my_respond), 200)
#                 return res
#         else:
#             my_respond = {
#                 'message': 'Waanu ka xunnahay, xogtaada ma aha nidaamka JSON. Fadlan iska hubi',
#                 'status': 'error'
#             }
#             res = make_response(jsonify(my_respond), 404)
#             return res
#     else:
#         return "Waanu ka xunnahay waxaan u malaynaynaa in boggani aanu hayn kan aad raadiyeysid!"
#
