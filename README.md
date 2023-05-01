# Rasa-Chatbot
<h3><b>Bank Chatbot Project</b></h3>

This project is a simple chatbot that is trained to understand user intents related to checking account balance, transaction history, and some basic intents like greetings and goodbyes. The chatbot is built using the Rasa framework, an open-source framework for building conversational AI chatbots.

<h3><b>Project Steps:</b></h3>

1. The Rasa project is initialized using the command <b>"rasa init"</b>. This sets up the basic project structure and files.

2. A Python dictionary is created to store the information for account balance and transaction history of a few persons.

3. Training examples for checking account balance and transaction history are added in the "nlu.yml" file. A lookup table for person names is also added to help identify the name of the person whose account balance or transaction history is being requested.

4. Rules are added to the "rules.yml" file to provide quick responses for common questions related to account balance and transaction history.

5. Required intents and actions are added to the "domain.yml" file. Custom actions are created to give account balance and transaction history based on user input.

6. A custom action server is created in the "actions.py" file to perform the required actions.

7. The required pipeline and policies are defined in the "config.yml" file.

8. The action endpoint is defined in the "endpoints.yml" file.


<h3><b>Requirements:</b></h3>
To run this project, you will need to install the following dependencies:

Rasa: <b>pip install rasa</b>



<h3><b>How to Use:</b></h3>

To run the chatbot, follow these steps:

1. Open two terminals.

2. Navigate to the project directory in both terminals.

3. In the first terminal, run the command <b>"rasa train"</b> to train the chatbot.

4. In the second terminal, start the custom actions server by running the command <b>"rasa run actions"</b>.

5. In the first terminal, launch the chatbot interface by running the command <b>"rasa shell"</b>.

6. Interact with the chatbot by typing in questions related to account balance and transaction history.

7. The chatbot will provide appropriate responses based on the information stored in its Python dictionary.

