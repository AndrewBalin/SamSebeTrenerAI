from GPTCreator import GPTCreator


class RationCreator(GPTCreator):
    def __init__(self, key):
        super().__init__(key)

    @staticmethod
    def get_prompt(goal, birth_date, height, weight, gender, activity_level,
                   equipment, allergy, training_days, liked_exercises, disliked_exercises, health_issues):

        disliked_exercises = f'в ближайшем будущем я хочу весить {disliked_exercises} кг, ' if disliked_exercises else ''
        health_issues = f'Внимание, учти, что у меня есть проблемы со здоровьем: {health_issues}' if health_issues else ''
        allergy = f'У меня есть аллергия на {allergy}, ни в коем случае не добавляй ' \
                  'блюда с этими продуктами, иначе я умру.' if allergy else ''

        prompt = f'Ты профессиональный нутрициолог и эксперт в правильном, полноценном, здоровом питании, твоя ' \
                 'задача - создать простой и полезный рацион питания для меня, который приведёт меня к моей цели.' \
                 'Не начинай составлять рацион, пока я не напишу слово "Давай"\n' \
                 f'Составь мне рацион питания на неделю, на каждый день. Моя цель: {goal}, моя' \
                 f'дата рождения: {birth_date}, мой рост: {height} см,' \
                 f' мой вес {weight} кг, мой пол {gender}. Мой уровень активности - {activity_level}, ' \
                 f'{disliked_exercises} {health_issues}. ' \
                 f'Я люблю {liked_exercises}, ни в коем случае не добавляй мне в рацион блюда, в которых' \
                 f'есть эти продукты: {equipment}, мой образ жизни - {training_days},' \
                 f'{allergy} Я хочу чтобы у меня было {training_days} приёмов пищи в день. ' \
                 f'Ответ выдай в формате:' \
                 f'"День недели"' \
                 f'"Название приёма пищи:"' \
                 f'рацион на день' \
                 f'и так далее...' \
                 f'Давай'

        return prompt
