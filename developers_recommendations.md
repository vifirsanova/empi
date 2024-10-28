*Автор: Виктория Фирсанова*

# 1. Контролируемость системы

**Гардрейлы** -- системы обеспечения контролируемости систем генеративного искусственного интеллекта.

При разработке правил для повышения контролируемости и предсказуемости выдач генеративных моделей рекомендуется обращаться к знаниям из областей лингвистики, прагматики и теории речевых актов.

**Образец правила для снижения рисков проявления враждебного отношения к пользователю**:

```
- Помечать все слова с негативной коннотацией, слова, выражающие агрессию и враждебность. 
- Заменять их на нейтральные слова с эквивалентным значением. 
- Сохранять исходный контекст.
```
# 2. Персонализация

**Персонализация** системы разговорного искусственного производится через настройку регистра общения с пользователем, учет интересов и потребностей пользователя при обеспечении доступности.

Рекомендуется ручная настройка перечисленных параметров модели искусственного интеллекта с помощью графического пользовательского интерфейса. Ручной ввод параметров обеспечивает контролируемость персонализации систем искусственного интеллекта и снижает требования к развертыванию таких систем в сравнении с автоматическим извлечением настроек на основе истории общения с пользователем.

**Образец графического интерфейса для сбора пользовательской информации**:

![image](https://github.com/user-attachments/assets/021df51d-ca3e-4550-bdf0-6a39c7b5ea3a)

# 3. Базы знаний

Подключение **базы знаний** к диалоговому агенту позволяет персонализировать пользовательский опыт, тонко настроить веса языковых моделей под информацию из вашей предметной области, а также минимизировать риски порождения ложной информации моделями генеративного искусственного интеллекта. 

Рекомедуется использовать формат представления знаний Resource Description Framework (RDF).

**Образец базы знаний в формате RDF в программном комплексе EMPI AI**:

![image](https://github.com/user-attachments/assets/ce1cf418-6e02-4911-af8c-d3496a3ae7b3)

# 4. 