# -*- coding: utf-8 -*-
"""ChatbotForFAQs.ipynb

Original file is located at
    https://colab.research.google.com/drive/1gx4Cq3dubHI6Tyh7Oso664XPBgpjjAkG

# **Introduction**

---



Hello, My name is Samyak Vaidya. Welcome to my chatbot project, designed to answer frequently asked questions (FAQs) about the Mahindra Bolero Neo Plus. I choose to work on the FAQs for this specific car upon my Friend request, as he was fascinated by the Mahindra Bolero Neo Plus. This project utilizes natural language processing (NLP) techniques with the SpaCy library to understand and generate responses based on predefined FAQs. The goal of this project is to demonstrate my skills in developing interactive and intelligent systems.




---

 # Mahindra Bolero Neo Plus

<img width="419" height="236" alt="Image" src="https://github.com/user-attachments/assets/7de34264-b32f-4e62-882e-0322830a22df" />


# `Project Overview:`

1. Importing the Required Library: SpaCy is imported to handle NLP tasks.
2. Loading the SpaCy Language Model: The English language model (en_core_web_sm) is loaded to process text.
3. Defining FAQs and Responses: A set of FAQs about the Mahindra Bolero Neo Plus and their corresponding answers are defined.
4. Defining the Chatbot Response Function: This function generates responses based on strict keyword matching to ensure the chatbot only answers predefined FAQs.
5. Displaying FAQs: The FAQs are displayed to the user before they start asking questions.
6. Interactive CLI: A command-line interface is implemented to allow users to interact with the chatbot directly.
"""

!pip install spacy
!python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')

# Define FAQs and responses for Mahindra Bolero Neo Plus
faqs = {
    "Who Owned Mahindra Bolero Neo Plus?": "Samyak Praveen Vaidya Owned This Car.",
    "What are the variants and prices of the Mahindra Bolero Neo Plus?": "The Bolero Neo Plus is available in two diesel variants: P4 (base) and P10 (top-spec). Ex-showroom prices start at ₹11.41 lakh for the P4 and go up to ₹12.51 lakh for the P10 (Delhi prices; on-road prices may vary by location and include taxes/insurance). The P10 adds features like alloy wheels, a touchscreen infotainment system, and enhanced interior upholstery.",
    "What is the engine specification and performance of the Mahindra Bolero Neo Plus?": "The Mahindra Bolero Neo Plus is powered by a 2.2-litre mHawk turbocharged diesel engine producing 118 bhp at 4,000 rpm and 280 Nm of torque between 1,800-2,800 rpm. The engine is paired exclusively with a 6-speed manual transmission. The top speed is around 125-130 km/h, and it excels in off-road conditions due to its robust ladder-frame construction.",
    "What is the mileage of the Bolero Neo Plus?": "Mahindra claims an ARAI-certified mileage of 14-18.9 kmpl (depending on variant and conditions), with real-world figures typically around 14 kmpl in mixed city and highway driving. Fuel tank capacity is 60 litres.",
    "How many seats does it have, and what are the seating and interior features?": "It accommodates up to 9 passengers in a flexible 2+3+4 bench-seat layout, ideal for large families or commercial use. Rear seats can be folded for extra cargo space. Interiors include practical features like fabric upholstery, a 9-inch touchscreen (in P10), Bluetooth connectivity, USB ports, rear AC vents, and ample storage. The cabin is spacious but basic, with a focus on durability over luxury.",
    "What are the key dimensions and ground clearance?": "The SUV measures 4,400 mm in length, 1,795 mm in width, 1,812 mm in height, with a 2,680 mm wheelbase. It offers a ground clearance of 180 mm (unladen), making it suitable for rough terrains, and boot space of up to 696 litres with seats folded.",
    "What safety features are available in Bolero Neo Plus?": "The Bolero Neo Plus has Standard safety includes dual front airbags, ABS with EBD, rear parking sensors, electronic stability control (ESC), seatbelt reminders, child safety locks, ISOFIX anchors, and an engine immobilizer. It has not yet been crash-tested by Global NCAP. The rigid chassis enhances overall protection.",
    "What are the color options in Bolero Neo Plus?": "The Bolero Neo Plus Available in three colors :- Napoli Black, Majestic Silver, and Diamond White.",
    "Is there an automatic transmission or petrol engine option in Bolero Neo Plus?": "No, it is diesel-only with manual transmission. There is no automatic variant or petrol engine available.",
    "Does it have a sunroof or advanced features like keyless entry in Bolero Neo Plus?": "No sunroof is offered in any variant. Keyless entry is absent even in the top P10; it uses a traditional key. However, the P10 includes conveniences like a rear parking camera and steering-mounted audio controls.",
    "What is the warranty and maintenance like in Bolero Neo Plus?": "It comes with a standard 3-year/1,00,000 km warranty, with options for extended coverage, roadside assistance, and corrosion protection. Maintenance costs are low (around ₹7,200 for 5 years/50,000 km), with service intervals every 10,000 km.",
    "What extended warranty options are there in Bolero Neo Plus?": "Beyond the standard 3-year/1,00,000 km warranty, Mahindra provides extensions up to 5 years/1,50,000 km for ₹15,000–₹25,000 (depending on variant). This includes roadside assistance and covers engine/transmission. Commercial users can opt for fleet packages with lower premiums.",
    "What is the 0–100 km/h acceleration and top speed in Bolero Neo Plus?": "The 2.2L mHawk diesel accelerates from 0–100 km/h in about 14–15 seconds (fully loaded), with a governed top speed of 140 km/h. It's tuned for low-end torque rather than outright speed, making it suitable for overtakes in traffic or loaded hauls rather than high-speed cruising.",
    "What are the braking and tyre specifications in Bolero Neo Plus?": "It features disc brakes at the front and drum at the rear, with good stopping power for its 1,900 kg kerb weight (from 100–0 km/h in about 45 metres). Tyres are 215/75 R15 (steel in P4, alloys in P10), offering solid grip on highways and dirt; recommended pressure is 32–35 PSI for optimal handling.",
    "What is the expected resale value after 3–5 years of Bolero Neo Plus?": "Resale holds strong at 65–75% of original price after 3 years (e.g., a ₹11 lakh model resells for ₹7–8 lakh), thanks to its rugged build and demand in commercial segments.",
    "What is the seating comfort like for long journeys in Bolero Neo Plus?": "The 2+3+4 layout provides ample space for 9 adults in city or short drives, with good legroom in the first two rows and armrests. However, the third-row bench is best for shorter occupants or city use; it's less comfortable for adults on highways due to firm cushioning and limited recline. Rear AC vents help maintain comfort.",
    "Does it have advanced suspension or ride tech?": "Yes, it features Mahindra's RIDEFLO technology, which optimizes suspension, steering, and braking for better handling on rough roads. The body-on-frame chassis and 180 mm ground clearance ensure a composed ride over potholes and uneven terrain, though it's firmer than urban SUVs like the Ertiga.",
    "What is the service network coverage like?": "Mahindra has over 1,000 service centers across India, with strong presence in Tier 2/3 cities and rural areas—ideal for Bolero owners. Mobile service vans cover remote locations, and the MyMahindra app allows booking with average wait times under 24 hours."
}

def chatbot_response(user_input):
    user_doc = nlp(user_input.lower())
    for question, answer in faqs.items():
        question_doc = nlp(question.lower())
        if all(token.text in user_doc.text for token in question_doc):  # Check if any keyword from the FAQ matches the user input
            return answer
    return "I'm sorry, you can only ask questions about the FAQs provided."

# Function to display FAQs
def display_faqs():
    print("Here are some frequently asked questions:")
    for question in faqs:
        print("-", question)

def chat_with_bot():
    print("\n\n Hello! I am an FAQ Chatbot. Ask me anything from the FAQs.")
    print("Type 'bye' to end the conversation.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye! \n < Thank You For Using Me >")
            break
        if user_input.lower() == 'thank you':
            print("My pleasure to provide help! Take care :) ")
            continue
        response = chatbot_response(user_input)
        print("Bot:", response)

# Start chatting with the bot
display_faqs()
print("\n\n")
chat_with_bot()