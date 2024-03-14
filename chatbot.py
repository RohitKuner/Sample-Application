import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyttsx3

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, the service is not available.")
        return ""

# Function to scrape information from a website
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Scraping logic to extract relevant information from the website
        # Replace this with your specific scraping code
        information = "Information scraped from the website..."
        return information
    except Exception as e:
        print("Error scraping website:", e)
        return "Sorry, I couldn't find the information."

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    # Define the URL of the website to scrape
    website_url = 'https://en.wikipedia.org/wiki/Disease_management_(agriculture)#:~:text=In%20agriculture%2C%20disease%20management%20is,protozoa%2C%20nematodes%20and%20parasitic%20plants.'

    print("Welcome to the Smart Chatbot. How can I assist you today?")
    while True:
        # Ask for user input through speech
        user_input = recognize_speech()

        if user_input.lower() == 'quit':
            print("Bye! Take care.")
            break

        # Scrape information from the website based on user input
        information = scrape_website(website_url)

        # Speak the information
        speak(information)
