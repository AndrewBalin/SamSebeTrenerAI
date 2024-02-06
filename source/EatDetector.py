from GPTCreator import GPTCreator


class EatDetector(GPTCreator):
    def __init__(self, key):
        super().__init__(key)

    def generate(self, prompt, url):
        completion = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=1000,
        )

        answer = completion.choices[0].message.content

    @staticmethod
    def get_prompt():
        prompt = 'Перечисли все блюда, которые есть на фотографии. Для каждого блюда укажи количество каллорий,' \
                 'белков, жиров и углеводов, которые в нём содержатся.' \
                 'Ответ выдай в чётком формате, не выволи ничего кроме того, что я указал в формате :' \
                 'Блюда:\n' \
                 'Блюдо (число (грамм)): число (калорий), число (белков), число (жиров), число (углеводов).' \
                 '(примерные, на твой взгляд, в том числе учти объём/количество на ихображении)\n' \
                 'Пример ответа:\n' \
                 'Блюда:\n' \
                 'Пюре картофельное (215): 150, 45, 11, 20\n\n' \
                 'Если ты сделал то, что я просил, в конце выведи слово "ОК"'

        return prompt
