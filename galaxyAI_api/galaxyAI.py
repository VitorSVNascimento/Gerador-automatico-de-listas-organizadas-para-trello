from dotenv import load_dotenv
import os
import openai as galaxyai
load_dotenv()

AI_MODEL = 'gpt-3.5-turbo'

def get_response(user_prompt:str) -> str:

    galaxyai.api_key = os.getenv('GALAXY_API_KEY')
    galaxyai.api_base = os.getenv('GALAXY_BASE_URL')


    sys_prompt = os.getenv('GPT_PROMPT')

    completion = galaxyai.ChatCompletion.create(
        model=AI_MODEL,
        messages=[
                {
                    'role':'system',
                    'content':sys_prompt
                },

                {
                    'role':'user',
                    'content':user_prompt
                }
            ]
    )

    print(completion)