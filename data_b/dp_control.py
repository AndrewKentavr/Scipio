import sqlite3

CONN = sqlite3.connect('data_b/scipio.db')
cur = CONN.cursor()


def get_cursor():
    return cur


# -----------------------------ANYTHING-----------------------------------------

def problem_translate_name(name):
    cur.execute(f"""SELECT translate_category FROM category
    WHERE '{name}' = value;""")
    result = cur.fetchall()
    return result[0][0]


def problem_category_random(name_category, tasks_theme):
    """
    :param name_category: Название категории вида: 'fractions'
    :param tasks_theme: Передаётся название таблици
    из которой будут брать задачи. Например: 'math'

    :return: Вся информация В СЛОВАРЕ, что есть по задаче. Например в задаче
    2 Условия и Ответ. Значит так и будет передоваться
    """
    cur.execute(
        f"""SELECT title, href, subcategory, complexity, classes, conditions, decisions_1, 
        decisions_2, answer, remarks FROM tasks_{tasks_theme}
                WHERE id_category = (SELECT id FROM category
                                WHERE value = '{name_category}')
                ORDER BY RANDOM()
                LIMIT 1;""")
    columns = ['title', 'href', 'subcategory', 'complexity', 'classes', 'conditions', 'decisions_1',
               'decisions_2', 'answer', 'remarks']
    result_0 = cur.fetchall()
    result = {}

    for i in range(len(result_0[0])):
        if result_0[0][i] is not None:
            result[columns[i]] = result_0[0][i]
        else:
            result[columns[i]] = ''

    return result


def finding_categories_table(tasks_theme):
    cur.execute(f"""SELECT value, translate_category FROM category
        WHERE id in (SELECT DISTINCT id_category FROM tasks_{tasks_theme});""")
    result_0 = cur.fetchall()
    return result_0


# -----------------------------MATH-----------------------------------------


def problem_search_random():  # <--------  Эта функция вообще где-то применяется?
    cur.execute(f"""SELECT * FROM math_problems 
    ORDER BY RANDOM() LIMIT 1;""")
    result = cur.fetchall()
    return result[0]


def formulas_search_random():
    cur.execute(f"""SELECT formulas, answer, explanation FROM math_formulas 
    ORDER BY RANDOM() LIMIT 1;""")
    result = cur.fetchall()
    return result[0]


# -----------------------------LOGIC-----------------------------------------
# -----------------------------FLASHCARD-----------------------------------------
def flashcard_dp_create(user_id, front, back, show):
    cur.execute(f"""INSERT INTO flashcards (user_id, front_card, back_card, show_card)
VALUES ({user_id}, '{front}', '{back}', '{show}');""")  # Без этого новые карточки не сохранялись
    cur.connection.commit()
    return


def flashcard_dp_info(user_id):
    cur.execute(f"""select id, front_card, back_card from flashcards
            where user_id = {user_id};""")
    result = cur.fetchall()
    return result


def flashcard_dp_info_game(user_id):
    cur.execute(f"""select id, front_card, back_card, show_card from flashcards
            where user_id = {user_id}""")
    result = cur.fetchall()
    return result


def flashcard_del(user_id, front_card, back_card):
    cur.execute(f"""DELETE FROM flashcards
        where user_id = {user_id} and front_card = '{front_card}' and back_card = '{back_card}';""")
    cur.connection.commit()
    return


def flashcard_one(user_id, id):
    cur.execute(f"""select id, front_card, back_card from flashcards
                where user_id = {user_id} and id = {id};""")
    result = cur.fetchall()
    return result


# -----------------------------TIMER-----------------------------------------

def timer_create_dp(user_id, time, tasks):
    cur.execute(f"""INSERT INTO Time (user_id, time, tasks)
VALUES ({user_id}, '{time}', '{tasks}');""")
    cur.connection.commit()
    return


def timer_del_dp(user_id, time):
    cur.execute(f"""DELETE FROM Time
where user_id = {user_id} and time = '{time}';""")
    cur.connection.commit()
    return


def timer_info_dp(user_id):
    cur.execute(f"""SELECT time FROM Time
where user_id == {user_id};""")
    c = cur.fetchall()
    all_timers = list(map(lambda x: x[0], c))
    return all_timers

# https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays
