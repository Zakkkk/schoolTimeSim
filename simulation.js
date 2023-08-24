const prompt = require('prompt-sync')()
var fs = require('fs');

const totalPopulation = parseInt(prompt("Population: "))
// const totalPopulation = 100

// Utils
let randomChance = (chance, functionToRun) => {
    let percent = Math.floor(Math.random() * (100 + 1))
    if (percent <= chance)
    functionToRun()
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function tallyNumbers(arr) {
    // Create an empty object to store the counts
    const countObj = {};
  
    // Loop through the array
    for (let i = 0; i < arr.length; i++) {
      const num = arr[i];
  
      // If the number is not in the countObj, initialize it to 1, otherwise increment it by 1
      if (!countObj[num]) {
        countObj[num] = 1;
      } else {
        countObj[num]++;
      }
    }
  
    return countObj;
}  

function calculateCumulativeData(data) {
    let cumulativeSum = 0;
    const cumulativeData = {};
  
    for (const key in data) {
      cumulativeSum += data[key];
      cumulativeData[key] = cumulativeSum;
    }
  
    return cumulativeData;
  }

// ----- //

function Person () {
    let modeNum = getRandomInt(1,10)
    if (modeNum <= 5) // pt
        this.modeOfTransport = 1
    if (modeNum > 5 && modeNum <= 8) // walk
        this.modeOfTransport = 2
    if (modeNum > 8) // car
        this.modeOfTransport = 3

    let personalityNum = getRandomInt(1,10)
    if (personalityNum <= 3) // early
        this.personalityType = 1
    if (personalityNum > 3 && personalityNum <= 7) // ontime
        this.personalityType = 2
    if (personalityNum > 7) // late
        this.personalityType = 3

    const findArrivalTime = (typeOfTransport, personalityType) => {
        let arrivalTime = 30

        if (personalityType == 1) // early
        arrivalTime -= getRandomInt(6,10)

        if (personalityType == 2) // on time
            arrivalTime += getRandomInt(-5,5)

        if (personalityType == 3) // late
            arrivalTime += getRandomInt(6,10)

        // car
        if (typeOfTransport == 3)
            arrivalTime += getRandomInt(-5,5)

        // walk
        if (typeOfTransport == 2)
            arrivalTime += getRandomInt(-10,10)

        // pt
        if (typeOfTransport == 1)
            arrivalTime += getRandomInt(-15,15)

        return arrivalTime
    }

    this.arrivalTime = findArrivalTime(this.modeOfTransport, this.personalityType)
}

let num_arrivalTimes = []
let data = {}

let people = []

for (let i = 0; i < totalPopulation; i++) { // create people
    people.push(new Person())
    console.log("person created")
}

for (let i = 0; i < totalPopulation; i++) { // find their times
    num_arrivalTimes.push(people[i].arrivalTime)
    console.log("arrival time found")
}

// data.arrivalTimes = num_arrivalTimes
data.tally = tallyNumbers(num_arrivalTimes)
data.cumalitiveData = calculateCumulativeData(data.tally)

fs.mkdir('bin', { recursive: true }, (err) => {
    if (err) throw err
})

fs.writeFile(`bin/${totalPopulation}_${new Date().getTime()}.json`, JSON.stringify(data), function (err) {
    if (err) throw err
    console.log('File created')
})