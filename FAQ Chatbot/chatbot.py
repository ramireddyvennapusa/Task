import google.generativeai as genai

genai.configure(api_key="AIzaSyBQiGk4ebXGGSqqdgZdYzQlBsOs4PBthtE")

faqs = {
    "programs": "Iron Lady offers leadership programs designed for women professionals.",
    "duration": "The program duration varies, but typically runs for 8 to 12 weeks.",
    "mode": "The programs are conducted both online and offline.",
    "certificate": "Yes, participants receive a certificate after successful completion.",
    "mentors": "The mentors are experienced industry leaders and certified coaches."
}

def get_answer(user_input):
    user_input = user_input.lower()
    if "program" in user_input:
        return faqs["programs"]
    elif "duration" in user_input:
        return faqs["duration"]
    elif "online" in user_input or "offline" in user_input:
        return faqs["mode"]
    elif "certificate" in user_input:
        return faqs["certificate"]
    elif "mentor" in user_input or "coach" in user_input:
        return faqs["mentors"]
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            return response.text
        except Exception as e:
            return "Sorry, I’m not sure about that right now."

def chat():
    print("Iron Lady Chatbot (type 'exit' to quit)\n")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            print("Chatbot: Goodbye")
            break
        reply = get_answer(user_message)
        print("Chatbot:", reply, "\n")

if __name__ == "__main__":
    chat()
