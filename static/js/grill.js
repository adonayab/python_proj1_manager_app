const htmlElementRemove = el => {
  el.remove();
};

// The contents of a timer
let timerContent = pos => {
  let timer = {
    hours: 0,
    minutes: 0,
    seconds: 5,
    size: "sm",
    timeUp: () => {
      $(pos)
        .html("EXPIRED")
        .css("color", "#bf360c");
      for (var i = 0; i < 300; i++) {
        $(pos)
          .fadeOut(900)
          .fadeIn(900);
      }
    }
  };
  return timer;
};

// Function that creates a timer
const countdown = (counterT, timerBody, stopBtn) => {
  const tim3 = document.getElementById(counterT);
  const tBody = document.getElementById(timerBody);
  const btn = document.getElementById(stopBtn);
  $(() => {
    $(tim3).countdowntimer(timerContent(tim3));
  });
  $(btn).click(() => {
    $(tim3).countdowntimer("destroy");
    htmlElementRemove(tBody);
  });
};

// HTML body of a timer
const timerBody = (place, foodName) => {
  const now = new Date();
  const start = now.toLocaleTimeString();
  const ready = moment(start, "hh:mm:ss A")
    .add(20, "seconds")
    .format("LTS");

  let counterId = "tim" + Math.random();
  const timerBodyId = "tim" + Math.random();
  const stopBtn = "tim" + Math.random();

  let markup = `
    <div class="col-auto ${foodName}" id=${timerBodyId}>
      <div class="row">
        <div class="col-auto">
          <p class="font-weight-bold light-blue-text text-accent-4">S</p>
        </div>
        <div class="col-auto">
          <p>${start}</p>
        </div>
        <div class="col-auto">
          <button class="btn bmd-btn-icon red-text" id="${stopBtn}">
            <i class="fas fa-times-circle"></i>
          </button>
        </div>
      </div>
      <div class="row">
        <div class="col-auto">
          <p class="font-weight-bold green-text text-darken-2">R</p>
        </div>
        <div class="col-auto">
          <p>${ready}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-auto">
          <p class="font-weight-bold pink-text text-darken-3">E</p>
        </div>
        <div class="col-auto">
          <p id="${counterId}"></p>
        </div>
      </div>
    </div>
  `;
  place.insertAdjacentHTML("beforebegin", markup);
  countdown(counterId, timerBodyId, stopBtn);
};

// Generating the timers in the HTML when a person clicks
let btns = document.querySelectorAll(".addB");
btns.forEach(btn => {
  let id = btn.id;
  $(`#${id}`).click(() => {
    let btnPos = document.querySelector(`#${id}`);
    let timers = document.querySelectorAll(`.${id}`);
    if (timers.length < 3) {
      timerBody(btnPos.parentNode, id);
    } else {
      alert("Max number of timers reached");
    }
  });
});
