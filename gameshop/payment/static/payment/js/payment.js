  document.addEventListener('DOMContentLoaded', function () {
    // Получаем форму и кнопку отправки
    const form = document.querySelector('.address-form');
    const submitBtn = document.getElementById('submit-btn');

    // Добавляем слушатель событий к форме
    form.addEventListener('submit', function (event) {
      // Проверяем, заполнены ли все обязательные поля формы
      const isFormValid = Array.from(form.elements).every(function (element) {
        return !(element.required && element.value.trim() === '');
      });

      // Дополнительно проверяем обязательность ZIP или почтового кода
      const zipCodeField = document.getElementById('postal-code');
      if (zipCodeField.required && zipCodeField.value.trim() === '') {
        isFormValid = false;
      }

      // Если форма не валидна, отменяем отправку и выводим сообщение
      if (!isFormValid) {
        event.preventDefault();
        alert('Все обязательные поля, включая ZIP или почтовый код, должны быть заполнены!');
      }
    });
  });


document.addEventListener('DOMContentLoaded', function () {
    // Получаем форму и кнопку отправки
    const form = document.querySelector('.address-form');
    const submitBtn = document.getElementById('submit-btn');

    // Добавляем слушатель событий к форме
    form.addEventListener('submit', function (event) {
      // Проверяем, заполнены ли все обязательные поля формы
      const isFormValid = Array.from(form.elements).every(function (element) {
        return !(element.required && element.value.trim() === '');
      });

      // Дополнительно проверяем обязательность ZIP или почтового кода
      const zipCodeField = document.getElementById('postal-code');
      if (zipCodeField.required && zipCodeField.value.trim() === '') {
        isFormValid = false;
      }

      // Если форма не валидна, отменяем отправку и выводим сообщение
      if (!isFormValid) {
        event.preventDefault();
        alert('Все обязательные поля должны быть заполнены!');
      }
    });
  });
