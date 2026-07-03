import streamlit as st
import random

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(page_title="🔮 미스틱 타로", page_icon="🔮", layout="centered")

# ---------------------------
# 메이저 아르카나 22장 데이터
# ---------------------------
TAROT_CARDS = [
    {"name": "The Fool (바보)", "emoji": "🃏", "upright": "새로운 시작, 순수한 도전, 자유로운 모험", "reversed": "무모함, 준비 부족, 방향 상실"},
    {"name": "The Magician (마법사)", "emoji": "🎩", "upright": "강한 의지, 창조력, 목표 실현의 힘", "reversed": "재능 낭비, 자만심, 계획의 실패"},
    {"name": "The High Priestess (여사제)", "emoji": "🌙", "upright": "직관, 내면의 지혜, 신비로운 통찰", "reversed": "혼란, 비밀 노출, 감정 억압"},
    {"name": "The Empress (여황제)", "emoji": "👑", "upright": "풍요, 창조, 따뜻한 보살핌", "reversed": "의존, 과잉보호, 창조력 정체"},
    {"name": "The Emperor (황제)", "emoji": "⚔️", "upright": "안정, 리더십, 확고한 질서", "reversed": "독단, 경직됨, 통제 상실"},
    {"name": "The Hierophant (교황)", "emoji": "⛪", "upright": "전통, 가르침, 신뢰할 수 있는 조언", "reversed": "고정관념, 반항, 관습 탈피"},
    {"name": "The Lovers (연인)", "emoji": "💕", "upright": "사랑, 조화로운 선택, 진실한 관계", "reversed": "갈등, 잘못된 선택, 불균형"},
    {"name": "The Chariot (전차)", "emoji": "🏇", "upright": "의지의 승리, 추진력, 목표 달성", "reversed": "방향성 상실, 좌절, 통제 불능"},
    {"name": "Strength (힘)", "emoji": "🦁", "upright": "용기, 인내, 내면의 강인함", "reversed": "자신감 부족, 나약함, 감정 폭발"},
    {"name": "The Hermit (은둔자)", "emoji": "🏮", "upright": "성찰, 고독한 지혜, 내면 탐구", "reversed": "고립, 회피, 소통 단절"},
    {"name": "Wheel of Fortune (운명의 수레바퀴)", "emoji": "🎡", "upright": "전환점, 행운, 순환하는 변화", "reversed": "불운, 통제 불가능한 변화"},
    {"name": "Justice (정의)", "emoji": "⚖️", "upright": "공정함, 균형, 인과응보", "reversed": "불공정, 편견, 왜곡된 판단"},
    {"name": "The Hanged Man (매달린 사람)", "emoji": "🙃", "upright": "관점의 전환, 희생, 기다림의 미학", "reversed": "정체, 저항, 시간 낭비"},
    {"name": "Death (죽음)", "emoji": "💀", "upright": "끝과 새로운 시작, 변화, 재탄생", "reversed": "변화 거부, 정체, 두려움"},
    {"name": "Temperance (절제)", "emoji": "🕊️", "upright": "균형, 조화, 인내심 있는 통합", "reversed": "불균형, 과잉, 조급함"},
    {"name": "The Devil (악마)", "emoji": "😈", "upright": "속박, 유혹, 물질적 집착", "reversed": "해방, 자각, 속박에서 벗어남"},
    {"name": "The Tower (탑)", "emoji": "🗼", "upright": "급격한 변화, 붕괴, 충격적 깨달음", "reversed": "위기 회피, 두려움 속 변화 지연"},
    {"name": "The Star (별)", "emoji": "⭐", "upright": "희망, 영감, 밝은 미래에 대한 믿음", "reversed": "절망, 자신감 상실, 방향성 부재"},
    {"name": "The Moon (달)", "emoji": "🌕", "upright": "불안, 무의식, 감춰진 진실", "reversed": "혼란 해소, 두려움 극복, 명료함"},
    {"name": "The Sun (태양)", "emoji": "☀️", "upright": "성공, 기쁨, 밝은 에너지와 활력", "reversed": "일시적 좌절, 과도한 낙관"},
    {"name": "Judgement (심판)", "emoji": "📯", "upright": "각성, 부활, 중요한 결단의 순간", "reversed": "후회, 자기 비판, 결단 회피"},
    {"name": "The World (세계)", "emoji": "🌍", "upright": "완성, 성취, 하나의 여정의 마무리", "reversed": "미완성, 지연, 마무리 부족"},
]

POSITIONS = ["🕰️ 과거", "✨ 현재", "🌠 미래"]

# ---------------------------
# 스타일
# ---------------------------
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top, #1a1a2e 0%, #0d0d1a 100%);
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e8d9ff !important;
    }

    /* 카드 뒷면 (뽑기 전) */
    .card-back {
        background: repeating-linear-gradient(45deg, #2b1a4a, #2b1a4a 10px, #3a2266 10px, #3a2266 20px);
        border: 2px solid #9b59f5;
        border-radius: 16px;
        padding: 30px 10px;
        text-align: center;
        box-shadow: 0 0 16px rgba(155, 89, 245, 0.4);
        margin-bottom: 10px;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        animation: pulse 2.5s ease-in-out infinite;
    }
    .card-back-symbol {
        font-size: 36px;
        opacity: 0.8;
    }
    .card-back-label {
        font-size: 12px;
        color: #c9a8ff !important;
        letter-spacing: 2px;
        margin-top: 8px;
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 16px rgba(155, 89, 245, 0.4); }
        50% { box-shadow: 0 0 28px rgba(155, 89, 245, 0.75); }
    }

    /* 카드 앞면 (뒤집힌 후) */
    .card-front {
        background: linear-gradient(145deg, #2b1a4a, #1a0f2e);
        border: 2px solid #ffd166;
        border-radius: 16px;
        padding: 16px 10px;
        text-align: center;
        box-shadow: 0 0 22px rgba(255, 209, 102, 0.5);
        margin-bottom: 10px;
        min-height: 180px;
        animation: flipIn 0.5s ease-out;
    }
    @keyframes flipIn {
        0% { transform: rotateY(90deg); opacity: 0; }
        100% { transform: rotateY(0deg); opacity: 1; }
    }
    .card-emoji { font-size: 42px; }
    .card-name {
        font-size: 16px;
        font-weight: bold;
        color: #d8b4ff !important;
        margin-top: 6px;
    }
    .card-position {
        font-size: 12px;
        color: #9b59f5 !important;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .card-orientation {
        font-size: 13px;
        color: #ffd166 !important;
        font-weight: bold;
        margin-top: 4px;
    }
    .card-meaning {
        font-size: 13px;
        color: #cfc4e8 !important;
        margin-top: 6px;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background: linear-gradient(90deg, #6a0dad, #9b59f5);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 15px;
        width: 100%;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #9b59f5, #6a0dad);
        box-shadow: 0 0 14px #9b59f5;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# 타이틀
# ---------------------------
st.title("🔮 미스틱 타로 리딩")
st.markdown("아래 카드를 **한 장씩 클릭**해서 뒤집어보세요. 과거 · 현재 · 미래가 밝혀집니다 🌌")
st.markdown("---")

# ---------------------------
# 세션 상태 초기화
# ---------------------------
if "drawn_cards" not in st.session_state:
    st.session_state.drawn_cards = None
if "revealed" not in st.session_state:
    st.session_state.revealed = [False, False, False]

def new_reading():
    chosen = random.sample(TAROT_CARDS, 3)
    result = []
    for card in chosen:
        orientation = random.choice(["upright", "reversed"])
        result.append({
            "name": card["name"],
            "emoji": card["emoji"],
            "orientation": "정방향" if orientation == "upright" else "역방향",
            "meaning": card["upright"] if orientation == "upright" else card["reversed"],
        })
    st.session_state.drawn_cards = result
    st.session_state.revealed = [False, False, False]

# ---------------------------
# 새 리딩 시작 버튼
# ---------------------------
if st.button("🔮 새로운 카드 뽑기 (섞기)"):
    new_reading()

st.markdown("")

# ---------------------------
# 카드 3장 표시
# ---------------------------
if st.session_state.drawn_cards:
    cols = st.columns(3)
    for i, (col, position, card) in enumerate(zip(cols, POSITIONS, st.session_state.drawn_cards)):
        with col:
            st.markdown(f"<div class='card-position' style='text-align:center;'>{position}</div>", unsafe_allow_html=True)

            if st.session_state.revealed[i]:
                # 앞면 (뒤집힌 카드)
                st.markdown(f"""
                <div class="card-front">
                    <div class="card-emoji">{card['emoji']}</div>
                    <div class="card-name">{card['name']}</div>
                    <div class="card-orientation">{card['orientation']}</div>
                    <div class="card-meaning">{card['meaning']}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # 뒷면 (클릭 전)
                st.markdown("""
                <div class="card-back">
                    <div class="card-back-symbol">🔮</div>
                    <div class="card-back-label">TAP TO REVEAL</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("카드 뒤집기", key=f"flip_{i}"):
                    st.session_state.revealed[i] = True
                    st.rerun()

    if all(st.session_state.revealed):
        st.markdown("---")
        st.success("✨ 세 장의 카드가 모두 열렸습니다. 당신의 이야기를 잘 들여다보세요.")
        st.balloons()
else:
    st.info("⬆️ 위 버튼을 눌러 카드를 섞고 리딩을 시작하세요!")

st.markdown("---")
st.caption("Made with Streamlit · ✨ Mystic Tarot Reading ✨")
