
import openai
from creds.credentials import OPENAI_KEY

openai.api_key = OPENAI_KEY


def get_chat_response(conversation):
	messages = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages= conversation
	)
	return messages