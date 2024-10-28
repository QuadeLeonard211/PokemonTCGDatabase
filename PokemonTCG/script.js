// script.js
//
// A javascript file with the inteded purpose of integrating the Pokemon TCG API with our front end environment


async function fetchCardData() {

    const url = 'https://api.pokemontcg.io/v2/cards';
//    const apiKey = api key
// Due to security concerns, we will not yet add the api key untl we have secure methods to protect it

    try {
        const response = await fetch(url, {
            headers: {
                'X-Api-Key': apiKey
            }
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        displayCardData(data.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


function displayCardData(cards) {
    const cardDisplay = document.getElementById('cardDisplay');
    cardDisplay.innerHTML = '';
    cards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.innerHTML = `
            <h2>${card.name}</h2>
            <img src="${card.images.small}" alt="${card.name}">
            <p>Set: ${card.set.name}</p>
            <p>Type: ${card.types?.join(', ')}</p>
        `;
        cardDisplay.appendChild(cardElement);
    });
}