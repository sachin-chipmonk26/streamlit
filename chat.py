import streamlit as st
import replicate
import os
import pandas as pd
from db import create_table, insert_order
import uuid  # To generate a unique order ID

try:
    # Assuming your dataset is a CSV file with columns 'user_prompt' and 'assistant_response'
    custom_dataset_path = r".\pizza.csv"
    custom_dataset_data = pd.read_csv(custom_dataset_path)
    custom_dataset = pd.DataFrame(custom_dataset_data)

    custom_user_path = r".\userdata.csv"
    custom_user_data = pd.read_csv(custom_user_path)
    custom_user = pd.DataFrame(custom_user_data)

    print(type(custom_dataset))
    print(custom_dataset.info())

    # App title
    st.set_page_config(page_title="🍕Pizza Bot🍕")

    # Replicate Credentials
    with st.sidebar:
        st.title('🍕Pizza Bot🍕')
        if 'REPLICATE_API_TOKEN' in st.secrets:
            st.success('API key already provided!', icon='✅')
            replicate_api = st.secrets['REPLICATE_API_TOKEN']
        else:
            replicate_api = st.text_input('Enter Replicate API token:', type='password')
            if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
                st.warning('Please enter your credentials!', icon='⚠️')
            else:
                st.success('Proceed to entering your prompt message!', icon='👉')
        os.environ['REPLICATE_API_TOKEN'] = replicate_api

        st.subheader('Models and parameters')

    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today? After adding your replicate API token, Type 'Hi' to continue"}]

    # Display or clear chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    # Initialize session state
    if 'order_values' not in st.session_state:
        st.session_state.order_values = {}

    # Function to add key-value pair to order_values
    def add_to_order_values(key, value):
        st.session_state.order_values[key] = value

    # Function to select category
    def select_category():
        # Display greeting message
        st.write("Please choose the Category")

        # Display buttons for category selection
        veg_pizza_button = st.button("Veg Pizza", key="veg_pizza")
        non_veg_pizza_button = st.button("Non Veg Pizza", key="non_veg_pizza")

        # Return the selected category
        if veg_pizza_button:
            add_to_order_values('category', 'Veg Pizza')
            return 'Veg Pizza'
        elif non_veg_pizza_button:
            add_to_order_values('category', 'Non Veg Pizza')
            return 'Non Veg Pizza'
        else:
            return None

    # Function to select pizza type
    def select_variety(category):
        # Display message for selecting variety
        st.write("Please choose your variety")

        # Display selectbox for variety selection based on the category
        if category == 'Veg Pizza':
            varieties = ['Veg Extravaganza', 'Peppy Paneer', 'Double cheese Margherita', 'Corn pizza', 'FarmHouse', 'Margherita']
        elif category == 'Non Veg Pizza':
            varieties = ['Chicken Sausage', 'Chicken Tikka', 'Barbeque Chicken', 'Chicken Golden Delight', 'Non-Veg Supreme', 'Chicken Dominator']
        else:
            varieties = []

        # Selectbox for variety selection
        selected_variety = st.selectbox("Select Variety", varieties)
        print("@@@", selected_variety)
        # Add the selected variety to order_values
        add_to_order_values('pizza_type', selected_variety)

        return selected_variety

    # Function to select size
    def select_size(pizza_type):
        # Display message for selecting size
        st.write(f"Please choose your size for {pizza_type}")

        # Display radio buttons for size selection
        sizes = ["Regular", "Medium", "Large"]
        selected_size = st.radio("Select Size", sizes, key="size")
        print("Qwerty",selected_size)
        # Add the selected size to order_values
        add_to_order_values('size', selected_size)

        # Display message for customization
        st.write("Would you like to customize your pizza?")

        # Display buttons for customization
        yes_button = st.button("Yes")
        no_button = st.button("No")

        # Add the choice to order_values
        if yes_button:
            add_to_order_values('is_customized', True)
        elif no_button:
            add_to_order_values('is_customized', False)

        return selected_size

    # Function to customize pizza based on user choice
    def customize_pizza(is_customized):
        while is_customized:
            st.write("Please choose how would you like to customize")

            # Display buttons for customization type
            crust_button = st.button("Crust type",key="crust_type")
            toppings_button = st.button("Toppings", key="toppings")
            extra_cheese_button = st.button("Add Extra Cheese", key="extra_cheese")
            done_button = st.button("I am done customizing", key="done_customizing")

            # Update customization type in order_values
            if crust_button:
                st.write("Pick a crust type")
                # Display buttons for crust type selection
                crust_types = ["Classic Hand Tossed", "Wheat Thin Crust", "Cheese Burst", "Fresh Pan Pizza", "Italian Crust", "Double Cheese Crunch"]
                selected_crust_type = st.button(crust_types)

                # Update crust type in order_values
                if selected_crust_type:
                    add_to_order_values('crust_type', selected_crust_type)

            elif toppings_button:
                add_to_order_values('customization_type', 'Toppings')
                
                # Display buttons for toppings selection
                st.write("Select one or more Toppings")
                toppings_list = [
                    "Black Olive - $0.75", "Onion - $0.50", "Crisp Capsicum - $0.60",
                    "Paneer - $1.00", "Mushroom - $0.80", "Golden Corn - $0.70",
                    "Fresh Tomato - $0.60", "Jalapeno - $0.75", "Red Paprika - $0.70",
                    "Babycorn - $1.20"
                ]
                selected_toppings = st.multiselect("Select Toppings", toppings_list)

                # Update toppings in order_values
                if selected_toppings:
                    add_to_order_values('toppings', selected_toppings)

            elif extra_cheese_button:
                add_to_order_values('customization_type', 'Add Extra Cheese')
                # Update extra_cheese in order_values
                add_to_order_values('extra_cheese', True)
                
            elif done_button:
                add_to_order_values('customization_type', 'I am done customizing')
                break  # Exit the loop when done customizing

    # Function to select quantity
    def select_quantity():
        st.write("Please choose the Quantity")

        # Display buttons for quantity selection
        quantities = [1, 2, 3, 4, 5, 6]
        selected_quantity = st.button("Select Quantity",quantities, key="quantity")

        # Update quantity in order_values
        if selected_quantity:
            add_to_order_values('quantity', selected_quantity)

            # Ask for user details
            user_name = st.text_input("Please enter your name")
            add_to_order_values('user_name', user_name)

            address = st.text_input("Please enter your full address")
            add_to_order_values('address', address)

            phone = st.text_input("Please enter your phone number")
            add_to_order_values('phone', phone)

            # Generate a unique order ID
            order_id = str(uuid.uuid4())
            add_to_order_values('orderID', order_id)

            # Update order status
            add_to_order_values('order_status', 'Processing')

    # Function to check if the user wants to order more pizza
    def order_more_pizza():
        st.write("Do you want to order more pizza?")
        yes_button = st.button("Yes, I want to")
        no_button = st.button("No, I don't want")
        
        if yes_button:
            # Reset order_values for a new order
            st.session_state.order_values = {}
        elif no_button:
            # Exit the application or take necessary action

    # User-provided prompt
         replicate_api = True
    while replicate_api:
        # Call the function to select category
        selected_category = select_category()
        print("@#",selected_category)
        # Update the order_values dictionary based on the selected category
        if selected_category:
            # Call the function to select variety
            selected_variety = select_variety(selected_category)
            # Update the order_values dictionary based on the selected variety
            if selected_variety:
                # Call the function to select size and customize
                selected_size = select_size(selected_variety)

                # Call the function to customize pizza based on the customization choice
                customize_pizza(st.session_state.order_values.get('is_customized', False))

        # Check if the user wants to order more pizza
        if st.session_state.order_values.get('is_customized', False):
            order_more_pizza()

        # Print the final order values
        print(st.session_state.order_values)
except Exception as e:
    print(f"An exception occurred: {e}")
