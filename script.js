document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one');

    elementOne.addEventListener('dblclick', () => elementOne.classList.add('animation'));

    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two');

    elementTwo.addEventListener('mouseover', () => elementTwo.style.boxShadow = '10px 10px')

    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three');
    
    elementThree.addEventListener('click', () => elementThree.style.display = 'none');

    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four');
    
    elementFour.addEventListener('click', () => elementFour.style.backgroundColor = 'green');
});