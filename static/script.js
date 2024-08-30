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

function is_touch_enabled() {
    return ( 'ontouchstart' in window ) ||
           ( navigator.maxTouchPoints > 0 ) ||
           ( navigator.msMaxTouchPoints > 0 );
}

function page_load() {
    if (is_touch_enabled()) {
        var panel = document.getElementById("panel");
        panel.style.paddingBottom = "12vmin";
    }
}
