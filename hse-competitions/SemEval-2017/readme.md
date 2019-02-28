# Semeval 2017 Task 4: Sentiment Analysis in Twitter
## Subtask C: Topic-Based Message Polarity Classification
Рассматривается задача классификации текста – определение тональности высказывания в социальной сети Twitter
по пятибалльной шкале – от -2 (крайне отрицательное) до +2 (крайне положительное). 
Материалом для данного исследования служат твиты соревнования SemEval-2017 English, Sentiment Analysis in Twitter, 
собранные с сайта http://alt.qcri.org/semeval2017/task4. Каждое высказывание размечено меткой -2, -1, 0, 1, 2, 
в зависимости от тональности написанного.  

В качестве решения предложен подход (подробнее https://habrahabr.ru/company/dca/blog/274027/) с использованием Рекуррентной Нейронной Сети с LSTM (долго краткосрочной памятью) слоями.

https://competitions.codalab.org/competitions/15937
