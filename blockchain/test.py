from pprint import pprint
from blockchain import accessibilityTools, toneOfVoice, userCard

# set variables for userCard
age = 25
interests = ['Technology', 'Art', 'Music', 'Fitness']
accessibilityTools = accessibilityTools(textToSpeech=True, simplifiedLanguage=False, enhancedVisualization=True)
toneOfVoice = toneOfVoice(formality="casual", positivity="high", humor="moderate")

# build userCard
userCard = userCard(age, interests, accessibilityTools, toneOfVoice).build()
pprint(userCard)
