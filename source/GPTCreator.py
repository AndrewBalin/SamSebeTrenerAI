from openai import OpenAI


class GPTCreator:
    def __init__(self, key):
        self.client = OpenAI(api_key=key)

    def generate(self, prompt, **kwargs):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        answer = completion.choices[0].message.content

        return answer

    @staticmethod
    def get_prompt(**kwargs):
        pass
