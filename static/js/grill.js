var t1 = 0,
  t2 = 0,
  t3 = 0,
  stbt = 0;

document.getElementById("add").addEventListener("click", addHtml);

function addHtml() {
  var timer;
  t1 = Math.floor(Math.random() * 1000);
  t2 = Math.floor(Math.random() * 1000);
  t3 = Math.floor(Math.random() * 1000);
  stbt = Math.floor(Math.random() * 1000);
  var html =
    '<td style="width: 27%;"><div class="row"><div class="col-auto"><p>S</p></div><div class="col-auto"><p id="%t1%"></p></div><div class="col-auto"><i class="material-icons btn" id="%stbt%" style="color: red;">timer_off</i></div></div><div class="row"><div class="col-auto"><p>R</p></div><div class="col-auto"><p id="%t2%"></p></div></div><div class="row"><div class="col-auto"><p>E</p></div><div class="col-auto"><p id="%t3%"></p></div></div></td>';

  var newHtml = html.replace("%t1%", t1);
  newHtml = newHtml.replace("%t2%", t2);
  newHtml = newHtml.replace("%t3%", t3);
  newHtml = newHtml.replace("%stbt%", stbt);

  document.getElementById("timerPlace").insertAdjacentHTML("afterend", newHtml);

  countdown(t1, t2, t3, stbt);
}

function countdown(startT, readyT, counterT, stpBtn) {
  var start = new Date();
  // Fetch the display elements
  var tim1 = document.getElementById(startT);
  var tim2 = document.getElementById(readyT);
  var tim3 = document.getElementById(counterT);
  var btn = document.getElementById(stpBtn);

  $(function() {
    $(tim3).countdowntimer({
      hours: 0,
      minutes: 0,
      seconds: 20,
      size: "sm",
      timeUp: function() {
        tim3.innerHTML = "EXPIRED";
        for (var i = 0; i < 300; i++) {
          $(tim3).fadeOut(900).fadeIn(900);
        }
      }
    });
  });

  tim1.innerHTML = start.toLocaleTimeString();
  tim2.innerHTML = moment(start, "hh:mm:ss A")
    .add(20, "seconds")
    .format("LTS");
}
