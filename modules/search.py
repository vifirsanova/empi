class Search():
  """
  Поиск по графу для реализации двух сценариев
  1. Шифрование данных: поиск данных, уязвимых для хакеров, с помощью графа знаний
  - ищет указание на персональные данные пользователя с помощью поиска по базе знаний и шифрует их
  - возвращает исходный текст с зашифрованными данными
  2. Извлечение информации для генерации информативного ответа
  - ищет по графу релевантную информацию и извлекает текст
  - текст можно использовать для обусловленной генерации с помощью LLM
  """
  def __init__(self):
    self.path = set()

  def graph_search(self, data, query):
    """
    Рекурсивная функция для поиска совпадений (query) по графу (data):
    - функция проходит по трем измерениям графа
    - ищет точные совпадения или наличие поискового запроса внутри последовательности
    """
    for k in data:
      if query in k.split() or query == k:
        self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
      if isinstance(data[k], dict):
        self.graph_search(data=data[k], query=query)
      else:
        if isinstance(data[k], str):
          if query in data[k].split() or query == data[k]:
            self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
        else:
          for elem in data[k]:
            if query in elem.split() or query == elem:
              self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
    return self.path