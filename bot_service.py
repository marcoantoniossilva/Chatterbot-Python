from bot import * 
from flask import Flask

VERSION = "1.0"


bot = ChatBot("Robô de atendimento da Linda Joia",
    read_only=True,
    statement_comparison_function=comparate_messages,
    response_selection_method=select_response,
    logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch",
        }
    ])
bot_service = Flask(__name__)

@bot_service.route("/version", methods=["GET"])
def get_version():
    return VERSION

@bot_service.route("/response/<message>", methods=["GET"])
def get_response(message):
    response = bot.get_response(message)

    return response.text

if __name__ == "__main__":
    bot_service.run()
