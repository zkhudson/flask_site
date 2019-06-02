function browserCheck(result){
    var result = window.navigator.userAgent;
    if (result.indexOf("Trident/7.0") > -1 || result.indexOf("Trident/6.0") > -1 || result.indexOf("Trident/5.0") > -1) {
        alert("This website uses CSS Grid for styling and layout, and your browser doesn't support CSS Grid. You should install or use a browser that supports CSS Grid, for example, Google Chrome or Mozilla Firefox.");
    }
}


