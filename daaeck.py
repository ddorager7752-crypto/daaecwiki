#python -m streamlit run 위키.py
import streamlit as st
from PIL import Image

suchlist=["다액","잇프","인프","잇티","엣티","엣프","엔프","아포","아포단","맵","대정령","다이나믹 웨폰"]


#검색어를 세션에 저장

st.set_page_config(
    page_title= '다액 위키',
    page_icon= '다액 로고.png'
)

def such(서치변수):

    if 서치변수 == '다액':
        st.session_state.session = '다액페이지'
    elif 서치변수 == '잇프':
        st.session_state.session = '잇프페이지'
    elif 서치변수 =='':
        st.session_state.session = 'mainpage'
    elif 서치변수 == "메인페이지":
        st.session_state.session = 'mainpage'
    elif 서치변수 == "다액 등장인물" or 서치변수 == "등장인물":
        st.session_state.session = '다액의등장인물들'
    elif 서치변수 == "인프" or  서치변수 == "인프페이지" :
        st.session_state.session = '인프페이지'
    elif 서치변수 == "잇티" or  서치변수 == "잇티페이지" :
        st.session_state.session = '잇티페이지'
    elif 서치변수 == "엣티" or  서치변수 == "엣티페이지" :
        st.session_state.session = '엣티페이지'
    elif 서치변수 == "엣프" or  서치변수 == "엣프페이지" :
        st.session_state.session = '엣프페이지'
    else:
        st.warning("결과없음")
    
    st.rerun()

def mainpage():
    st.title("다액위키 모음")
    서치변수 = st.text_input("검색")

    if st.button("검색하기"):
        such(서치변수)

#    for word in suchlist:


def 다액페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("다액")
    daaek_img = Image.open("다액.jpg")
    st.image(daaek_img)

    st.table(
    {
        "제목": '다액',
        "개발년도":"2025",
        "제작자": "곽우찬"

    }
    )
    st.header("개요")
    st.write()
    st.write("다액에 관한 페이지")
    st.write("다액은 다이나믹 액션의 줄임말이다.원래는 개발자가 좋아하는 액괴계 영상에서 영감을 얻었으나 다액시리즈의 스토리와 연관이 없어서 다이나믹 액션으로 뜻을 바꾸었다.")
    st.write()
    st.header("개발년도와 역사")
    st.write()
    st.write("다액이라는 단어의 역사")
    st.write("다액이라는 단어는 2023년 후반에 생각했으나 그 당시에는 사용은 하지 않았다. 그리고 2025년에 어느날 다액을 본격적으로 사용하기 시작하였다. \n그 배경을 보자면 개발자의자캐 새로운 세계관에서는 새 시리즈의 닉네임을 결정하고 있었다. 이름을 결정하던 도중 아에코(다액 변형말) 시사닉세이트 등이 후보로 올라가다가 다액이 최종 후보가 되었다.")
    st.write()
    st.header("줄거리")
    st.write("다액 세계관의 스토리는 악의 범죄조직 아포단과 정의를 지키는 SWAT전사들 S.SWAT팀이 싸우는 내용이다. 그리고 더 자세한 것은 다른 다액위키 사이트에서 찾아야한다.")
    st.write()
    st.header("등장인물")
    if st.button("해당페이지(다액/등장인물)로 가기"):
        st.session_state.session = '다액의등장인물들'
        st.rerun()
def 잇프페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("잇프")
    itf_img = Image.open("잇프.jpg")
    st.image(itf_img)
    
    st.table(
        {
            "제목": '잇프',
            "나이":"15세",
            "키": "176cm",
            "몸무게":"55kg"

        }
    )

    st.divider()
    st.header("개요")
    st.write()
    st.write("잇프는 다액 시리즈에 나오는 주인공 캐릭터이다.")
    st.write()

    st.divider()
    st.header("작중행정")
    st.write()
    st.write("잇프는 미출시게임 다액에 나오는 주인공으로  스토리 기준 다액시리즈의 모든 게임에서 나온다. ")
    st.write()
    st.header("전투스킬")
    st.write()
    st.write("일반 주먹때리기(펀치)")
    st.write("일반 발차기(킥)")
    st.write("쉐도우 실드(다이나믹 웨폰)")
    st.write("롤링 스트라이크(점프해서 하는 롤링 토네이도 킥)")
    st.write("결정화폭풍(필살기이다. 적에게 결정화 빔을 쏘면서 폭풍을 일으킨다.)")
    st.write()
    st.header("가족 관계")
    st.write()
    st.write("잇프는 작중에 부모님이 잇프는15살인아들인데 SWAT대원을 시키는 아동확대 피해자이다.")
    st.header("속성")
    st.write()
    st.write("얼음속성(컨셉은 일반경찰)")
    
    #itf_img = Image.open("잇프.jpg")
    #st.image(itf_img)

    
def 다액의등장인물들():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("다액의 등장인물들")
    #itf_img = Image.open("잇프.png")
    #st.image(itf_img)


    st.write("다액 등장인물의 관한 페이지")
    st.write()
    st.write("미리 확인하기")
    st.table(
    {
        "SWAT대원들" :['잇프','인프','잇티',"엣티","엣프","엔프"],
        "악당목록" : ["기계수","잡몹","아포","카이"] }
    )
    
def 인프페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    inf_img = Image.open("inf.jpg")
    st.image(inf_img)
    st.title("인프")
    
    st.table(
        {
            "제목": '인프',
            "나이":"15세",
            "키": "180cm",
            "몸무게":"75kg"

        }
    )

    st.divider()
    st.header("개요")
    st.write()
    st.write("인프는 다액 시리즈에 나오는 캐릭터이다.")
    st.write()

    st.divider()
    st.header("작중행정")
    st.write()
    st.write("인프는 미출시게임 다액에 나오는 캐릭터로 스토리 기준 다액시리즈의 모든 게임에서 나온다. ")
    st.write()
    st.header("전투스킬")
    st.write()
    st.write("일반 주먹때리기(펀치)")
    st.write("일반 발차기(킥)")
    st.write("슈페리어 머신건(다이나믹 웨폰)")
    st.write("하이퍼 크러시(멱살을 잡고 던지는 기술)")
    st.write("패닉 웨이브(필살기이다.적을 실드 안에 가둬서 전기충격한다.)")
    st.write()
    st.header("속성")
    st.write()
    st.write("물 속성이다.(컨셉도 해양경찰)")

def 엣티페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("엣티")
    엣티_img = Image.open("etty.jpg")
    st.image(엣티_img)
    
    st.table(
        {
            "제목": '엣티',
            "나이":"16세",
            "키": "189cm",
            "몸무게":"85kg"

        }
    )

    st.divider()
    st.header("개요")
    st.write()
    st.write("엣티는 다액 시리즈에 나오는 캐릭터이다.")
    st.write()

    st.divider()
    st.header("작중행정")
    st.write()
    st.write("엣티는 미출시게임 다액에 나오는 캐릭터로 스토리 기준 다액시리즈의 모든 게임에서 나온다. 그리고 경찰특공대에서 리더이다.")
    st.write()
    st.header("전투스킬")
    st.write()
    st.write("일반 주먹때리기(펀치)")
    st.write("일반 발차기(킥)")
    st.write("피닉스칼리버(다이나믹 웨폰)")
    st.write("불주먹(불 붙은 주먹으로 때린다.)")
    st.write("피닉스 롤링 펀치(필살기이다. 적에게 회전하는 불주먹으로 데미지를 입힌다.)")
    st.write()
    st.header("가족 관계")
    st.write()
    st.write("잇프와 비슷하게 엣티는 작중에 부모님이 엣티라는 열여섯살아들에게 SWAT대원을 시키는 아동확대 피해자이다. 그리고 잇프의 형이다.")
    st.header("속성")
    st.write()
    st.write("불속성(컨셉은 소방관)")

def 엣프페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("엣프")
    엣프_img = Image.open("etf.jpg")
    st.image(엣프_img)
    
    st.table(
        {
            "제목": '엣프',
            "나이":"15세",
            "키": "168cm",
            "몸무게":"48kg"

        }
    )

    st.divider()
    st.header("개요")
    st.write()
    st.write("엣프는 다액 시리즈에 나오는 캐릭터이다.")
    st.write()

    st.divider()
    st.header("작중행정")
    st.write()
    st.write("엣프는 미출시게임 다액에 나오는 캐릭터로 스토리 기준 다액시리즈의 모든 게임에서 나온다. 그리고 5인조 경찰특공대에서 유일한 여성멤버 이다.")
    st.write()
    st.header("전투스킬")
    st.write()
    st.write("일반 주먹때리기(펀치)")
    st.write("일반 발차기(킥)")
    st.write("사이클론 보우(다이나믹 웨폰)")
    st.write("플라즈마 빔(광선장풍을 발사한다.)")
    st.write("일도양단 슬래시(필살기이다.아주 강력한 장풍으로 적을 반으로 가른다.)")
    st.write()
    st.write("바람속성(컨셉은 항공경찰)")

def 잇티페이지():
    서치변수 = st.text_input("검색")
    if st.button("검색하기"):
        such(서치변수)

    st.title("잇티")
    itty_img = Image.open("itty.jpg")
    st.image(itty_img)
    
    st.table(
        {
            "제목": '잇티',
            "나이":"15세",
            "키": "170cm",
            "몸무게":"54kg"

        }
    )

    st.divider()
    st.header("개요")
    st.write()
    st.write("잇티는 다액 시리즈에 나오는 캐릭터이다.")
    st.write()

    st.divider()
    st.header("작중행정")
    st.write()
    st.write("잇티는 미출시게임 다액에 나오는 캐릭터로 스토리 기준 다액시리즈의 모든 게임에서 나온다. ")
    st.write()
    st.header("전투스킬")
    st.write()
    st.write("일반 주먹때리기(펀치)")
    st.write("일반 발차기(킥)")
    st.write("라이트닝 스피어(다이나믹 웨폰)")
    st.write("토네이도 킥(360도 돌려차기)")
    st.write("기가 스피어(적에게 팔꿈치 치기로 필살기를 날린다.)")
    st.write()
    st.header("속성")
    st.write()
    st.write("전기 속성이다.(컨셉은 구급대원)")


#세션에 뭐가 들어있는지 확인
if 'session' not in st.session_state:
    st.session_state.session = 'mainpage'
if st.session_state.session == 'mainpage':
    mainpage()
elif st.session_state.session == '다액페이지':
    다액페이지()
elif st.session_state.session == '잇프페이지':
    잇프페이지()
elif st.session_state.session == '다액의등장인물들':
    다액의등장인물들()
elif st.session_state.session == '인프' or st.session_state.session == '인프페이지':
    인프페이지()
elif st.session_state.session == '잇티' or st.session_state.session == '잇티페이지':
    잇티페이지()
elif st.session_state.session == '엣티' or st.session_state.session == '엣티페이지':
    엣티페이지()
elif st.session_state.session == '엣프' or st.session_state.session == '엣프페이지':
    엣프페이지()
else:
    st.write("그런페이지는 존재하지 않아요!")
    서치변수 = st.text_input("검색")
    such(서치변수)



