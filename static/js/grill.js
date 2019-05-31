var countDownDate = new Date().getTime() + 20000; // 4hrs = 14400000
var start = new Date();
var ready = new Date().getTime() + 10000; // 30mins = 1800000 20mins = 1200000

// Update the count down every 1 second
var x = setInterval(countDown, 1000);

function countDown() {
  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="t1"
  document.getElementById("t3").innerHTML =
    hours + "h " + minutes + "m " + seconds + "s ";

  document.getElementById("t1").innerHTML = start.toLocaleTimeString();
  document.getElementById("t2").innerHTML = moment(start, "hh:mm:ss A")
    .add(20, "seconds")
    .format("LTS");

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("t3").innerHTML = "EXPIRED";
  }
}


document.getElementById("add").addEventListener("click", addHtml);

function addHtml() {
  var html =
    '<td><div class="row"><div class="col-auto"><p>S</p></div><div class="col-auto"><p id="t1"></p></div></div><div class="row"><div class="col-auto"><p>R</p></div><div class="col-auto"><p id="t2"></p></div></div><div class="row"><div class="col-auto"><p>E</p></div><div class="col-auto"><p id="t3"></p></div></div></td>';

  document.getElementById("timerPlace").insertAdjacentHTML("afterend", html);
}