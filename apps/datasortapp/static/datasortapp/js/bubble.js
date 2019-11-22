// bubble_sort Visualization
// Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/143-quicksort.html
// https://editor.p5js.org/codingtrain/sketches/vic6Qzo-j
// https://youtu.be/eqo2LxRADhU

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
  bubbleSort(values);
}

async function bubbleSort(arr){

  var len = arr.length;
  for (var i = len-1; i>=0; i--){ 
    for(var j = 1; j<=i; j++){
      await sleep(10)
      
      states[j]= 0
      // let index = j
      // states[j] = 0
      if(arr[j-1]>arr[j]){
          states[j-1]= -1
          var temp = arr[j-1];
          arr[j-1] = arr[j];
          
          arr[j] = temp;
          states[j]= 0
          
       }
       states[j]= -1
      // states[i-1]=-1
      // states[j-1]=-1
    }
  }
  return arr;
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
      fill('#D6FFB7');
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