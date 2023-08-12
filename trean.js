
const trainAList={"CHN": 0, "SLM":350 ,"BLR":550, "KRN":900 ,"HYB":1200,"NGP":1600, "ITJ":19,"BPL":2000, "AGA":2500, "NDL":2700 }

const trainBList={"TVC":0, "SRR":300,"MAQ":600 , "MAO":1000, "PNE":1400,"HYB":2000, "NGP":2400,"ITJ":2700,"BPL":2800,"PTA":3800,"NJP":4200,"GHY":4700 }


// const trainA = ['ENGINE', 'NDL', 'NDL', 'KRN', 'GHY', 'SLM', 'NJP', 'NGP', 'BLR'];
// const trainB = ['ENGINE', 'NJP', 'GHY', 'AGA', 'BPL', 'PTA'];


//...........................//
function processTrains(trainA, trainB) {

const removeElementsBeforeHyb = (list) => {
    const keys = Object.keys(list);
    const hybIndex = keys.indexOf("HYB");
    
    if (hybIndex !== -1) {
        const newKeys = keys.slice(hybIndex);
        const newObject = {};
        for (const key of newKeys) {
            newObject[key] = list[key];
        }
        return newObject;
    }
    
    return list;
};

const taianAsorted = removeElementsBeforeHyb(trainAList);
const taianBsorted = removeElementsBeforeHyb(trainBList);

console.log("TA",taianAsorted);
console.log("TB",taianBsorted);

// Merge the two objects
const mergedObj = {};

for (const key in taianAsorted) {
  if (mergedObj[key] === undefined) {
    mergedObj[key] = [taianAsorted[key]];
  } else {
    mergedObj[key].push(taianAsorted[key]);
  }
}



console.log(mergedObj);

    // // Arriving at Hyderabad
    // arrivalTrainA.splice(arrivalTrainA.indexOf('HYB'), 1);
    // TrainB.splice(arrivalTrainB.indexOf('HYB'), 1);
    // TrainA.push('HYB');
    // arrivalTrainB.push('HYB');

    // // Departure from Hyderabad as Train AB
    // departureTrainAB = departureTrainAB.concat(arrivalTrainA.slice(0, -1), arrivalTrainB.slice(0, -1));
    // departureTrainAB.sort((a, b) => getDistance(b) - getDistance(a));
    // departureTrainAB.unshift('ENGINE', 'ENGINE');

    // // Print results
    // console.log(`ARRIVAL TRAIN_A ${arrivalTrainA.join(' ')}`);
    // console.log(`ARRIVAL TRAIN_B ${arrivalTrainB.join(' ')}`);
    // console.log(`DEPARTURE TRAIN_AB ${departureTrainAB.join(' ')}`);
}

const trainA = ['ENGINE', 'NDL', 'NDL', 'KRN', 'GHY', 'SLM', 'NJP', 'NGP', 'BLR'];
const trainB = ['ENGINE', 'NJP', 'GHY', 'AGA', 'BPL', 'PTA'];

processTrains(trainA, trainB);
// ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP
// ARRIVAL TRAIN_B ENGINE NJP GHY AGA BPL PTA
