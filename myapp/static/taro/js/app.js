function main2() {
    window.location.href = "/raskl/";  // Переход на защищённую страницу
}

function main4() {
    window.location.href = "/page5/"; // URL маршрута на страницу page5.html
}

function redirectToQuestion(questionId) {
    const url = `/page5?question_id=${questionId}`;
    window.location.href = url;
}


function tg() {
    window.location.href = 'https://t.me/Utinoelico';
}

function vk() {
    window.location.href = 'https://vk.com/dumnkonechno';
}

document.querySelector('.card').addEventListener('click', function () {
    const container = this.parentElement;
    container.classList.toggle('active');
});

document.querySelector('.card img').addEventListener('click', () => {
    location.reload();  // Перезагрузка страницы для отображения интерпретации
});