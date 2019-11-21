// QuickSort Visualization
// Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/143-quicksort.html
// https://editor.p5js.org/codingtrain/sketches/vic6Qzo-j
// https://youtu.be/eqo2LxRADhU

var values = [];
var numLines = 500;
var sortHist = [];
function setup() {
  createCanvas(windowWidth, windowHeight);

  for (i = 0; i < numLines; i++) {
    values[i] =random(height);
  }
  sortHist = mergeSort(values);
  frameRate(1);
}
  
var historyIndex = 0;
function draw() {
  background(0);
  for (i = 0; i < sortHist[historyIndex].length; i++) {
    let col = color(sortHist[historyIndex][i], height, height);
    stroke(255);
    fill(255);
    var location = map(i, 0, sortHist[historyIndex].length, 0, width);
    rect(location, height - sortHist[historyIndex][i], width/numLines, height);
  } 
  historyIndex++;
  if (historyIndex > sortHist.length -1){
    noLoop();
  }
}

function mergeSort(array) {
  var arrays = [array.slice()],
  n = array.length,
  array0 = array,
  array1 = new Array(n);

  for (var m = 1; m < n; m <<= 1) {
    for (var i = 0; i < n; i += (m << 1)) {
      merge(i, Math.min(i + m, n), Math.min(i + (m << 1), n));
    }
    arrays.push(array1.slice());
    array = array0, array0 = array1, array1 = array;
  }

function merge(left, right, end) {
  for (var i0 = left, i1 = right, j = left; j < end; ++j) {
    array1[j] = array0[i0 < right && (i1 >= end || array0[i0] <=    array0[i1]) ? i0++ : i1++];
   }
 }
 return arrays;
}  
