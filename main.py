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
            "what's the best way to start the day": "Starting the day with a healthy breakfast, positive affirmations, and a plan for the day can contribute to a successful day ahead.",
            "tell me a fun fact about the human body": "The human brain can generate about 20 watts of electrical power, enough to power a dim light bulb.",
            "how to overcome procrastination": "Overcoming procrastination involves breaking tasks into smaller steps, setting deadlines, and finding motivation. What task are you procrastinating on?",
            "tell me a technology fact": "The first computer programmer was Ada Lovelace, who wrote the first algorithm intended for implementation on Charles Babbage's analytical engine.",
            "recommend a book": "I recommend 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams. It's a humorous science fiction classic.",
            "how to learn a new language": "To learn a new language, immerse yourself in it, practice regularly, use language learning apps, and try conversing with native speakers.",
            "tell me a historical fact": "Did you know that Cleopatra lived closer to the invention of the iPhone than to the construction of the Great Pyramid of Giza?",
            "how to improve memory": "Improving memory involves staying mentally active, getting enough sleep, eating a healthy diet, and practicing memory exercises.",
            "tell me a weather forecast": "I'm sorry, I cannot provide real-time weather information. You may want to check a reliable weather website or app for the latest forecast.",
            "how to start a blog": "Starting a blog involves choosing a niche, setting up a website, creating valuable content, and promoting your blog through social media and other channels.",
            "tell me a joke": "Sure, here's one: Why did the computer go to therapy? It had too many bytes of emotional baggage!",
            "what's the meaning of life": "The meaning of life is a philosophical question. Many people find meaning in relationships, personal achievements, or helping others.",
            "sing a song": "I'm not a great singer, but here's a short tune for you: La la la!",
            "how to meditate": "Meditation involves finding a quiet space, focusing on your breath, and letting go of thoughts. It can help reduce stress and improve mindfulness.",
            "tell me a science fact": "The Earth's core is hotter than the surface of the Sun. It reaches temperatures of up to 9,000 degrees Fahrenheit (5,000 degrees Celsius).",
            "how to start a healthy lifestyle": "Starting a healthy lifestyle includes eating a balanced diet, staying active, getting enough sleep, and managing stress. What specific changes are you considering?",
            "tell me a travel tip": "When traveling, pack essential items, research local customs, and be open to new experiences. Traveling can broaden your perspective and create lasting memories.",
            "how to play the guitar": "Learning to play the guitar takes practice and patience. Start with basic chords, use online tutorials, and practice regularly to build muscle memory.",
            "tell me a mystery fact": "The Voynich Manuscript is an ancient book filled with illustrations and text in an unknown script. Its meaning and origin remain a mystery to this day.",
            "how to grow plants indoors": "Growing plants indoors requires proper lighting, watering, and choosing the right plants for your space. Consider factors like sunlight and humidity.",
            "tell me a movie recommendation": "I recommend watching 'The Shawshank Redemption.' It's a classic film with a compelling storyline and great performances.",
            "how to take better photos": "To take better photos, learn about composition, lighting, and your camera settings. Practice regularly and experiment with different techniques.",
            "tell me a sports fact": "Did you know that basketball was invented by Dr. James Naismith in December 1891? The first game was played with a soccer ball and two peach baskets.",
            "how to write a poem": "Writing a poem involves expressing emotions, using vivid imagery, and experimenting with different poetic forms. Let your creativity flow!",
            "tell me a fun fact about space": "Space is not completely empty; it contains tiny particles, such as dust and gas. These particles can pose challenges for spacecraft and telescopes.",
            "how to start a small business": "Starting a small business involves creating a business plan, securing funding, and understanding your target market. What type of business are you interested in?",
            "tell me a cat fact": "Cats have five toes on their front paws but only four toes on their back paws. Some cats are also polydactyl, meaning they have extra toes.",
            "how to make a delicious smoothie": "To make a delicious smoothie, blend your favorite fruits, add yogurt or milk, and consider adding some greens for extra nutrition.",
            "tell me a technology prediction": "Some technology predictions suggest that in the future, we may see advancements in artificial intelligence, virtual reality, and renewable energy.",
            "how to write a short story": "Writing a short story involves creating interesting characters, developing a plot, and building a captivating narrative. Start with a strong opening!",
            "tell me a historical figure": "One historical figure is Leonardo da Vinci, a polymath known for his contributions to art, science, engineering, and anatomy.",
            "how to improve productivity": "Improving productivity involves setting clear goals, prioritizing tasks, minimizing distractions, and taking breaks. What specific tasks are you working on?",
            "tell me a fun fact about birds": "Did you know that hummingbirds are the only birds that can fly backward? They are also the smallest birds, weighing as little as two grams.",
            "how to make a perfect cup of coffee": "To make a perfect cup of coffee, start with freshly ground beans, use clean and cold water, and adjust the brewing time to your taste preferences.",
            "tell me a mythological story": "In Greek mythology, Pandora was the first woman on Earth. She was created by the gods, and her curiosity led her to open a box, releasing troubles into the world.",
            "how to improve public speaking": "Improving public speaking skills involves practice, preparation, and connecting with your audience. Record your speeches to identify areas for improvement.",
            "tell me a dog fact": "Dogs have an extraordinary sense of smell and can be trained to detect various scents, including diseases and certain types of cancers.",
            "how to create digital art": "Creating digital art involves using graphic design software and a drawing tablet. Experiment with different tools and techniques to find your unique style.",
            "tell me a science fiction recommendation": "I recommend reading 'Dune' by Frank Herbert. It's a classic science fiction novel with an epic and imaginative storyline.",
            "how to stay motivated": "Staying motivated involves setting clear goals, breaking them into smaller tasks, and celebrating small achievements along the way. What are you currently working on?",
            "tell me a fun fact about insects": "There are more than one million known species of insects, and they play crucial roles in ecosystems as pollinators, decomposers, and prey for other animals.",
            "how to learn to code": "Learning to code involves choosing a programming language, practicing regularly, and working on real-world projects. There are many online resources available for beginners.",
            "tell me a technology trend": "One technology trend is the rise of 5G networks, offering faster and more reliable internet connectivity. This can lead to advancements in various industries.",
            "how to stay positive": "Staying positive involves practicing gratitude, surrounding yourself with positive influences, and focusing on solutions rather than problems. What brings you joy?",
            "tell me a sports trivia": "In 1992, the Olympic Games featured basketball as an official sport for the first time. The United States 'Dream Team' won the gold medal.",
            "how to make homemade pizza": "To make homemade pizza, start with fresh dough, add your favorite toppings, and bake in a preheated oven. Enjoy a delicious and customizable meal!",
            "tell me a psychology fact": "The placebo effect is a psychological phenomenon where patients experience real improvements in symptoms after receiving a treatment with no therapeutic effect.",
            "how to grow a garden": "Growing a garden involves choosing the right plants for your climate, providing adequate sunlight and water, and tending to the soil. What type of plants are you interested in?",
            "tell me a movie trivia": "Did you know that the first movie ever made was 'Roundhay Garden Scene' in 1888? It is a short film directed by Louis Le Prince.",
            "how to start a podcast": "Starting a podcast involves choosing a niche, planning episodes, and selecting the right equipment. Share your passion and connect with your audience through engaging content.",
            "tell me a fun fact about the ocean": "The Mariana Trench is the deepest part of the world's oceans, reaching depths of about 36,070 feet (10,994 meters). It's home to unique and mysterious deep-sea creatures.",
            "how to make a healthy salad": "To make a healthy salad, include a variety of colorful vegetables, add lean proteins, and use a light dressing. It's a nutritious and delicious meal option.",
            "tell me a mythology fact": "In Norse mythology, Thor is the god of thunder, lightning, storms, oak trees, strength, the protection of mankind, and fertility.",
            "how to improve time management": "Improving time management involves setting priorities, creating a schedule, and eliminating time-wasting activities. What specific tasks are you struggling to manage?",
            "tell me a fun fact about the solar system": "Jupiter is the largest planet in our solar system and has more than twice the mass of all the other planets combined.",
            "how to start a fitness routine": "Starting a fitness routine involves setting fitness goals, choosing activities you enjoy, and gradually increasing intensity. Remember to listen to your body and stay consistent.",
            "tell me a fun fact about dinosaurs": "The Stegosaurus, a dinosaur from the Late Jurassic period, had large bony plates along its back and four sharp spikes on its tail for defense against predators.",
            "how to bake chocolate chip cookies": "To bake chocolate chip cookies, mix butter, sugars, flour, and chocolate chips, then drop spoonfuls onto a baking sheet. Bake until golden brown and enjoy warm!",
            "tell me a literature recommendation": "I recommend reading 'To Kill a Mockingbird' by Harper Lee. It's a classic novel that addresses issues of racial injustice and moral growth.",
            "how to improve communication skills": "Improving communication skills involves active listening, clear expression, and adapting your communication style to your audience. What communication challenges are you facing?",
            "tell me a fun fact about the human brain": "The human brain has about 86 billion neurons, and it generates electrical impulses that create thoughts, memories, and emotions.",
            "how to start a book club": "Starting a book club involves finding like-minded individuals, choosing a reading schedule, and discussing books together. It's a great way to share literary experiences.",
            "tell me a technology fact": "The World Wide Web was invented by Sir Tim Berners-Lee in 1989. It revolutionized the way information is shared and accessed globally.",
            "how to overcome fear": "Overcoming fear involves facing it gradually, practicing relaxation techniques, and reframing negative thoughts. What specific fear are you looking to overcome?",
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
            "how to make homemade pizza": "To make homemade pizza, prepare dough, add sauce, cheese, and your favorite toppings. Bake until the crust is golden brown and enjoy your delicious creation!",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "how to start a blog": "Starting a blog involves choosing a niche, selecting a platform, and creating engaging content. Share your passion and connect with your audience.",
            "tell me a space fact": "There are more stars in the observable universe than there are grains of sand on all the beaches on Earth.",
            "how to write a poem": "Writing a poem allows for creativity and self-expression. Experiment with different forms, rhyme schemes, and let your emotions guide your words.",
            "tell me a fun fact about dogs": "Dogs have an extraordinary sense of smell, with some breeds being able to detect certain diseases and locate missing persons.",
            "how to make a healthy smoothie": "Create a healthy smoothie by blending fruits, greens, and a liquid base like yogurt or almond milk. It's a nutritious and tasty way to start your day.",
            "tell me a technology fact": "The first computer programmer was Ada Lovelace, who wrote the first algorithm intended for implementation on Charles Babbage's Analytical Engine.",
            "how to learn a new language": "Learning a new language involves consistent practice, using language learning apps, and immersing yourself in the language through books, movies, and conversations.",
            "tell me a historical fact": "In 1969, humans first set foot on the moon during NASA's Apollo 11 mission, with astronauts Neil Armstrong and Buzz Aldrin making history.",
            "how to make a perfect cup of coffee": "Brewing a perfect cup of coffee involves choosing high-quality beans, grinding them to the right consistency, and using the correct water temperature.",
            "tell me a fun fact about birds": "The Arctic Tern holds the record for the longest migratory journey, flying from the Arctic to the Antarctic and back, covering about 44,000 miles (70,000 km) each way.",
            "how to create a workout routine": "Creating a workout routine includes a mix of cardiovascular exercises, strength training, and flexibility exercises. Find activities you enjoy to stay motivated.",
            "tell me a motivational quote": "Here's one: 'The only way to do great work is to love what you do.' - Steve Jobs",
            "how to make chocolate chip cookies": "Make delicious chocolate chip cookies by combining butter, sugar, flour, and chocolate chips. Bake until golden brown and enjoy warm with a glass of milk.",
            "tell me a fun fact about space": "Space is not completely silent. It contains sound waves, but they require a medium like a planet's atmosphere to be heard.",
            "how to take better photos": "Taking better photos involves understanding your camera settings, experimenting with composition, and practicing regularly. Capture the moments that matter to you.",
            "tell me a science fact": "The Earth's atmosphere is composed of approximately 78% nitrogen, 21% oxygen, and trace amounts of other gases.",
            "how to start a podcast": "Starting a podcast involves choosing a niche, getting the right equipment, and planning engaging content. Share your passion and connect with your audience through audio.",
            "tell me a fun fact about insects": "Ants can carry objects up to 50 times their own body weight. They are also known for their complex social structures.",
            "how to make a paper airplane": "Create a paper airplane by folding a sheet of paper into a simple design. Experiment with different folds to achieve various flight patterns.",
            "tell me a travel fact": "The Great Wall of China is visible from space, and it stretches over 13,000 miles (21,196 km) through various terrains.",
            "how to meditate": "Meditation involves finding a quiet space, focusing on your breath or a mantra, and allowing thoughts to come and go. Practice regularly for a calmer mind.",
            "tell me a fun fact about the human body": "The human brain can generate about 20 watts of electrical power, enough to power a dim light bulb.",
            "how to make a homemade face mask": "Create a homemade face mask using natural ingredients like honey, yogurt, and oats. It's a rejuvenating and cost-effective skincare option.",
            "tell me a fun fact about music": "The world's longest concert lasted for over 639 hours, featuring continuous performances of various musical genres.",
            "how to improve productivity": "Improving productivity involves effective time management, setting realistic goals, and minimizing distractions. Prioritize tasks and stay focused.",
            "tell me a fun fact about plants": "Bamboo is one of the fastest-growing plants and can grow up to 35 inches (90 cm) in a single day under the right conditions.",
            "how to make a budget": "Creating a budget involves tracking income, expenses, and setting financial goals. Allocate funds wisely and save for future needs.",
            "tell me a fun fact about the ocean": "The Pacific Ocean is the largest and deepest ocean, covering an area larger than all the landmasses combined.",
            "how to bake a cake": "Baking a cake involves mixing flour, sugar, eggs, and other ingredients, then baking until a toothpick comes out clean. Decorate as desired and enjoy.",
            "tell me a fun fact about technology": "The first computer mouse was made of wood and had two metal wheels. It was invented by Douglas Engelbart in 1964.",
            "how to create digital illustrations": "Creating digital illustrations involves using graphic design software and a tablet. Experiment with brushes, layers, and colors to bring your ideas to life.",
            "tell me a fun fact about birds": "Hummingbirds are the only birds that can fly backward and hover in mid-air. Their wings beat at a remarkable rate of 50 to 80 times per second.",
            "how to write a short story": "Writing a short story involves developing characters, setting, and a plot with a clear beginning, middle, and end. Explore different genres and styles.",
            "tell me a fun fact about the human body": "The human body has over 600 muscles, each serving a unique function in movement and support.",
            "how to start a morning routine": "Starting a morning routine involves activities like stretching, mindfulness, and planning your day. It sets a positive tone for the rest of the day.",
            "tell me a sports recommendation": "I recommend watching the Olympics for a diverse range of sports and incredible athletic performances. It's a celebration of talent and dedication.",
            "how to make a homemade face mask": "To make a homemade face mask, use ingredients like honey, yogurt, and turmeric for a natural and nourishing treatment for your skin.",
            "tell me a historical event": "One historical event is the moon landing on July 20, 1969, when humans first set foot on the lunar surface during the Apollo 11 mission.",
            "how to learn a new instrument": "Learning a new instrument involves practice, patience, and finding enjoyable songs to play. Start with the basics and gradually challenge yourself.",
            "tell me a fun fact about the Great Wall of China": "The Great Wall of China is over 13,000 miles long and was built to protect against invasions. It's an iconic symbol of Chinese history and engineering.",
            "how to start a creative project": "Starting a creative project involves brainstorming ideas, setting goals, and taking the first step. Let your imagination flow and enjoy the creative process.",
            "tell me a cat recommendation": "Cats are known for their independent yet affectionate nature. Consider adopting from a shelter and providing a loving home for a furry friend.",
            "how to make a delicious cup of tea": "To make a delicious cup of tea, choose high-quality tea leaves, use fresh water, and steep for the recommended time. Enjoy the soothing aroma and flavor.",
            "tell me a fun fact about pandas": "Pandas have a 'thumb' that is actually an enlarged wrist bone, helping them grip bamboo. They are also skilled climbers.",
            "how to create a workout routine": "Creating a workout routine involves combining cardiovascular exercises, strength training, and flexibility workouts. Set realistic goals and stay consistent.",
            "tell me a motivational quote": "Here's one: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill",
            "how to make a refreshing smoothie": "To make a refreshing smoothie, blend fruits like berries and mango with yogurt or a non-dairy alternative. It's a tasty and hydrating treat!",
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

