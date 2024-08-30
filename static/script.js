function play(evnt) {
    event.stopPropagation();
    var stream = document.getElementById("stream");
    if (stream.paused || stream.currentTime == 0) {
        stream.play();
    } else {
        stream.pause();
    }
}

report_play_done = false;
function report_play(url) {
    if(report_play_done) return;
    var oReq = new XMLHttpRequest();
    oReq.open("GET", url);
    oReq.send();
    report_play_done = true;
}

function report_download(url) {
    var oReq = new XMLHttpRequest();
    oReq.open("GET", url);
    oReq.send();
}
