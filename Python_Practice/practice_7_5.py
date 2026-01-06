# 실습 7.1-1 텍스트 파일 통계
import datetime


# 1. 테스트 파일로 로직 구현하기
# file_path = "C:/AWS13th_JimmyKim/TIL/aws13th-JimmyKim-til/Python_Practice/target_file"
# with open(file_path + "/7_5_test.txt", 'r', encoding='utf-8') as f:

# 2. 함수로 만들기 시작
def prac1(file):
    try: # 풀이에서는 파일이 없는지도 확인하는 예외처리 넣어줬다.
        with open(file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]
            # 난 반복문으로 한줄씩 읽어오도록 구현했는데...
            print(lines)
            total_lines = len(lines) # 전체 줄 수
            print(f"전체 줄 수 : {total_lines}")
        #    x = list(line.split() for line in lines)
        #    print(x)
        #    y = list(len(i) for i in x)
        #    print(y)
            # 이제 두개 합쳐서 한줄로 만들면
        #    total_words = sum(list(len(i) for i in list(line.split() for line in lines)))
            # 굳이 list 두번 쓰는건 낭비네. 풀이에서 처럼 한방에 리스트 컴프리헨션 쓰는게 나을듯
            total_words = sum(len(line.split()) for line in lines)
            print(f"전체 단어 수 : {total_words}")
        #    z = list(len(i) for i in lines)
        #    print(z)
            total_characters = sum(len(line) for line in lines)
            print(f"전체 문자 수 : {total_characters}")
            maximum_line = max(list(len(i) for i in lines))
            print(f"가장 긴 줄의 길이 : {maximum_line}")
            # 풀이에서는 왜 굳이 if else 0을 쓴거지???

    except FileNotFoundError:
        print(f"에러 발생 : {file}을 찾을 수 없습니다.")

# 실습 7.1-2 간단한 일기장
import os
from datetime import datetime
file_path = "C:/AWS13th_JimmyKim/TIL/aws13th-JimmyKim-til/Python_Practice/target_file"
class prac2:
    def __init__(self):
        pass
    def write_diary(self, contents):
        with open(file_path + "/diary_" + datetime.now().strftime('%Y-%m-%d') + ".txt", 'w', encoding='utf-8') as f:
            f.write(contents)

    def read_diary(self, date):
        try:
            with open(file_path + "/diary_" + date + ".txt", 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return date + " 날짜에 일기가 없습니다."

    def diary_list(self):
        diary_list = [i for i in os.listdir(file_path) if i.startswith("diary")]
        return diary_list

diary = prac2()
diary.write_diary("이거 되나? 한번 해보자")
print(diary.diary_list())
print(diary.read_diary('2026-01-03'))

# GPT 도움이 없이는 못만들 것 같다...
# 풀이 에서는 파일 저장할 디렉토리를 생성자로 받아왔다.
# 파일 디렉토리를 덕지덕지 붙여서 구현했는데 저렇게 하니 풀이가 훨씬 깔끔하다.

# 실습 7.1-3 파일 복사 프로그램
# 1. 테스트 파일로 로직 구현하기
import os
#file_path = "C:/AWS13th_JimmyKim/TIL/aws13th-JimmyKim-til/Python_Practice/target_file"
# 2. 함수 형태로 구현하기
def prac3(source_file_path, target_file_path):
    copied_size = 0 #진행율 확인. 풀이에서 쓰네...
    # 파일 유무
#    if not os.path.exists(file_path+"/7_5_test.txt"):
    if not os.path.exists(source_file_path):
        print(f"해당 경로에 파일이 없습니다.")
        return 0
    # 파일 사이즈
#    file_size = os.path.getsize(file_path+"/7_5_test.txt")
    file_size = os.path.getsize(target_file_path)
    # 복사 (열어서 쓰기)
#    with open(file_path + "/7_5_test.txt", 'rb') as f:
#        with open(file_path+"/copied_result.txt", 'wb') as d:
    with open(source_file_path, 'rb') as f:
        with open(target_file_path, 'wb') as d:
    # 구글링한 청크 사이즈 만큼씩 읽기 구현
           while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                d.write(chunk)
                copied_size += len(chunk) # 파일 사이즈 진행율 확인용. 굳이 여기선 안써도될듯
    #    d.close() 피드백 반영 -- 2026.01.06 굳이 필요없다.
    #f.close() 피드백 반영 -- 2026.01.06 굳이 필요없다.
    target_size = os.path.getsize(target_file_path)
    print(file_size)
    print(target_size)

#풀이에서 1번과 마찬가지로, try except로 예외처리를 해두었다.
#프로그램 목적이 복사 붙여넣기라서 그런지 복사 에러 발생 시 예외처리로 구현해져있다.
