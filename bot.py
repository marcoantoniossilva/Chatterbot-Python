from chatterbot import ChatBot
from difflib import SequenceMatcher

ACCEPTANCE = 0.70

def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(),2)
        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)

    return similarity

def select_response(message, list_response, storage=None):
    response = list_response[0]
    print("resposta escolhida:", response)

    return response


def execute_bot():
    bot = ChatBot("Robô de atendimento da Linda Joia",
        read_only=True,
        statement_comparison_function=comparate_messages,
        response_selection_method=select_response,
        logic_adapters=[
            {
                "import_path":"chatterbot.logic.BestMatch",
            }
        ])

    while True:
        chat_input = input("Digite alguma coisa...\n",)
        response = bot.get_response(chat_input)

        if response.confidence > 0.0:
            print(response.text)
        else:
            print("Ainda não sei como responder essa pergunta :(")
            print("Pergunte outra coisa...")

if __name__ == "__main__":
    execute_bot()