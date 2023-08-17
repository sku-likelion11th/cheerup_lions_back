// 반응형 텍스트 변경
const inputpw = document.querySelector('.input-pw');
const submitbtn = document.querySelector('.input-submit');

// 응원하기 댓글창
function checkMediaQuery() {
    if (window.matchMedia('(max-width: 650px)').matches) {
        inputpw.placeholder = '비번';
        submitbtn.value = '게시';
    } else {
        inputpw.placeholder = '비밀번호 입력';
        submitbtn.value = '게시하기';
    }
}

window.addEventListener('load', checkMediaQuery);
window.addEventListener('resize', checkMediaQuery);
