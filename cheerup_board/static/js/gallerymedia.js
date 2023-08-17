// 갤러리 댓글창
const inputpw1 = document.querySelector('.input-pw1');
const submitbtn1 = document.querySelector('.input-submit1');

// 미디어 쿼리 감지 함수
function checkMediaQuery1() {
    if (window.matchMedia('(max-width: 768px)').matches) {
        inputpw1.placeholder = '비번';
        submitbtn1.value = '게시';
    } else {
        inputpw1.placeholder = '비밀번호 입력';
        submitbtn1.value = '게시하기';
    }
}

// 페이지 로드시 및 리사이즈 이벤트 시 미디어 쿼리 감지 함수 호출
window.addEventListener('load', checkMediaQuery1);
window.addEventListener('resize', checkMediaQuery1);