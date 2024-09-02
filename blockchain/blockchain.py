import hashlib  # creates cryptographic hash of the blocks
import datetime as date # creates timestamps at each block
import uuid # creates unique IDs
from pprint import pprint
import json
import re

class Block:
    def __init__(self, data, blockId="", previousBlockHash=""):
        """
        args:
        :blockId: unique block identifier, the position of the block in the chain
        :previousBlockHash: the cryptographic hash of the previous block in the chain
        :timestamp: the time at which the block was added in the chain
        :data: the data stored in the block
        :hash: the cryptographic hash of the current block
        """
        self.blockId = blockId
        self.previousBlockHash = previousBlockHash
        self.timestamp = date.datetime.now()
        self.data = data
        self.hash = self.get_hash()

    def get_hash(self):
        """
        calculate hash using sha256
        :return: hash for the current block
        """
        hash_str = str(self.blockId) + str(self.timestamp) + str(self.data) + str(self.previousBlockHash)
        return hashlib.sha256(hash_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
        :chain: empty chain with one root block
        """
        self.chain = [self.root()]

    def root(self):
        """
        create empty root block
        :return: empty root block
        """
        return Block(data='Root', blockId=0, previousBlockHash=0)

    def add_block(self, block):
        """
        add a new block to the chain
        :block: Block object
        """
        # calculate hash
        block.previousBlockHash = self.top_block().hash
        block.hash = block.get_hash()

        # calculate block ID
        block.blockId = self.top_block().blockId + 1

        # TODO: if validate() == True:
        self.chain.append(block)

    def top_block(self):
        """
        get a top block in the chain
        :return: top block in the chain
        """
        return self.chain[-1]

    def validate(self):
        """
        TODO guardrail checks
        :return:
        """
        pass

class Data():
    def __init__(self, userCard, log, currentPromptTokens, generatedResult, extractedInfo, guardrail):
        """
        :userCard: user data
        :log: machine-human interaction history
        :currentPromptTokens: tokenized prompt
        :generatedResult: LLM generation result
        :extractedInfo: RAG retrieval output
        :guardrail: relevant guardrail in XML
        """
        self.userCard = userCard
        self.log = log
        self.currentPromptTokens = currentPromptTokens
        self.generatedResult = generatedResult
        self.extractedInfo = extractedInfo
        self.guardrail = guardrail
        self.data = dict()

    def build(self):
        self.data['userCard'] = self.userCard
        self.data['log'] = self.log
        self.data['currentPromptTokens'] = self.currentPromptTokens
        self.data['generatedResult'] = self.generatedResult
        self.data['extractedInfo'] = self.extractedInfo
        self.data['guardrail'] = self.guardrail
        return self.data

class userCard():
    def __init__(self, age, interests, accessibilityTools, toneOfVoice):
        """
        :userId: unique user identifier (ID)
        :age: user age (int)
        :interests: list of interests (list)
        :accessibilityTools: list of relevant accessiblity settings (dict)
        :toneOfVoice: list of relevant tone of voice settings (dict)
        """
        self.userId = self.generate_id()
        self.age = age
        self.interests = interests
        self.accessibilityTools = self.parse_tools(accessibilityTools)
        self.toneOfVoice = self.parse_tone(toneOfVoice)
        self.card = dict()

    def generate_id(self):
        """
        generates unique user identifier
        :return: user ID
        """
        return uuid.uuid4()

    def parse_tools(self, accessibilityTools):
        """
        :return: accessibilityTools (dict)
        """
        return {"textToSpeech": accessibilityTools.textToSpeech, "simplifiedLanguage": accessibilityTools.simplifiedLanguage, "enhancedVisualization": accessibilityTools.enhancedVisualization}

    def parse_tone(self, toneOfVoice):
        """
        :return: toneOfVoice (dict)
        """
        return {"formality": toneOfVoice.formality, "positivity": toneOfVoice.positivity, "humor": toneOfVoice.humor}

    def build(self):
        self.card['userId'] = self.userId
        self.card['age'] = self.age
        self.card['interests'] = self.interests
        self.card['accessibilityTools'] = self.accessibilityTools
        self.card['toneOfVoice'] = self.toneOfVoice
        return self.card

class accessibilityTools():
    def __init__(self, textToSpeech, simplifiedLanguage, enhancedVisualization):
        """
        :textToSpeech: (Bool)
        :simplifiedLanguage: (Bool)
        :enhancedVisualization: (Bool)
        """
        self.textToSpeech = textToSpeech
        self.simplifiedLanguage = simplifiedLanguage
        self.enhancedVisualization = enhancedVisualization

class toneOfVoice():
    def __init__(self, formality, positivity, humor):
        """
        :formality: (str)
        :positivity: (str)
        :humor: (str)
        """
        self.formality = formality
        self.positivity = positivity
        self.humor = humor

# 1. create the chain
blockchain = Blockchain()

# 2. import userCard values from json
with open('data.json') as f:
    user_data = json.load(f)

age = user_data['age']

interests = user_data['interests'].lower()
interests = re.sub(r'\W', ' ', interests)
interests = interests.split()

accessibilityTools = accessibilityTools(textToSpeech=user_data["speech"], simplifiedLanguage=user_data["language"], enhancedVisualization=user_data["visuals"])
toneOfVoice = toneOfVoice(formality=user_data["formality"], positivity=user_data["positivity"], humor=user_data["humor"])
# 3. build userCard
userCard = userCard(age, interests, accessibilityTools, toneOfVoice).build()

# set other variables
log = 'sample log placeholder'
currentPromptTokens = 'prompt'
generatedResult = 'LLM result'
extractedInfo = 'RAG result'
guardrail = 'guardrail.xml'

# create a block
sample_block = Block(Data(userCard, log, currentPromptTokens, generatedResult,extractedInfo, guardrail).build())
sample_block_ = Block(Data(userCard, log, currentPromptTokens, generatedResult,extractedInfo, guardrail).build())

# add a block
blockchain.add_block(sample_block)
blockchain.add_block(sample_block_)

for block in blockchain.chain:
    print('Block ID:', str(block.blockId))
    print('Previous Hash:', str(block.previousBlockHash))
    print('Timestamp:', str(block.timestamp))
    print('Data:')
    pprint(block.data)
    print('Hash:', block.hash)
    print()
