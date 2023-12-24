import os
import time
import speech_recognition as sr
import pygame.font

class Jarvis:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jarvis")
        self.font = pygame.font.SysFont(None, 36)

    def display_text(self, text):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(text_surface, (10, 10))
        pygame.display.flip()

    def get_audio(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something...")
            try:
                audio = r.listen(source, timeout=5)
                words_said = r.recognize_google(audio)
                print("You said:", words_said)
                return words_said.lower()
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return ""

    def run_jarvis(self):
        running = True

        while running:
            try:
                words_said = self.get_audio()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if words_said:
                    response = self.generate_response(words_said)
                    if response:
                        self.display_text(response)

            except Exception as e:
                print(f"An error occurred: {e}")

        pygame.quit()

    def generate_response(self, words_said):
        responses = {
            "how are you": "I'm fine thank you, and you?",
            "stop": "Goodbye! Take care.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what's the weather": "I'm sorry, I cannot provide real-time weather information.",
            "thank you": "You're welcome!",
            "your name": "I'm Jarvis, your virtual assistant.",
            "bye": "Goodbye! Take care.",
            "favorite color": "I don't have a favorite color. I'm a machine learning model!",
            "tell me about yourself": "I am Jarvis, an AI assistant designed to help you with various tasks. How can I assist you today?",
            "what's the meaning of life": "The meaning of life is a philosophical question. Many people find meaning in relationships, personal achievements, or helping others.",
            "sing a song": "I'm not a great singer, but here's a short tune for you: La la la!",
            "what's your favorite book": "I don't have preferences, but I can recommend books based on your interests!",
            "are you human": "No, I'm an artificial intelligence designed to assist you.",
            "how do you work": "I analyze input data and provide responses based on pre-existing patterns.",
            "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "what's the time": "I'm sorry, I don't have real-time information, but your device should display the current time.",
            "tell me a riddle": "I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
            "are you friendly": "Yes, I'm here to assist and provide information in a friendly manner.",
            "who is your favorite superhero": "I don't have personal preferences, but I can share information about popular superheroes!",
            "do you play video games": "I don't play video games, but I can help you find information about them!",
            "what's the meaning of love": "Love is a complex and profound emotion that can take many forms. It's often described as a deep affection and connection with someone or something.",
            "how to stay motivated": "Staying motivated involves setting goals, staying positive, and taking breaks when needed. What specific area do you need motivation in?",
            "tell me a science fact": "A teaspoonful of neutron star material would weigh about 6 billion tons on Earth. Neutron stars are incredibly dense remnants of supernova explosions.",
            "what's your favorite movie": "I don't watch movies, but I can recommend popular movies based on genres you enjoy!",
            "do you believe in aliens": "I don't have personal beliefs, but the existence of extraterrestrial life is a topic of scientific exploration and speculation.",
            "what's the meaning of happiness": "Happiness is a subjective experience that can come from various sources, such as relationships, accomplishments, and personal fulfillment.",
            "tell me a travel tip": "When traveling, it's helpful to pack essentials in a carry-on bag, research local customs, and have a backup plan for unexpected situations.",
            "what's the latest technology": "The field of technology is rapidly evolving. Some recent advancements include artificial intelligence, quantum computing, and advancements in renewable energy.",
            "tell me a joke": "Sure, here's one: Why did the computer go to therapy? It had too many bytes of emotional baggage!",
            "how to learn a new language": "Learning a new language involves consistent practice, immersion, and using language-learning resources. What language are you interested in learning?",
            "tell me a historical fact": "In 1969, humans landed on the moon for the first time during NASA's Apollo 11 mission.",
            "what's your favorite music": "I don't have personal preferences, but I can recommend music based on your taste. What genres do you enjoy?",
            "how does the internet work": "The internet is a global network of interconnected computers that communicate through standardized protocols. It enables the sharing of information and resources worldwide.",
            "tell me a positive quote": "Here's one: 'The only way to do great work is to love what you do.' - Steve Jobs",
            "what's the meaning of success": "Success can be defined in various ways, but it often involves achieving personal goals, overcoming challenges, and finding fulfillment.",
            "tell me a gardening tip": "Water your plants early in the morning to reduce evaporation and give them enough time to absorb moisture throughout the day.",
            "what's the best way to relax": "Relaxation methods vary from person to person, but common techniques include deep breathing, meditation, and engaging in activities you enjoy.",
            "tell me a myth": "In Greek mythology, the goddess Athena was born fully grown and armored from the forehead of her father, Zeus.",
            "what's your favorite quote": "I don't have favorites, but here's a quote: 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt",
            "how to stay focused": "Staying focused involves setting priorities, minimizing distractions, and taking breaks when needed. What tasks are you working on?",
            "tell me a space fact": "There are more stars in the observable universe than there are grains of sand on all the beaches on Earth.",
            "what's your favorite animal": "I don't have preferences, but I can provide information about a wide range of animals. What animal are you interested in?",
            "how to cook a perfect omelette": "To cook a perfect omelette, whisk eggs, add desired ingredients, cook over medium heat, and fold the omelette when the edges set. Enjoy!",
            "tell me a motivational quote": "Here's one: 'Believe you can and you're halfway there.' - Theodore Roosevelt",
            "what's the best way to start the day": "Starting the day with a healthy breakfast, positive affirmations, and a plan for the day can contribute to a successful day ahead.",
            "tell me a fun fact about the human body": "The human brain can generate about 20 watts of electrical power, enough to power a dim light bulb.",
            "how to overcome procrastination": "Overcoming procrastination involves breaking tasks into smaller steps, setting deadlines, and finding motivation. What task are you procrastinating on?",
            "tell me a technology fact": "The first computer programmer was Ada Lovelace, who wrote the first algorithm designed for implementation on Charles Babbage's analytical engine.",
            "what's the meaning of friendship": "Friendship involves mutual trust, support, and companionship. It's a valuable connection between individuals.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what's your favorite hobby": "I don't have hobbies, but I'm here to assist you with any information or tasks you have.",
            "how to stay positive": "Staying positive involves focusing on the good, practicing gratitude, and surrounding yourself with positive influences.",
            "tell me a random fact": "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "what's the best way to learn": "The best way to learn depends on individual preferences, but effective methods include active engagement, repetition, and real-world application.",
            "tell me a science joke": "Why do biologists look forward to casual Fridays? They're allowed to wear genes to work!",
            "what's the secret to happiness": "The secret to happiness varies for each person but often involves finding joy in the present moment, cultivating positive relationships, and pursuing meaningful goals.",
            "tell me a travel fact": "The Great Wall of China is the longest wall in the world, stretching over 13,000 miles.",
            "how to improve memory": "Improving memory involves techniques like regular exercise, adequate sleep, and mnemonic devices. What specific aspect of memory would you like to enhance?",
            "tell me a historical joke": "Why did the Ancient Egyptians never play hide and seek? Because good pharaohs were hard to find!",
            "what's the best way to study": "Effective study methods include active learning, creating a study schedule, and taking breaks. What subject are you studying?",
            "tell me a positive fact": "The world's smallest mammal is the bumblebee bat, weighing about as much as a paperclip.",
            "what's the best way to relax": "Relaxation methods vary from person to person, but common techniques include deep breathing, meditation, and engaging in activities you enjoy.",
            "tell me a myth": "In Norse mythology, Thor's hammer, Mjolnir, was so powerful that it could level mountains.",
            "what's your favorite quote": "I don't have favorites, but here's a quote: 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt",
            "how to stay focused": "Staying focused involves setting priorities, minimizing distractions, and taking breaks when needed. What tasks are you working on?",
            "tell me a space fact": "There are more stars in the observable universe than there are grains of sand on all the beaches on Earth.",
            "what's your favorite animal": "I don't have preferences, but I can provide information about a wide range of animals. What animal are you interested in?",
            "how to cook a perfect omelette": "To cook a perfect omelette, whisk eggs, add desired ingredients, cook over medium heat, and fold the omelette when the edges set. Enjoy!",
            "tell me a motivational quote": "Here's one: 'Believe you can and you're halfway there.' - Theodore Roosevelt",
            "what's the best way to start the day": "Starting the day with a healthy breakfast, positive affirmations, and a plan for the day can contribute to a successful day ahead.",
            "tell me a fun fact about the human body": "The human brain can generate about 20 watts of electrical power, enough to power a dim light bulb.",
            "how to overcome procrastination": "Overcoming procrastination involves breaking tasks into smaller steps, setting deadlines, and finding motivation. What task are you procrastinating on?",
            "tell me a technology fact": "The first computer programmer was Ada Lovelace, who wrote the first algorithm designed for implementation on Charles Babbage's analytical engine.",
            "what's the meaning of friendship": "Friendship involves mutual trust, support, and companionship. It's a valuable connection between individuals.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what's your favorite hobby": "I don't have hobbies, but I'm here to assist you with any information or tasks you have.",
            "how to stay positive": "Staying positive involves focusing on the good, practicing gratitude, and surrounding yourself with positive influences.",
            "tell me a random fact": "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "what's the best way to learn": "The best way to learn depends on individual preferences, but effective methods include active engagement, repetition, and real-world application.",
            "tell me a science joke": "Why do biologists look forward to casual Fridays? They're allowed to wear genes to work!",
            "hello": "Hello!",
            "good morning": "Good morning!",
            "good night": "Good night!",
            "how's it going": "It's going well, thank you!",
            "what's up": "Not much, just assisting you!",
            "who are you": "I am Jarvis, an artificial intelligence assistant.",
            "where are you from": "I exist in the digital realm, created to assist you.",
            "do you have siblings": "I don't have siblings, but I'm here for you!",
            # Add more responses as needed
        }

        return responses.get(words_said, "I didn't understand that.")

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run_jarvis()
