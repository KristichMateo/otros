const crypto = [
    { name: "Bytecoin", value: 100 },
    { name: "Mapple", value: 98 },
    { name: "Microtof", value: 102 },
    { name: "Pecsi", value: 74 }
];

// ------------------------------------------------------------------------------ //
//! forEach()

crypto.forEach( (coins) => console.log("forEach() method: ",coins.value)); //por cada uno ejecuto una funcion, coins sera el elemento en ese indice al momento de la iteracion

// ------------------------------------------------------------------------------ //
//! find()

const findeCrypto = crypto.find( (element) => element.name === "Mapple"); //devuelve el primer elemento que cumpla con esa condicion    
console.log("find() method: ", findeCrypto);

// ------------------------------------------------------------------------------ //
//! filter()

const filterCrypto = crypto.filter( (element) => element.value >= 100);
console.log("filter() method: ", filterCrypto);

// ------------------------------------------------------------------------------ //
//! map()

const mapCrypto = crypto.map( (coins) => { //Ejecuta una funcion por cada elemento, es usado para modificar el array
    return {
        name: coins.name,
        value: coins.value,
        newValue: Math.round(coins.value * 1.15)
    };
});
console.log("map() method: ", mapCrypto);

// ------------------------------------------------------------------------------ //
//! reduce()

const totalCrypto = crypto.reduce( (count, coin) => count + coin.value, 0)
console.log("reduce() method: ", totalCrypto);

// ------------------------------------------------------------------------------ //
//! some()

const someCrypto = crypto.some( (element) => element.name === "Mapplee");
console.log("some() method: ", someCrypto);

// ------------------------------------------------------------------------------ //
//! sort()

const sortCrypto = crypto.sort( (firstElement, secondElement) => secondElement.name - firstElement.name);
console.log("sort() method: ", sortCrypto);