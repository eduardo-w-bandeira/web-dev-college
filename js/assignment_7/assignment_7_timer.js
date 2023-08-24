"use strict"

function nextJuly1(currentDate) {
  let cYear = currentDate.getFullYear();
  let jDate = new Date("July 1, 2024");
  jDate.setFullYear(cYear);
  if (jDate - currentDate < 0) jDate.setFullYear(cYear + 1);
  return jDate;
}


function displayclock() {
  let thisDay = new Date();
  let localDate = thisDay.toLocaleDateString();
  let localTime = thisDay.toLocaleTimeString();
  document.getElementById('currentTime').innerHTML = '<span>${localDate}</span><span>${localTime}</span>';
  let j1Date = nextJuly1(thisDay);
  j1Date.setHours(21);
  let days = (j1Date - thisDay) / (1000 * 60 * 60 * 24);
  let hrs = (days - Math.floor(days)) * 24;
  let mins = (hrs - Math.floor(hrs)) * 60;
  let secs = (mins - Math.floor(mins)) * 60;
  document.getElementById('dLeft').innerText = Math.floor(days);
  document.getElementById('hLeft').innerText = Math.floor(hrs);
  document.getElementById('mLeft').innerText = Math.floor(mins);
  document.getElementById('sLeft').innerText = Math.floor(secs);
}

/* Run and display the countdown clock */
displayclock();

setInterval(displayclock, 1000);
