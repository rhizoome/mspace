function play() {
    var stream = document.getElementById("stream");
     if (stream.paused || stream.currentTime == 0) {
         stream.play();
     } else {
         stream.pause();
     }
}

report_done = false;
function report_play(url) {
    if(report_done) return;
    var oReq = new XMLHttpRequest();
    oReq.open("GET", url);
    oReq.send();
    report_done = true;
}
