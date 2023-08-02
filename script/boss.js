let result = document.querySelectorAll("ul>li .job-card-body")
result.forEach((node) => {
    rs = node.innerText.split("\n")
    try {
        city = rs[1].split("·")[0]
        salary = rs[2]
        degree = rs[4]
        if (rs.length > 8) {
            company = rs[8].match(/\d+人/)[0]
        } else {
            company = rs[7].match(/\d+人/)[0]
        }
        url = `http://127.0.0.1:8000/?city=${city}&salary=${salary}&degree=${degree}&company=${company}`
        var httpRequest = new XMLHttpRequest();
            httpRequest.open('GET', url, true);
            httpRequest.send();
            httpRequest.onreadystatechange = function () {
                if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                    console.log(httpRequest.responseText);
                }
            };
    } catch (err) {
        console.log("一个错误：" + err.message)
    } 
});
let next = document.querySelector("a .ui-icon-arrow-right")
next.click()