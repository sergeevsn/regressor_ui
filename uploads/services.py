# Бизнес-логика для приложения UPLOADS
# Загрузка файлов, обновление сессии, проверка файлов

import os

import pandas as pd
from django.conf import settings


def get_full_filename(fname):
    return os.path.join(settings.BASE_DIR, 'data', fname)

def handle_uploaded_file(f, fname):
    """ Загрузка файла на сервер """
    try:
        with open(get_full_filename(fname), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except OSError:
        return False
    finally:
        return True


def initialize_data_file_names(request):
    """ инициализация имен файлов в сессии """
    request.session['features_file_name'] = ''
    request.session['target_file_name'] = ''


def update_data_file_names(request):
    """ обновление имен файлов после загрузки из формы """
    request.session['features_file_name'] = request.FILES.get('file1', None).name
    request.session['target_file_name'] = request.FILES.get('file2', None).name


def check_data_files(request):
    """ Проверка файлов """
    if not (request.session['features_file_name']):
        print('Нет имени feature-файла в сессии')
        return False
    if not (request.session['target_file_name']):
        print('Нет имени target-файла в сессии')
        return False
    return True


def get_features_table_preview(request):
    df = pd.read_csv(get_full_filename(request.session['features_file_name']), delim_whitespace=True).describe().apply(lambda x: round(x, 2))
    df_table = df.apply(lambda series: series.apply(lambda value: f"{value:,}")).to_html()
    return df_table


def get_target_table_preview(request):
    df = pd.read_csv(get_full_filename(request.session['target_file_name']), delim_whitespace=True).describe().apply(lambda x: round(x, 2))
    df_table =  df.apply(lambda series: series.apply(lambda value: f"{value:,}")).to_html()
    return df_table


