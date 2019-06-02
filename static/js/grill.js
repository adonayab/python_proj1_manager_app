var t1 = 0,
  t2 = 0,
  t3 = 0;

document.getElementById("add").addEventListener("click", addHtml);

function addHtml() {
  var timer;
  t1 = Math.floor(Math.random() * 1000);
  t2 = Math.floor(Math.random() * 1000);
  t3 = Math.floor(Math.random() * 1000);
  var html =
    '<td style="width: 20%;"><div class="row"><div class="col-auto"><p>S</p></div><div class="col-auto"><p id="%t1%"></p></div></div><div class="row"><div class="col-auto"><p>R</p></div><div class="col-auto"><p id="%t2%"></p></div></div><div class="row"><div class="col-auto"><p>E</p></div><div class="col-auto"><p id="%t3%"></p></div></div></td>';

  var newHtml = html.replace("%t1%", t1);
  newHtml = newHtml.replace("%t2%", t2);
  newHtml = newHtml.replace("%t3%", t3);

  document.getElementById("timerPlace").insertAdjacentHTML("afterend", newHtml);

  countdown(t1, t2, t3);
}

function countdown(startT, readyT, counterT) {
  var countDownDate = new Date().getTime() + 20000; // 4hrs = 14400000
  var start = new Date();

  // Fetch the display elements
  var tim1 = document.getElementById(startT);
  var tim2 = document.getElementById(readyT);
  var tim3 = document.getElementById(counterT);

  // Set the timer
  var interval = setInterval(function() {
    var now = new Date();
    var distance = countDownDate - now;

    if (distance >= 0) {
      var hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      tim3.innerHTML = hours + "h " + minutes + "m " + seconds + "s ";

      tim1.innerHTML = start.toLocaleTimeString();
      tim2.innerHTML = moment(start, "hh:mm:ss A")
        .add(20, "seconds")
        .format("LTS");
    }
    else {
      tim3.innerHTML = "EXPIRED";
    }
  }, 1000);
}
