$(document).ready(function() {
    $('#chatForm').submit(function(event) { // 폼 제출
        event.preventDefault(); // 폼 기본 동작 중단

        const password = $('.input-pw').val();
        const message = $('.input-text').val();

        // 둘 중 하나라도 비어있으면
        if (password === '' || message === '') {
            alert('비밀번호나 메시지가 비어있습니다.');
            if (password === '') {
                $('.input-pw').focus();
            } else {
                $('.input-text').focus();
            }
            return;
        }

        console.log(password, message);

        const data = {
            password: password, // 비번
            message: message // text
        };

        $.ajax({
            type: 'POST',
            url: '/',
            data: JSON.stringify(data), // 비번, 메세지 전달
            contentType: 'application/json',
            success: function(response) {
                // 성공
                console.log('성공');
                // 폼 초기화
                $('.input-pw').val('');
                $('.input-text').val('');
            },
            error: function(error) {
                // 실패 시 동작
                console.error('데이터 전송 실패:', error);
            }
        });
    });
});


// 수정, 삭제 비밀번호 입력시,,,,, 맞나이게?
correctpw = document.querySelector('.pw_confirm').textContent;
console.log(correctpw);

function checkpasswordEdit() {
    checkpw = prompt('비밀번호 4자리를 입력하세요.');
    console.log(checkpw);

    if (correctpw === checkpw) {
        console.log('수정 ㄱㄱ');

    } else {
        alert('비밀번호가 일치하지 않습니다.');
    }
}

function checkpasswordRemove() {
    checkpw = prompt('비밀번호 4자리를 입력하세요.');
    console.log(checkpw);

    if (correctpw === checkpw) {
        console.log('삭제 ㄱㄱ');

    } else {
        alert('비밀번호가 일치하지 않습니다.');
    }
}