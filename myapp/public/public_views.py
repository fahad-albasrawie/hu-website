from myapp import app
from flask import render_template, request, jsonify, session, redirect, url_for, make_response
from myapp.article.article_model import ArticleDatabase, ArticleModel, check_article_model_connection
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    article_data = []
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
            return render_template('public/index.html', article_data=article_data)
    else:
        print('Connection to the database failed at getting dashboard data!')
        article_data = {

        }
    return render_template('public/index.html', article_data=article_data)

@app.route('/president-message')
def president_message():
    return render_template('public/president_message.html')

@app.route('/deputy_vice_president_office')
def deputy_vice_president_office():
    return render_template('public/deputy_vice_president_office.html')

@app.route('/deans_and_director')
def deans_and_director():
    return render_template('public/deans_and_director.html')

@app.route('/board_of_director')
def board_of_director():
    return render_template('public/board_of_director.html')

@app.route('/public_relationship_office')
def public_relationship_office():
    return render_template('public/public_relationship_office.html')

@app.route('/register_office')
def register_office():
    return render_template('public/register_office.html')

@app.route('/finance_office')
def finance_office():
    return render_template('public/finance_office.html')

@app.route('/hrm')
def hrm():
    return render_template('public/hrm.html')

@app.route('/vission_mission')
def vission_mission():
    return render_template('public/vission_mission.html')

@app.route('/educational_goals')
def educational_goals():
    return render_template('public/educational_goals.html')

@app.route('/our_history')
def our_history():
    return render_template('public/our_history.html')

@app.route('/awards')
def awards():
    return render_template('public/awards.html')

@app.route('/career')
def career():
    return render_template('public/career.html')

@app.route('/contact_us')
def contact_us():
    return render_template('public/contact_us.html')

@app.route('/quality_policy_and_objectives')
def quality_policy_and_objectives():
    return render_template('public/quality_policy_and_objectives.html')

@app.route('/entry_requirements')
def entry_requirements():
    return render_template('public/entry_requirements.html')

@app.route('/how_to_apply')
def how_to_apply():
    return render_template('public/how_to_apply.html')

@app.route('/scholarships_and_financial_assistance')
def scholarships_and_financial_assistance():
    return render_template('public/scholarships_and_financial_assistance.html')

@app.route('/dean_message')
def dean_message():
    return render_template('public/dean_message.html')

@app.route('/programmes')
def programmes():
    return render_template('public/programmes.html')

@app.route('/academic_calender')
def academic_calender():
    return render_template('public/academic_calender.html')

@app.route('/postgraduate')
def postgraduate():
    return render_template('public/postgraduate.html')

@app.route('/postgraduate_diploma')
def postgraduate_diploma():
    return render_template('public/postgraduate_diploma.html')

@app.route('/national_partnerships')
def national_partnerships():
    return render_template('public/national_partnerships.html')

@app.route('/international_partnerships')
def international_partnerships():
    return render_template('public/international_partnerships.html')

@app.route('/international_organisations')
def international_organisations():
    return render_template('public/international_organisations.html')

@app.route('/accreditations')
def accreditations():
    return render_template('public/accreditation.html')

@app.route('/student_affairs_deanship')
def student_affairs_deanship():
    return render_template('public/student_affairs_deanship.html')

@app.route('/hu_facilities')
def hu_facilities():
    return render_template('public/hu_facilities.html')

@app.route('/industrial_training')
def industrial_training():
    return render_template('public/industrial_training.html')

@app.route('/ict_center')
def ict_center():
    return render_template('public/ict_center.html')

@app.route('/research_public_center')
def research_public_center():
    return render_template('public/research_public_center.html')

@app.route('/faq')
def faq():
    return render_template('public/faq.html')

# @app.route('/news')
# def news():
#     return render_template('public/news.html')

@app.route('/alumni')
def alumni():
    return render_template('public/alumni.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('public/privacy_policy.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('public/disclaimer.html')

@app.route('/security_policy')
def security_policy():
    return render_template('public/security_policy.html')

