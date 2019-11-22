let values = [];
let w = 10;

let states = [];

function setup() {
  createCanvas(windowWidth, windowHeight);
  values = new Array(floor(width / w));
  for (let i = 0; i < values.length; i++) {
    values[i] = random(height);
    states[i] = -1;
  }
  radixSort(values);
}

async var getDigit = function(num,nth){
    // get last nth digit of a number
    var ret = 0;
    while(nth--){
      ret = num % 10
      num = Math.floor((num - ret) / 10)
    }
    return ret
  }
  
  // radixSort
 async radixSort(list){
    var max = Math.floor(Math.log10(Math.max.apply(Math,list))),  
        // get the length of digits of the max value in this array
        digitBuckets = [],
        idx = 0;
  
    for(var i = 0;i<max+1;i++){
  
      // rebuild the digit buckets according to this digit
      digitBuckets = []
      for(var j = 0;j<list.length;j++){
        var digit = getDigit(list[j],i+1);
  
        digitBuckets[digit] = digitBuckets[digit] || [];
        digitBuckets[digit].push(list[j]);
      }
  
      // rebuild the list according to this digit
      idx = 0
      for(var t = 0; t< digitBuckets.length;t++){
        if(digitBuckets[t] && digitBuckets[t].length > 0){
          for(j = 0;j<digitBuckets[t].length;j++){
            list[idx++] = digitBuckets[t][j];
          }
        }
      }
    }
    return list
  }
 

// async function quickSort(arr, start, end) {
//   if (start >= end) {
//     return;
//   }
//   let index = await partition(arr, start, end);
//   states[index] = -1;

//   await Promise.all([
//     quickSort(arr, start, index - 1),
//     quickSort(arr, index + 1, end)
//   ]);
// }

// async function partition(arr, start, end) {
//   for (let i = start; i < end; i++) {
//     states[i] = 1;
//   }

//   let pivotValue = arr[end];
//   let pivotIndex = start;
//   states[pivotIndex] = 0;
//   for (let i = start; i < end; i++) {
//     if (arr[i] < pivotValue) {
//       await swap(arr, i, pivotIndex);
//       states[pivotIndex] = -1;
//       pivotIndex++;
//       states[pivotIndex] = 0;
//     }
//   }
//   await swap(arr, pivotIndex, end);

//   for (let i = start; i < end; i++) {
//     if (i != pivotIndex) {
//       states[i] = -1;
//     }
//   }

//   return pivotIndex;
// }

function draw() {
  background(0);

  for (let i = 0; i < values.length; i++) {
    noStroke();
    if (states[i] == 0) {
      fill('#E0777D');
    } else if (states[i] == 1) {
      fill('#4169e1');
    } else if (states[i] == -1) {
      fill('#ff9000'); 
    } else {
      fill(255);
    }
    rect(i * w, height - values[i], w, values[i]);
  }
}

async function swap(arr, a, b) {
  await sleep(50);
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}