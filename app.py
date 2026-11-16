import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("버튼을 눌러 오늘 먹을 점심 메뉴를 추천받아 보세요!")

# 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "국밥",
    "비빔밥",
    "파스타",
    "햄버거",
    "쌀국수",
    "떡볶이",
    "마라탕",
    "칼국수",
]

# 구분선
st.divider()

# 추천 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 메뉴 추천받기", type="primary", use_container_width=True):
  selected_menu = random.choice(lunch_menus)

  # 추천 결과 출력
  st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 🎉")
  st.balloons()  # 축하 풍선 애니메이션 효과
else:
  st.info("위 버튼을 누르면 메뉴가 나타납니다.")
