//CONSULTA A API DE POKEMON: 
const apiUrl = 'https://pokeapi.co/api/v2/pokemon/';

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        console.log('Lista de Pokémon:', data.results);
    })
    .catch(error => {
        console.error('Error al obtener la lista de Pokémon:', error.message);
    });
