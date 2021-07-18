## Create GrandPy Bot, the grandpa-robot 🤖 👴

Create a robot that would respond to you like your grandfather! If you ask him for the address of a place, he will give
it to you, of course, but with a long and very interesting story.

### Specifications
####Features
- Interactions in AJAX: the user sends his question by pressing enter and the answer is displayed directly on the screen, without reloading the page.
- You will use the Google Maps API and the Media Wiki API.
- Nothing is saved. If the user reloads the page, all history is lost.

####User journey
The user opens their browser and enters the URL you provided. It arrives in front of a page containing the following elements:

- header: logo and catchphrase
- central zone: empty zone (which will be used to display the dialog) and form field to send a question.
- footer: your first and last name, link to your Github repository and other social networks if you have any
- The user types in "Hi GrandPy! Do you know the address of OpenClassrooms?" in the form field and then press the Enter key. The message is displayed in the area above which displays all the messages exchanged. An icon rotates to indicate that GrandPy is thinking.

Then a new message appears: "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." Below, a Google Maps map also appears with a marker indicating the requested address.

GrandPy sends a new message: "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"
