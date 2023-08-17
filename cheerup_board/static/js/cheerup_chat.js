function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function checkpasswordRemove(id) {
    var checkpw = prompt('비밀번호 4자리를 입력하세요.');
    var csrfToken = getCookie('csrftoken');

    // AJAX 요청 생성
    $.ajax({
        url: '/message/delete/'+id+'/',  // Django URL에 맞게 수정
        method: 'POST',
        headers: { 'X-CSRFToken': csrfToken },  // CSRF 토큰을 헤더에 포함
        data: { "annoy_password": checkpw },
        dataType: 'json',
        success: function(response) {
            console.log('서버 응답:', response.message);
            location.reload();
        },
        error: function(xhr, status, error) {
            console.error('에러:', error);
        }
    });
}