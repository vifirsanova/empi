# EMPI
Empathic Machine Processors for Inclusion (EMPI) is a project that supports the inclusion of people with special needs.

EMPI is a set of Conversational AI and mobile development tools for inclusive education, mental well-being and harmonious social interaction. Visit [EMPI web-page](https://vifirsanova.github.io/empi-web/) to learn more, and contact [Victoria Firsanova](mailto:vifirsanova@gmail.com) to contribute.

## Demos

1. [AI-driven Teaching Assitant](https://colab.research.google.com/github/vifirsanova/empi/blob/main/demos/teaching_assistant.ipynb) for inclusive education (uses GPU)
2. [EMPI AI Chat-bot greetings scenario](https://colab.research.google.com/github/vifirsanova/empi/blob/main/demos/greetings_scenario.ipynb)

## Data

**EMPI Dataset**

The EMPI Dataset by Victoria Firsanova is a closed graph knowledge base. The EMPI Dataset enables personal data cyphering, and retrieval-augmented generation. Feel free to [learn more](https://github.com/vifirsanova/empi/blob/main/KB/graph.ipynb) or [contribute.](https://colab.research.google.com/github/vifirsanova/empi/blob/main/demos/graph_crowdsoursing_ui.ipynb)

**The ASD QA Dataset**

The [ASD QA dataset](https://figshare.com/articles/dataset/Autism_Spectrum_Disorder_and_Asperger_Syndrome_Question_Answering_Dataset_1_0/13295831) by Victoria Firsanova is used to train [Word Embeddings](https://github.com/vifirsanova/empi/blob/main/notebooks/create_embeddings.ipynb) for the model.

***The detailed dataset statistics***
| Parameter                          | Description          |
| ---------------------------------- | -------------------- |
| The number of QA pairs             | 4,138                |
| The number of irrelevant questions | 352                  |
|The average question length         |53 symbols / 8 words  |
|The average answer length           |141 symbols / 20 words|
|The average reading paragraph length|453 symbols / 63 words|
|Max question length                 |226 symbols / 32 words|
|Max answer length                   |555 symbols / 85 words|
|Max reading paragraph length        |551 symbols / 94 words|
|Min question length                 |9 symbols / 2 words   |
|Min answer length                   |5 symbols / 1 words   |
|Min reading paragraph length        |144 symbols / 17 words|

The ASD QA dataset is available on HuggingFace:

1. [Train set](https://huggingface.co/datasets/missvector/asd-qa-train)
2. [Validation set](https://huggingface.co/datasets/missvector/asd-qa-val)
3. [Test set](https://huggingface.co/datasets/missvector/asd-qa-test)

## The model architecture

![the model architecture](https://github.com/vifirsanova/empi/blob/main/illustrations/model_architecture.png)

## Building Blocks

The model combines the power of Blockchain with Conversational AI technologies to create [personal user blocks](https://github.com/vifirsanova/empi/blob/main/illustrations/user_data.json) that store user data, app settings and chat logs for interpretability research.

```
{
 "username": "Аня",
 "init_log": "ЭМПИК:\nПривет! Как тебя зовут?\nПриветик! Меня зовут Аня.\nЭМПИК:\nРасскажи мне о себе: что тебе нужно для комфортного общения со мной?    \nНапример, озвучивание текста, крупный шрифт или упрощенный язык.\nАня: Думаю, что мне понадобится распознавание речи.\nЭМПИК:\nОтлично! Я тебя понял. Включаю режим: <распознавание речи>Думаю, что мне понадобится распознавание речи.",
 "setting": ["распознавание речи", "распознавание речи", {"технология": "text-to-speech", "принцип работы": "технология автоматического воспроизведения текста, например, функция “прямая речь” в iphone", "для кого": ["рас", "афазия", "нарушения процесса порождения речи"]}, ["рас", "афазия", "нарушения процесса порождения речи"]]
}
```

## Previous version navigation (see old_ver branch)

* dataset
  * crowdsourcing_task.png: sample of the crowdsourcing task
  * dataset.json: full dataset used for fine-tuning
  * dataset_structure.png: the image presentnting the overall dataset structure
  * get_articles.py: script used to get data that formed the dataset
  * pages.txt: data that formed the dataset
* demos
  * fine_tuning_demo.ipynb: notebook contains full code for the model fine-tuning
* fine-tuning: pieces of code forming fine_tuning_demo.ipynb
  * data_pre-processing.ipynb: notebook contains the code for data pre-processing
  * model_fine-tuning.ipynb: notebook contains the code for the model fine-tuning with HuggingFace tools
  * load_model_to_hub.ipynb: notebook contains the code for loading the model to HuggingFace repository
* layouts: layouts for the mobile app
  * 1.png: chatbot interface
  * 2.png: chatbot interface and its features
  * 3.png: Social Stories catalogue
  * 4.png: Favourites for Social Stories
  * 5.png: Planning Calendar
  * 6.png: adding element to the Planning Calendar
* retriever_reader: description of the chatbot architecture
  * IR_QA_structure.png: image presenting the structure of the architecture
  * approach_description.md: textual description of the architecture
* survey: layouts for UX/UI survey
  * 1.pdf: asking for demographic information
  * 2.pdf: asking for interesting topics
  * 3.pdf: asking for preferrable language style
  * 4.pdf: asking to rate the layouts for the mobile app interface
  * 5.pdf: asking to describe the desirable virtual assitant
