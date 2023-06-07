import pandas as pd
import Levenshtein

# 데이터 로드
data = pd.read_csv('ChatbotData.csv')

def get_most_similar_question(query):

    min_distance = float('inf')
    most_similar_index = None
    
    for i, question in enumerate(data['Q']):
        distance = Levenshtein.distance(query, question)
        if distance < min_distance:
            min_distance = distance
            most_similar_index = i
    
    return most_similar_index

# Chat 입력 받기
chat_input = input('질문: ')

# 가장 유사한 학습데이터의 인덱스 찾기
most_similar_index = get_most_similar_question(chat_input)

# 가장 유사한 학습데이터의 답변 출력
print('답변:', data.loc[most_similar_index, 'A'])