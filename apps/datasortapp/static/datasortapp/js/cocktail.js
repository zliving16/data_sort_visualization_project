// QuickSort Visualization
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
  cocktailSort(values, 0, values.length - 1);
}

async function cocktailSort(arr)
{
	var swapped;
	do {
		for(var i = 0; i < arr.length - 2; i++) {
      await sleep(5)
      states[i]= 0
			if(arr[i] > arr[i+1]) {
        var temp = arr[i];
        states[i-1]= -1
        states[i+1]= 0
				arr[i] = arr[i+1];
				arr[i+1] = temp;
				swapped = true;
      }
      //states[i]= -1
		}	
		if(!swapped) {
			break;
		}
		swapped = false;
		for( i = arr.length - 2; i > 0; i--) {
      await sleep(5)
      
			if(arr[i] > arr[i+1]) {
        var temp1 = arr[i];
        states[i-1]= 0
        states[i+1]= -1
				arr[i] = arr[i+1];
				arr[i+1] = temp1;
				swapped = true;
      }
      //states[i]= -1
		}
	} while(swapped);
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
    }else {
      fill('#a7a3c7');
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