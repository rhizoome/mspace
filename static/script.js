report_play_done = false;
function report_play(url) {
    if (report_play_done) return;
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

function play() {
    var stream = document.getElementById("stream");
    if (stream.paused || stream.currentTime == 0) {
        stream.play();
    } else {
        stream.pause();
    }
}

function is_ios() {
    return [
        'iPad Simulator',
        'iPhone Simulator',
        'iPod Simulator',
        'iPad',
        'iPhone',
        'iPod'
    ].includes(navigator.platform)
    || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

function page_load() {
    if (is_ios()) {
        var stream_div = document.getElementById("stream-div");
        stream_div.style.top = "-7%";
    }
}
