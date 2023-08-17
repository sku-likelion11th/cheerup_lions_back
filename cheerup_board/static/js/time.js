// 해커톤 종료 카운트 다운
const countdownElement = document.getElementById('countdown'); // display

const targetDate = new Date(2023, 7, 19, 7, 0, 0); // 종료 시각

function updateCountdown() {
    const now = new Date(); // 현 시각
    const timeLeft = targetDate - now; // 남은 시각 

    if (timeLeft > 0) {
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        countdownElement.textContent = `${days}일 ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        setTimeout(updateCountdown, 1000); // Update every 1 second
    } else {
        countdownElement.textContent = "해커톤 종료";
    }
}

updateCountdown();