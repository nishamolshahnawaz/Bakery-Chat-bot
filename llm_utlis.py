#import google.generativeai as genai
import google.genai as genai
from menu_loader import load_menu
from google.genai import types
import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")

#genai.configure(api_key=API_KEY)
client=genai.Client(api_key=API_KEY)  #communicationn object
#model=genai.GenerativeModel("gemini-3.5-flash-lite")
#chat= model.start_chat()
CAKE_MENU=load_menu()
SYSTEM_INSTRUCTIONS=f"""
You are a friendly asistant for a homemade cake business
based in Dubai and Sharjah.
Your name in nisha's Cake World Assistant.

Here is the cake Menu:
{CAKE_MENU}

Help the customer place a cake order.

Follow these  steps:

1. Greet the customer warmly.
2. If the customer wants to see the menu, show the available cakes.
3. Ask which cake they would like to order.
4. Make sure the selected cake exists in the menu.
5. Ask for the Quantity.
6. Ask for the delivery location.
7. Ask for the preferred delivery time.
8. Ask for the occasion.
9. Ak whether they need any special decorations.
10. Once all information is collected, provide a clear summary.

The order summary should contain:
- cake name
- Quantity
- Price
- Delivery location
- Delivery time
- Occasion
- Decorationns
- Total price

Payment is offline/on delivery.

Be friendly and use emojis occasionally.
Do not invent cakes that are not i the menu.
"""
#chat=model.start_chat()
# chat.send_message(SYSTEM_INSTRUCTIONS)
# def send_message_to_llm(message):
#     response=chat.send_message(message)
#     text=response.text
#     return text

chat =None
def start_session():
    global chat
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTIONS
   )
)

def send_message_to_llm(message):
    response = chat.send_message(message)
    text = response.text
    return text