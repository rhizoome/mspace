function play() {
    var stream = document.getElementById("stream");
    var play = document.getElementById("btn_play");
    var stop = document.getElementById("btn_stop");
    if (stream.paused || stream.currentTime == 0) {
        stream.play();
        play.style.display = "none";
    } else {
        stream.pause();
        play.style.display = "inline-block";
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
