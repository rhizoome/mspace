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
