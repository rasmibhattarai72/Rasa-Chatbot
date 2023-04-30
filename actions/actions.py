from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


account_balances = {
    "Rasmi": 6000,
    "Usha": 5000,
    "Sabina": 3000,
    "Soniya": 2000,
    "Smriti": 1000
}

transaction_records = {
"Rasmi": [
{"date": "2022-01-01", "description": "Salary Credit", "amount": 20000},
{"date": "2022-01-10", "description": "Grocery Shopping", "amount": -1500},
{"date": "2022-01-15", "description": "Rent Payment", "amount": -6000}
],
"Usha": [
{"date": "2022-01-01", "description": "Salary Credit", "amount": 15000},
{"date": "2022-01-10", "description": "Grocery Shopping", "amount": -2000},
{"date": "2022-01-15", "description": "Rent Payment", "amount": -5000}
],
"Sabina": [
{"date": "2022-01-01", "description": "Salary Credit", "amount": 10000},
{"date": "2022-01-10", "description": "Grocery Shopping", "amount": -1000},
{"date": "2022-01-15", "description": "Rent Payment", "amount": -4000}
],
"Soniya": [
{"date": "2022-01-01", "description": "Salary Credit", "amount": 8000},
{"date": "2022-01-10", "description": "Grocery Shopping", "amount": -500},
{"date": "2022-01-15", "description": "Rent Payment", "amount": -3000}
],
"Smriti": [
{"date": "2022-01-01", "description": "Salary Credit", "amount": 5000},
{"date": "2022-01-10", "description": "Grocery Shopping", "amount": -700},
{"date": "2022-01-15", "description": "Rent Payment", "amount": -4000}
]
}

class ActionGiveBalance(Action):
    def name(self) -> Text:
        return "action_give_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = next(tracker.get_latest_entity_values("person"), None)

        balance = account_balances.get(name, None)

        if balance is None:
            message = f"Sorry, I don't have the account balance of {name}."
        else:
            message = f"The account balance of {name} is {balance}."

        dispatcher.utter_message(text=message)

        return []
    
class TransactionHistory(Action):

    def name(self) -> Text:
        return "action_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = next(tracker.get_latest_entity_values("person"), None)

        transactions = transaction_records.get(name, None)

        if transactions is None:
            message = f"Sorry, I don't have the transaction records of {name}."
        else:
            message = f"The transaction records of {name} are: {transactions}."

        dispatcher.utter_message(text=message)

        return []