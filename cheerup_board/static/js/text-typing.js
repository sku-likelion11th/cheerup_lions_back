var words = ['해커톤에 참여한 여러분, 파이팅!', '해커톤에서 모두의 열정을 보여줘!', '해커톤 참가자 모두 힘냅시다!', '지금의 노력이 모두 성공으로 이어질 거예요.', '해커톤에서 놀라운 결과물을 만들어봐요!', '함께 힘내서 이번 해커톤도 대성공하자!'];
var part, i = 0, offset = 0, len = words.length, forwards = true, skip_count = 0, skip_delay = 15, speed = 70;

var wordflick = function () {
    setInterval(function () {
        if (forwards) {
            if (offset >= words[i].length) {
                ++skip_count;
                if (skip_count == skip_delay) {
                    forwards = false;
                    skip_count = 0;
                }
            }
        } else {
            if (offset == 1) {
                forwards = true;
                i++;
                offset = 0;
                if (i >= len) {
                    i = 0;
                }
            }
        }
        part = words[i].substr(0, offset);
        if (skip_count == 0) {
            if (forwards) {
                offset++;
            } else {
                offset--;
            }
        }
        $('.word').text('"' + (part.length > 0 ? part : '\u200B') + '"'); // 이 부분을 수정했습니다.
    }, speed);
};

function fetchAndAddWords() {
    fetch('/get_messages/')
        .then(response => response.json())
        .then(data => {
            const fetchedMessages = data.messages;
            words.push(...fetchedMessages);
            len = words.length; // 새로운 길이로 업데이트
        })
        .catch(error => {
            console.error('Error fetching messages:', error);
        });
}

$(document).ready(function () {
    wordflick();
    fetchAndAddWords();
});
