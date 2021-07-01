import os
from flask import Flask, render_template,request,escape
from vsearch import search4letters
from flask import Flask, render_template, redirect, request, url_for, flash, session
from functools import wraps
import pandas as pd
# import matplotlib.pyplot as plt

app = Flask(__name__)
def read_data_users():
    return pd.read_csv('./datas/movielens-1m/users.dat',
                      sep="::",
                      engine="python",
                      header=None,
                      names="UserID::Gender::Age::Occupation::Zip-code".split("::")
                      )

def read_data_movies():
    return pd.read_csv('./datas/movielens-1m/movies.dat',
                      sep="::",
                      engine="python",
                      header=None,
                      names="电影ID::电影名称::电影类型".split("::")
                      )

@app.route('/index.html')
def home_index():
    title = "Douban Movie Data Show"
    return render_template('index.html',
                           the_title=title, )


@app.route('/Tables_Animation.html')
# def Animation_datas():
#     title = "Animation_datas"
#     return render_template('Tables_Animation.html',
#                            the_title=title, )

def get_movies_Animation():
    title = "Animation_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Animation = df[df['电影类型'].str.contains('Animation')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Animation.html",
        # male_data、female_data 是HTML文件中的变量
        Animation_data=df_Animation.to_html(classes="Animation", index=False),
    )

@app.route('/Tables_Drama.html')
# def Drama_datas():
#     title = "Drama_datas"
#     return render_template('Tables_Drama.html',
#                            the_title=title, )

def get_movies_Drama():
    title = "Drama_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Drama = df[df['电影类型'].str.contains('Drama')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Drama.html",
        # male_data、female_data 是HTML文件中的变量
        Drama_data=df_Drama.to_html(classes="Drama", index=False),
    )

@app.route('/Tables_Comedy.html')
# def Comedy_datas():
#     title = "Comedy_datas"
#     return render_template('Tables_Comedy.html',
#                            the_title=title, )

def get_movies_Comedy():
    title = "Comedy_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Comedy = df[df['电影类型'].str.contains('Comedy')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Comedy.html",
        # male_data、female_data 是HTML文件中的变量
        Comedy_data=df_Comedy.to_html(classes="Comedy", index=False),
    )

@app.route('/Tables_Film_Noir.html')
# def Film_Noir_datas():
#     title = "Film-Noir_datas"
#     return render_template('Tables_Film_Noir.html',
#                            the_title=title, )

def get_movies_Film_Noir():
    title = "Film_Noir_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Film_Noir = df[df['电影类型'].str.contains('Film-Noir')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Film_Noir.html",
        # male_data、female_data 是HTML文件中的变量
        Film_Noir_data=df_Film_Noir.to_html(classes="Film-Noir", index=False),
    )

@app.route('/Tables_Thriller.html')
# def Thriller_datas():
#     title = "Thriller_datas"
#     return render_template('Tables_Thriller.html',
#                            the_title=title, )

def get_movies_Thriller():
    title = "Thriller_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Thriller = df[df['电影类型'].str.contains('Thriller')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Thriller.html",
        # male_data、female_data 是HTML文件中的变量
        Thriller_data=df_Thriller.to_html(classes="Thriller", index=False),
    )

@app.route('/Tables_Western.html')
# def Western_datas():
#     title = "Western_datas"
#     return render_template('Tables_Western.html',
#                            the_title=title, )

def get_movies_Western():
    title = "Western_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Western = df[df['电影类型'].str.contains('Western')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Western.html",
        # male_data、female_data 是HTML文件中的变量
        Western_data=df_Western.to_html(classes="Western", index=False),
    )

@app.route('/Tables_Romance.html')
# def Romance_datas():
#     title = "Romance_datas"
#     return render_template('Tables_Romance.html',
#                            the_title=title, )

def get_movies_Romance():
    title = "Romance_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Romance = df[df['电影类型'].str.contains('Romance')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Romance.html",
        # male_data、female_data 是HTML文件中的变量
        Romance_data=df_Romance.to_html(classes="Romance", index=False),
    )

@app.route('/Tables_Musical.html')
# def Musical_datas():
#     title = "Musical_datas"
#     return render_template('Tables_Musical.html',
#                            the_title=title, )

def get_movies_Musical():
    title = "Musical_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Musical = df[df['电影类型'].str.contains('Musical')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Musical.html",
        # male_data、female_data 是HTML文件中的变量
        Musical_data=df_Musical.to_html(classes="Musical", index=False),
    )

@app.route('/Tables_Children.html')
# def Children_datas():
#     title = "Children_datas"
#     return render_template('Tables_Children.html',
#                            the_title=title, )

def get_movies_Children():
    title = "Children_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Children = df[df['电影类型'].str.contains('Children')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Children.html",
        # male_data、female_data 是HTML文件中的变量
        Children_data=df_Children.to_html(classes="Children", index=False),
    )

@app.route('/Tables_Adventure.html')
# def Adventure_datas():
#     title = "Adventure_datas"
#     return render_template('Tables_Adventure.html',
#                            the_title=title, )

def get_movies_Adventure():
    title = "Adventure_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Adventure = df[df['电影类型'].str.contains('Adventure')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Adventure.html",
        # male_data、female_data 是HTML文件中的变量
        Adventure_data=df_Adventure.to_html(classes="Adventure", index=False),
    )

@app.route('/Tables_Fantasy.html')
# def Fantasy_datas():
#     title = "Fantasy_datas"
#     return render_template('Tables_Fantasy.html',
#                            the_title=title, )

def get_movies_Fantasy():
    title = "Fantasy_datas"
    df = read_data_movies()
    # 筛选数据目标（处理数据）
    df_Fantasy = df[df['电影类型'].str.contains('Fantasy')]
    # 返回页面结果（变量名称 python文件中的变量 VS HTML文件中的变量）
    return render_template(
        "Tables_Fantasy.html",
        # male_data、female_data 是HTML文件中的变量
        Fantasy_data=df_Fantasy.to_html(classes="Fantasy", index=False),
    )

@app.route('/Static_state.html')
def Static_state():
    title = "Static_state"
    return render_template('Static_state.html',
                           the_title=title, )


if __name__ == '__main__':
    app.run()
