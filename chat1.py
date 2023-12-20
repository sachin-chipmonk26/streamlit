# Import necessary libraries
import streamlit as st

# Define pizza categories and questions
categories = {
    "types" : "",
    "varieties":"",
    "sizes":"",
    "is_customized":"",
    "customize":"",
    "crust_type":"",
    'toppings':"",
    "extra_cheese":""
}

non_veg_pizza_types = [
    "Chicken Dominator",
    "Cheese and Pepperoni",
    "Non Veg Supreme",
    "Chicken Mexicana",
    "Chicken Golden Delight",
    "Barbeque Chicken",
    "Chicken Fiesta"
]

veg_pizza_types = [
    "Veg Extravaganza",
    "Peppy Paneer",
    "Double Cheese Margherita",
    "Corn Pizza",
    "FarmHouse",
    "Margherita"
]

pizza_sizes = [
    "Regular",
    "Medium",
    "Large"
]   

customization_types = [
    "Crust type",
    "Toppings",
    "Add Extra Cheese",
    "I am done customizing"
]

crust_types = {
    "Classic Hand Tossed": 1.50,
    "Wheat Thin Crust": 2.00,
    "Cheese Burst": 2.50,
    "Fresh Pan Pizza": 1.75,
    "Italian Crust": 2.25,
    "Double Cheese Crunch": 2.75
}

toppings_dict = {
    "Black Olive": 0.75,
    "Onion": 0.50,
    "Crisp Capsicum": 0.60,
    "Paneer": 1.00,
    "Mushroom": 0.80,
    "Golden Corn": 0.70,
    "Fresh Tomato": 0.60,
    "Jalapeno": 0.75,
    "Red Paprika": 0.70,
    "Babycorn": 1.20
}


if 'types' not in st.session_state:
    st.session_state['types'] = ''
if 'veg_varieties' not in st.session_state:
    st.session_state['veg_varieties'] = ''
if 'non_veg_varieties' not in st.session_state:
    st.session_state['non_veg_varieties'] = ''
if 'sizes' not in st.session_state:
    st.session_state['sizes'] = ''
if 'is_customized' not in st.session_state:
    st.session_state['is_customized'] = ""
if 'customize' not in st.session_state:
    st.session_state['customize'] = ""
if 'crust' not in st.session_state:
    st.session_state['crust'] = ""
if 'toppings' not in st.session_state:
    st.session_state['toppings'] = ""
if 'extra_cheese' not in st.session_state:
    st.session_state['extra_cheese'] = ""


def click_button_type(types):
    st.session_state['types'] = types

def click_button_variety(varieties):
    if(len(st.session_state['types'])!=0 and st.session_state['types'].lower() == "veg pizza"):
        st.session_state['veg_varieties'] = varieties
        
    elif(len(st.session_state['types'])!=0 and st.session_state['types'].lower() == "non veg pizza"):
        st.session_state['non_veg_varieties'] = varieties

def click_button_size(sizes):
    st.session_state['sizes'] = sizes

def click_button_is_customize(flag):
    st.session_state['is_customized'] = flag

def click_button_customize(customize):
    st.session_state['customize'] = customize

def click_button_crust(crust):
    st.session_state['crust'] = crust

def click_button_topping(toppings):
    st.session_state['toppings'] = toppings

def add_extra_cheese(cheese):
    st.session_state['extra_cheese'] = cheese

# Streamlit app
def pizza_ordering_chatbot():
    st.title("Pizza Ordering Chatbot")

    # User greeting
    user_input = st.text_input("Say 'hi' to start the chatbot:")
    
    if user_input.lower() == 'hi':
        st.text("Hello! I'm the pizza ordering chatbot. Choose a category to get started.")
        st.button('Veg Pizza', on_click=click_button_type,args=['Veg Pizza'])
        st.button('Non Veg Pizza', on_click=click_button_type,args=['Non Veg Pizza'])
        st.text(st.session_state['types'])

        if(len(st.session_state['types'])!=0 and st.session_state['types'].lower() == "veg pizza"):
            st.text("Choose the variety of veg Pizza")
            st.button('Veg Extravaganza', on_click=click_button_variety,args=['Veg Extravaganza'])
            st.button('Peppy Paneer', on_click=click_button_variety,args=['Peppy Paneer'])
            st.button('Double Cheese Margherita', on_click=click_button_variety,args=['Double Cheese Margherita'])
            st.button('Corn Pizza', on_click=click_button_variety,args=['Corn Pizza'])
            st.button('FarmHouse', on_click=click_button_variety,args=['FarmHouse'])
            st.button('Margherita', on_click=click_button_variety,args=['Margherita'])  
            st.text(st.session_state['veg_varieties'])    
            if(len(st.session_state['veg_varieties'])!=0 and st.session_state['veg_varieties'].lower() in [pizza.lower() for pizza in veg_pizza_types]):
                st.text('Please choose your size')
                st.button('Regular', on_click=click_button_size,args=['Regular'])
                st.button('Medium', on_click=click_button_size,args=['Medium'])
                st.button('Large', on_click=click_button_size,args=['Large'])
                st.text(st.session_state['sizes'])
                if(len(st.session_state['sizes'])!=0 and st.session_state['sizes'].lower() in [pizza.lower() for pizza in pizza_sizes]):
                    st.text("Would you like to customize your pizza")
                    st.button('Yes', on_click=click_button_is_customize,args=["Yes"])
                    st.button('No', on_click=click_button_is_customize,args=["No"])
                    st.text(st.session_state["is_customized"])
                    if(len(st.session_state['is_customized'])!=0 and st.session_state['is_customized'].lower() == "yes"):
                        # while True:
                        st.text('Please choose how would you like to customize')
                        st.button('Crust type', on_click=click_button_customize,args=['Crust type'])
                        st.button('Toppings', on_click=click_button_customize,args=['Toppings'])
                        st.button('Add Extra Cheese', on_click=click_button_customize,args=['Add Extra Cheese'])
                        st.button('I am done customizing', on_click=click_button_customize,args=['I am done customizing'])
                        st.text(st.session_state["customize"])
                        if(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "crust type"):
                            st.text("Pick a crust type")
                            st.button('Classic Hand Tossed', on_click=click_button_crust,args=['Classic Hand Tossed'])
                            st.button('Wheat Thin Crust', on_click=click_button_crust,args=['Wheat Thin Crust'])
                            st.button('Cheese Burst', on_click=click_button_crust,args=['Cheese Burst'])
                            st.button('Fresh Pan Pizza', on_click=click_button_crust,args=['Fresh Pan Pizza'])
                            st.button('Italian Crust', on_click=click_button_crust,args=['Italian Crust'])
                            st.button('Double Cheese Crunch', on_click=click_button_crust,args=['Double Cheese Crunch'])
                            st.text(st.session_state["crust"])
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "toppings"):
                            st.text("Select one or more Toppings")
                            st.button('Black Olive', on_click=click_button_topping,args=['Black Olive'])
                            st.button('Onion', on_click=click_button_topping,args=['Onion'])
                            st.button('Crisp Capsicum', on_click=click_button_topping,args=['Crisp Capsicum'])
                            st.button('Paneer', on_click=click_button_topping,args=['Paneer'])
                            st.button('Mushroom', on_click=click_button_topping,args=['Mushroom'])
                            st.button('Golden Corn', on_click=click_button_topping,args=['Golden Corn'])
                            st.button('Fresh Tomato', on_click=click_button_topping,args=['Fresh Tomato'])
                            st.button('Jalapeno', on_click=click_button_topping,args=['Jalapeno'])
                            st.button('Red Paprika', on_click=click_button_topping,args=['Red Paprika'])
                            st.button('Babycorn', on_click=click_button_topping,args=['Babycorn'])
                            st.text(st.session_state["toppings"])
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "add extra cheese"):
                            add_extra_cheese("Yes")
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "i am done customizing"):
                            st.text("Coding in progress")
                            categories["types"] = st.session_state["types"]
                            if(len(st.session_state["veg_varieties"])>0):
                                categories['varieties'] = st.session_state["veg_varieties"]
                            else:
                                categories['varieties'] = st.session_state["non_veg_varieties"]
                            categories['crust_type'] = st.session_state["crust"]
                            categories['toppings'] = st.session_state["toppings"]
                            categories['extra_cheese'] = st.session_state["extra_cheese"]

                            print("types", categories["varieties"])  # Fix: Added the missing closing parenthesis
                            print("types", categories["crust_type"])  # Fix: Added the missing closing parenthesis
                            print("types", categories["toppings"])  # Fix: Added the missing closing parenthesis
                            print("types", categories["extra_cheese"])  # Fix: Added the missing closing parenthesis
                            

                    elif(len(st.session_state['is_customized'])!=0 and st.session_state['is_customized'].lower() == "no"):
                        st.text("Coding in progress")
        elif(len(st.session_state['types'])!=0 and st.session_state['types'].lower() == "non veg pizza"):
            st.text("Choose the variety of non veg Pizza")
            st.button('Chicken Dominator', on_click=click_button_variety,args=['Chicken Dominator'])
            st.button('Cheese and Pepperoni', on_click=click_button_variety,args=['Cheese and Pepperoni'])
            st.button('Non Veg Supreme', on_click=click_button_variety,args=['Non Veg Supreme'])
            st.button('Chicken Mexicana', on_click=click_button_variety,args=['Chicken Mexicana'])
            st.button('Chicken Golden Delight', on_click=click_button_variety,args=['Chicken Golden Delight'])
            st.button('Barbeque Chicken', on_click=click_button_variety,args=['Barbeque Chicken'])
            st.button('Chicken Fiesta', on_click=click_button_variety,args=['Chicken Fiesta'])
            st.text(st.session_state['non_veg_varieties'])  
            if(len(st.session_state['non_veg_varieties'])!=0 and st.session_state['non_veg_varieties'].lower() in [pizza.lower() for pizza in non_veg_pizza_types]):
                st.text('Please choose your size')
                st.button('Regular', on_click=click_button_size,args=['Regular'])
                st.button('Medium', on_click=click_button_size,args=['Medium'])
                st.button('Large', on_click=click_button_size,args=['Large'])
                st.text(st.session_state['sizes'])
                if(len(st.session_state['sizes'])!=0 and st.session_state['sizes'].lower() in [pizza.lower() for pizza in pizza_sizes]):
                    st.text("Would you like to customize your pizza")
                    st.button('Yes', on_click=click_button_is_customize,args=["Yes"])
                    st.button('No', on_click=click_button_is_customize,args=["No"])
                    st.text(st.session_state["is_customized"])
                    if(len(st.session_state['is_customized'])!=0 and st.session_state['is_customized'].lower() == "yes"):
                        st.text('Please choose how would you like to customize')
                        st.button('Crust type', on_click=click_button_customize,args=['Crust type'])
                        st.button('Toppings', on_click=click_button_customize,args=['Toppings'])
                        st.button('Add Extra Cheese', on_click=click_button_customize,args=['Add Extra Cheese'])
                        st.button('I am done customizing', on_click=click_button_customize,args=['I am done customizing'])
                        st.text(st.session_state["customize"])
                        if(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "crust type"):
                            st.text("Pick a crust type")
                            st.button('Classic Hand Tossed', on_click=click_button_crust,args=['Classic Hand Tossed'])
                            st.button('Wheat Thin Crust', on_click=click_button_crust,args=['Wheat Thin Crust'])
                            st.button('Cheese Burst', on_click=click_button_crust,args=['Cheese Burst'])
                            st.button('Fresh Pan Pizza', on_click=click_button_crust,args=['Fresh Pan Pizza'])
                            st.button('Italian Crust', on_click=click_button_crust,args=['Italian Crust'])
                            st.button('Double Cheese Crunch', on_click=click_button_crust,args=['Double Cheese Crunch'])
                            st.text(st.session_state["crust"])
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "toppings"):
                            st.text("Select one or more Toppings")
                            st.button('Black Olive', on_click=click_button_topping,args=['Black Olive'])
                            st.button('Onion', on_click=click_button_topping,args=['Onion'])
                            st.button('Crisp Capsicum', on_click=click_button_topping,args=['Crisp Capsicum'])
                            st.button('Paneer', on_click=click_button_topping,args=['Paneer'])
                            st.button('Mushroom', on_click=click_button_topping,args=['Mushroom'])
                            st.button('Golden Corn', on_click=click_button_topping,args=['Golden Corn'])
                            st.button('Fresh Tomato', on_click=click_button_topping,args=['Fresh Tomato'])
                            st.button('Jalapeno', on_click=click_button_topping,args=['Jalapeno'])
                            st.button('Red Paprika', on_click=click_button_topping,args=['Red Paprika'])
                            st.button('Babycorn', on_click=click_button_topping,args=['Babycorn'])
                            st.text(st.session_state["toppings"])
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "add extra cheese"):
                            add_extra_cheese("Yes")
                        elif(len(st.session_state['customize'])!=0 and st.session_state['customize'].lower() == "i am done customizing"):
                            st.text("Coding in progress")

                    elif(len(st.session_state['is_customized'])!=0 and st.session_state['is_customized'].lower() == "no"):
                        st.text("Coding in progress")



        
if __name__ == "__main__":
    pizza_ordering_chatbot()