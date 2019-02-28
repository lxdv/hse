import re

def preprocess(data):
    data = str(data)
    # ЕЁ
    regular = re.compile(r"[Ёё]")
    data = regular.sub(r"е", data)
    
    #заменить необычные пробелы на обычные
    regular = re.compile(r"\s")
    data = regular.sub(' ',data)
    
    # кавычки
    regular = re.compile(r"[\"«»‘’“”„“`’']+")
    data = regular.sub('"',data)
    
    # тире, дефис
    regular = re.compile(r"[‒–—―‐-‑_-]+")
    data = regular.sub(' ',data)
    
    #убрать пробелы между символами
    regular = re.compile(r"\s([.,?!:%]+)")
    data = regular.sub(r'\1', data)
    
    
    # точки, вопросы, восклицательные
    regular = re.compile(r"[…]")
    data = regular.sub('.', data)
    regular = re.compile(r"[.]{2,5}")
    data = regular.sub('.', data)
    regular = re.compile(r"[,]{2,4}")
    data = regular.sub(',', data)
    regular = re.compile(r"[!]{2,5}")
    data = regular.sub('!', data)
    regular = re.compile(r"[?]{2,5}")
    data = regular.sub('?', data)
    regular = re.compile(r"[:]{2,3}")
    data = regular.sub(':', data)
    regular = re.compile(r"[%]{2,3}")
    data = regular.sub("%", data)
    
    # 16летняя -> 16 летняя
    regular = re.compile('(\d+)([А-Яа-яA-Za-z]+)')
    data = regular.sub(r'\1 \2', data)
    regular = re.compile('([А-Яа-яA-Za-z]+)(\d+)')
    data = regular.sub(r'\1 \2', data)
    
    # смайлы
    regular = re.compile(r"\s{0,1}[:]{0,1}[)]{1,5}")
    data = regular.sub(" good ", data)
    regular = re.compile(r"\s{0,1}[:]{0,1}[(]{1,5}")
    data = regular.sub(" bad ", data)
    
    regular = re.compile(r'([A-Za-zА-Яа-я]+)[^A-Za-zА-Яа-я0-9\s.!?,\"%:#@*]+([A-Za-zА-Яа-я]+)')
    data = regular.sub(r" \1 \2", data)
     
    # 3 символа подряд    
    regular = re.compile(r'([.!?,:%]{3})\s*')
    data = regular.sub(r" symbols ", data)
    
    #КАПС
    regular = re.compile(r"([A-ZА-Я]{3,})")
    data = regular.sub(r"\1 allcaps ", data)
    
    # пробелы после символов
    regular = re.compile(r'([^0-9][.!?,:%]+)\s*')
    data = regular.sub(r"\1 ", data)
    
    regular = re.compile(r"\s+")
    data = regular.sub(" ", data)
    
    regular = re.compile(r'^[\s]+')
    data = regular.sub("", data)
    regular = re.compile(r'[\s]+$')
    data = regular.sub("", data)
    
    return data

def make_year(data):
    return(int(data[0:4]))
def make_month(data):
    return(int(data[5:7]))
def make_day(data):
    return(int(data[8:]))


# title
# for i in range(0,len(train_data)):
#     X_train.append(str(train_data.iloc[i,5]))
#     y_train.append(int(train_data.iloc[i,4]))
    
# for i in range(0,len(val_data)):
#     X_val.append(str(val_data.iloc[i,5]))
#     y_val.append(int(val_data.iloc[i,4]))

# input_title = Input(shape=(maxlen,))
# input_review = Input(shape=(maxlen,))

# title = Embedding(max_features, embedding_dim, input_length=7)(input_title)
# review = Embedding(max_features,
#                     embedding_dim,
#                     weights=[embedding_matrix],
#                     input_length=maxlen,
#                     trainable=False)(input_review)

# shared_LSTM = LSTM(64)

# title = shared_LSTM(title)
# review = shared_LSTM(review)

# model_LSTM = Concatenate()([title,review])
# model_LSTM = Dropout(0.5)(model_LSTM)
# out = Dense(5,activation = 'softmax')(model_LSTM)

# model = Model([input_title,input_review], out)

# model.compile(loss='categorical_crossentropy',
#               optimizer='adam', metrics = ['accuracy'])