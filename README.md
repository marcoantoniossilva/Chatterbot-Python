# Chatterbot-Python
Simple chat robot using Python and flask

Usage:

1º - Configure questions and answers in the dictionaries present in /conversations or create new ones. If you have created new dictionaries, you must add them to the 'CONVERSATION_SETTINGS' array in 'trainer.py.

2º - Run the 'trainer.py' file to train the robot with the previously configured questions and answers.

3º - Run the file 'bot_service.py' and keep it listening on the console.

4º - Run the file '/chat/index.js' with the node (node /chat/index.js) and open localhost: 3000 in the browser.
